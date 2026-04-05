from pathlib import Path
import subprocess
import sys
import json
import shutil
from datetime import datetime, UTC

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PACKET_DIR = PROJECT_ROOT / "data" / "update_packets"
SIM_DIR = PROJECT_ROOT / "data" / "simulation"
LOG_DIR = PROJECT_ROOT / "data" / "update_logs"

APPLY_PACKET_SCRIPT = PROJECT_ROOT / "src" / "apply_update_packet.py"
TRADEOFF_SCRIPT = PROJECT_ROOT / "src" / "run_tradeoff_matrix.py"

LATEST_PACKET_PATH = PACKET_DIR / "latest_update_packet.json"
TRADEOFF_RESULTS_PATH = SIM_DIR / "tradeoff_matrix_results.json"

LOG_DIR.mkdir(parents=True, exist_ok=True)


def run_step(command: list[str], step_name: str) -> None:
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


def load_json(path: Path):
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def summarize_results(results: list[dict]) -> dict:
    if not results:
        return {
            "count": 0,
            "best_overall_score": None,
            "worst_overall_score": None,
            "average_overall_score": None,
            "best_scenario": None,
            "worst_scenario": None,
            "mode_averages": {}
        }

    sorted_results = sorted(results, key=lambda x: x["overall_system_score"], reverse=True)
    best = sorted_results[0]
    worst = sorted_results[-1]

    avg = round(sum(x["overall_system_score"] for x in results) / len(results), 3)

    mode_groups = {}
    for row in results:
        mode = row["mode"]
        mode_groups.setdefault(mode, []).append(row["overall_system_score"])

    mode_averages = {
        mode: round(sum(vals) / len(vals), 3)
        for mode, vals in mode_groups.items()
    }

    return {
        "count": len(results),
        "best_overall_score": best["overall_system_score"],
        "worst_overall_score": worst["overall_system_score"],
        "average_overall_score": avg,
        "best_scenario": best,
        "worst_scenario": worst,
        "mode_averages": mode_averages
    }


def compare_summaries(before: dict | None, after: dict | None) -> dict:
    if before is None:
        return {
            "status": "no_previous_results",
            "overall_average_delta": None,
            "best_score_delta": None,
            "worst_score_delta": None,
            "mode_average_deltas": {}
        }

    mode_average_deltas = {}
    all_modes = set(before.get("mode_averages", {}).keys()) | set(after.get("mode_averages", {}).keys())
    for mode in sorted(all_modes):
        before_val = before.get("mode_averages", {}).get(mode)
        after_val = after.get("mode_averages", {}).get(mode)
        if before_val is not None and after_val is not None:
            mode_average_deltas[mode] = round(after_val - before_val, 3)
        else:
            mode_average_deltas[mode] = None

    return {
        "status": "compared",
        "overall_average_delta": round(after["average_overall_score"] - before["average_overall_score"], 3),
        "best_score_delta": round(after["best_overall_score"] - before["best_overall_score"], 3),
        "worst_score_delta": round(after["worst_overall_score"] - before["worst_overall_score"], 3),
        "mode_average_deltas": mode_average_deltas
    }


def extract_top_n(results: list[dict], n: int = 5) -> list[dict]:
    return sorted(results, key=lambda x: x["overall_system_score"], reverse=True)[:n]


def main():
    if not LATEST_PACKET_PATH.exists():
        raise FileNotFoundError(f"Missing update packet: {LATEST_PACKET_PATH}")

    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")

    before_results = load_json(TRADEOFF_RESULTS_PATH)
    before_summary = summarize_results(before_results) if before_results else None

    if TRADEOFF_RESULTS_PATH.exists():
        backup_before = LOG_DIR / f"tradeoff_matrix_before_{timestamp}.json"
        shutil.copy2(TRADEOFF_RESULTS_PATH, backup_before)
        print(f"Backed up previous tradeoff results to: {backup_before}")

    python_cmd = sys.executable

    run_step(
        [python_cmd, str(APPLY_PACKET_SCRIPT)],
        "apply_update_packet"
    )

    run_step(
        [python_cmd, str(TRADEOFF_SCRIPT)],
        "run_tradeoff_matrix"
    )

    after_results = load_json(TRADEOFF_RESULTS_PATH)
    if after_results is None:
        raise FileNotFoundError(f"Expected tradeoff results were not created: {TRADEOFF_RESULTS_PATH}")

    after_summary = summarize_results(after_results)
    comparison = compare_summaries(before_summary, after_summary)

    after_backup = LOG_DIR / f"tradeoff_matrix_after_{timestamp}.json"
    shutil.copy2(TRADEOFF_RESULTS_PATH, after_backup)

    report = {
        "run_id": f"update_cycle_{timestamp}",
        "applied_at_utc": timestamp,
        "packet_path": str(LATEST_PACKET_PATH),
        "before_summary": before_summary,
        "after_summary": after_summary,
        "comparison": comparison,
        "top_5_after": extract_top_n(after_results, 5)
    }

    report_path = LOG_DIR / f"update_cycle_report_{timestamp}.json"
    save_json(report_path, report)

    print("\n=== Update cycle completed ===")
    print(f"Saved after-results backup to: {after_backup}")
    print(f"Saved update cycle report to: {report_path}")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()