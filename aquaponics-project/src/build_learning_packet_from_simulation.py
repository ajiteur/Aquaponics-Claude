from pathlib import Path
import json
from datetime import datetime, UTC

PROJECT_ROOT = Path(__file__).resolve().parent.parent

FULL_BOT_REPORT_PATH = PROJECT_ROOT / "data" / "logs" / "update_logs"
TUNING_REPORT_DIR = PROJECT_ROOT / "data" / "logs" / "update_logs"
LEARNING_PACKET_DIR = PROJECT_ROOT / "data" / "knowledge" / "learning_packets"

MULTI_DAY_SUMMARY_PATH = PROJECT_ROOT / "data" / "simulation" / "multi_day_summary.json"
PARAM_LIBRARY_PATH = PROJECT_ROOT / "data" / "simulation" / "parameter_library.json"

LEARNING_PACKET_DIR.mkdir(parents=True, exist_ok=True)


def load_json(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def latest_matching_file(folder: Path, prefix: str) -> Path:
    files = sorted(folder.glob(f"{prefix}*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files:
        raise FileNotFoundError(f"No files found in {folder} with prefix {prefix}")
    return files[0]


def main():
    timestamp = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

    latest_full_bot_report = latest_matching_file(FULL_BOT_REPORT_PATH, "full_bot_cycle_report_")
    latest_tuning_report = latest_matching_file(TUNING_REPORT_DIR, "tuning_experiments_report_")

    full_bot = load_json(latest_full_bot_report)
    tuning = load_json(latest_tuning_report)
    multi_day = load_json(MULTI_DAY_SUMMARY_PATH)
    parameter_library = load_json(PARAM_LIBRARY_PATH)

    final_day = multi_day[-1]
    best_tuning = tuning["ranked_results"][0]

    nh3 = final_day["unionized_nh3_mg_L"]
    tan = final_day["tan_mg_L"]
    nitrate = final_day["nitrate_mg_L"]

    if nh3 >= 0.5:
        learned_risk_band = "critical_mortality_risk"
    elif nh3 >= 0.25:
        learned_risk_band = "high_warning"
    elif nh3 >= 0.08:
        learned_risk_band = "species_stress_warning"
    else:
        learned_risk_band = "normal"

    learning_packet = {
        "generated_at_utc": timestamp,
        "source_reports": {
            "full_bot_cycle_report": str(latest_full_bot_report),
            "tuning_experiments_report": str(latest_tuning_report),
            "multi_day_summary": str(MULTI_DAY_SUMMARY_PATH)
        },
        "simulation_observations": [
            {
                "observation_id": "obs_nh3_7day_current_baseline",
                "type": "simulation_outcome",
                "scope": "starter_tilapia_lettuce_system",
                "statement": f"After 7 simulated days, unionized NH3 reached {nh3} mg/L under the current baseline scenario.",
                "tags": ["nh3", "7_day_run", "baseline", "risk"],
                "status": "observed"
            },
            {
                "observation_id": "obs_tan_7day_current_baseline",
                "type": "simulation_outcome",
                "scope": "starter_tilapia_lettuce_system",
                "statement": f"After 7 simulated days, TAN reached {tan} mg/L under the current baseline scenario.",
                "tags": ["tan", "7_day_run", "baseline"],
                "status": "observed"
            },
            {
                "observation_id": "obs_best_tuning_candidate",
                "type": "tuning_outcome",
                "scope": "scenario_tuning_experiments",
                "statement": f"Best tuning candidate was {best_tuning['experiment']} with final NH3 {best_tuning['final_day']['unionized_nh3_mg_L']} mg/L.",
                "tags": ["tuning", "best_candidate", "nh3"],
                "status": "observed"
            }
        ],
        "evidence_map_updates": [
            {
                "map_id": "sim_validation_nh3_thresholds",
                "link_type": "simulation_validation",
                "related_entities": [
                    "fish_tilapia",
                    "unionized_nh3_warning_mg_L",
                    "unionized_nh3_critical_mg_L"
                ],
                "summary": "Simulation confirms NH3 is a decisive risk driver and should remain central in scoring and stability checks.",
                "latest_observed_value": nh3,
                "latest_risk_band": learned_risk_band
            },
            {
                "map_id": "sim_validation_pH_tradeoff_modes",
                "link_type": "simulation_validation",
                "related_entities": [
                    "pH_target_general",
                    "pH_compromise_optimal",
                    "pH_target_plant_yield_mode"
                ],
                "summary": "Simulation supports keeping separate robust compromise and plant-yield modes rather than collapsing to one pH rule."
            }
        ],
        "parameter_library_proposals": [
            {
                "proposal_id": "prop_keep_multi_record_pH_structure",
                "target": "parameter_library",
                "action": "retain_structure",
                "field": "process_modes",
                "reason": "Simulation still shows meaningful tradeoff between robust compromise mode and plant-yield mode."
            },
            {
                "proposal_id": "prop_add_nh3_risk_band_labels",
                "target": "parameter_library",
                "action": "extend_metadata",
                "field": "unionized_NH3_thresholds",
                "reason": "Simulation outcomes are now being interpreted against risk bands; store explicit labels in the library."
            },
            {
                "proposal_id": "prop_add_scenario_default_hints",
                "target": "parameter_library",
                "action": "add_experimental_defaults",
                "field": "scenario_tuning_hints",
                "value": {
                    "feed_rate_percent_body_weight_per_day": best_tuning["settings"]["feed_rate"],
                    "plant_count": best_tuning["settings"]["plant_count"],
                    "biofilter_maturity": best_tuning["settings"]["biofilter_maturity"],
                    "water_volume_l": best_tuning["settings"]["water_volume_l"]
                },
                "reason": "Best 7-day tuning candidate should be stored as experimental defaults, not as accepted truth."
            }
        ],
        "model_update_proposals": [
            {
                "proposal_id": "model_keep_nh3_as_primary_toxicity_signal",
                "target": "nitrogen_model",
                "action": "keep",
                "reason": "Simulation reinforces that TAN alone is not enough; NH3 drives the actual risk signal."
            },
            {
                "proposal_id": "model_test_more_biofilter_capacity",
                "target": "scenario_defaults",
                "action": "test",
                "reason": "Best current tuning result came from raising biofilter maturity to 1.0."
            },
            {
                "proposal_id": "model_test_more_water_or_lower_feed",
                "target": "scenario_defaults",
                "action": "test",
                "reason": "Top candidates also included more water and lower feed, suggesting nitrogen loading remains the main bottleneck."
            }
        ],
        "atomic_fact_tickets": [
            {
                "ticket_id": "ticket_no_auto_atomic_fact_promotion_from_sim",
                "target": "atomic_facts",
                "action": "no_change",
                "reason": "Simulation outcomes should not directly promote accepted atomic facts; they are model observations, not external evidence."
            }
        ]
    }

    output_path = LEARNING_PACKET_DIR / "latest_learning_packet.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(learning_packet, f, indent=2)

    print(f"Saved learning packet to: {output_path}")
    print(json.dumps(learning_packet, indent=2))


if __name__ == "__main__":
    main()
