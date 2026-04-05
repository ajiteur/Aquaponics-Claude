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


def restore_baseline_scenario(baseline_backup: Path):
    shutil.copy2(baseline_backup, SCENARIO_PATH)


def build_packet(feed_rate: float, plant_count: int, biofilter_maturity: float, water_volume_l: float, mode: str) -> dict:
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
                "mode": mode
            },
            "operations_policy": {
                "target_pH_mode": mode
            }
        }
    }


def score_candidate(final_day: dict) -> float:
    nh3 = final_day["unionized_nh3_mg_L"]
    stability = final_day["system_stability_score"]
    fish_biomass = final_day["fish_biomass_kg"]
    plant_biomass = final_day["plant_avg_biomass_g"]
    cost = final_day["daily_operating_cost"]

    # Lower NH3 is better
    nh3_component = max(0.0, 1.0 - (nh3 / 0.25))
    cost_component = max(0.0, 1.0 - (cost / 3.0))
    fish_component = min(1.0, fish_biomass / 10.0)
    plant_component = min(1.0, plant_biomass / 50.0)

    return round(
        (stability * 0.35) +
        (nh3_component * 0.35) +
        (fish_component * 0.15) +
        (plant_component * 0.10) +
        (cost_component * 0.05),
        3
    )


def is_viable(final_day: dict) -> tuple[bool, list[str]]:
    reasons = []

    if final_day["unionized_nh3_mg_L"] >= 0.08:
        reasons.append("nh3_above_target")

    if final_day["fish_biomass_kg"] <= 8.0:
        reasons.append("fish_not_growing")

    if final_day["plant_avg_biomass_g"] <= 20.0:
        reasons.append("plants_not_growing")

    return (len(reasons) == 0, reasons)


def main():
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    baseline_backup = OUTPUT_DIR / f"scenario_baseline_backup_{timestamp}.json"
    shutil.copy2(SCENARIO_PATH, baseline_backup)

    feed_rates = [1.0, 1.25, 1.5, 1.75, 2.0]
    plant_counts = [90, 120, 150]
    biofilter_maturities = [0.9, 1.0]
    water_volumes = [4000.0, 5000.0, 6000.0]
    modes = ["robust_compromise_mode"]

    all_results = []
    viable_results = []

    for feed_rate in feed_rates:
        for plant_count in plant_counts:
            for biofilter_maturity in biofilter_maturities:
                for water_volume_l in water_volumes:
                    for mode in modes:
                        restore_baseline_scenario(baseline_backup)

                        packet = build_packet(
                            feed_rate=feed_rate,
                            plant_count=plant_count,
                            biofilter_maturity=biofilter_maturity,
                            water_volume_l=water_volume_l,
                            mode=mode
                        )
                        write_packet(packet)

                        run_step(
                            [sys.executable, str(APPLY_TUNING_SCRIPT)],
                            f"apply_tuning_{feed_rate}_{plant_count}_{biofilter_maturity}_{water_volume_l}_{mode}"
                        )

                        run_step(
                            [sys.executable, str(SIM_N_DAYS_SCRIPT), str(SCENARIO_PATH), "7"],
                            f"simulate_7_days_{feed_rate}_{plant_count}_{biofilter_maturity}_{water_volume_l}_{mode}"
                        )

                        summary = load_json(PROJECT_ROOT / "data" / "simulation" / "multi_day_summary.json")
                        final_day = summary[-1]

                        viable, reasons = is_viable(final_day)
                        composite_score = score_candidate(final_day)

                        row = {
                            "settings": {
                                "feed_rate_percent_body_weight_per_day": feed_rate,
                                "plant_count": plant_count,
                                "biofilter_maturity": biofilter_maturity,
                                "water_volume_l": water_volume_l,
                                "mode": mode
                            },
                            "final_day": final_day,
                            "viable": viable,
                            "reasons_if_not_viable": reasons,
                            "composite_score": composite_score
                        }

                        all_results.append(row)
                        if viable:
                            viable_results.append(row)

    ranked_viable = sorted(viable_results, key=lambda x: x["composite_score"], reverse=True)
    ranked_all = sorted(all_results, key=lambda x: x["composite_score"], reverse=True)

    report = {
        "run_id": f"viable_scenario_search_{timestamp}",
        "criteria": {
            "unionized_nh3_mg_L_below": 0.08,
            "fish_biomass_must_exceed_start": 8.0,
            "plant_avg_biomass_must_exceed_start": 20.0
        },
        "counts": {
            "tested": len(all_results),
            "viable": len(viable_results),
            "non_viable": len(all_results) - len(viable_results)
        },
        "top_10_viable": ranked_viable[:10],
        "top_10_all": ranked_all[:10]
    }

    report_path = OUTPUT_DIR / f"viable_scenarios_report_{timestamp}.json"
    save_json(report_path, report)

    restore_baseline_scenario(baseline_backup)

    print(f"Saved viable scenario report to: {report_path}")
    print(json.dumps({
        "tested": report["counts"]["tested"],
        "viable": report["counts"]["viable"],
        "top_3_viable": ranked_viable[:3]
    }, indent=2))


if __name__ == "__main__":
    main()