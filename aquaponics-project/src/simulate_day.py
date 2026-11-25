from pathlib import Path
import json
import subprocess
import sys
from datetime import datetime, UTC

import nitrification_model

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
    daily_gain = calibration["ideal_rate_g_per_plant_day"] * plant_score * nitrate_availability_score
    plant_crop["harvestable_cut_mass_g_per_plant"] = round(
        plant_crop.get("harvestable_cut_mass_g_per_plant", 0.0) + daily_gain, 3
    )
    plant_crop["harvest_calibration"] = calibration

    if plant_crop["days_since_transplant"] < period_days:
        return None

    plant_count = plant_crop["plant_count"]
    harvested_mass_kg = plant_count * plant_crop["harvestable_cut_mass_g_per_plant"] / 1000.0
    grow_area_m2 = plant_count / calibration["planting_density_plants_m2"]
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
        "grow_area_m2_at_anchor_density": round(grow_area_m2, 3),
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
    feed_rate_pct = feeding["feed_rate_percent_body_weight_per_day"]
    daily_feed_kg = total_biomass_kg * (feed_rate_pct / 100.0)

    fcr = feeding.get("feed_conversion_ratio") or 1.5
    fish_growth_efficiency = 0.8
    fish_biomass_gain_kg = (daily_feed_kg / fcr) * fish_score * fish_growth_efficiency

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
    daily_nitrate_uptake_mg_l = plant_crop["plant_count"] * nitrate_uptake_mg_l_per_plant_day * plant_score * nitrate_availability_score
    new_nitrate = max(0.0, water["nitrate_mg_L"] + nitrate_generated_mg_l - daily_nitrate_uptake_mg_l)

    water["tan_mg_L"] = round(new_tan, 3)
    water["nitrate_mg_L"] = round(new_nitrate, 3)

    # Simple pH drift from nitrification acidification
    pH_drift_per_mg_l_tan_removed = nitrogen_model.get("pH_drift_per_mg_l_tan_removed", 0.01)
    pH_drop = tan_removed_mg_l * pH_drift_per_mg_l_tan_removed

    if scenario["operations_policy"].get("pH_control_enabled", False):
        target_mode = scenario["operations_policy"].get("target_pH_mode", system["mode"])
        if target_mode == "plant_yield_optimization_mode":
            target_pH = 6.25
        elif target_mode == "robust_compromise_mode":
            target_pH = 6.9
        else:
            target_pH = 6.5

        corrected_pH = water["pH"] - pH_drop
        if corrected_pH < target_pH and scenario["operations_policy"].get("base_dosing_enabled", False):
            dosing_gain = min(0.15, target_pH - corrected_pH)
            corrected_pH += dosing_gain

        water["pH"] = round(corrected_pH, 3)
    else:
        water["pH"] = round(max(5.0, water["pH"] - pH_drop), 3)

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
        "nitrate_availability_score": round(nitrate_availability_score, 3),
        "fish_growth_score": fish_score,
        "plant_growth_score": plant_score,
        "system_stability_score": system_score,
        "daily_fish_biomass_gain_kg": round(fish_biomass_gain_kg, 3),
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