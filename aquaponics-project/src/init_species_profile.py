from pathlib import Path
import json
from datetime import datetime, UTC

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SPECIES_DIR = PROJECT_ROOT / "data" / "simulation" / "species"
FISH_DIR = SPECIES_DIR / "fish"
PLANT_DIR = SPECIES_DIR / "plants"

FISH_DIR.mkdir(parents=True, exist_ok=True)
PLANT_DIR.mkdir(parents=True, exist_ok=True)

generated_at = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

templates = {
    FISH_DIR / "tilapia.json": {
        "species_id": "fish_tilapia",
        "common_name": "Tilapia",
        "category": "fish",
        "status": "template",
        "generated_at_utc": generated_at,
        "environment": {
            "preferred_pH": {"min": None, "max": None, "unit": "pH"},
            "tolerated_pH": {"min": None, "max": None, "unit": "pH"},
            "preferred_temp_c": {"min": None, "max": None, "unit": "C"},
            "tolerated_temp_c": {"min": None, "max": None, "unit": "C"},
            "minimum_dissolved_oxygen_mg_L": None
        },
        "chemistry_response": {
            "unionized_nh3_warning_mg_L": None,
            "unionized_nh3_critical_mg_L": None,
            "tan_guidance_notes": []
        },
        "simulation_weights": {
            "pH_weight": 1.0,
            "temperature_weight": 1.0,
            "oxygen_weight": 1.0,
            "ammonia_weight": 1.0
        },
        "growth_notes": [],
        "stress_notes": [],
        "evidence": []
    },
    PLANT_DIR / "lettuce.json": {
        "species_id": "plant_lettuce",
        "common_name": "Lettuce",
        "category": "plant",
        "status": "template",
        "generated_at_utc": generated_at,
        "environment": {
            "preferred_pH": {"min": None, "max": None, "unit": "pH"},
            "tolerated_pH": {"min": None, "max": None, "unit": "pH"},
            "preferred_temp_c": {"min": None, "max": None, "unit": "C"},
            "tolerated_temp_c": {"min": None, "max": None, "unit": "C"}
        },
        "nutrient_response": {
            "nitrate_demand_level": None,
            "high_pH_nutrient_lockout_notes": [],
            "low_pH_sensitivity_notes": []
        },
        "simulation_weights": {
            "pH_weight": 1.0,
            "temperature_weight": 1.0,
            "nitrate_weight": 1.0
        },
        "growth_notes": [],
        "stress_notes": [],
        "evidence": []
    },
    PLANT_DIR / "basil.json": {
        "species_id": "plant_basil",
        "common_name": "Basil",
        "category": "plant",
        "status": "template",
        "generated_at_utc": generated_at,
        "environment": {
            "preferred_pH": {"min": None, "max": None, "unit": "pH"},
            "tolerated_pH": {"min": None, "max": None, "unit": "pH"},
            "preferred_temp_c": {"min": None, "max": None, "unit": "C"},
            "tolerated_temp_c": {"min": None, "max": None, "unit": "C"}
        },
        "nutrient_response": {
            "nitrate_demand_level": None,
            "high_pH_nutrient_lockout_notes": [],
            "low_pH_sensitivity_notes": []
        },
        "simulation_weights": {
            "pH_weight": 1.0,
            "temperature_weight": 1.0,
            "nitrate_weight": 1.0
        },
        "growth_notes": [],
        "stress_notes": [],
        "evidence": []
    }
}

for path, payload in templates.items():
    if not path.exists():
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)

print("Created species profile templates:")
for path in templates:
    print(f" - {path}")