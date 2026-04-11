from pathlib import Path
import json
from datetime import datetime, UTC
import copy

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SPECIES_DIR = PROJECT_ROOT / "data" / "simulation" / "species"
EVIDENCE_DIR = PROJECT_ROOT / "data" / "simulation" / "species_evidence"
PACKET_DIR = PROJECT_ROOT / "data" / "knowledge" / "update_packets"
LOG_DIR = PROJECT_ROOT / "data" / "logs" / "update_logs"

PACKET_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)


def load_json(path: Path):
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


def extend_unique_list(target_list: list, new_items: list):
    existing = {json.dumps(x, sort_keys=True) for x in target_list}
    for item in new_items:
        key = json.dumps(item, sort_keys=True)
        if key not in existing:
            target_list.append(item)
            existing.add(key)


def resolve_species_path(category: str, filename: str) -> Path:
    return SPECIES_DIR / category / filename


def main():
    packet_path = PACKET_DIR / "latest_update_packet.json"
    if not packet_path.exists():
        raise FileNotFoundError(f"Missing packet: {packet_path}")

    packet = load_json(packet_path)

    timestamp = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    log = {
        "applied_at_utc": timestamp,
        "packet_file": str(packet_path),
        "changes": []
    }

    for species_update in packet.get("species_updates", []):
        category = species_update["category"]
        filename = species_update["filename"]
        species_path = resolve_species_path(category, filename)

        if not species_path.exists():
            raise FileNotFoundError(f"Species file not found: {species_path}")

        original = load_json(species_path)
        updated = copy.deepcopy(original)

        if "set_fields" in species_update:
            deep_update(updated, species_update["set_fields"])

        if "append_growth_notes" in species_update:
            updated.setdefault("growth_notes", [])
            extend_unique_list(updated["growth_notes"], species_update["append_growth_notes"])

        if "append_stress_notes" in species_update:
            updated.setdefault("stress_notes", [])
            extend_unique_list(updated["stress_notes"], species_update["append_stress_notes"])

        if "append_evidence" in species_update:
            updated.setdefault("evidence", [])
            extend_unique_list(updated["evidence"], species_update["append_evidence"])

        updated["updated_at_utc"] = timestamp

        save_json(species_path, updated)

        log["changes"].append({
            "type": "species_update",
            "file": str(species_path),
            "fields_updated": list(species_update.get("set_fields", {}).keys()),
            "growth_notes_added": len(species_update.get("append_growth_notes", [])),
            "stress_notes_added": len(species_update.get("append_stress_notes", [])),
            "evidence_added": len(species_update.get("append_evidence", []))
        })

    for evidence_update in packet.get("evidence_updates", []):
        filename = evidence_update["filename"]
        evidence_path = EVIDENCE_DIR / filename

        if not evidence_path.exists():
            raise FileNotFoundError(f"Evidence file not found: {evidence_path}")

        original = load_json(evidence_path)
        updated = copy.deepcopy(original)

        updated.setdefault("evidence_records", [])
        extend_unique_list(updated["evidence_records"], evidence_update.get("append_records", []))

        updated["updated_at_utc"] = timestamp
        save_json(evidence_path, updated)

        log["changes"].append({
            "type": "evidence_update",
            "file": str(evidence_path),
            "records_added": len(evidence_update.get("append_records", []))
        })

    log_path = LOG_DIR / f"update_log_{timestamp.replace(':', '').replace('-', '')}.json"
    save_json(log_path, log)

    print(f"Applied update packet: {packet_path}")
    print(f"Saved update log: {log_path}")
    print(json.dumps(log, indent=2))


if __name__ == "__main__":
    main()
