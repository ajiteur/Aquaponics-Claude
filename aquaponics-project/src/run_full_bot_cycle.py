from pathlib import Path
import subprocess
import sys
import json
from datetime import datetime, UTC

PROJECT_ROOT = Path(__file__).resolve().parent.parent

BUILD_PACKET_SCRIPT = PROJECT_ROOT / "src" / "build_update_packet_from_report.py"
UPDATE_CYCLE_SCRIPT = PROJECT_ROOT / "src" / "run_update_cycle.py"
SIM_N_DAYS_SCRIPT = PROJECT_ROOT / "src" / "simulate_n_days.py"

SCENARIO_PATH = PROJECT_ROOT / "data" / "simulation" / "scenarios" / "starter_tilapia_lettuce_system.json"
MULTI_DAY_SUMMARY_PATH = PROJECT_ROOT / "data" / "simulation" / "multi_day_summary.json"
LOG_DIR = PROJECT_ROOT / "data" / "update_logs"

LOG_DIR.mkdir(parents=True, exist_ok=True)


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


def load_json(path: Path):
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def summarize_multi_day(final_day: dict | None) -> dict:
    if not final_day:
        return {
            "status": "missing"
        }

    nh3 = final_day["unionized_nh3_mg_L"]
    tan = final_day["tan_mg_L"]

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
        "final_day": final_day,
        "risk_band": risk_band,
        "interpretation": {
            "tan_high": tan >= 1.0,
            "nh3_warning_triggered": nh3 >= 0.08,
            "nh3_high_warning_triggered": nh3 >= 0.25,
            "nh3_critical_triggered": nh3 >= 0.5
        }
    }


def main():
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    python_cmd = sys.executable

    run_step(
        [python_cmd, str(BUILD_PACKET_SCRIPT)],
        "build_update_packet_from_report"
    )

    run_step(
        [python_cmd, str(UPDATE_CYCLE_SCRIPT)],
        "run_update_cycle"
    )

    run_step(
        [python_cmd, str(SIM_N_DAYS_SCRIPT), str(SCENARIO_PATH), "7"],
        "simulate_n_days"
    )

    multi_day = load_json(MULTI_DAY_SUMMARY_PATH)
    final_day = multi_day[-1] if multi_day else None
    multi_day_summary = summarize_multi_day(final_day)

    report = {
        "run_id": f"full_bot_cycle_{timestamp}",
        "completed_at_utc": timestamp,
        "scenario_path": str(SCENARIO_PATH),
        "multi_day_summary": multi_day_summary
    }

    report_path = LOG_DIR / f"full_bot_cycle_report_{timestamp}.json"
    save_json(report_path, report)

    print("\n=== Full bot cycle completed ===")
    print(f"Saved full bot cycle report to: {report_path}")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()