from pathlib import Path
import json
from datetime import datetime, UTC

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SPECIES_PATH = PROJECT_ROOT / "data" / "simulation" / "species" / "plants" / "lettuce.json"
EVIDENCE_PATH = PROJECT_ROOT / "data" / "simulation" / "species_evidence" / "lettuce_evidence.json"

SPECIES_PATH.parent.mkdir(parents=True, exist_ok=True)
EVIDENCE_PATH.parent.mkdir(parents=True, exist_ok=True)

generated_at = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

lettuce_profile = {
    "species_id": "plant_lettuce",
    "scientific_name": "Lactuca sativa",
    "common_name": "Lettuce",
    "category": "plant",
    "status": "starter_profile",
    "generated_at_utc": generated_at,
    "environment": {
        "preferred_pH": {"min": 5.5, "max": 6.0, "unit": "pH"},
        "tolerated_pH": {"min": 5.5, "max": 7.0, "unit": "pH"},
        "preferred_temp_c": {"min": 18.0, "max": 24.0, "unit": "C"},
        "tolerated_temp_c": {"min": 10.0, "max": 24.0, "unit": "C"}
    },
    "nutrient_response": {
        "nitrate_demand_level": "moderate_high",
        "hydroponic_n_target_ppm": 150.0,
        "aquaponics_nitrate_minimal_spec_mg_L": 47.0,
        "n_response_biomass_gain_up_to_mg_L_N": 150.0,
        "foliar_n_plateau_near_mg_L_N": 111.4,
        "high_pH_nutrient_lockout_notes": [
            "High source-water pH above about 7 can interfere with nutrient availability.",
            "Elevated pH reduces solubility of iron, manganese, and zinc, which can limit uptake."
        ],
        "low_pH_sensitivity_notes": [
            "In calibrated hydroponic lettuce systems, drifting outside the acceptable pH band increases deficiency risk.",
            "Treat pH below the preferred band as a quality and nutrient-balance risk rather than an immediate lethal threshold."
        ]
    },
    "simulation_weights": {
        "pH_weight": 1.0,
        "temperature_weight": 1.0,
        "nitrate_weight": 1.0
    },
    "growth_notes": [
        "Stage timing baseline: germination about 3 days, seedling phase about 10 days, then post-transplant growth to harvest about 30 to 40 days.",
        "With proper management, yields of about 2 to 6 kg per square meter per crop cycle are reported.",
        "Alternative production anchor: about 150 g marketable head at about 35 days after seeding under controlled CEA lighting conditions."
    ],
    "stress_notes": [
        "Prolonged heat and high temperature fluctuations increase bolting risk, bitterness, and unmarketable crop output.",
        "Tipburn is a calcium-related physiological disorder often driven by humid microclimates and low transpiration rather than low calcium supply alone.",
        "Cooler low-light operation can still produce lettuce, but it slows time to harvest."
    ],
    "validation_benchmarks": {
        "hydroponic_baseline": {
            "target_pH_range": {"min": 5.5, "max": 6.0, "unit": "pH"},
            "day_temperature_c_max": 24.0,
            "night_temperature_c_target": 18.0,
            "notes": "Use as plant-optimized hydroponic lettuce baseline."
        },
        "aquaponics_context": {
            "minimal_nitrate_mg_L": 47.0,
            "notes": "Use as aquaponics nitrate anchor, not as universal plant-only requirement."
        }
    },
    "future_fields": {
        "preferred_air_temp_c": {"min": 18.0, "max": 24.0, "unit": "C"},
        "tolerated_air_temp_c": {"min": 10.0, "max": 24.0, "unit": "C"},
        "preferred_solution_temp_c": {"min": None, "max": 25.0, "unit": "C"},
        "tolerated_solution_temp_c": {"min": 18.0, "max": 27.0, "unit": "C"},
        "propagation_pH": {"min": 5.5, "max": 6.0, "unit": "pH"},
        "propagation_ec_mS_cm": 1.0,
        "yield_kg_m2_crop_cycle": {"min": 2.0, "max": 6.0, "unit": "kg/m2/cycle"},
        "head_weight_g_anchor": 150.0,
        "harvest_day_anchor": 35
    },
    "evidence": [
        {
            "source_id": "cornell_cea_hydroponic_lettuce_handbook",
            "type": "university_manual_pdf",
            "notes": "Strong hydroponic pH optimum and CEA setpoints."
        },
        {
            "source_id": "uk_ccd_cp63_hydroponic_lettuce",
            "type": "university_extension_pdf",
            "notes": "Lettuce-specific pH, temperature, fertigation, timeline, and yield anchors."
        },
        {
            "source_id": "uh_ctahr_small_scale_lettuce_aquaponics",
            "type": "university_extension_pdf",
            "notes": "Aquaponics-specific nitrate anchor."
        },
        {
            "source_id": "egro_dialing_in_lettuce_fertility",
            "type": "technical_guide_pdf",
            "notes": "Nitrogen response curve and diminishing returns anchor."
        },
        {
            "source_id": "egro_tipburn_e406",
            "type": "technical_alert_pdf",
            "notes": "Tipburn mechanism and mitigation knobs."
        },
        {
            "source_id": "jia_2025_water_lettuce_ph",
            "type": "peer_reviewed_article",
            "notes": "High-pH lockout mechanism and broader tolerance context."
        }
    ]
}

