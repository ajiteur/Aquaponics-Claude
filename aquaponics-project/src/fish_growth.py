"""Tilapia growth from feed, FCR and water temperature.

Candidate model, pending review (Batch 003). Canon is the "growth_feed_model" block
of data/knowledge/species/fish/tilapia.json:

    daily gain (kg) = feed offered (kg) x f_T(water temperature) / FCR

f_T is piecewise linear through sourced points (feeding stops near 17 C, one third of
optimum growth at 22 C, full rate 27 to 32 C, zero at the bioenergetic-model Tmax).
Feed offered is the scenario's direct input (Mode A) unless the scenario asks for the
SRAC 282 size table. All outputs are scenario estimates, not validated.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RUNTIME_PROFILE = PROJECT_ROOT / "data" / "simulation" / "species" / "fish" / "tilapia.json"
MODEL_ID = "tilapia_feed_fcr_temperature"


def load_model(path: Path = RUNTIME_PROFILE) -> dict:
    model = json.loads(path.read_text(encoding="utf-8")).get("growth_feed_model")
    if not model:
        raise KeyError(f"growth_feed_model not found in {path}")
    return model


def temperature_factor(water_temp_c: float, model: dict) -> float:
    points = model["temperature_response"]["points_c_factor"]
    if water_temp_c <= points[0][0] or water_temp_c >= points[-1][0]:
        return 0.0
    for (t0, f0), (t1, f1) in zip(points, points[1:]):
        if t0 <= water_temp_c <= t1:
            return f0 + (f1 - f0) * (water_temp_c - t0) / (t1 - t0)
    return 0.0


def feeding_rate_pct(average_weight_g: float, model: dict, pick: str = "mid") -> float:
    """SRAC 282 suggested feeding rate (% body weight per day) for a fish size."""
    for band in model["feeding_rate_pct_body_weight_by_size"]["bands"]:
        upper = band["max_g"]
        if average_weight_g >= band["min_g"] and (upper is None or average_weight_g < upper):
            if pick == "low":
                return band["min_pct"]
            if pick == "high":
                return band["max_pct"]
            return (band["min_pct"] + band["max_pct"]) / 2.0
    raise ValueError(f"No feeding band for {average_weight_g} g")


def daily_gain_kg(feed_kg: float, water_temp_c: float, model: dict, fcr: float | None = None) -> float:
    fcr = fcr or model["feed_conversion_ratio"]["simulation_default"]
    return feed_kg * temperature_factor(water_temp_c, model) / fcr


def seasonal_temp_c(day: int, winter_c: float, summer_c: float, start_day_of_year: int = 0) -> float:
    """Cosine between winter (day 15) and summer (half a year later); a stated assumption."""
    doy = (start_day_of_year + day) % 365
    mid = (winter_c + summer_c) / 2.0
    amp = (summer_c - winter_c) / 2.0
    return mid - amp * math.cos(2 * math.pi * (doy - 15) / 365.0)


def grow_out(start_g: float, days: int, model: dict, temp_for_day, pick: str = "mid", fcr: float | None = None) -> float:
    """Single-fish grow-out with feed from the size table. Returns final weight in g."""
    w = start_g
    for day in range(days):
        feed_g = w * feeding_rate_pct(w, model, pick) / 100.0
        w += daily_gain_kg(feed_g, temp_for_day(day), model, fcr)
    return w


def uvi_check(model: dict | None = None) -> dict:
    """Compare a size-table grow-out with UVI's measured 79 to 814 g in 24 weeks."""
    model = model or load_model()
    v = model["validation"]["uvi_growout"]
    temps = v["water_temp_c"]
    out = {"published_end_g": v["end_g"], "start_g": v["start_g"], "days": v["days"], "cases": {}}
    for pick in ("low", "mid", "high"):
        for label, temp_fn in (
            ("optimum_temperature", lambda d: 28.0),
            ("uvi_seasonal_24_to_29c_mean_over_year", None),
        ):
            if temp_fn is None:
                # Average over all start dates: UVI staggers tanks through the year.
                finals = [
                    grow_out(v["start_g"], v["days"], model,
                             lambda d, s=s: seasonal_temp_c(d, temps["winter"], temps["summer"], s), pick, v["fcr"])
                    for s in range(0, 365, 30)
                ]
                end = sum(finals) / len(finals)
            else:
                end = grow_out(v["start_g"], v["days"], model, temp_fn, pick, v["fcr"])
            out["cases"][f"{pick}_feed_{label}"] = {
                "model_end_g": round(end, 1),
                "error_fraction": round(end / v["end_g"] - 1.0, 3),
            }
    return out


if __name__ == "__main__":
    print(json.dumps(uvi_check(), indent=2))
