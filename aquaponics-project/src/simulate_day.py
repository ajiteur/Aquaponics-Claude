from pathlib import Path
import json
import subprocess
import sys
from datetime import datetime, UTC

import fish_growth
import nitrate_sinks
import nitrification_model
import ph_buffer

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SCENARIO_DIR = PROJECT_ROOT / "data" / "simulation" / "scenarios"
SPECIES_DIR = PROJECT_ROOT / "data" / "simulation" / "species"
DAYLOG_DIR = PROJECT_ROOT / "data" / "simulation" / "day_logs"
DAYLOG_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_SCENARIO = SCENARIO_DIR / "starter_tilapia_lettuce_system.json"


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def species_id_to_filename(species_id: str) -> tuple[str, str]:
    if species_id.startswith("fish_"):
        return "fish", species_id.replace("fish_", "", 1) + ".json"
    if species_id.startswith("plant_"):
        return "plants", species_id.replace("plant_", "", 1) + ".json"
    raise ValueError(f"Unsupported species_id: {species_id}")


def run_overlap_score(
    fish_name: str,
    plant_name: str,
    pH: float,
    water_temp_c: float,
    air_temp_c: float,
    do_mg_l: float,
    nh3_mg_l: float,
    mode: str,
    ph_context: str = "hydroponic",
) -> dict:
    cmd = [
        sys.executable,
        "src/simulate_overlap_score.py",
        fish_name,
        plant_name,
        str(pH),
        str(water_temp_c),
        str(air_temp_c),
        str(do_mg_l),
        str(nh3_mg_l),
        mode,
        ph_context,
    ]

    result = subprocess.run(
        cmd,
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"simulate_overlap_score failed\n\nSTDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}"
        )

    return json.loads(result.stdout)


def shoot_n_uptake_g_day(plant_profile: dict, fresh_gain_g_per_plant: float | None, plant_count: int) -> float | None:
    """Plant N uptake from growth: fresh shoot gain x dry matter x tissue N.

    Returns None when the profile has no uptake model or no growth figure is available.
    """
    model = plant_profile.get("nutrient_response", {}).get("shoot_n_uptake_model")
    if not model or fresh_gain_g_per_plant is None:
        return None
    dry_matter = model["shoot_dry_matter_fraction"]["simulation_default"]
    tissue_n = model["tissue_n_fraction_of_dry_mass"]["simulation_default"]
    return fresh_gain_g_per_plant * plant_count * dry_matter * tissue_n


def target_ph_for_mode(mode: str) -> float:
    """pH set-point used by the pH-control policy for each operating mode."""
    if mode == "plant_yield_optimization_mode":
        return 6.25
    if mode == "robust_compromise_mode":
        return 6.9
    return 6.5


def plant_ph_context(scenario: dict) -> str:
    """Coupled loops score plant pH against aquaponic ranges where the profile has them."""
    loop_type = scenario.get("system", {}).get("loop_type")
    return "aquaponics_coupled" if loop_type == "coupled" else "hydroponic"


def clamp(value: float, min_value: float = 0.0, max_value: float = 1.0) -> float:
    return max(min_value, min(max_value, value))


def crop_cycle_calibration(plant_profile: dict) -> dict | None:
    """Return the yield calibration from the species profile, or None if incomplete.

    The calibrated rate spreads the yield anchor (kg/m2 per harvest) evenly over the
    growing period at the anchor planting density. It describes ideal conditions at
    the anchor site; daily plant and nitrate scores scale it down.
    """
    context = plant_profile.get("validation_benchmarks", {}).get("aquaponics_context", {})
    cycle = context.get("crop_cycle_context") or {}
    anchor_kg_m2 = context.get("yield_anchor_kg_m2_batch")
    density = cycle.get("planting_density_plants_m2")
    period_days = cycle.get("growing_period_days")
    if not anchor_kg_m2 or not density or not period_days:
        return None
    target_g_per_plant = anchor_kg_m2 * 1000.0 / density
    return {
        "yield_anchor_kg_m2_per_harvest": anchor_kg_m2,
        "planting_density_plants_m2": density,
        "growing_period_days": int(period_days),
        "target_cut_mass_g_per_plant": target_g_per_plant,
        "ideal_rate_g_per_plant_day": target_g_per_plant / period_days,
        "basis": "calibrated_to_canonical_yield_anchor",
    }


