import json
from pathlib import Path
from datetime import datetime, UTC

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SIM_DIR = PROJECT_ROOT / "data" / "simulation"
SIM_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_PATH = SIM_DIR / "parameter_library.json"

parameter_library = {
    "generated_at_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "version": "0.1",
    "notes": [
        "Seeded from corroborated Layer 1 parameter report.",
        "These are simulation inputs, not final universal truths.",
        "Use strategy modes instead of one single global pH rule."
    ],
    "parameters": {
        "pH_target_general": {
            "kind": "range",
            "min": 6.0,
            "max": 7.0,
            "unit": "pH",
            "status": "accepted_candidate",
            "description": "General operational target range for aquaponics systems."
        },
        "pH_compromise_optimal": {
            "kind": "range",
            "min": 6.8,
            "max": 7.0,
            "unit": "pH",
            "status": "accepted_candidate",
            "description": "Compromise range balancing fish, plants, and nitrifiers."
        },
        "pH_tolerable_all_components": {
            "kind": "range",
            "min": 6.4,
            "max": 7.4,
            "unit": "pH",
            "status": "accepted_candidate",
            "description": "Tolerable envelope for fish, plants, and nitrifiers."
        },
        "TAN_guideline_mg_L": {
            "kind": "upper_bound",
            "max": 1.0,
            "unit": "mg/L",
            "status": "guidance_candidate",
            "description": "Recommended TAN guidance level; interpret with pH and temperature."
        },
        "unionized_NH3_monitor_mg_L": {
            "kind": "warning_threshold",
            "value": 0.25,
            "unit": "mg/L",
            "severity": "warning",
            "description": "Increase monitoring at or above this unionized ammonia level."
        },
        "unionized_NH3_mortality_mg_L": {
            "kind": "warning_threshold",
            "value": 0.50,
            "unit": "mg/L",
            "severity": "critical",
            "description": "Fish mortality risk threshold."
        },
        "alkalinity_target_mg_L_as_CaCO3": {
            "kind": "lower_bound",
            "min": 100.0,
            "unit": "mg/L as CaCO3",
            "status": "accepted_candidate",
            "description": "Target alkalinity to stabilize pH and support nitrification."
        },
        "nitrification_inhibited_at_or_below_pH": {
            "kind": "upper_bound",
            "max": 6.0,
            "unit": "pH",
            "severity": "warning",
            "description": "Nitrification inhibition begins around or below this pH."
        },
        "nitrifier_dieoff_risk_below_pH": {
            "kind": "upper_bound",
            "max": 5.5,
            "unit": "pH",
            "severity": "critical",
            "description": "Nitrifier dieoff risk below this pH."
        },
        "plant_nutrient_availability_declines_above_pH": {
            "kind": "lower_bound",
            "min": 7.0,
            "unit": "pH",
            "severity": "warning",
            "description": "Some nutrients become less available above this pH."
        },
        "phosphorus_solubility_declines_below_pH": {
            "kind": "upper_bound",
            "max": 6.0,
            "unit": "pH",
            "severity": "warning",
            "description": "Phosphorus solubility decreases sharply below this pH."
        },
        "hydroponic_baseline_best_pH": {
            "kind": "range",
            "min": 5.8,
            "max": 6.2,
            "unit": "pH",
            "description": "Hydroponic plant best-performance baseline."
        },
        "hydroponic_baseline_acceptable_pH": {
            "kind": "range",
            "min": 5.5,
            "max": 6.5,
            "unit": "pH",
            "description": "Hydroponic plant acceptable baseline."
        }
    },
    "process_modes": {
        "robust_compromise_mode": {
            "target_pH_range": [6.8, 7.0],
            "description": "General-purpose robust aquaponics compromise mode."
        },
        "broad_operational_mode": {
            "target_pH_range": [6.0, 7.0],
            "description": "General target band for practical system operation."
        },
        "plant_yield_optimization_mode": {
            "target_pH_range": [6.0, 6.5],
            "description": "Plant-favoring mode; requires stronger nitrification and TAN monitoring."
        }
    },
    "dependencies": [
        {
            "if": {"parameter": "pH", "operator": "<=", "value": 6.0},
            "then": {"effect": "nitrification_efficiency_declines", "severity": "warning"}
        },
        {
            "if": {"parameter": "pH", "operator": "<", "value": 5.5},
            "then": {"effect": "nitrifier_dieoff_risk", "severity": "critical"}
        },
        {
            "if": {"parameter": "pH", "operator": ">", "value": 7.0},
            "then": {"effect": "some_micronutrient_availability_declines", "severity": "warning"}
        },
        {
            "if": {"parameter": "unionized_NH3_mg_L", "operator": ">=", "value": 0.25},
            "then": {"effect": "increase_monitoring", "severity": "warning"}
        },
        {
            "if": {"parameter": "unionized_NH3_mg_L", "operator": ">=", "value": 0.50},
            "then": {"effect": "fish_mortality_risk", "severity": "critical"}
        }
    ],
    "next_species_to_collect": {
        "fish": ["tilapia", "channel_catfish", "trout"],
        "plants": ["lettuce", "basil", "tomato"]
    }
}

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(parameter_library, f, indent=2)

print(f"Saved parameter library to: {OUTPUT_PATH}")