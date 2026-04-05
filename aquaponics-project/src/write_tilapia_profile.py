from pathlib import Path
import json
from datetime import datetime, UTC

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SPECIES_PATH = PROJECT_ROOT / "data" / "simulation" / "species" / "fish" / "tilapia.json"
EVIDENCE_PATH = PROJECT_ROOT / "data" / "simulation" / "species_evidence" / "tilapia_evidence.json"

SPECIES_PATH.parent.mkdir(parents=True, exist_ok=True)
EVIDENCE_PATH.parent.mkdir(parents=True, exist_ok=True)

generated_at = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

tilapia_profile = {
    "species_id": "fish_tilapia",
    "scientific_name": "Oreochromis niloticus",
    "common_name": "Nile tilapia",
    "category": "fish",
    "status": "starter_profile",
    "generated_at_utc": generated_at,
    "environment": {
        "preferred_pH": {"min": 6.5, "max": 8.5, "unit": "pH"},
        "tolerated_pH": {"min": 5.0, "max": 10.0, "unit": "pH"},
        "preferred_temp_c": {"min": 27.0, "max": 30.0, "unit": "C"},
        "tolerated_temp_c": {"min": 25.0, "max": 32.0, "unit": "C"},
        "minimum_dissolved_oxygen_mg_L": 5.0
    },
    "chemistry_response": {
        "unionized_nh3_warning_mg_L": 0.08,
        "unionized_nh3_critical_mg_L": 0.2,
        "nh3_upper_ceiling_guidance_mg_L": 1.0
    },
    "simulation_weights": {
        "pH_weight": 1.0,
        "temperature_weight": 1.0,
        "oxygen_weight": 1.0,
        "ammonia_weight": 1.0
    },
    "growth_notes": [
        "Temperature strongly drives growth: near optimal temperatures, growth can be about 3x that at about 22 C.",
        "Under good temperature regimes, males may reach about 200 g in 3 to 4 months and about 400 g in 5 to 6 months, depending on system design."
    ],
    "stress_notes": [
        "Chronic dissolved oxygen below about 3.5 mg/L reduces growth and feed conversion.",
        "Handling or harvest in cooler water increases disease-induced mortality risk."
    ],
    "validation_benchmarks": {
        "uvi_aquaponics_context": {
            "pH_range": {"min": 7.0, "max": 7.5, "unit": "pH"},
            "rearing_tank_do_mg_L": {
                "lettuce_trials": {"min": 5.0, "max": 6.0},
                "basil_trials": {"min": 4.0, "max": 5.0}
            },
            "tan_mg_L": {"min": 1.1, "max": 2.9},
            "notes": "Use as aquaponics validation benchmark, not as universal species requirement."
        }
    },
    "future_fields": {
        "temp_optimal_growth_tank_c": {"min": 27.0, "max": 29.0, "unit": "C"},
        "temp_optimal_growth_general_c": {"min": 29.0, "max": 31.0, "unit": "C"},
        "temp_habitat_preferred_c": {"min": 31.0, "max": 36.0, "unit": "C"},
        "lethal_temp_low_c": {"min": 10.0, "max": 12.0, "unit": "C"},
        "feeding_stops_below_temp_c": 17.2
    },
    "evidence": [
        {
            "source_id": "srac_282_tank_culture",
            "type": "university_extension_pdf",
            "notes": "Tank or RAS operating ranges for temperature, dissolved oxygen, pH and NH3 guidance."
        },
        {
            "source_id": "srac_283_life_history_biology",
            "type": "university_extension_pdf",
            "notes": "Tolerance thresholds, NH3 sensitivity ladder, cold stress and disease notes."
        },
        {
            "source_id": "worldfish_water_quality_management_2022",
            "type": "institutional_pdf",
            "notes": "Ideal ranges for temperature, dissolved oxygen and pH."
        },
        {
            "source_id": "uvi_tilapia_basil_aquaponics",
            "type": "experiment_station_pdf",
            "notes": "Aquaponics-specific operating benchmark and validation values."
        },
        {
            "source_id": "fao_nile_tilapia_species_info",
            "type": "official_reference_page",
            "notes": "Species anchor and hard-bound temperature context."
        }
    ]
}