def plant_score_relative_to_anchor(
    plant_profile: dict,
    plant_score: float,
    fish_name: str,
    plant_name: str,
    water: dict,
    mode: str,
    ph_context: str = "hydroponic",
) -> float:
    """Express today's plant score as a fraction of the score at the yield-anchor site.

    The yield anchor was achieved under specific conditions, so those conditions count
    as 100 percent. Scores above the anchor are clamped to 1.0: the model does not
    predict yields above the anchor. Falls back to the raw score when no reference
    conditions are recorded.
    """
    context = plant_profile.get("validation_benchmarks", {}).get("aquaponics_context", {})
    ref = (context.get("crop_cycle_context") or {}).get("anchor_reference_conditions")
    if not ref:
        return plant_score
    reference = run_overlap_score(
        fish_name=fish_name,
        plant_name=plant_name,
        pH=ref["pH"],
        water_temp_c=ref["water_temperature_c"],
        air_temp_c=ref["air_temperature_c"],
        do_mg_l=water["dissolved_oxygen_mg_L"],
        nh3_mg_l=water["unionized_nh3_mg_L"],
        mode=mode,
        ph_context=ph_context,
    )
    reference_score = reference["plant_assessment"]["overall_plant_score"]
    if not reference_score:
        return plant_score
    return clamp(plant_score / reference_score)


def _interp(points: list, x: float, above: float) -> float:
    if x >= points[-1][0]:
        return above
    if x <= points[0][0]:
        return points[0][1]
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        if x0 <= x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return above


def yield_response_factors(
    plant_profile: dict, density: float, dli: float | None, exponent_b: float | None = None
) -> dict:
    """Candidate basil density and light factors; both 1.0 at the UVI anchor.

    exponent_b overrides the profile's density exponent (sensitivity runs, e.g. the
    open-canopy exponent); None uses the profile value.
    """
    model = plant_profile.get("yield_response_model")
    if not model:
        return {"density_factor": 1.0, "light_factor": 1.0, "basis": "no_yield_response_model"}
    dens = model["density_response"]
    b = dens["yield_per_m2_exponent_b"] if exponent_b is None else float(exponent_b)
    ratio = density / dens["anchor_density_plants_m2"]
    density_factor = min(dens["cap_per_plant_factor_at_or_below_anchor"], ratio ** (b - 1.0))
    light = model["light_response"]
    if dli is None:
        light_factor, light_basis = light["factor_when_dli_missing"], "dli_not_given_assume_anchor_light"
    else:
        light_factor, light_basis = _interp(light["points_dli_factor"], float(dli), light["above_last_point"]), "scenario_dli"
    return {
        "density_factor": round(density_factor, 4),
        "light_factor": round(light_factor, 4),
        "density_plants_m2": density,
        "density_exponent_b": b,
        "dli_mol_m2_day": dli,
        "basis": f"{model['model_id']}_candidate; light: {light_basis}",
    }


