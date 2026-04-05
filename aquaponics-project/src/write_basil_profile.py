from pathlib import Path
import json
from datetime import datetime, UTC

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SPECIES_PATH = PROJECT_ROOT / "data" / "simulation" / "species" / "plants" / "basil.json"
EVIDENCE_PATH = PROJECT_ROOT / "data" / "simulation" / "species_evidence" / "basil_evidence.json"

SPECIES_PATH.parent.mkdir(parents=True, exist_ok=True)
EVIDENCE_PATH.parent.mkdir(parents=True, exist_ok=True)

generated_at = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

basil_profile = {
    "species_id": "plant_basil",
    "scientific_name": "Ocimum basilicum",
    "common_name": "Sweet basil",
    "category": "plant",
    "status": "starter_profile",
    "generated_at_utc": generated_at,
    "environment": {
        "preferred_pH": {"min": 5.8, "max": 6.2, "unit": "pH"},
        "tolerated_pH": {"min": 5.5, "max": 6.5, "unit": "pH"},
        "preferred_temp_c": {"min": 26.0, "max": 28.0, "unit": "C"},
        "tolerated_temp_c": {"min": 10.0, "max": 31.0, "unit": "C"}
    },
    "nutrient_response": {
        "nitrate_demand_level": "moderate",
        "hydroponic_n_target_ppm": {
            "min": 100.0,
            "max": 150.0,
            "unit": "ppm N"
        },
        "preferred_ec_mS_cm": {
            "min": 0.5,
            "max": 1.5,
            "unit": "mS/cm"
        },
        "operational_ec_mS_cm": {
            "min": 1.0,
            "max": 1.6,
            "unit": "mS/cm"
        },
        "aquaponics_nitrate_n_anchor_mg_L": 42.0,
        "high_pH_nutrient_lockout_notes": [
            "At pH above about 6.5, basil risk increases for iron deficiency and interveinal chlorosis.",
            "Aquaponics can still operate near neutral pH, but supplementation with Ca, K, and Fe may be needed."
        ],
        "low_pH_sensitivity_notes": [
            "Below about pH 5.8, basil risk increases for iron and manganese toxicity symptoms.",
            "Corrective action thresholds are suggested around 5.5 to 5.7 on the low side."
        ]
    },
    "simulation_weights": {
        "pH_weight": 1.0,
        "temperature_weight": 1.0,
        "nitrate_weight": 1.0
    },
    "growth_notes": [
        "Aquaponic basil yield anchor: about 2.0 kg/m2 in batch production and about 1.8 kg/m2 in staggered production under UVI commercial-scale conditions.",
        "Cultivar selection affects basil yield more than the difference between common hydroponic systems such as NFT versus DFT.",
        "Preferred root-zone or nutrient solution temperature is about 27.5 C for greater growth for most cultivars."
    ],
    "stress_notes": [
        "Basil is chilling sensitive: temperatures below about 10 C can cause chilling injury and marketability loss, with severe injury at 5 C or below.",
        "Successive cutting can weaken basil plants and increase root disease risk such as Pythium in aquaponic systems.",
        "Downy mildew risk increases when leaf wetness lasts at least 4 hours and night humidity exceeds 95 percent for at least 7.5 hours."
    ],
    "validation_benchmarks": {
        "hydroponic_baseline": {
            "preferred_pH_range": {"min": 5.8, "max": 6.2, "unit": "pH"},
            "preferred_air_temp_c": {"min": 26.0, "max": 28.0, "unit": "C"},
            "preferred_rootzone_temp_c": 27.5
        },
        "aquaponics_context": {
            "operating_pH_range": {"min": 6.9, "max": 7.6, "unit": "pH"},
            "nitrate_n_anchor_mg_L": 42.0,
            "yield_anchor_kg_m2_batch": 2.0,
            "yield_anchor_kg_m2_staggered": 1.8,
            "notes": "Use as aquaponics operating benchmark, not as plant-only optimum."
        }
    },
    "future_fields": {
        "preferred_air_temp_c": {"min": 26.0, "max": 28.0, "unit": "C"},
        "preferred_rootzone_temp_c": {"value": 27.5, "unit": "C"},
        "cold_stress_threshold_c": 10.0,
        "severe_cold_injury_c": 5.0,
        "aquaponics_operating_pH_context": {"min": 6.9, "max": 7.6, "unit": "pH"},
        "ec_tolerance_upper_mS_cm": 5.5
    },
    "evidence": [
        {
            "source_id": "basil_corroboration_report_2026",
            "type": "corroboration_report_pdf",
            "notes": "Structured basil Layer 1 corroboration report synthesized from Tier 1 and Tier 2 sources."
        }
    ]
}