lettuce_evidence = {
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
    "evidence_records": [
        {
            "field": "preferred_pH",
            "value": {"min": 5.5, "max": 6.0, "unit": "pH"},
            "source_id": "uk_ccd_cp63_hydroponic_lettuce",
            "trust_tier": "tier_1",
            "status": "promote",
            "notes": "Optimal range for nutrient uptake in hydroponic lettuce."
        },
        {
            "field": "preferred_pH",
            "value": {"optimum": 5.8, "acceptable_min": 5.6, "acceptable_max": 6.0, "unit": "pH"},
            "source_id": "cornell_cea_hydroponic_lettuce_handbook",
            "trust_tier": "tier_1",
            "status": "promote",
            "notes": "Tight CEA setpoint framing."
        },
        {
            "field": "tolerated_pH",
            "value": {"min": 5.5, "max": 7.0, "unit": "pH"},
            "source_id": "lettuce_corroboration_normalized_summary",
            "trust_tier": "tier_1_2_synthesis",
            "status": "promote_with_context",
            "notes": "General operational window; quality and deficiency risk rises outside preferred band."
        },
        {
            "field": "preferred_temp_c",
            "value": {"min": 18.0, "max": 24.0, "unit": "C"},
            "source_id": "uk_ccd_cp63_hydroponic_lettuce",
            "trust_tier": "tier_1",
            "status": "promote",
            "notes": "Day should not exceed 24 C; night around 18 C."
        },
        {
            "field": "preferred_temp_c",
            "value": {"day": 24.0, "night": 19.0, "unit": "C"},
            "source_id": "cornell_cea_hydroponic_lettuce_handbook",
            "trust_tier": "tier_1",
            "status": "promote",
            "notes": "Corroborating CEA setpoints."
        },
        {
            "field": "tolerated_temp_c",
            "value": {"night_min": 10.0, "day_min": 15.0, "unit": "C"},
            "source_id": "uk_ccd_cp63_hydroponic_lettuce",
            "trust_tier": "tier_1",
            "status": "promote_with_context",
            "notes": "Suboptimal winter tolerance with longer production time."
        },
        {
            "field": "nitrate_anchor",
            "value": 47.0,
            "unit": "mg/L nitrate",
            "source_id": "uh_ctahr_small_scale_lettuce_aquaponics",
            "trust_tier": "tier_1",
            "status": "promote",
            "notes": "Aquaponics-specific minimal nitrate specification supporting good lettuce growth."
        },
        {
            "field": "hydroponic_n_target",
            "value": 150.0,
            "unit": "ppm N",
            "source_id": "uk_ccd_cp63_hydroponic_lettuce",
            "trust_tier": "tier_1",
            "status": "promote",
            "notes": "Strong numeric fertigation anchor."
        },
        {
            "field": "n_response_curve",
            "value": {
                "biomass_gain_up_to_mg_L_N": 150.0,
                "foliar_n_plateau_near_mg_L_N": 111.4
            },
            "source_id": "egro_dialing_in_lettuce_fertility",
            "trust_tier": "tier_2",
            "status": "promote",
            "notes": "Useful for diminishing-returns simulation."
        },
        {
            "field": "stress_note",
            "value": "Bolting risk rises with prolonged heat and temperature fluctuations, causing bitterness and unmarketable crop.",
            "source_id": "uk_ccd_cp63_hydroponic_lettuce",
            "trust_tier": "tier_1",
            "status": "promote",
            "notes": "Simulation-ready quality failure mode."
        },
        {
            "field": "stress_note",
            "value": "Tipburn is driven by humid microclimates and low transpiration reducing calcium transport to inner leaves.",
            "source_id": "egro_tipburn_e406",
            "trust_tier": "tier_2",
            "status": "promote",
            "notes": "Mechanistic stress note."
        },
        {
            "field": "growth_note",
            "value": {
                "germination_days": 3,
                "seedling_days": 10,
                "post_transplant_days_to_harvest_min": 30,
                "post_transplant_days_to_harvest_max": 40
            },
            "source_id": "uk_ccd_cp63_hydroponic_lettuce",
            "trust_tier": "tier_1",
            "status": "promote",
            "notes": "Excellent simulation stage timing."
        },
        {
            "field": "growth_note",
            "value": {"yield_min": 2.0, "yield_max": 6.0, "unit": "kg/m2/crop_cycle"},
            "source_id": "uk_ccd_cp63_hydroponic_lettuce",
            "trust_tier": "tier_1",
            "status": "promote",
            "notes": "Yield anchor."
        },
        {
            "field": "growth_note",
            "value": {"head_weight_g": 150.0, "harvest_day": 35},
            "source_id": "cornell_cea_hydroponic_lettuce_handbook",
            "trust_tier": "tier_1",
            "status": "promote",
            "notes": "Per-head anchor."
        }
    ]
}

with open(SPECIES_PATH, "w", encoding="utf-8") as f:
    json.dump(lettuce_profile, f, indent=2)

with open(EVIDENCE_PATH, "w", encoding="utf-8") as f:
    json.dump(lettuce_evidence, f, indent=2)

print(f"Wrote species profile: {SPECIES_PATH}")
print(f"Wrote evidence file: {EVIDENCE_PATH}")