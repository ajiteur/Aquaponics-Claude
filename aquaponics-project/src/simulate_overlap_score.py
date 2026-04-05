import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PARAM_LIBRARY_PATH = PROJECT_ROOT / "data" / "simulation" / "parameter_library.json"
FISH_DIR = PROJECT_ROOT / "data" / "simulation" / "species" / "fish"
PLANT_DIR = PROJECT_ROOT / "data" / "simulation" / "species" / "plants"


def load_json(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def clamp(value: float, min_value: float = 0.0, max_value: float = 1.0) -> float:
    return max(min_value, min(max_value, value))


def midpoint(min_v: float, max_v: float) -> float:
    return (min_v + max_v) / 2.0


def score_by_ranges(value: float, preferred_min: float, preferred_max: float, tolerated_min: float, tolerated_max: float) -> float:
    """
    Returns a 0..1 score.
    - 1.0 inside preferred range
    - drops linearly from preferred edge to tolerated edge
    - 0 outside tolerated range
    """
    if value < tolerated_min or value > tolerated_max:
        return 0.0

    if preferred_min <= value <= preferred_max:
        return 1.0

    if value < preferred_min:
        span = preferred_min - tolerated_min
        if span <= 0:
            return 0.0
        return clamp((value - tolerated_min) / span)

    if value > preferred_max:
        span = tolerated_max - preferred_max
        if span <= 0:
            return 0.0
        return clamp((tolerated_max - value) / span)

    return 0.0


def score_minimum_only(value: float, target_min: float, soft_floor: float | None = None) -> float:
    """
    For variables like dissolved oxygen where higher is better up to a minimum.
    - 1.0 at or above target_min
    - linear drop to 0 at soft_floor
    """
    if soft_floor is None:
        soft_floor = target_min * 0.5

    if value >= target_min:
        return 1.0
    if value <= soft_floor:
        return 0.0

    return clamp((value - soft_floor) / (target_min - soft_floor))


def score_ammonia(unionized_nh3: float, warning: float, critical: float, ceiling: float | None = None) -> float:
    """
    Lower NH3 is better.
    - <= warning: 1.0
    - warning..critical: drops to 0.5
    - critical..ceiling: drops to 0.0
    - > ceiling: 0.0
    """
    if ceiling is None:
        ceiling = critical

    if unionized_nh3 <= warning:
        return 1.0

    if unionized_nh3 <= critical:
        span = critical - warning
        if span <= 0:
            return 0.5
        return 1.0 - 0.5 * ((unionized_nh3 - warning) / span)

    if unionized_nh3 <= ceiling:
        span = ceiling - critical
        if span <= 0:
            return 0.0
        return 0.5 * (1.0 - ((unionized_nh3 - critical) / span))

    return 0.0


def score_mode_ph(pH: float, mode_range: list[float], tolerated_range: list[float] | None = None) -> float:
    mode_min, mode_max = mode_range
    if tolerated_range is None:
        tolerated_range = [mode_min, mode_max]

    tol_min, tol_max = tolerated_range
    return score_by_ranges(pH, mode_min, mode_max, tol_min, tol_max)

def get_mode_ranges(parameter_library: dict, mode_name: str) -> tuple[list[float], list[float]]:
    mode = parameter_library["process_modes"][mode_name]
    target_range = mode["target_pH_range"]

    if "tolerable_range" in mode:
        tolerable_range = mode["tolerable_range"]
    else:
        global_tol = parameter_library["parameters"]["pH_tolerable_all_components"]
        tolerable_range = [
            min(target_range[0], global_tol["min"]),
            max(target_range[1], global_tol["max"])
        ]

    return target_range, tolerable_range


def compute_balance_score(scores: list[float]) -> float:
    valid = [s for s in scores if s is not None]
    if not valid:
        return 0.0

    max_score = max(valid)
    min_score = min(valid)

    if max_score <= 0:
        return 0.0

    return round(min_score / max_score, 3)


def nitrification_score_from_library(pH: float, library: dict) -> dict:
    inhibited_at = library["parameters"]["nitrification_inhibited_at_or_below_pH"]["max"]
    dieoff_below = library["parameters"]["nitrifier_dieoff_risk_below_pH"]["max"]

    if pH < dieoff_below:
        return {
            "score": 0.0,
            "status": "critical",
            "note": f"pH below {dieoff_below} creates nitrifier dieoff risk."
        }

    if pH <= inhibited_at:
        return {
            "score": 0.4,
            "status": "warning",
            "note": f"pH at or below {inhibited_at} inhibits nitrification."
        }

    return {
        "score": 1.0,
        "status": "ok",
        "note": "No low-pH nitrification penalty triggered."
    }


def plant_ph_tradeoff_warning(pH: float, library: dict) -> dict:
    high_ph = library["parameters"]["plant_nutrient_availability_declines_above_pH"]["min"]
    low_ph = library["parameters"]["phosphorus_solubility_declines_below_pH"]["max"]

    warnings = []

    if pH > high_ph:
        warnings.append(f"Some nutrient availability may decline above pH {high_ph}.")

    if pH < low_ph:
        warnings.append(f"Phosphorus solubility may decline below pH {low_ph}.")

    return {
        "triggered": len(warnings) > 0,
        "messages": warnings
    }


def load_species_profile(species_name: str, category: str) -> dict | None:
    if category == "fish":
        path = FISH_DIR / f"{species_name}.json"
    else:
        path = PLANT_DIR / f"{species_name}.json"

    if not path.exists():
        return None

    return load_json(path)


def has_complete_range(profile: dict, path: list[str]) -> bool:
    node = profile
    for key in path:
        if key not in node:
            return False
        node = node[key]
    return isinstance(node, dict) and node.get("min") is not None and node.get("max") is not None


def score_fish(profile: dict, pH: float, water_temp_c: float, do_mg_l: float, unionized_nh3_mg_l: float) -> dict:
    env = profile["environment"]
    chem = profile["chemistry_response"]

    pH_score = score_by_ranges(
        pH,
        env["preferred_pH"]["min"],
        env["preferred_pH"]["max"],
        env["tolerated_pH"]["min"],
        env["tolerated_pH"]["max"],
    )

    temp_score = score_by_ranges(
    water_temp_c,
    env["preferred_temp_c"]["min"],
    env["preferred_temp_c"]["max"],
    env["tolerated_temp_c"]["min"],
    env["tolerated_temp_c"]["max"],
   )

    # Tilapia-specific operational soft floor from your evidence notes
    do_score = score_minimum_only(
        do_mg_l,
        env["minimum_dissolved_oxygen_mg_L"],
        soft_floor=3.5
    )

    nh3_score = score_ammonia(
        unionized_nh3_mg_l,
        chem["unionized_nh3_warning_mg_L"],
        chem["unionized_nh3_critical_mg_L"],
        chem.get("nh3_upper_ceiling_guidance_mg_L", chem["unionized_nh3_critical_mg_L"])
    )

    overall = round((pH_score + temp_score + do_score + nh3_score) / 4.0, 3)

    return {
        "species_id": profile["species_id"],
        "pH_score": round(pH_score, 3),
        "temperature_score": round(temp_score, 3),
        "dissolved_oxygen_score": round(do_score, 3),
        "unionized_nh3_score": round(nh3_score, 3),
        "overall_fish_score": overall
    }


def score_plant(profile: dict, pH: float, air_temp_c: float) -> dict:
    env = profile["environment"]

    if not has_complete_range(profile, ["environment", "preferred_pH"]) or not has_complete_range(profile, ["environment", "tolerated_pH"]):
        return {
            "species_id": profile.get("species_id"),
            "status": "incomplete_profile",
            "note": "Plant pH ranges are not filled yet."
        }

    if not has_complete_range(profile, ["environment", "preferred_temp_c"]) or not has_complete_range(profile, ["environment", "tolerated_temp_c"]):
        return {
            "species_id": profile.get("species_id"),
            "status": "incomplete_profile",
            "note": "Plant temperature ranges are not filled yet."
        }

    pH_score = score_by_ranges(
        pH,
        env["preferred_pH"]["min"],
        env["preferred_pH"]["max"],
        env["tolerated_pH"]["min"],
        env["tolerated_pH"]["max"],
    )

    temp_score = score_by_ranges(
        air_temp_c,
    env["preferred_temp_c"]["min"],
    env["preferred_temp_c"]["max"],
    env["tolerated_temp_c"]["min"],
    env["tolerated_temp_c"]["max"],
    )

    overall = round((pH_score + temp_score) / 2.0, 3)

    return {
        "species_id": profile["species_id"],
        "pH_score": round(pH_score, 3),
        "temperature_score": round(temp_score, 3),
        "overall_plant_score": overall
    }


def main():
    if len(sys.argv) < 7:
        raise ValueError(
        "Usage:\n"
        "python src/simulate_overlap_score.py <fish_name> <plant_name_or_none> <pH> <water_temp_c> <air_temp_c> <do_mg_l> <unionized_nh3_mg_l> [mode]\n\n"
        "Example:\n"
        "python src/simulate_overlap_score.py tilapia lettuce 6.9 28 24 5.5 0.05 robust_compromise_mode"
       )

    fish_name = sys.argv[1]
    plant_name = sys.argv[2]
    pH = float(sys.argv[3])
    water_temp_c = float(sys.argv[4]) 
    air_temp_c = float(sys.argv[5])
    do_mg_l = float(sys.argv[6])
    unionized_nh3_mg_l = float(sys.argv[7]) if len(sys.argv) > 7 else 0.05
    mode_name = sys.argv[8] if len(sys.argv) > 8 else "robust_compromise_mode"

    parameter_library = load_json(PARAM_LIBRARY_PATH)

    fish_profile = load_species_profile(fish_name, "fish")
    if fish_profile is None:
        raise FileNotFoundError(f"Fish profile not found: {fish_name}")

    plant_profile = None
    if plant_name.lower() != "none":
        plant_profile = load_species_profile(plant_name, "plant")
        if plant_profile is None:
            raise FileNotFoundError(f"Plant profile not found: {plant_name}")

    if mode_name not in parameter_library["process_modes"]:
        raise ValueError(f"Unknown mode: {mode_name}")

    mode_range, tolerated_range = get_mode_ranges(parameter_library, mode_name)
    mode_pH_score = score_mode_ph(pH, mode_range, tolerated_range)
    nitrification = nitrification_score_from_library(pH, parameter_library)
    plant_tradeoff = plant_ph_tradeoff_warning(pH, parameter_library)

    fish_result = score_fish(fish_profile, pH, water_temp_c, do_mg_l, unionized_nh3_mg_l)

    plant_result = None
    if plant_profile is not None:
        plant_result = score_plant(plant_profile, pH, air_temp_c)

        components = [
        fish_result["overall_fish_score"],
        round(mode_pH_score, 3),
        nitrification["score"]
    ]

    if plant_result and "overall_plant_score" in plant_result:
        components.append(plant_result["overall_plant_score"])

    raw_average_score = round(sum(components) / len(components), 3)
    balance_score = compute_balance_score(components)

    overall_system_score = round(raw_average_score * (0.5 + 0.5 * balance_score), 3)

    output = {
        "inputs": {
            "fish": fish_name,
            "plant": plant_name,
            "pH": pH,
            "water_temperature_c": water_temp_c,
            "air_temperature_c": air_temp_c,
            "dissolved_oxygen_mg_L": do_mg_l,
            "unionized_nh3_mg_L": unionized_nh3_mg_l,
            "mode": mode_name
        },
        "mode_assessment": {
            "target_range": mode_range,
            "tolerable_range": tolerated_range,
            "mode_pH_score": round(mode_pH_score, 3)
        },
        "fish_assessment": fish_result,
        "plant_assessment": plant_result,
        "nitrification_assessment": nitrification,
        "plant_tradeoff_warning": plant_tradeoff,
        "raw_average_score": raw_average_score,
        "balance_score": balance_score,
        "overall_system_score": overall_system_score
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()