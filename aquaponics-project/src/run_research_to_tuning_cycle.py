from pathlib import Path
import subprocess
import sys
import json
import shutil
from datetime import datetime, UTC

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RESEARCH_BOT_SCRIPT = PROJECT_ROOT / "src" / "research_interventions_bot.py"
BUILD_TUNING_PACKET_SCRIPT = PROJECT_ROOT / "src" / "build_tuning_packet_from_intervention_digest.py"
APPLY_TUNING_PACKET_SCRIPT = PROJECT_ROOT / "src" / "apply_scenario_tuning_packet.py"
SIM_N_DAYS_SCRIPT = PROJECT_ROOT / "src" / "simulate_n_days.py"

SCENARIO_PATH = PROJECT_ROOT / "data" / "simulation" / "scenarios" / "starter_tilapia_lettuce_system.json"
MULTI_DAY_SUMMARY_PATH = PROJECT_ROOT / "data" / "simulation" / "multi_day_summary.json"
UPDATE_LOGS_DIR = PROJECT_ROOT / "data" / "logs" / "update_logs"

UPDATE_LOGS_DIR.mkdir(parents=True, exist_ok=True)


def run_step(command: list[str], step_name: str) -> str:
    print(f"\n=== Running: {step_name} ===")
    print("Command:", " ".join(command))

    result = subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True
    )

    if result.stdout:
        print(result.stdout)

    if result.returncode != 0:
        raise RuntimeError(
            f"{step_name} failed.\n\nSTDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}"
        )

    if result.stderr:
        print(result.stderr)

    return result.stdout


