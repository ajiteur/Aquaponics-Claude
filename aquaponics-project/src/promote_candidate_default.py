from __future__ import annotations

from datetime import datetime, UTC
from pathlib import Path
import json
import sys


PROJECT_ROOT = Path(__file__).resolve().parent.parent
UPDATE_LOGS_DIR = PROJECT_ROOT / "data" / "logs" / "update_logs"
DEFAULTS_PATH = PROJECT_ROOT / "data" / "simulation" / "scenario_defaults.json"

RESEARCH_REPORT_PREFIX = "research_to_tuning_cycle_report_"
COMPARE_REPORT_PREFIX = "compare_lettuce_vs_basil_"

DEFAULT_KEYS = [
    "feed_rate_percent_body_weight_per_day",
    "plant_count",
    "biofilter_maturity",
    "water_volume_l",
    "mode",
]


def load_json(path: Path, default=None):
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)


def latest_matching_report() -> Path | None:
    candidates = list(UPDATE_LOGS_DIR.glob(f"{RESEARCH_REPORT_PREFIX}*.json"))
    candidates.extend(UPDATE_LOGS_DIR.glob(f"{COMPARE_REPORT_PREFIX}*.json"))
    if not candidates:
        return None
    return max(candidates, key=lambda path: path.stat().st_mtime)


def extract_defaults_from_scenario(scenario: dict) -> dict:
    return {
        "feed_rate_percent_body_weight_per_day": scenario["feeding"]["feed_rate_percent_body_weight_per_day"],
        "plant_count": scenario["plant_crop"]["plant_count"],
        "biofilter_maturity": scenario["system"]["biofilter_maturity"],
        "water_volume_l": scenario["system"]["water_volume_l"],
        "mode": scenario["system"]["mode"],
    }


def recommendation_indicates_new_best_default(report: dict) -> bool:
    recommendation = report.get("recommendation")
    if not isinstance(recommendation, dict):
        return False

    decision = recommendation.get("decision")
    return decision in {
        "candidate_new_best_default",
        "new_best_default",
        "promote_new_best_default",
    }


def infer_candidate_scenario_path(report: dict, report_path: Path) -> Path | None:
    recommendation = report.get("recommendation", {})

    explicit_path = recommendation.get("scenario_path") or recommendation.get("new_best_default_scenario_path")
    if explicit_path:
        return Path(explicit_path)

    report_type = report.get("report_type")
    if report_type == "compare_lettuce_vs_basil":
        winner = recommendation.get("winner")
        scenarios = report.get("scenarios", {})
        if winner in scenarios:
            scenario_path = scenarios[winner].get("scenario_path")
            if scenario_path:
                return Path(scenario_path)
        return None

    scenario_path = report.get("scenario_path")
    if scenario_path:
        return Path(scenario_path)

    source_files = report.get("source_files", {})
    source_scenario_path = source_files.get("scenario_path")
    if source_scenario_path:
        return Path(source_scenario_path)

    return None


def main():
    report_path = Path(sys.argv[1]) if len(sys.argv) > 1 else latest_matching_report()
    if report_path is None:
        raise FileNotFoundError(f"No comparison or research-to-tuning report found in: {UPDATE_LOGS_DIR}")

    if not report_path.is_absolute():
        report_path = PROJECT_ROOT / report_path

    report = load_json(report_path)
    if report is None:
        raise FileNotFoundError(f"Report not found: {report_path}")

    if not recommendation_indicates_new_best_default(report):
        print(json.dumps({
            "status": "no_change",
            "reason": "latest_report_does_not_recommend_new_best_default",
            "report_path": str(report_path),
            "report_type": report.get("report_type"),
            "recommendation": report.get("recommendation"),
        }, indent=2))
        return

    candidate_scenario_path = infer_candidate_scenario_path(report, report_path)
    if candidate_scenario_path is None:
        raise ValueError(
            f"Report recommends a new best default but does not identify a candidate scenario: {report_path}"
        )

    if not candidate_scenario_path.is_absolute():
        candidate_scenario_path = PROJECT_ROOT / candidate_scenario_path

    candidate_scenario = load_json(candidate_scenario_path)
    if candidate_scenario is None:
        raise FileNotFoundError(f"Candidate scenario not found: {candidate_scenario_path}")

    candidate_defaults = extract_defaults_from_scenario(candidate_scenario)

    defaults_doc = load_json(DEFAULTS_PATH, default={
        "updated_at_utc": None,
        "experimental_defaults": {},
    })

    current_defaults = defaults_doc.get("experimental_defaults", {})
    if current_defaults == candidate_defaults:
        print(json.dumps({
            "status": "no_change",
            "reason": "candidate_defaults_already_match_current_defaults",
            "report_path": str(report_path),
            "candidate_scenario_path": str(candidate_scenario_path),
            "experimental_defaults": current_defaults,
        }, indent=2))
        return

    timestamp = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    defaults_doc["experimental_defaults"] = candidate_defaults
    defaults_doc["updated_at_utc"] = timestamp

    save_json(DEFAULTS_PATH, defaults_doc)

    print(json.dumps({
        "status": "updated",
        "report_path": str(report_path),
        "candidate_scenario_path": str(candidate_scenario_path),
        "previous_defaults": current_defaults,
        "new_defaults": candidate_defaults,
        "updated_at_utc": timestamp,
    }, indent=2))


if __name__ == "__main__":
    main()
