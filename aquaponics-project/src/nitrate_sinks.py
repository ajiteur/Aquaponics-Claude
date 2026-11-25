"""Nitrate sinks for the daily simulation: water exchange and a calibrated residual loss.

Before this module the only nitrate sink was plant shoot uptake, so nitrate built up
far above UVI's measured level at UVI-scale feed. The model (candidate, pending
review) is record "nitrate_sinks" in data/knowledge/models/nitrification_models.json:

    residual loss  = residual_loss_fraction x nitrified N   (denitrification + solids N)
    water exchange = exchange_fraction x nitrate in the water

The residual loss fraction is calibrated so that, at the UVI basil anchor (feed
ratio, nitrate level, water volume per m2), the steady-state balance closes. It is a
calibration, not a measurement. All outputs are scenario estimates, not validated.
"""

from __future__ import annotations

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RUNTIME_MODEL_PATH = PROJECT_ROOT / "data" / "simulation" / "models" / "nitrification_models.json"
MODEL_ID = "nitrate_sinks"


def load_model(path: Path = RUNTIME_MODEL_PATH) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    for record in data["records"]:
        if record.get("model_id") == MODEL_ID:
            return record
    raise KeyError(f"{MODEL_ID} not found in {path}")


def anchor_shoot_n_uptake_g_per_m2_day(plant_profile: dict) -> float | None:
    """Basil shoot N uptake per m2 per day at the yield anchor, from the profile."""
    context = plant_profile.get("validation_benchmarks", {}).get("aquaponics_context", {})
    cycle = context.get("crop_cycle_context") or {}
    yield_kg_m2 = context.get("yield_anchor_kg_m2_batch")
    period = cycle.get("growing_period_days")
    uptake = plant_profile.get("nutrient_response", {}).get("shoot_n_uptake_model")
    if not (yield_kg_m2 and period and uptake):
        return None
    fresh_g_m2_day = yield_kg_m2 * 1000.0 / period
    return (
        fresh_g_m2_day
        * uptake["shoot_dry_matter_fraction"]["simulation_default"]
        * uptake["tissue_n_fraction_of_dry_mass"]["simulation_default"]
    )


def calibrated_residual_loss_fraction(model: dict, tan_mg_per_g_feed: float, plant_profile: dict) -> float | None:
    """Fraction of nitrified N lost to denitrification and solids at the UVI anchor.

    Steady state per m2 of grow area:
        nitrified = uptake + exchange_fraction x nitrate x volume + f x nitrified
    """
    anchors = model["residual_loss"]["calibration"]["anchors"]
    uptake = anchor_shoot_n_uptake_g_per_m2_day(plant_profile)
    if uptake is None:
        return None
    nitrified = anchors["feed_ratio_g_per_m2_day"] * tan_mg_per_g_feed / 1000.0
    exchange = (
        model["water_exchange"]["fraction_of_system_volume_per_day"]
        * anchors["nitrate_n_mg_L"]
        * anchors["water_volume_l_per_m2_grow_area"]
        / 1000.0
    )
    if nitrified <= 0:
        return None
    return max(0.0, min(1.0, (nitrified - uptake - exchange) / nitrified))


def apply_sinks(
    *,
    nitrate_mg_l: float,
    nitrified_mg_l: float,
    plant_uptake_mg_l: float,
    exchange_fraction: float,
    residual_loss_fraction: float,
) -> dict:
    """Advance nitrate one day through generation, uptake and the two sinks."""
    after_uptake = max(0.0, nitrate_mg_l + nitrified_mg_l - plant_uptake_mg_l)
    residual = min(after_uptake, residual_loss_fraction * nitrified_mg_l)
    after_residual = after_uptake - residual
    exchanged = exchange_fraction * after_residual
    return {
        "new_nitrate_mg_L": after_residual - exchanged,
        "residual_loss_mg_L": residual,
        "water_exchange_loss_mg_L": exchanged,
    }
