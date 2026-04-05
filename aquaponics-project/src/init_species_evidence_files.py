from pathlib import Path
import json
from datetime import datetime, UTC

PROJECT_ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = PROJECT_ROOT / "data" / "simulation" / "species_evidence"

generated_at = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

templates = {
    "tilapia_evidence.json": {
        "species_id": "fish_tilapia",
        "generated_at_utc": generated_at,
        "target_fields": [
            "preferred_pH",
            "tolerated_pH",
            "preferred_temp_c",
            "tolerated_temp_c",
            "minimum_dissolved_oxygen_mg_L",
            "unionized_nh3_warning_mg_L",
            "unionized_nh3_critical_mg_L",
            "growth_notes",
            "stress_notes"
        ],
        "evidence_records": []
    },
    "lettuce_evidence.json": {
        "species_id": "plant_lettuce",
        "generated_at_utc": generated_at,
        "target_fields": [
            "preferred_pH",
            "tolerated_pH",
            "preferred_temp_c",
            "tolerated_temp_c",
            "nitrate_demand_level",
            "growth_notes",
            "stress_notes",
            "high_pH_nutrient_lockout_notes",
            "low_pH_sensitivity_notes"
        ],
        "evidence_records": []
    },
    "basil_evidence.json": {
        "species_id": "plant_basil",
        "generated_at_utc": generated_at,
        "target_fields": [
            "preferred_pH",
            "tolerated_pH",
            "preferred_temp_c",
            "tolerated_temp_c",
            "nitrate_demand_level",
            "growth_notes",
            "stress_notes",
            "high_pH_nutrient_lockout_notes",
            "low_pH_sensitivity_notes"
        ],
        "evidence_records": []
    }
}

EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

for filename, payload in templates.items():
    path = EVIDENCE_DIR / filename
    if not path.exists():
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)

print("Created species evidence files:")
for filename in templates:
    print(f" - {EVIDENCE_DIR / filename}")