def update_harvestable_mass(
    scenario: dict,
    plant_crop: dict,
    plant_profile: dict,
    plant_score: float,
    nitrate_availability_score: float,
) -> dict | None:
    """Grow harvestable cut mass for one day and emit a harvest event at cycle end.

    Returns the harvest event for this day, or None. Does nothing when the species
    profile has no complete crop-cycle calibration.
    """
    calibration = crop_cycle_calibration(plant_profile)
    if calibration is None:
        return None

    policy = plant_crop.setdefault("harvest_policy", {})
    period_days = int(policy.get("growing_period_days") or calibration["growing_period_days"])
    density = plant_crop.get("planting_density_plants_m2") or calibration["planting_density_plants_m2"]
    overrides = plant_crop.get("yield_response_overrides") or {}
    response = yield_response_factors(
        plant_profile, density, scenario.get("light", {}).get("dli_mol_m2_day"), overrides.get("density_exponent_b")
    )
    daily_gain = (
        calibration["ideal_rate_g_per_plant_day"] * plant_score * nitrate_availability_score
        * response["density_factor"] * response["light_factor"]
    )
    plant_crop["yield_response_factors"] = response
    plant_crop["last_daily_cut_gain_g_per_plant"] = round(daily_gain, 4)
    plant_crop["harvestable_cut_mass_g_per_plant"] = round(
        plant_crop.get("harvestable_cut_mass_g_per_plant", 0.0) + daily_gain, 3
    )
    plant_crop["harvest_calibration"] = calibration

    if plant_crop["days_since_transplant"] < period_days:
        return None

    plant_count = plant_crop["plant_count"]
    harvested_mass_kg = plant_count * plant_crop["harvestable_cut_mass_g_per_plant"] / 1000.0
    grow_area_m2 = plant_count / density
    cull_fraction = policy.get("cull_fraction")
    if isinstance(cull_fraction, (int, float)) and 0.0 <= cull_fraction < 1.0:
        saleable_harvest_mass_kg = round(harvested_mass_kg * (1.0 - cull_fraction), 3)
        saleable_basis = "runtime_harvested_mass_minus_explicit_scenario_cull_fraction"
    else:
        saleable_harvest_mass_kg = None
        saleable_basis = "null_no_explicit_cull_fraction_in_scenario"

    events = scenario.setdefault("harvest_events", [])
    event = {
        "day": scenario["time"]["day"] + 1,
        "crop_cycle_number": len(events) + 1,
        "species_id": plant_crop["species_id"],
        "plant_count": plant_count,
        "grow_area_m2_at_anchor_density": round(plant_count / calibration["planting_density_plants_m2"], 3),
        "grow_area_m2": round(grow_area_m2, 3),
        "planting_density_plants_m2": density,
        "days_in_cycle": plant_crop["days_since_transplant"],
        "harvested_mass_kg": round(harvested_mass_kg, 3),
        "harvested_mass_kg_per_m2": round(harvested_mass_kg / grow_area_m2, 3),
        "cull_fraction": cull_fraction,
        "saleable_harvest_mass_kg": saleable_harvest_mass_kg,
        "saleable_basis": saleable_basis,
        "output_basis": "runtime_native_calibrated_simulation",
        "estimate_status": "scenario_estimate",
        "note": "Scenario estimate, not validated. Calibrated to the UVI raft yield anchor; not observed harvest data.",
    }
    events.append(event)

    # Replant: the next cycle starts from transplant with no harvestable mass.
    plant_crop["harvestable_cut_mass_g_per_plant"] = 0.0
    plant_crop["days_since_transplant"] = 0
    return event


