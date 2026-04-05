from pathlib import Path
import json
import subprocess
import sys
from datetime import datetime, UTC

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


def clamp(value: float, min_value: float = 0.0, max_value: float = 1.0) -> float:
    return max(min_value, min(max_value, value))


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
    nitrate_anchor = (
        plant_profile.get("nutrient_response", {}).get("aquaponics_nitrate_minimal_spec_mg_L")
    )
    nitrate_state = water["nitrate_mg_L"]
    if nitrate_anchor is None or nitrate_anchor <= 0:
        nitrate_availability_score = 1.0
    else:
        nitrate_availability_score = clamp(nitrate_state / nitrate_anchor)

    base_plant_growth_g_per_day = 4.0
    plant_growth_g = base_plant_growth_g_per_day * plant_score * nitrate_availability_score

    plant_crop["average_biomass_g"] = round(plant_crop["average_biomass_g"] + plant_growth_g, 2)
    plant_crop["days_since_transplant"] += 1

    # Nitrogen updates
    tan_generation_mg_per_g_feed = nitrogen_model.get("tan_generation_mg_per_g_feed", 30.0)
    nitrification_capture_efficiency = nitrogen_model.get("nitrification_capture_efficiency", 0.9)
    nitrate_uptake_mg_l_per_plant_day = nitrogen_model.get("nitrate_uptake_mg_l_per_plant_day", 0.05)

    water_volume_l = system["water_volume_l"]
    daily_feed_g = daily_feed_kg * 1000.0

    daily_tan_input_mg_l = (daily_feed_g * tan_generation_mg_per_g_feed) / water_volume_l
    effective_nitrification = nitrification_score * system.get("biofilter_maturity", 1.0) * nitrification_capture_efficiency
    tan_removed_mg_l = daily_tan_input_mg_l * effective_nitrification

    old_tan = water["tan_mg_L"]
    new_tan = max(0.0, old_tan + daily_tan_input_mg_l - tan_removed_mg_l)

    old_unionized_nh3 = water["unionized_nh3_mg_L"]
    if old_tan > 0:
        new_unionized_nh3 = old_unionized_nh3 * (new_tan / old_tan)
    else:
        new_unionized_nh3 = old_unionized_nh3

    nitrate_generated_mg_l = tan_removed_mg_l
    daily_nitrate_uptake_mg_l = plant_crop["plant_count"] * nitrate_uptake_mg_l_per_plant_day * plant_score * nitrate_availability_score
    new_nitrate = max(0.0, water["nitrate_mg_L"] + nitrate_generated_mg_l - daily_nitrate_uptake_mg_l)

    water["tan_mg_L"] = round(new_tan, 3)
    water["unionized_nh3_mg_L"] = round(new_unionized_nh3, 3)
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
        "daily_nitrate_uptake_mg_L_equivalent": round(daily_nitrate_uptake_mg_l, 3),
        "nitrate_availability_score": round(nitrate_availability_score, 3),
        "fish_growth_score": fish_score,
        "plant_growth_score": plant_score,
        "system_stability_score": system_score,
        "daily_fish_biomass_gain_kg": round(fish_biomass_gain_kg, 3),
        "daily_plant_biomass_gain_g_per_plant": round(plant_growth_g, 3),
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