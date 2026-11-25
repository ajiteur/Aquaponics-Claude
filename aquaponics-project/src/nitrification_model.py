"""Surface-based biofilm nitrification for the daily simulation.

Replaces the old placeholder, which removed a fixed fraction of each day's TAN
input and so let TAN climb without limit at high feed rates.

The model (candidate, pending review) lives in
data/knowledge/models/nitrification_models.json, record
"biofilm_nitrification_capacity". In short:

    capacity  = nitrifying surfaces expressed as feed they can treat x TAN per g feed
    removal   = capacity x min(1, TAN / TAN_saturation) x f_pH x f_T x f_DO x maturity

Removal is stepped hourly within the day so the concentration term does not
overshoot. All outputs are simulation estimates, not observed data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from mvp_tan_nh3_risk import calculate_unionized_nh3_chemistry

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RUNTIME_MODEL_PATH = PROJECT_ROOT / "data" / "simulation" / "models" / "nitrification_models.json"
MODEL_ID = "biofilm_nitrification_capacity"
FEED_TO_TAN_N_FACTOR = 0.092  # Ebeling et al. 2006: PTAN = F x PC x 0.092
SUBSTEPS_PER_DAY = 24


def load_model(path: Path = RUNTIME_MODEL_PATH) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    for record in data["records"]:
        if record.get("model_id") == MODEL_ID:
            return record
    raise KeyError(f"{MODEL_ID} not found in {path}")


def media_feed_loading_low_end(path: Path = RUNTIME_MODEL_PATH) -> dict[str, float]:
    """Conservative (low-end) feed loading per biofilter variant, kg feed/m3 media/day."""
    data = json.loads(path.read_text(encoding="utf-8"))
    for record in data["records"]:
        if record.get("model_id") == "biofilter_feed_loading_capacities":
            out = {}
            for variant in record.get("variants", []):
                # Canon nests the range under feed_loading.range; the runtime mirror
                # flattens it to feed_loading_kg_feed_per_m3_media_day.
                loading = variant.get("feed_loading_kg_feed_per_m3_media_day") or variant.get("feed_loading", {})
                low = (loading.get("range") or {}).get("min", loading.get("min"))
                if low is not None:
                    out[variant["variant_id"]] = float(low)
            return out
    return {}


def tan_mg_per_g_feed(feeding: dict, nitrogen_model: dict) -> tuple[float, str]:
    """TAN-N produced per g feed. Uses the canonical protein formula when protein is known."""
    protein = feeding.get("feed_protein_fraction")
    if isinstance(protein, (int, float)) and 0 < protein < 1:
        return protein * FEED_TO_TAN_N_FACTOR * 1000.0, "canonical_ptan_formula_feed_x_protein_x_0.092"
    return float(nitrogen_model.get("tan_generation_mg_per_g_feed", 30.0)), "scenario_placeholder_tan_generation_mg_per_g_feed"


def resolve_surfaces(scenario: dict, plant_profile: dict | None) -> dict[str, Any] | None:
    """Return the nitrifying surfaces for this scenario, or None if none can be determined."""
    system = scenario.get("system", {})
    surfaces = system.get("nitrification_surfaces")
    if isinstance(surfaces, dict):
        return {**surfaces, "basis": surfaces.get("basis", "scenario_explicit")}

    if scenario.get("crop_system_type") == "architecture_dwc_raft" and plant_profile:
        cycle = (
            plant_profile.get("validation_benchmarks", {})
            .get("aquaponics_context", {})
            .get("crop_cycle_context")
            or {}
        )
        density = cycle.get("planting_density_plants_m2")
        plant_count = scenario.get("plant_crop", {}).get("plant_count")
        if density and plant_count:
            return {
                "raft_grow_area_m2": plant_count / density,
                "basis": "derived_plant_count_over_profile_planting_density",
            }
    return None


def capacity_g_tan_day(surfaces: dict, model: dict, tan_per_g_feed_mg: float, media_loading: dict[str, float]) -> float:
    raft_anchor = next(
        a for a in model["capacity_anchors"] if a["parameter"] == "raft_waste_treatment_capacity_feed_equivalent"
    )
    feed_capacity_g_day = (surfaces.get("raft_grow_area_m2") or 0.0) * raft_anchor["value"]

    biofilter = surfaces.get("dedicated_biofilter")
    if isinstance(biofilter, dict) and biofilter.get("media_volume_m3"):
        loading = biofilter.get("feed_loading_kg_per_m3_day")
        if loading is None:
            loading = media_loading.get(biofilter.get("variant_id"))
        if loading is None:
            raise ValueError(f"No feed loading known for biofilter variant {biofilter.get('variant_id')!r}")
        feed_capacity_g_day += biofilter["media_volume_m3"] * loading * 1000.0

    return feed_capacity_g_day * tan_per_g_feed_mg / 1000.0


def ph_factor(pH: float, model: dict) -> float:
    resp = model["pH_response"]
    low, full = resp["practically_ceases_below_pH"], resp["full_rate_at_or_above_pH"]
    if pH >= full:
        return 1.0
    if pH <= low:
        return 0.0
    return (pH - low) / (full - low)


def temperature_factor(water_temp_c: float, model: dict) -> float:
    resp = model["temperature_response"]
    opt_min = resp["optimal_range_c"]["min"]
    if water_temp_c >= opt_min:
        return 1.0
    return max(0.0, 1.0 - resp["rate_change_per_c_below_optimum"] * (opt_min - water_temp_c))


def do_factor(do_mg_l: float, model: dict) -> float:
    threshold = model["dissolved_oxygen_response"]["inefficient_below_do_mg_L"]
    return max(0.0, min(1.0, do_mg_l / threshold))


def step_day(
    *,
    tan_mg_l: float,
    daily_tan_input_g: float,
    capacity_g_day: float,
    water_volume_l: float,
    pH: float,
    water_temp_c: float,
    do_mg_l: float,
    maturity: float,
    model: dict,
    tan_saturation_mg_l: float | None = None,
) -> dict[str, Any]:
    """Advance TAN one day. Returns new TAN (mg/L) and TAN removed (g and mg/L)."""
    if tan_saturation_mg_l is None:
        tan_saturation_mg_l = model["concentration_response"]["simulation_default_tan_saturation_mg_L"]
    f_ph = ph_factor(pH, model)
    f_t = temperature_factor(water_temp_c, model)
    f_do = do_factor(do_mg_l, model)
    effective_capacity_g_day = capacity_g_day * f_ph * f_t * f_do * maturity

    # Implicit (backward Euler) hourly steps: removal is evaluated at the end of
    # each step, which is stable and gives the exact steady state in the linear range.
    tan_g = tan_mg_l * water_volume_l / 1000.0
    saturation_g = tan_saturation_mg_l * water_volume_l / 1000.0
    capacity_step_g = effective_capacity_g_day / SUBSTEPS_PER_DAY
    input_step_g = daily_tan_input_g / SUBSTEPS_PER_DAY
    removed_g = 0.0
    for _ in range(SUBSTEPS_PER_DAY):
        available = tan_g + input_step_g
        linear_end = available / (1.0 + capacity_step_g / saturation_g)
        if linear_end < saturation_g:
            new_tan_g = linear_end
        else:
            new_tan_g = max(available - capacity_step_g, saturation_g)
        removed_g += available - new_tan_g
        tan_g = new_tan_g

    new_tan = tan_g * 1000.0 / water_volume_l
    return {
        "new_tan_mg_L": new_tan,
        "tan_removed_g": removed_g,
        "tan_removed_mg_L": removed_g * 1000.0 / water_volume_l,
        "factors": {
            "pH": round(f_ph, 3),
            "temperature": round(f_t, 3),
            "dissolved_oxygen": round(f_do, 3),
            "biofilter_maturity": maturity,
        },
        "capacity_g_tan_day": round(capacity_g_day, 3),
        "effective_capacity_g_tan_day": round(effective_capacity_g_day, 3),
        "tan_saturation_mg_L": tan_saturation_mg_l,
        "load_to_effective_capacity_ratio": (
            round(daily_tan_input_g / effective_capacity_g_day, 3) if effective_capacity_g_day > 0 else None
        ),
    }


def steady_state_tan_mg_l(daily_tan_input_g: float, effective_capacity_g_day: float, tan_saturation_mg_l: float) -> float | None:
    """Steady-state TAN in the linear regime, or None if load exceeds capacity (TAN keeps rising)."""
    if effective_capacity_g_day <= 0 or daily_tan_input_g >= effective_capacity_g_day:
        return None
    return daily_tan_input_g / effective_capacity_g_day * tan_saturation_mg_l


def unionized_nh3(tan_mg_l: float, pH: float, water_temp_c: float) -> dict[str, float]:
    chem = calculate_unionized_nh3_chemistry(
        estimated_tan_n_mg_l=tan_mg_l, ph=pH, water_temp_c=water_temp_c, freshwater_assumption=True
    )
    return {"nh3_mg_L": chem["estimated_nh3_mg_l"], "nh3_n_mg_L": chem["estimated_nh3_n_mg_l"]}