def main():
    scenario_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SCENARIO

    if not scenario_path.is_absolute():
        scenario_path = PROJECT_ROOT / scenario_path

    if not scenario_path.exists():
        raise FileNotFoundError(f"Scenario not found: {scenario_path}")

    scenario = load_json(scenario_path)

    water = scenario["water_state"]
    fish_batch = scenario["fish_batch"]
    plant_crop = scenario["plant_crop"]
    feeding = scenario["feeding"]
    economics = scenario["economics"]
    equipment = scenario["equipment"]
    system = scenario["system"]
    nitrogen_model = scenario["nitrogen_model"]

    water_temp_c = water.get("water_temperature_c", water.get("temperature_c"))
    air_temp_c = water.get("air_temperature_c", water_temp_c)

    fish_category, fish_filename = species_id_to_filename(fish_batch["species_id"])
    plant_category, plant_filename = species_id_to_filename(plant_crop["species_id"])

    fish_profile = load_json(SPECIES_DIR / fish_category / fish_filename)
    plant_profile = load_json(SPECIES_DIR / plant_category / plant_filename)

    fish_name = fish_filename.replace(".json", "")
    plant_name = plant_filename.replace(".json", "")

    overlap = run_overlap_score(
        fish_name=fish_name,
        plant_name=plant_name,
        pH=water["pH"],
        water_temp_c=water_temp_c,
        air_temp_c=air_temp_c,
        do_mg_l=water["dissolved_oxygen_mg_L"],
        nh3_mg_l=water["unionized_nh3_mg_L"],
        mode=system["mode"],
        ph_context=plant_ph_context(scenario),
    )

    fish_score = overlap["fish_assessment"]["overall_fish_score"]
    plant_score = overlap["plant_assessment"]["overall_plant_score"]
    nitrification_score = overlap["nitrification_assessment"]["score"]
    system_score = overlap["overall_system_score"]

    # Feeding and fish growth
    total_biomass_kg = fish_batch["total_biomass_kg"]
    growth_model = fish_profile.get("growth_feed_model") if feeding.get("growth_model") == fish_growth.MODEL_ID else None
    if feeding.get("fixed_feed_kg_per_day") is not None:
        # Fixed daily ration (published trials that feed a set amount, not % body weight).
        feed_rate_pct = 100.0 * feeding["fixed_feed_kg_per_day"] / max(total_biomass_kg, 1e-9)
        feed_rate_basis = "scenario_fixed_daily_ration"
    elif growth_model and feeding.get("feed_rate_source") == "profile_size_table":
        feed_rate_pct = fish_growth.feeding_rate_pct(fish_batch["average_weight_g"], growth_model)
        feed_rate_basis = "srac_282_size_table_midpoint_candidate"
    else:
        feed_rate_pct = feeding["feed_rate_percent_body_weight_per_day"]
        feed_rate_basis = "scenario_direct_input"
    daily_feed_kg = total_biomass_kg * (feed_rate_pct / 100.0)

    if growth_model:
        # Candidate (Batch 003): gain = feed x f_T / FCR. Water-quality stress is not applied (gap).
        fcr = growth_model["feed_conversion_ratio"]["simulation_default"]
        fish_temperature_factor = fish_growth.temperature_factor(water_temp_c, growth_model)
        fish_biomass_gain_kg = fish_growth.daily_gain_kg(daily_feed_kg, water_temp_c, growth_model, fcr)
        fish_growth_basis = "tilapia_feed_fcr_temperature_candidate"
    else:
        fcr = feeding.get("feed_conversion_ratio") or 1.5
        fish_growth_efficiency = 0.8
        fish_temperature_factor = None
        fish_biomass_gain_kg = (daily_feed_kg / fcr) * fish_score * fish_growth_efficiency
        fish_growth_basis = "placeholder_fcr_x_fish_score_x_0.8"

    fish_batch["total_biomass_kg"] = round(fish_batch["total_biomass_kg"] + fish_biomass_gain_kg, 3)
    fish_batch["average_weight_g"] = round(
        (fish_batch["total_biomass_kg"] * 1000.0) / max(fish_batch["count"], 1), 2
    )
    fish_batch["age_days"] += 1

    # Plant growth
    # Lettuce records this anchor as aquaponics_nitrate_minimal_spec_mg_L; basil records
    # it as aquaponics_nitrateN_anchor_mg_L. Before this fallback basil was never
    # nitrate-limited because the lookup always returned None.
    nutrient_response = plant_profile.get("nutrient_response", {})
    nitrate_anchor = nutrient_response.get("aquaponics_nitrate_minimal_spec_mg_L")
    if nitrate_anchor is None:
        nitrate_anchor = nutrient_response.get("aquaponics_nitrateN_anchor_mg_L")
    nitrate_state = water["nitrate_mg_L"]
    if nitrate_anchor is None or nitrate_anchor <= 0:
        nitrate_availability_score = 1.0
    else:
        nitrate_availability_score = clamp(nitrate_state / nitrate_anchor)

    # Standing biomass growth is still a placeholder rate (not calibrated).
    base_plant_growth_g_per_day = 4.0
    plant_growth_g = base_plant_growth_g_per_day * plant_score * nitrate_availability_score

    plant_crop["average_biomass_g"] = round(plant_crop["average_biomass_g"] + plant_growth_g, 2)
    plant_crop["days_since_transplant"] += 1

    # Harvestable cut mass, calibrated to the species yield anchor when available.
    relative_plant_score = plant_score_relative_to_anchor(
        plant_profile, plant_score, fish_name, plant_name, water, system["mode"], plant_ph_context(scenario)
    )
    harvest_event = update_harvestable_mass(
        scenario, plant_crop, plant_profile, relative_plant_score, nitrate_availability_score
    )

    # Nitrogen updates
    nitrate_uptake_mg_l_per_plant_day = nitrogen_model.get("nitrate_uptake_mg_l_per_plant_day", 0.05)
    water_volume_l = system["water_volume_l"]
    daily_feed_g = daily_feed_kg * 1000.0

    tan_per_g_feed_mg, tan_generation_basis = nitrification_model.tan_mg_per_g_feed(feeding, nitrogen_model)
    daily_tan_input_g = daily_feed_g * tan_per_g_feed_mg / 1000.0
    daily_tan_input_mg_l = daily_tan_input_g * 1000.0 / water_volume_l

    old_tan = water["tan_mg_L"]
    surfaces = nitrification_model.resolve_surfaces(scenario, plant_profile)
    if surfaces is not None:
        # Surface-based biofilm model (candidate): capacity from raft area and any
        # dedicated biofilter, limited by TAN concentration, pH, temperature and DO.
        model = nitrification_model.load_model()
        capacity = nitrification_model.capacity_g_tan_day(
            surfaces, model, tan_per_g_feed_mg, nitrification_model.media_feed_loading_low_end()
        )
        step = nitrification_model.step_day(
            tan_mg_l=old_tan,
            daily_tan_input_g=daily_tan_input_g,
            capacity_g_day=capacity,
            water_volume_l=water_volume_l,
            pH=water["pH"],
            water_temp_c=water_temp_c,
            do_mg_l=water["dissolved_oxygen_mg_L"],
            maturity=system.get("biofilter_maturity", 1.0),
            model=model,
            tan_saturation_mg_l=nitrogen_model.get("tan_saturation_mg_L"),
        )
        new_tan = step["new_tan_mg_L"]
        tan_removed_mg_l = step["tan_removed_mg_L"]
        steady_state = nitrification_model.steady_state_tan_mg_l(
            daily_tan_input_g, step["effective_capacity_g_tan_day"], step["tan_saturation_mg_L"]
        )
        nitrification_summary = {
            "model_basis": "biofilm_nitrification_capacity_candidate",
            "surfaces": surfaces,
            "tan_generation_basis": tan_generation_basis,
            "tan_mg_per_g_feed": round(tan_per_g_feed_mg, 3),
            "daily_tan_input_g": round(daily_tan_input_g, 3),
            **{k: v for k, v in step.items() if k not in ("new_tan_mg_L", "tan_removed_mg_L")},
            "tan_removed_g": round(step["tan_removed_g"], 3),
            "steady_state_tan_mg_L": round(steady_state, 3) if steady_state is not None else None,
        }
    else:
        # Legacy placeholder: removes a fixed fraction of today's input. Kept only for
        # scenarios with no nitrifying surface defined; TAN can climb without limit.
        nitrification_capture_efficiency = nitrogen_model.get("nitrification_capture_efficiency", 0.9)
        effective_nitrification = nitrification_score * system.get("biofilter_maturity", 1.0) * nitrification_capture_efficiency
        tan_removed_mg_l = daily_tan_input_mg_l * effective_nitrification
        new_tan = max(0.0, old_tan + daily_tan_input_mg_l - tan_removed_mg_l)
        nitrification_summary = {
            "model_basis": "legacy_placeholder_fraction_of_input",
            "tan_generation_basis": tan_generation_basis,
            "note": "No nitrification_surfaces in scenario and none derivable; placeholder used.",
        }

    nitrate_generated_mg_l = tan_removed_mg_l
    # update_harvestable_mass (above) records today's cut-mass gain, including on harvest day.
    uptake_g = shoot_n_uptake_g_day(
        plant_profile, plant_crop.get("last_daily_cut_gain_g_per_plant"), plant_crop["plant_count"]
    )
    if uptake_g is not None:
        # Growth-based uptake (candidate): today's calibrated cut-mass gain x dry matter x tissue N.
        daily_nitrate_uptake_mg_l = uptake_g * 1000.0 / water_volume_l
        nitrate_uptake_basis = "growth_based_shoot_n_uptake_candidate"
    else:
        daily_nitrate_uptake_mg_l = plant_crop["plant_count"] * nitrate_uptake_mg_l_per_plant_day * plant_score * nitrate_availability_score
        nitrate_uptake_basis = "legacy_placeholder_per_plant_rate"
    # Plants cannot take up more nitrate than the water holds.
    daily_nitrate_uptake_mg_l = min(daily_nitrate_uptake_mg_l, water["nitrate_mg_L"] + nitrate_generated_mg_l)
    sinks_cfg = system.get("nitrate_sinks")
    if isinstance(sinks_cfg, dict):
        # Water exchange and calibrated residual N loss (candidate, pending Batch 002).
        sinks_model = nitrate_sinks.load_model()
        exchange_fraction = sinks_cfg.get("water_exchange_fraction_per_day")
        if exchange_fraction is None:
            exchange_fraction = sinks_model["water_exchange"]["fraction_of_system_volume_per_day"]
        residual_fraction = sinks_cfg.get("residual_loss_fraction")
        residual_basis = "scenario_explicit"
        if residual_fraction is None and sinks_cfg.get("residual_loss") == "calibrated_uvi_filter_tanks":
            residual_fraction = nitrate_sinks.calibrated_residual_loss_fraction(sinks_model, tan_per_g_feed_mg, plant_profile)
            residual_basis = "calibrated_to_uvi_basil_nitrate_anchor"
        if residual_fraction is None:
            residual_fraction, residual_basis = 0.0, "none"
        sink_step = nitrate_sinks.apply_sinks(
            nitrate_mg_l=water["nitrate_mg_L"],
            nitrified_mg_l=nitrate_generated_mg_l,
            plant_uptake_mg_l=daily_nitrate_uptake_mg_l,
            exchange_fraction=exchange_fraction,
            residual_loss_fraction=residual_fraction,
        )
        new_nitrate = sink_step["new_nitrate_mg_L"]
        nitrate_sink_summary = {
            "model_basis": "nitrate_sinks_candidate",
            "water_exchange_fraction_per_day": exchange_fraction,
            "residual_loss_fraction": round(residual_fraction, 4),
            "residual_loss_basis": residual_basis,
            "residual_loss_mg_L": round(sink_step["residual_loss_mg_L"], 3),
            "water_exchange_loss_mg_L": round(sink_step["water_exchange_loss_mg_L"], 3),
        }
        residual_n_loss_mg_l = sink_step["residual_loss_mg_L"]
    else:
        new_nitrate = max(0.0, water["nitrate_mg_L"] + nitrate_generated_mg_l - daily_nitrate_uptake_mg_l)
        exchange_fraction, residual_n_loss_mg_l = 0.0, 0.0
        nitrate_sink_summary = {"model_basis": "none", "note": "No nitrate_sinks in scenario; only plant uptake removes nitrate."}

    water["tan_mg_L"] = round(new_tan, 3)
    water["nitrate_mg_L"] = round(new_nitrate, 3)

    chemistry_cfg = scenario.get("water_chemistry") or {}
    policy = scenario["operations_policy"]
    ph_summary = None
    if chemistry_cfg.get("model") == ph_buffer.MODEL_ID:
        # Carbonate alkalinity buffer (candidate, UQ-018): pH from an alkalinity balance.
        target_pH = None
        if policy.get("pH_control_enabled", False) and policy.get("base_dosing_enabled", False):
            target_pH = chemistry_cfg.get("target_pH", target_ph_for_mode(policy.get("target_pH_mode", system["mode"])))
        exchange = chemistry_cfg.get("water_exchange_fraction_per_day")
        if exchange is None:
            exchange = exchange_fraction
        ph_step = ph_buffer.step_day(
            water=water,
            cfg=chemistry_cfg,
            temp_c=water_temp_c,
            tan_nitrified_mg_l=tan_removed_mg_l,
            residual_n_loss_mg_l=residual_n_loss_mg_l,
            plant_no3_uptake_mg_l=daily_nitrate_uptake_mg_l,
            exchange_fraction=exchange,
            target_ph=target_pH,
            model=ph_buffer.load_model(),
        )
        water["alkalinity_mg_L_as_CaCO3"] = round(ph_step["alkalinity_mg_L_as_CaCO3"], 3)
        water["dissolved_co2_mg_L"] = round(ph_step["dissolved_co2_mg_L"], 3)
        water["pH"] = round(ph_step["pH"], 3)
        ph_summary = {
            **{k: v for k, v in ph_step.items() if k not in ("alkalinity_mg_L_as_CaCO3", "dissolved_co2_mg_L", "pH")},
            "target_pH": target_pH,
            "water_exchange_fraction_per_day": exchange,
            "base_dose_g_total": {b: round(g * water_volume_l / 1000.0, 2) for b, g in ph_step["base_dose_g_per_m3"].items()},
        }
    else:
        # Legacy placeholder: simple pH drift from nitrification acidification
        pH_drift_per_mg_l_tan_removed = nitrogen_model.get("pH_drift_per_mg_l_tan_removed", 0.01)
        pH_drop = tan_removed_mg_l * pH_drift_per_mg_l_tan_removed

        if scenario["operations_policy"].get("pH_control_enabled", False):
            target_mode = scenario["operations_policy"].get("target_pH_mode", system["mode"])
            target_pH = target_ph_for_mode(target_mode)

            corrected_pH = water["pH"] - pH_drop
            if corrected_pH < target_pH and scenario["operations_policy"].get("base_dosing_enabled", False):
                dosing_gain = min(0.15, target_pH - corrected_pH)
                corrected_pH += dosing_gain

            water["pH"] = round(corrected_pH, 3)
        else:
            water["pH"] = round(max(5.0, water["pH"] - pH_drop), 3)
        ph_summary = {"model_basis": "legacy_placeholder_drift"}

    # Unionized ammonia from TAN-N, pH and temperature (Emerson-type pKa formula).
    nh3 = nitrification_model.unionized_nh3(water["tan_mg_L"], water["pH"], water_temp_c)
    water["unionized_nh3_mg_L"] = round(nh3["nh3_mg_L"], 4)
    water["unionized_nh3_n_mg_L"] = round(nh3["nh3_n_mg_L"], 4)

    # Energy / cost
    daily_energy_kwh = (
        (equipment["pump_power_w"] * equipment["pump_hours_per_day"]) +
        (equipment["aerator_power_w"] * equipment["aerator_hours_per_day"]) +
        (equipment["heater_power_w"] * equipment["heater_hours_per_day"]) +
        (equipment["lights_power_w"] * equipment["lights_hours_per_day"])
    ) / 1000.0

    daily_energy_cost = daily_energy_kwh * economics["electricity_tariff_per_kwh"]
    daily_feed_cost = daily_feed_kg * economics["feed_cost_per_kg"]
    total_daily_operating_cost = round(daily_energy_cost + daily_feed_cost, 2)

    # Derived summary
    scenario["time"]["day"] += 1
    scenario["derived"] = {
        "daily_feed_kg": round(daily_feed_kg, 3),
        "daily_energy_kwh": round(daily_energy_kwh, 3),
        "daily_tan_input_mg_L_equivalent": round(daily_tan_input_mg_l, 3),
        "nitrification": nitrification_summary,
        "daily_nitrate_uptake_mg_L_equivalent": round(daily_nitrate_uptake_mg_l, 3),
        "nitrate_uptake_basis": nitrate_uptake_basis,
        "nitrate_sinks": nitrate_sink_summary,
        "ph_buffer": ph_summary,
        "nitrate_availability_score": round(nitrate_availability_score, 3),
        "fish_growth_score": fish_score,
        "plant_growth_score": plant_score,
        "system_stability_score": system_score,
        "daily_fish_biomass_gain_kg": round(fish_biomass_gain_kg, 3),
        "fish_growth_basis": fish_growth_basis,
        "fish_feed_rate_basis": feed_rate_basis,
        "fish_feed_rate_percent_body_weight": round(feed_rate_pct, 3),
        "fish_temperature_factor": None if fish_temperature_factor is None else round(fish_temperature_factor, 3),
        "fish_fcr_used": fcr,
        "daily_plant_biomass_gain_g_per_plant": round(plant_growth_g, 3),
        "plant_score_relative_to_anchor": round(relative_plant_score, 3),
        "harvestable_cut_mass_g_per_plant": plant_crop.get("harvestable_cut_mass_g_per_plant"),
        "harvest_event_today": harvest_event,
        "daily_operating_cost": total_daily_operating_cost
    }

    scenario["updated_at_utc"] = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    updated_scenario_path = scenario_path.parent / f"{scenario_path.stem}_day_{scenario['time']['day']}.json"
    log_path = DAYLOG_DIR / f"day_log_{scenario['time']['day']}_{timestamp}.json"

    day_log = {
        "scenario_file": str(scenario_path),
        "saved_scenario_file": str(updated_scenario_path),
        "day": scenario["time"]["day"],
        "overlap_assessment": overlap,
        "derived": scenario["derived"],
        "water_state_after": scenario["water_state"],
        "fish_batch_after": scenario["fish_batch"],
        "plant_crop_after": scenario["plant_crop"]
    }

    save_json(updated_scenario_path, scenario)
    save_json(log_path, day_log)

    print(f"Saved updated scenario to: {updated_scenario_path}")
    print(f"Saved day log to: {log_path}")
    print(json.dumps(day_log, indent=2))


if __name__ == "__main__":
    main()