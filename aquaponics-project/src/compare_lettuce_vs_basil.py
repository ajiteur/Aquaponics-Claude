from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import json
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SUMMARY_PATH = PROJECT_ROOT / "data" / "simulation" / "multi_day_summary.json"
REPORTS_DIR = PROJECT_ROOT / "data" / "logs" / "update_logs"
SIMULATE_N_DAYS_PATH = PROJECT_ROOT / "src" / "simulate_n_days.py"
SCENARIOS = {
    "lettuce": PROJECT_ROOT / "data" / "simulation" / "scenarios" / "starter_tilapia_lettuce_system.json",
    "basil": PROJECT_ROOT / "data" / "simulation" / "scenarios" / "starter_tilapia_basil_system.json",
}
METRICS = [
    "unionized_nh3_mg_L",
    "tan_mg_L",
    "nitrate_mg_L",
    "fish_biomass_kg",
    "plant_avg_biomass_g",
    "daily_operating_cost",
    "system_stability_score",
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def classify_nh3_risk(unionized_nh3_mg_L: float) -> str:
    if unionized_nh3_mg_L >= 0.5:
        return "critical_mortality_risk"
    if unionized_nh3_mg_L >= 0.25:
        return "high_warning"
    if unionized_nh3_mg_L >= 0.08:
        return "species_stress_warning"
    return "normal"


def run_simulation(scenario_path: Path, num_days: int = 7) -> dict:
    if not scenario_path.exists():
        raise FileNotFoundError(f"Scenario not found: {scenario_path}")

    result = subprocess.run(
        [sys.executable, str(SIMULATE_N_DAYS_PATH), str(scenario_path), str(num_days)],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(
            "simulate_n_days failed\n\n"
            f"Scenario: {scenario_path}\n\n"
            f"STDOUT:\n{result.stdout}\n\n"
            f"STDERR:\n{result.stderr}"
        )

    if not SUMMARY_PATH.exists():
        raise FileNotFoundError(f"Summary file not found after simulation: {SUMMARY_PATH}")

    summary = load_json(SUMMARY_PATH)
    if not isinstance(summary, list) or not summary:
        raise ValueError(f"Summary file did not contain day entries: {SUMMARY_PATH}")

    final_day = summary[-1]
    missing_metrics = [metric for metric in METRICS if metric not in final_day]
    if missing_metrics:
        raise KeyError(
            f"Final day summary missing metrics {missing_metrics} for scenario {scenario_path}"
        )

    return {
        "scenario_path": str(scenario_path),
        "days_simulated": num_days,
        "final_day": final_day,
        "nh3_risk_band": classify_nh3_risk(final_day["unionized_nh3_mg_L"]),
    }


def build_comparison(results: dict) -> dict:
    lettuce_final = results["lettuce"]["final_day"]
    basil_final = results["basil"]["final_day"]

    final_day_comparison = {}
    for metric in METRICS:
        lettuce_value = lettuce_final[metric]
        basil_value = basil_final[metric]
        final_day_comparison[metric] = {
            "lettuce": lettuce_value,
            "basil": basil_value,
            "difference_basil_minus_lettuce": round(basil_value - lettuce_value, 6),
        }

    final_day_comparison["unionized_nh3_risk_band"] = {
        "lettuce": results["lettuce"]["nh3_risk_band"],
        "basil": results["basil"]["nh3_risk_band"],
    }

    return final_day_comparison


def save_report(report: dict) -> Path:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output_path = REPORTS_DIR / f"compare_lettuce_vs_basil_{timestamp}.json"

    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)

    return output_path


def main():
    results = {}
    for name, scenario_path in SCENARIOS.items():
        results[name] = run_simulation(scenario_path, num_days=7)

    report = {
        "report_type": "compare_lettuce_vs_basil",
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "days_simulated_per_scenario": 7,
        "scenarios": results,
        "final_day_comparison": build_comparison(results),
    }

    output_path = save_report(report)
    print(f"Saved comparison report to: {output_path}")
    print(json.dumps(report["final_day_comparison"], indent=2))


if __name__ == "__main__":
    main()
