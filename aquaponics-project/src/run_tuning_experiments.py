from pathlib import Path
import subprocess
import sys
import json
import shutil
from datetime import datetime, UTC

PROJECT_ROOT = Path(__file__).resolve().parent.parent

TUNING_PACKET_PATH = PROJECT_ROOT / "data" / "tuning_packets" / "latest_scenario_tuning_packet.json"
SCENARIO_PATH = PROJECT_ROOT / "data" / "simulation" / "scenarios" / "starter_tilapia_lettuce_system.json"

APPLY_TUNING_SCRIPT = PROJECT_ROOT / "src" / "apply_scenario_tuning_packet.py"
SIM_N_DAYS_SCRIPT = PROJECT_ROOT / "src" / "simulate_n_days.py"

OUTPUT_DIR = PROJECT_ROOT / "data" / "update_logs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def run_step(command: list[str], step_name: str) -> str:
    result = subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"{step_name} failed.\n\nSTDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}"
        )
    return result.stdout


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def write_packet(packet: dict):
    save_json(TUNING_PACKET_PATH, packet)


def extract_final_day_from_stdout(stdout: str) -> dict:
    data = json.loads(stdout.split("Saved multi-day summary to:")[-1].strip()) if False else None
    # We read the saved summary file instead.
    summary_path = PROJECT_ROOT / "data" / "simulation" / "multi_day_summary.json"
    summary = load_json(summary_path)
    return summary[-1]


def score_candidate(final_day: dict) -> float:
    nh3 = final_day["unionized_nh3_mg_L"]
    stability = final_day["system_stability_score"]
    fish_biomass = final_day["fish_biomass_kg"]
    plant_biomass = final_day["plant_avg_biomass_g"]
    cost = final_day["daily_operating_cost"]

    # Strong penalty for NH3 above warning levels
    if nh3 >= 0.5:
        nh3_penalty = 0.0
    elif nh3 >= 0.25:
        nh3_penalty = 0.3
    elif nh3 >= 0.2:
        nh3_penalty = 0.5
    elif nh3 >= 0.08:
        nh3_penalty = 0.75
    else:
        nh3_penalty = 1.0

    return round(
        (stability * 0.4) +
        (nh3_penalty * 0.35) +
        (fish_biomass / 10.0 * 0.15) +
        (plant_biomass / 50.0 * 0.10) -
        (cost / 10.0 * 0.05),
        3
    )


def build_packet(feed_rate: float, plant_count: int, biofilter_maturity: float, water_volume_l: float) -> dict:
    return {
        "scenario_filename": "starter_tilapia_lettuce_system.json",
        "set_fields": {
            "feeding": {
                "feed_rate_percent_body_weight_per_day": feed_rate
            },
            "plant_crop": {
                "plant_count": plant_count
            },
            "system": {
                "biofilter_maturity": biofilter_maturity,
                "water_volume_l": water_volume_l,
                "mode": "robust_compromise_mode"
            },
            "operations_policy": {
                "target_pH_mode": "robust_compromise_mode"
            }
        }
    }


def restore_baseline_scenario(baseline_backup: Path):
    shutil.copy2(baseline_backup, SCENARIO_PATH)


def main():
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    baseline_backup = OUTPUT_DIR / f"scenario_baseline_backup_{timestamp}.json"
    shutil.copy2(SCENARIO_PATH, baseline_backup)

    experiments = [
        {"name": "baseline_tuned", "feed_rate": 2.0, "plant_count": 90, "biofilter_maturity": 0.9, "water_volume_l": 4000.0},
        {"name": "lower_feed_1_75", "feed_rate": 1.75, "plant_count": 90, "biofilter_maturity": 0.9, "water_volume_l": 4000.0},
        {"name": "lower_feed_1_5", "feed_rate": 1.5, "plant_count": 90, "biofilter_maturity": 0.9, "water_volume_l": 4000.0},
        {"name": "more_plants_120", "feed_rate": 2.0, "plant_count": 120, "biofilter_maturity": 0.9, "water_volume_l": 4000.0},
        {"name": "biofilter_1_0", "feed_rate": 2.0, "plant_count": 90, "biofilter_maturity": 1.0, "water_volume_l": 4000.0},
        {"name": "more_water_5000", "feed_rate": 2.0, "plant_count": 90, "biofilter_maturity": 0.9, "water_volume_l": 5000.0}
    ]

    results = []

    for exp in experiments:
        restore_baseline_scenario(baseline_backup)

        packet = build_packet(
            feed_rate=exp["feed_rate"],
            plant_count=exp["plant_count"],
            biofilter_maturity=exp["biofilter_maturity"],
            water_volume_l=exp["water_volume_l"]
        )
        write_packet(packet)

        run_step([sys.executable, str(APPLY_TUNING_SCRIPT)], f"apply_tuning_{exp['name']}")
        run_step([sys.executable, str(SIM_N_DAYS_SCRIPT), str(SCENARIO_PATH), "7"], f"simulate_7_days_{exp['name']}")

        summary = load_json(PROJECT_ROOT / "data" / "simulation" / "multi_day_summary.json")
        final_day = summary[-1]
        composite_score = score_candidate(final_day)

        results.append({
            "experiment": exp["name"],
            "settings": exp,
            "final_day": final_day,
            "composite_score": composite_score
        })

    ranked = sorted(results, key=lambda x: x["composite_score"], reverse=True)

    report = {
        "run_id": f"tuning_experiments_{timestamp}",
        "ranked_results": ranked
    }

    report_path = OUTPUT_DIR / f"tuning_experiments_report_{timestamp}.json"
    save_json(report_path, report)

    restore_baseline_scenario(baseline_backup)

    print(f"Saved tuning experiments report to: {report_path}")
    print(json.dumps(ranked[:3], indent=2))


if __name__ == "__main__":
    main()