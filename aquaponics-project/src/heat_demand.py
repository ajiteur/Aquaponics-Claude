"""Greenhouse heat demand and heating cost from monthly climate normals.

Candidate model, pending review (Batch 003). Canon lives in
data/knowledge/models/greenhouse_heat_models.json:

    hourly heat demand = max(0, K x (T_set - T_out) - a x I_solar)      [W per m2 floor]

- T_out: monthly mean min and max, spread over the day as a cosine peaking at 15:00.
- I_solar: monthly global radiation spread over the daylight hours as a half sine;
  day length from latitude and the mid-month solar declination.
- K (effective loss coefficient per m2 floor, cover and infiltration together) and
  a (solar utilisation) are not measured. They are calibrated so the model
  reproduces two KEMA 2012 Venlo heat-demand figures under De Bilt normals, then
  checked against a third, independent figure (chrysanthemum, de Gelder & Kempkes 2007).

Cooling (India) is reported as hours above the basil preferred range, plus a fan-pad
electricity range from a single low-confidence source. All outputs are scenario
estimates, not validated.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "data" / "knowledge" / "models" / "greenhouse_heat_models.json"
BASIL_PATH = PROJECT_ROOT / "data" / "knowledge" / "species" / "plants" / "basil.json"
RESULTS_PATH = PROJECT_ROOT / "data" / "simulation" / "results" / "greenhouse_heat_demand.json"
DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
MID_MONTH_DAY_OF_YEAR = (15, 46, 74, 105, 135, 166, 196, 227, 258, 288, 319, 349)
T_PEAK_HOUR = 15.0


def load_models(path: Path = MODEL_PATH) -> dict[str, dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return {r["model_id"]: r for r in data["records"]}


def day_length_hours(latitude_deg: float, day_of_year: int) -> float:
    """Astronomical day length (Cooper 1969 declination)."""
    decl = math.radians(23.45) * math.sin(2 * math.pi * (284 + day_of_year) / 365.0)
    x = -math.tan(math.radians(latitude_deg)) * math.tan(decl)
    x = max(-1.0, min(1.0, x))
    return 24.0 * math.acos(x) / math.pi


def hourly_profile(climate: dict, month: int) -> list[dict]:
    """24 hourly (temperature C, solar W/m2, is_day) values for a mean day of the month."""
    m = climate["monthly"]
    t_min, t_max = m["t_min_c"][month], m["t_max_c"][month]
    t_mean = (t_min + t_max) / 2.0
    amp = (t_max - t_min) / 2.0
    n = day_length_hours(climate["latitude_deg"], MID_MONTH_DAY_OF_YEAR[month])
    sunrise = 12.0 - n / 2.0
    rad = m.get("global_radiation_mj_m2_month")
    daily_j = rad[month] * 1e6 / DAYS_IN_MONTH[month] if rad else None
    hours = []
    for h in range(24):
        mid = h + 0.5
        temp = t_mean + amp * math.cos(2 * math.pi * (mid - T_PEAK_HOUR) / 24.0)
        is_day = sunrise <= mid <= sunrise + n
        solar = None
        if daily_j is not None:
            # half-sine over the day; peak = daily x pi / (2 x N x 3600)
            solar = daily_j * math.pi / (2 * n * 3600.0) * math.sin(math.pi * (mid - sunrise) / n) if is_day else 0.0
        hours.append({"t_c": temp, "solar_w_m2": solar, "is_day": is_day})
    return hours


def annual_heat_demand_mj_m2(
    climate: dict,
    k_w_m2_k: float,
    solar_utilisation: float,
    day_setpoint_c: float,
    night_setpoint_c: float,
    night_k_factor: float = 1.0,
) -> dict:
    """Annual and monthly heat demand, MJ per m2 floor. night_k_factor < 1 models a closed screen."""
    monthly = []
    for month in range(12):
        joules = 0.0
        for hr in hourly_profile(climate, month):
            if hr["is_day"]:
                setpoint, k = day_setpoint_c, k_w_m2_k
            else:
                setpoint, k = night_setpoint_c, k_w_m2_k * night_k_factor
            gain = solar_utilisation * (hr["solar_w_m2"] or 0.0)
            joules += max(0.0, k * (setpoint - hr["t_c"]) - gain) * 3600.0
        monthly.append(joules * DAYS_IN_MONTH[month] / 1e6)
    return {"annual_mj_m2": sum(monthly), "monthly_mj_m2": monthly}


def degree_hours_below(climate: dict, threshold_c: float) -> dict:
    """Degree-hours and hours per year with outdoor air below a threshold (mean-day basis)."""
    dh = hours = 0.0
    for month in range(12):
        for hr in hourly_profile(climate, month):
            if hr["t_c"] < threshold_c:
                dh += (threshold_c - hr["t_c"]) * DAYS_IN_MONTH[month]
                hours += DAYS_IN_MONTH[month]
    return {"degree_hours": dh, "hours": hours}


def hours_above(climate: dict, threshold_c: float) -> float:
    return sum(
        DAYS_IN_MONTH[month]
        for month in range(12)
        for hr in hourly_profile(climate, month)
        if hr["t_c"] > threshold_c
    )


def screen_night_k_factor(model: dict) -> float:
    u = model["cover_u_values_w_m2_k"]
    return u["single_glass_with_thermal_screen"]["value"] / u["single_glass_asabe"]["value"]


def night_factor(point: dict, screen_factor: float) -> float:
    return screen_factor if point.get("night_screen") else 1.0


def calibrate_k(climate: dict, point: dict, solar_utilisation: float, screen_factor: float) -> float:
    """K that reproduces the calibration point for a given solar utilisation (bisection; demand rises with K)."""
    lo, hi = 0.0, 200.0
    for _ in range(60):
        mid = (lo + hi) / 2
        got = annual_heat_demand_mj_m2(
            climate, mid, solar_utilisation, point["day_setpoint_c"], point["night_setpoint_c"],
            night_factor(point, screen_factor),
        )["annual_mj_m2"]
        lo, hi = (mid, hi) if got < point["heat_demand_mj_m2_yr"] else (lo, mid)
    return (lo + hi) / 2


def calibration_set(climate: dict, model: dict) -> list[dict]:
    """One (solar utilisation, K) pair per grid value. K and a cannot both be identified from
    the data, so results are reported as the range across the grid."""
    point = model["calibration"]["point"]
    sf = screen_night_k_factor(model)
    return [
        {"solar_utilisation": a, "k_w_m2_k": calibrate_k(climate, point, a, sf)}
        for a in model["calibration"]["solar_utilisation_grid"]
    ]


def demand_range(climate: dict, cal: list[dict], case: dict, screen_factor: float, k_scale: float = 1.0,
                 use_solar: bool = True) -> dict:
    runs = [
        annual_heat_demand_mj_m2(
            climate, c["k_w_m2_k"] * k_scale, c["solar_utilisation"] if use_solar else 0.0,
            case["day_setpoint_c"], case["night_setpoint_c"], night_factor(case, screen_factor),
        )
        for c in cal
    ]
    lo = min(runs, key=lambda r: r["annual_mj_m2"])
    hi = max(runs, key=lambda r: r["annual_mj_m2"])
    return {"low": lo, "high": hi}


def heating_gas_and_cost(heat: dict, gas: dict, price: dict | None) -> dict:
    """heat: {'low': MJ/m2, 'high': MJ/m2}."""
    mj = gas["lower_heating_value_mj_per_m3_aeq"]
    eff = gas["boiler_heat_use_fraction"]
    gas_lo = heat["low"] / (mj * eff["max"])
    gas_hi = heat["high"] / (mj * eff["min"])
    out = {
        "heat_demand_mj_m2_yr": {"low": round(heat["low"], 1), "high": round(heat["high"], 1)},
        "heat_demand_m3_aeq_m2_yr": {"low": round(heat["low"] / mj, 1), "high": round(heat["high"] / mj, 1)},
        "heat_demand_kwh_th_m2_yr": {"low": round(heat["low"] / 3.6), "high": round(heat["high"] / 3.6)},
        "gas_m3_m2_yr": {"low": round(gas_lo, 1), "high": round(gas_hi, 1)},
    }
    if price:
        out["gas_cost_eur_m2_yr"] = {"low": round(gas_lo * price["low"], 2), "high": round(gas_hi * price["high"], 2)}
    else:
        out["gas_cost_eur_m2_yr"] = None
    return out


def karnataka_tariff() -> dict | None:
    """Karnataka electricity tariff (INR/kWh), approved in Batch 001 for scenario use only."""
    path = PROJECT_ROOT / "data" / "scenarios" / "unit_configuration_candidates_v0.json"
    if not path.exists():
        return None
    rate = json.loads(path.read_text(encoding="utf-8")).get("locations", {}).get("karnataka", {}).get("electricity_per_kwh")
    if not rate or rate.get("approval_status") != "approved":
        return None
    return rate


def build_results(
    models: dict | None = None, gas_price_eur_m3: dict | None = None, electricity_inr_kwh: dict | None = None
) -> dict:
    models = models or load_models()
    hm = models["greenhouse_heat_demand_degree_hour"]
    nl = models["climate_normals_de_bilt_1991_2020"]
    ka = models["climate_normals_bengaluru_1991_2020"]
    sf = screen_night_k_factor(hm)
    cal = calibration_set(nl, hm)
    ks = [c["k_w_m2_k"] for c in cal]

    checks = []
    for point in hm["validation"]["points"]:
        r = demand_range(nl, cal, point, sf)
        checks.append({
            "point_id": point["point_id"],
            "published_mj_m2_yr": point["heat_demand_mj_m2_yr"],
            "model_mj_m2_yr": {"low": round(r["low"]["annual_mj_m2"], 1), "high": round(r["high"]["annual_mj_m2"], 1)},
            "error_fraction": {
                "low": round(r["low"]["annual_mj_m2"] / point["heat_demand_mj_m2_yr"] - 1.0, 3),
                "high": round(r["high"]["annual_mj_m2"] / point["heat_demand_mj_m2_yr"] - 1.0, 3),
            },
            "caveat": point.get("caveat"),
        })

    nl_cases = []
    for case in hm["setpoint_cases"]:
        r = demand_range(nl, cal, case, sf)
        nl_cases.append({
            **{key: case[key] for key in ("case_id", "day_setpoint_c", "night_setpoint_c", "night_screen", "setpoint_basis")},
            **heating_gas_and_cost(
                {"low": r["low"]["annual_mj_m2"], "high": r["high"]["annual_mj_m2"]}, hm["gas"], gas_price_eur_m3
            ),
            "monthly_heat_demand_mj_m2_high": [round(v, 1) for v in r["high"]["monthly_mj_m2"]],
            "extrapolated_beyond_calibration": max(case["day_setpoint_c"], case["night_setpoint_c"])
            > hm["calibration"]["calibrated_setpoint_max_c"],
        })

    pe = hm["karnataka_polyhouse"]
    ka_cases = []
    for case in hm["setpoint_cases"]:
        if case["case_id"].endswith("_night_screen"):
            continue  # polyhouse cases are unscreened; skip the screened duplicates
        unscreened = {**case, "night_screen": False}
        lo = demand_range(ka, cal, unscreened, sf, pe["k_scale"]["min"], use_solar=False)["low"]["annual_mj_m2"]
        hi = demand_range(ka, cal, unscreened, sf, pe["k_scale"]["max"], use_solar=False)["high"]["annual_mj_m2"]
        ka_cases.append({
            "case_id": case["case_id"],
            "day_setpoint_c": case["day_setpoint_c"],
            "night_setpoint_c": case["night_setpoint_c"],
            "heat_demand_kwh_th_m2_yr": {"low": round(lo / 3.6), "high": round(hi / 3.6)},
            "hours_below_night_setpoint_yr": round(degree_hours_below(ka, case["night_setpoint_c"])["hours"]),
        })

    basil = json.loads(BASIL_PATH.read_text(encoding="utf-8"))["environment"]
    chill_c = basil["tolerated_temp_c"]["min"]
    pref_max = basil["preferred_temp_c"]["max"]
    tol_max = basil["tolerated_temp_c"]["max"]
    record_lows = ka["monthly"].get("record_low_c")
    fan = pe["fan_pad_electricity"]
    fan_kwh = {
        "low": fan["kwh_per_day"]["min"] / fan["house_floor_m2"] * 365,
        "high": fan["kwh_per_day"]["max"] / fan["house_floor_m2"] * 365,
    }

    return {
        "estimate_status": "scenario_estimate",
        "label": "scenario estimate, not validated",
        "model_id": hm["model_id"],
        "approval_batch": hm["approval_batch"],
        "calibration": {
            "calibration_point": hm["calibration"]["point"]["point_id"],
            "solar_utilisation_grid": [c["solar_utilisation"] for c in cal],
            "k_w_m2_floor_k": {"low": round(min(ks), 2), "high": round(max(ks), 2)},
            "night_screen_k_factor": round(sf, 3),
            "implied_k_over_glass_u": {
                "low": round(min(ks) / hm["cover_u_values_w_m2_k"]["single_glass"]["max"], 2),
                "high": round(max(ks) / hm["cover_u_values_w_m2_k"]["single_glass"]["min"], 2),
                "note": "K includes infiltration and geometry; no source gives the cover-to-floor ratio, so this cannot be checked (gap).",
            },
            "validation": checks,
        },
        "netherlands_glasshouse": {
            "climate": nl["model_id"],
            "gas_price_eur_m3": gas_price_eur_m3,
            "gas_price_basis": "catalog natural_gas_price_per_m3, Netherlands (CBS, tier 1)" if gas_price_eur_m3 else "missing",
            "cases": nl_cases,
        },
        "karnataka_polyhouse": {
            "climate": ka["model_id"],
            "heating": {
                "cases": ka_cases,
                "basis": "NL-calibrated K scaled for single film, no screen, no solar credit, mean-day normals.",
                "note": "Cold nights below the monthly mean minimum are not represented, so true needs are higher.",
                "chilling_threshold_c": chill_c,
                "months_record_low_below_chilling": (
                    [i + 1 for i, t in enumerate(record_lows) if t < chill_c] if record_lows else None
                ),
                "record_low_confidence": "low (tier 3 mirror citing IMD)",
            },
            "cooling": {
                "preferred_air_max_c": pref_max,
                "hours_above_preferred_max_yr": round(hours_above(ka, pref_max)),
                "tolerated_max_c": tol_max,
                "hours_above_tolerated_max_yr": round(hours_above(ka, tol_max)),
                "note": "Outdoor air only. A polyhouse runs warmer than outside in daytime; inside temperature is not modelled.",
                "fan_pad_electricity_kwh_m2_yr_if_run_every_day": {k: round(v) for k, v in fan_kwh.items()},
                "fan_pad_confidence": fan["review_metadata"]["confidence"],
                "electricity_cost_inr_m2_yr_if_run_every_day": (
                    {
                        "low": round(fan_kwh["low"] * electricity_inr_kwh["low"]),
                        "high": round(fan_kwh["high"] * electricity_inr_kwh["high"]),
                    }
                    if electricity_inr_kwh else None
                ),
                "electricity_tariff_inr_kwh": (
                    {"low": electricity_inr_kwh["low"], "high": electricity_inr_kwh["high"],
                     "basis": "Karnataka electricity_per_kwh in data/scenarios/unit_configuration_candidates_v0.json "
                              "(Batch 001 approved for scenario use only, low confidence; fixed charges excluded)"}
                    if electricity_inr_kwh else "missing"
                ),
            },
        },
        "gaps": hm["gaps"],
    }


def gas_price_from_catalog() -> dict | None:
    path = PROJECT_ROOT / "data" / "catalog" / "components_v0.json"
    if not path.exists():
        return None
    found = []

    def walk(o):
        if isinstance(o, dict):
            if o.get("input_id") == "natural_gas_price_per_m3" and o.get("region") == "netherlands":
                found.append(o["value"])
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(json.loads(path.read_text(encoding="utf-8")))
    return found[0] if found else None


def main() -> None:
    results = build_results(gas_price_eur_m3=gas_price_from_catalog(), electricity_inr_kwh=karnataka_tariff())
    RESULTS_PATH.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results["calibration"], indent=1))
    for c in results["netherlands_glasshouse"]["cases"]:
        print(c["case_id"], c["heat_demand_m3_aeq_m2_yr"], c["gas_m3_m2_yr"], c["gas_cost_eur_m2_yr"])
    print(json.dumps(results["karnataka_polyhouse"], indent=1))


if __name__ == "__main__":
    main()