tilapia_evidence = {
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
        "nh3_upper_ceiling_guidance_mg_L",
        "growth_notes",
        "stress_notes"
    ],
    "evidence_records": [
        {
            "field": "preferred_pH",
            "value": {"min": 6.5, "max": 8.5, "unit": "pH"},
            "source_id": "worldfish_water_quality_management_2022",
            "trust_tier": "tier_2",
            "status": "promote",
            "notes": "Ideal pH for growth and survival."
        },
        {
            "field": "tolerated_pH",
            "value": {"min": 5.0, "max": 10.0, "unit": "pH"},
            "source_id": "srac_283_life_history_biology",
            "trust_tier": "tier_1",
            "status": "promote",
            "notes": "Survivable range; do best around 6 to 9."
        },
        {
            "field": "preferred_temp_c",
            "value": {"min": 27.0, "max": 30.0, "unit": "C"},
            "source_id": "worldfish_water_quality_management_2022",
            "trust_tier": "tier_2",
            "status": "promote",
            "notes": "Optimal survival range."
        },
        {
            "field": "preferred_temp_c",
            "value": {"min": 27.0, "max": 29.0, "unit": "C"},
            "source_id": "srac_282_tank_culture",
            "trust_tier": "tier_1",
            "status": "promote",
            "notes": "Tank growth optimum."
        },
        {
            "field": "tolerated_temp_c",
            "value": {"min": 25.0, "max": 32.0, "unit": "C"},
            "source_id": "srac_282_tank_culture",
            "trust_tier": "tier_1",
            "status": "promote",
            "notes": "Acceptable growth range."
        },
        {
            "field": "minimum_dissolved_oxygen_mg_L",
            "value": 5.0,
            "source_id": "srac_282_tank_culture",
            "trust_tier": "tier_1",
            "status": "promote",
            "notes": "Use 5 mg/L as operational minimum for good growth."
        },
        {
            "field": "unionized_nh3_warning_mg_L",
            "value": 0.08,
            "source_id": "srac_283_life_history_biology",
            "trust_tier": "tier_1",
            "status": "promote",
            "notes": "Feeding suppression begins."
        },
        {
            "field": "unionized_nh3_critical_mg_L",
            "value": 0.2,
            "source_id": "srac_283_life_history_biology",
            "trust_tier": "tier_1",
            "status": "promote_with_context",
            "notes": "First mortalities may begin under prolonged exposure; context dependent."
        },
        {
            "field": "nh3_upper_ceiling_guidance_mg_L",
            "value": 1.0,
            "source_id": "srac_282_tank_culture",
            "trust_tier": "tier_1",
            "status": "promote",
            "notes": "Upper ceiling guidance in tank culture."
        },
        {
            "field": "validation_benchmark",
            "value": {
                "pH_min": 7.0,
                "pH_max": 7.5,
                "do_lettuce_trials_min": 5.0,
                "do_lettuce_trials_max": 6.0,
                "do_basil_trials_min": 4.0,
                "do_basil_trials_max": 5.0,
                "tan_min": 1.1,
                "tan_max": 2.9
            },
            "source_id": "uvi_tilapia_basil_aquaponics",
            "trust_tier": "tier_1",
            "status": "validation_only",
            "notes": "Aquaponics benchmark, not universal requirement."
        },
        {
            "field": "future_fields",
            "value": {
                "temp_habitat_preferred_c": {"min": 31.0, "max": 36.0},
                "lethal_temp_low_c": {"min": 10.0, "max": 12.0},
                "feeding_stops_below_temp_c": 17.2
            },
            "source_id": "fao_nile_tilapia_species_info",
            "trust_tier": "tier_1",
            "status": "keep_as_evidence_note",
            "notes": "Useful for later cold snap and reproduction mechanics."
        }
    ]
}

with open(SPECIES_PATH, "w", encoding="utf-8") as f:
    json.dump(tilapia_profile, f, indent=2)

with open(EVIDENCE_PATH, "w", encoding="utf-8") as f:
    json.dump(tilapia_evidence, f, indent=2)

print(f"Wrote species profile: {SPECIES_PATH}")
print(f"Wrote evidence file: {EVIDENCE_PATH}")