from pathlib import Path
import json
from datetime import datetime, UTC

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DIGEST_DIR = PROJECT_ROOT / "data" / "report_digests"
PACKET_DIR = PROJECT_ROOT / "data" / "update_packets"

DIGEST_DIR.mkdir(parents=True, exist_ok=True)
PACKET_DIR.mkdir(parents=True, exist_ok=True)

INPUT_PATH = DIGEST_DIR / "latest_species_report_digest.json"
OUTPUT_PATH = PACKET_DIR / "latest_update_packet.json"


def load_json(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"Missing input file: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def main():
    digest = load_json(INPUT_PATH)

    packet = {
        "generated_at_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_digest_file": str(INPUT_PATH),
        "species_updates": [],
        "evidence_updates": []
    }

    species_update = {
        "category": digest["category"],
        "filename": digest["species_filename"],
        "set_fields": digest.get("set_fields", {}),
        "append_growth_notes": digest.get("append_growth_notes", []),
        "append_stress_notes": digest.get("append_stress_notes", []),
        "append_evidence": digest.get("append_evidence", [])
    }

    evidence_update = {
        "filename": digest["evidence_filename"],
        "append_records": digest.get("append_records", [])
    }

    packet["species_updates"].append(species_update)
    packet["evidence_updates"].append(evidence_update)

    save_json(OUTPUT_PATH, packet)

    print(f"Built update packet from digest: {INPUT_PATH}")
    print(f"Saved update packet to: {OUTPUT_PATH}")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()