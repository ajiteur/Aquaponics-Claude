from pathlib import Path
import json
from datetime import datetime, UTC

PROJECT_ROOT = Path(__file__).resolve().parent.parent

LEARNING_PACKET_PATH = PROJECT_ROOT / "data" / "learning_packets" / "latest_learning_packet.json"
EVIDENCE_MAP_PATH = PROJECT_ROOT / "aquaponics-knowledge" / "06_evidence_maps" / "simulation_validation_map.json"
MODEL_TICKETS_PATH = PROJECT_ROOT / "data" / "model_tickets" / "latest_model_tickets.json"
SCENARIO_DEFAULTS_PATH = PROJECT_ROOT / "data" / "simulation" / "scenario_defaults.json"
LOG_DIR = PROJECT_ROOT / "data" / "update_logs"

LOG_DIR.mkdir(parents=True, exist_ok=True)
EVIDENCE_MAP_PATH.parent.mkdir(parents=True, exist_ok=True)
MODEL_TICKETS_PATH.parent.mkdir(parents=True, exist_ok=True)
SCENARIO_DEFAULTS_PATH.parent.mkdir(parents=True, exist_ok=True)


def load_json(path: Path, default=None):
    if not path.exists():
        return {} if default is None else default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def extend_unique_records(target_list: list, new_items: list):
    existing = {json.dumps(item, sort_keys=True) for item in target_list}
    for item in new_items:
        key = json.dumps(item, sort_keys=True)
        if key not in existing:
            target_list.append(item)
            existing.add(key)


def main():
    learning_packet = load_json(LEARNING_PACKET_PATH)
    if not learning_packet:
        raise FileNotFoundError(f"Missing or empty learning packet: {LEARNING_PACKET_PATH}")

    timestamp = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

    evidence_map = load_json(EVIDENCE_MAP_PATH, default={
        "updated_at_utc": None,
        "simulation_observations": [],
        "simulation_validation_links": []
    })

    model_tickets = load_json(MODEL_TICKETS_PATH, default={
        "updated_at_utc": None,
        "tickets": []
    })

    scenario_defaults = load_json(SCENARIO_DEFAULTS_PATH, default={
        "updated_at_utc": None,
        "experimental_defaults": {}
    })

    # 1) simulation observations -> evidence map
    evidence_map.setdefault("simulation_observations", [])
    extend_unique_records(
        evidence_map["simulation_observations"],
        learning_packet.get("simulation_observations", [])
    )

    evidence_map.setdefault("simulation_validation_links", [])
    extend_unique_records(
        evidence_map["simulation_validation_links"],
        learning_packet.get("evidence_map_updates", [])
    )
    evidence_map["updated_at_utc"] = timestamp

    # 2) model proposals -> model tickets
    model_tickets.setdefault("tickets", [])
    extend_unique_records(
        model_tickets["tickets"],
        learning_packet.get("model_update_proposals", [])
    )
    extend_unique_records(
        model_tickets["tickets"],
        learning_packet.get("atomic_fact_tickets", [])
    )
    model_tickets["updated_at_utc"] = timestamp

    # 3) experimental scenario defaults from proposals
    for proposal in learning_packet.get("parameter_library_proposals", []):
        if (
            proposal.get("target") == "parameter_library"
            and proposal.get("action") == "add_experimental_defaults"
            and proposal.get("field") == "scenario_tuning_hints"
        ):
            scenario_defaults["experimental_defaults"] = proposal.get("value", {})
    scenario_defaults["updated_at_utc"] = timestamp

    save_json(EVIDENCE_MAP_PATH, evidence_map)
    save_json(MODEL_TICKETS_PATH, model_tickets)
    save_json(SCENARIO_DEFAULTS_PATH, scenario_defaults)

    log = {
        "applied_at_utc": timestamp,
        "learning_packet": str(LEARNING_PACKET_PATH),
        "outputs": {
            "evidence_map": str(EVIDENCE_MAP_PATH),
            "model_tickets": str(MODEL_TICKETS_PATH),
            "scenario_defaults": str(SCENARIO_DEFAULTS_PATH)
        },
        "counts": {
            "simulation_observations": len(learning_packet.get("simulation_observations", [])),
            "evidence_map_updates": len(learning_packet.get("evidence_map_updates", [])),
            "model_update_proposals": len(learning_packet.get("model_update_proposals", [])),
            "atomic_fact_tickets": len(learning_packet.get("atomic_fact_tickets", []))
        }
    }

    log_path = LOG_DIR / f"apply_learning_packet_log_{timestamp.replace(':', '').replace('-', '')}.json"
    save_json(log_path, log)

    print(f"Applied learning packet: {LEARNING_PACKET_PATH}")
    print(f"Saved evidence map: {EVIDENCE_MAP_PATH}")
    print(f"Saved model tickets: {MODEL_TICKETS_PATH}")
    print(f"Saved scenario defaults: {SCENARIO_DEFAULTS_PATH}")
    print(f"Saved log: {log_path}")
    print(json.dumps(log, indent=2))


if __name__ == "__main__":
    main()