basil_evidence = {
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
    "evidence_records": [
        {
            "field": "preferred_pH",
            "value": {"min": 5.8, "max": 6.2, "unit": "pH"},
            "source_id": "basil_corroboration_report_2026",
            "trust_tier": "tier_1_2_synthesis",
            "status": "promote",
            "notes": "Hydroponic or soilless plant-optimized preferred pH band."
        },
        {
            "field": "tolerated_pH",
            "value": {"min": 5.5, "max": 6.5, "unit": "pH"},
            "source_id": "basil_corroboration_report_2026",
            "trust_tier": "tier_1_2_synthesis",
            "status": "promote",
            "notes": "Standard hydroponic operational tolerance band."
        },
        {
            "field": "aquaponics_operating_pH_context",
            "value": {"min": 6.9, "max": 7.6, "unit": "pH"},
            "source_id": "basil_corroboration_report_2026",
            "trust_tier": "tier_1_2_synthesis",
            "status": "promote_with_context",
            "notes": "Aquaponics system-optimized pH range under nitrification constraints."
        },
        {
            "field": "preferred_temp_c",
            "value": {"min": 26.0, "max": 28.0, "unit": "C"},
            "source_id": "basil_corroboration_report_2026",
            "trust_tier": "tier_1_2_synthesis",
            "status": "promote",
            "notes": "Preferred air temperature range for basil growth."
        },
        {
            "field": "preferred_rootzone_temp_c",
            "value": {"value": 27.5, "unit": "C"},
            "source_id": "basil_corroboration_report_2026",
            "trust_tier": "tier_1_2_synthesis",
            "status": "promote",
            "notes": "Preferred nutrient solution or root-zone temperature."
        },
        {
            "field": "cold_stress_threshold_c",
            "value": 10.0,
            "source_id": "basil_corroboration_report_2026",
            "trust_tier": "tier_1_2_synthesis",
            "status": "promote",
            "notes": "Chilling injury risk begins below about 10 C."
        },
        {
            "field": "severe_cold_injury_c",
            "value": 5.0,
            "source_id": "basil_corroboration_report_2026",
            "trust_tier": "tier_1_2_synthesis",
            "status": "promote",
            "notes": "Severe chilling injury threshold."
        },
        {
            "field": "nitrate_anchor",
            "value": 42.0,
            "unit": "mg/L nitrate-N",
            "source_id": "basil_corroboration_report_2026",
            "trust_tier": "tier_1_2_synthesis",
            "status": "promote_with_context",
            "notes": "Aquaponics nitrate-N operating anchor from UVI basil production."
        },
        {
            "field": "hydroponic_n_target",
            "value": {"min": 100.0, "max": 150.0, "unit": "ppm N"},
            "source_id": "basil_corroboration_report_2026",
            "trust_tier": "tier_1_2_synthesis",
            "status": "promote",
            "notes": "Hydroponic nitrogen target band."
        },
        {
            "field": "preferred_ec_mS_cm",
            "value": {"min": 0.5, "max": 1.5, "unit": "mS/cm"},
            "source_id": "basil_corroboration_report_2026",
            "trust_tier": "tier_1_2_synthesis",
            "status": "promote",
            "notes": "Preferred hydroponic EC band."
        },
        {
            "field": "ec_tolerance_upper_mS_cm",
            "value": 5.5,
            "source_id": "basil_corroboration_report_2026",
            "trust_tier": "tier_1_2_synthesis",
            "status": "promote_with_context",
            "notes": "High EC tolerance note from an 8-week study; use as robustness note, not preferred target."
        },
        {
            "field": "stress_note",
            "value": "Below about pH 5.8, basil risk increases for Fe and Mn toxicity symptoms.",
            "source_id": "basil_corroboration_report_2026",
            "trust_tier": "tier_1_2_synthesis",
            "status": "promote",
            "notes": "Low-pH toxicity rule."
        },
        {
            "field": "stress_note",
            "value": "Above about pH 6.5, basil risk increases for Fe deficiency and interveinal chlorosis.",
            "source_id": "basil_corroboration_report_2026",
            "trust_tier": "tier_1_2_synthesis",
            "status": "promote",
            "notes": "High-pH deficiency rule."
        },
        {
            "field": "growth_note",
            "value": {
                "aquaponics_yield_batch_kg_m2": 2.0,
                "aquaponics_yield_staggered_kg_m2": 1.8,
                "field_comparison_kg_m2": 0.6
            },
            "source_id": "basil_corroboration_report_2026",
            "trust_tier": "tier_1_2_synthesis",
            "status": "promote",
            "notes": "Aquaponics yield anchors for basil."
        }
    ]
}

with open(SPECIES_PATH, "w", encoding="utf-8") as f:
    json.dump(basil_profile, f, indent=2)

with open(EVIDENCE_PATH, "w", encoding="utf-8") as f:
    json.dump(basil_evidence, f, indent=2)

print(f"Wrote species profile: {SPECIES_PATH}")
print(f"Wrote evidence file: {EVIDENCE_PATH}")