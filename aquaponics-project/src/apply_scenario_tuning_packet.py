from pathlib import Path
import json
from datetime import datetime, UTC
import copy

PROJECT_ROOT = Path(__file__).resolve().parent.parent

TUNING_DIR = PROJECT_ROOT / "data" / "tuning_packets"
SCENARIO_DIR = PROJECT_ROOT / "data" / "simulation" / "scenarios"
LOG_DIR = PROJECT_ROOT / "data" / "update_logs"

TUNING_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

INPUT_PACKET = TUNING_DIR / "latest_scenario_tuning_packet.json"


def load_json(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def deep_update(target: dict, updates: dict):
    for key, value in updates.items():
        if isinstance(value, dict) and isinstance(target.get(key), dict):
            deep_update(target[key], value)
        else:
            target[key] = value


def main():
    packet = load_json(INPUT_PACKET)

    scenario_filename = packet["scenario_filename"]
    scenario_path = SCENARIO_DIR / scenario_filename
    scenario = load_json(scenario_path)

    original = copy.deepcopy(scenario)

    if "set_fields" in packet:
        deep_update(scenario, packet["set_fields"])

    scenario["updated_at_utc"] = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

    save_json(scenario_path, scenario)

    log = {
        "applied_at_utc": scenario["updated_at_utc"],
        "scenario_file": str(scenario_path),
        "packet_file": str(INPUT_PACKET),
        "changed_top_level_keys": list(packet.get("set_fields", {}).keys()),
        "before": {
            "feed_rate_percent_body_weight_per_day": original["feeding"]["feed_rate_percent_body_weight_per_day"],
            "plant_count": original["plant_crop"]["plant_count"],
            "biofilter_maturity": original["system"]["biofilter_maturity"],
            "water_volume_l": original["system"]["water_volume_l"],
            "mode": original["system"]["mode"]
        },
        "after": {
            "feed_rate_percent_body_weight_per_day": scenario["feeding"]["feed_rate_percent_body_weight_per_day"],
            "plant_count": scenario["plant_crop"]["plant_count"],
            "biofilter_maturity": scenario["system"]["biofilter_maturity"],
            "water_volume_l": scenario["system"]["water_volume_l"],
            "mode": scenario["system"]["mode"]
        }
    }

    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    log_path = LOG_DIR / f"scenario_tuning_log_{timestamp}.json"
    save_json(log_path, log)

    print(f"Applied scenario tuning packet: {INPUT_PACKET}")
    print(f"Updated scenario: {scenario_path}")
    print(f"Saved tuning log: {log_path}")
    print(json.dumps(log, indent=2))


if __name__ == "__main__":
    main()