def load_json(path: Path, default=None):
    if not path.exists():
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def latest_matching_file(folder: Path, prefix: str) -> Path | None:
    files = sorted(folder.glob(f"{prefix}*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    return files[0] if files else None


def summarize_final_day(final_day: dict | None) -> dict:
    if not final_day:
        return {
            "status": "missing"
        }

    nh3 = final_day["unionized_nh3_mg_L"]

    if nh3 >= 0.5:
        risk_band = "critical_mortality_risk"
    elif nh3 >= 0.25:
        risk_band = "high_warning"
    elif nh3 >= 0.08:
        risk_band = "species_stress_warning"
    else:
        risk_band = "normal"

    return {
        "status": "ok",
        "day": final_day["day"],
        "pH": final_day["pH"],
        "tan_mg_L": final_day["tan_mg_L"],
        "unionized_nh3_mg_L": final_day["unionized_nh3_mg_L"],
        "nitrate_mg_L": final_day["nitrate_mg_L"],
        "fish_biomass_kg": final_day["fish_biomass_kg"],
        "avg_fish_weight_g": final_day["avg_fish_weight_g"],
        "plant_avg_biomass_g": final_day["plant_avg_biomass_g"],
        "daily_operating_cost": final_day["daily_operating_cost"],
        "system_stability_score": final_day["system_stability_score"],
        "risk_band": risk_band
    }


def compare_runs(label_a: str, a: dict | None, label_b: str, b: dict | None) -> dict:
    if not a or not b:
        return {
            "status": "missing_data",
            "comparison": f"{label_a}_vs_{label_b}"
        }

    return {
        "status": "compared",
        "comparison": f"{label_a}_vs_{label_b}",
        "unionized_nh3_delta": round(b["unionized_nh3_mg_L"] - a["unionized_nh3_mg_L"], 3),
        "tan_delta": round(b["tan_mg_L"] - a["tan_mg_L"], 3),
        "nitrate_delta": round(b["nitrate_mg_L"] - a["nitrate_mg_L"], 3),
        "fish_biomass_delta": round(b["fish_biomass_kg"] - a["fish_biomass_kg"], 3),
        "plant_biomass_delta": round(b["plant_avg_biomass_g"] - a["plant_avg_biomass_g"], 3),
        "daily_operating_cost_delta": round(b["daily_operating_cost"] - a["daily_operating_cost"], 3),
        "system_stability_delta": round(b["system_stability_score"] - a["system_stability_score"], 3)
    }


def choose_recommendation(
    baseline: dict | None,
    tuned: dict | None,
    best_known: dict | None
) -> dict:
    if not tuned:
        return {
            "decision": "insufficient_data",
            "reason": "Tuned run missing."
        }

    if tuned["unionized_nh3_mg_L"] < 0.08:
        if best_known and tuned["unionized_nh3_mg_L"] <= best_known["unionized_nh3_mg_L"]:
            return {
                "decision": "candidate_new_best_default",
                "reason": "Tuned scenario meets NH3 viability target and matches or improves on best known viable NH3."
            }
        return {
            "decision": "viable_but_compare_with_best_known",
            "reason": "Tuned scenario meets NH3 viability target."
        }

    if baseline and tuned["unionized_nh3_mg_L"] < baseline["unionized_nh3_mg_L"]:
        return {
            "decision": "improved_but_not_viable",
            "reason": "Tuned scenario improves NH3 versus current baseline but still exceeds viability target."
        }

    return {
        "decision": "no_meaningful_improvement",
        "reason": "Tuned scenario did not beat the baseline on the primary NH3 risk goal."
    }


def main():
    issue = (
        "Find trusted interventions for reducing high TAN and unionized NH3 in a coupled tilapia-lettuce aquaponics system over a 7-day horizon."
        if len(sys.argv) < 2
        else " ".join(sys.argv[1:])
    )

    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")

    if not SCENARIO_PATH.exists():
        raise FileNotFoundError(f"Scenario not found: {SCENARIO_PATH}")

    baseline_backup = UPDATE_LOGS_DIR / f"baseline_scenario_backup_{timestamp}.json"
    shutil.copy2(SCENARIO_PATH, baseline_backup)

    # 1) Baseline run on backed-up scenario
    run_step(
        [sys.executable, str(SIM_N_DAYS_SCRIPT), str(baseline_backup), "7"],
        "baseline_simulate_n_days"
    )
    baseline_summary_full = load_json(MULTI_DAY_SUMMARY_PATH, default=[])
    baseline_final_day = baseline_summary_full[-1] if baseline_summary_full else None
    baseline_summary = summarize_final_day(baseline_final_day)

    # 2) Research bot
    run_step(
        [sys.executable, str(RESEARCH_BOT_SCRIPT), issue],
        "research_interventions_bot"
    )

    # 3) Build tuning packet from intervention digest
    run_step(
        [sys.executable, str(BUILD_TUNING_PACKET_SCRIPT)],
        "build_tuning_packet_from_intervention_digest"
    )

    # 4) Apply tuning packet to live scenario
    run_step(
        [sys.executable, str(APPLY_TUNING_PACKET_SCRIPT)],
        "apply_scenario_tuning_packet"
    )

    # 5) Run tuned scenario
    run_step(
        [sys.executable, str(SIM_N_DAYS_SCRIPT), str(SCENARIO_PATH), "7"],
        "tuned_simulate_n_days"
    )
    tuned_summary_full = load_json(MULTI_DAY_SUMMARY_PATH, default=[])
    tuned_final_day = tuned_summary_full[-1] if tuned_summary_full else None
    tuned_summary = summarize_final_day(tuned_final_day)

    # 6) Load best known viable scenario from search, if present
    viable_report_path = latest_matching_file(UPDATE_LOGS_DIR, "viable_scenarios_report_")
    viable_report = load_json(viable_report_path, default=None) if viable_report_path else None

    best_known_viable = None
    if viable_report and viable_report.get("top_10_viable"):
        best_known_viable = viable_report["top_10_viable"][0]["final_day"]

    best_known_summary = summarize_final_day(best_known_viable) if best_known_viable else None

    report = {
        "run_id": f"research_to_tuning_cycle_{timestamp}",
        "completed_at_utc": timestamp,
        "issue": issue,
        "scenario_path": str(SCENARIO_PATH),
        "baseline_scenario_backup": str(baseline_backup),
        "baseline_summary": baseline_summary,
        "tuned_summary": tuned_summary,
        "best_known_viable_summary": best_known_summary,
        "comparisons": {
            "tuned_vs_baseline": compare_runs("baseline", baseline_summary, "tuned", tuned_summary),
            "tuned_vs_best_known_viable": compare_runs("best_known_viable", best_known_summary, "tuned", tuned_summary)
        },
        "recommendation": choose_recommendation(
            baseline=baseline_summary,
            tuned=tuned_summary,
            best_known=best_known_summary
        ),
        "source_files": {
            "viable_report": str(viable_report_path) if viable_report_path else None,
            "multi_day_summary": str(MULTI_DAY_SUMMARY_PATH)
        }
    }

    report_path = UPDATE_LOGS_DIR / f"research_to_tuning_cycle_report_{timestamp}.json"
    save_json(report_path, report)

    print("\n=== Research-to-tuning cycle completed ===")
    print(f"Saved report to: {report_path}")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
