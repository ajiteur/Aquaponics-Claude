import json
import re
from pathlib import Path
from datetime import datetime, UTC
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FACTS_DIR = PROJECT_ROOT / "aquaponics-knowledge" / "03_atomic_facts"
CONFIG_DIR = PROJECT_ROOT / "configs"
EVIDENCE_MAPS_DIR = PROJECT_ROOT / "aquaponics-knowledge" / "06_evidence_maps"
EVIDENCE_MAPS_DIR.mkdir(parents=True, exist_ok=True)

PROMOTION_POLICY_PATH = CONFIG_DIR / "promotion_policy.yaml"
SOURCE_REGISTRY_PATH = CONFIG_DIR / "source_registry.yaml"
PROMOTION_LOG_PATH = EVIDENCE_MAPS_DIR / "promotion_log.json"

# Accepted outputs
CORE_PATH = FACTS_DIR / "atomic_facts_core.json"
PARAMS_PATH = FACTS_DIR / "parameter_ranges.json"
GUIDANCE_PATH = FACTS_DIR / "operational_guidance.json"
WARNINGS_PATH = FACTS_DIR / "warnings_and_cautions.json"

# Provisional outputs
PROV_CORE_PATH = FACTS_DIR / "provisional_core_candidates.json"
PROV_PARAMS_PATH = FACTS_DIR / "provisional_parameter_ranges.json"
PROV_GUIDANCE_PATH = FACTS_DIR / "provisional_operational_guidance.json"
PROV_WARNINGS_PATH = FACTS_DIR / "provisional_warnings_and_cautions.json"


def load_json_bucket(path: Path) -> dict:
    if not path.exists():
        return {"facts": []}
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        return {"facts": []}
    if "facts" not in data or not isinstance(data["facts"], list):
        data["facts"] = []
    return data


def save_json_bucket(path: Path, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def normalize_statement(text: str) -> str:
    s = (text or "").lower().strip()

    # remove soft guidance language so near-identical guidance can corroborate
    soft_phrases = [
        "should be maintained",
        "should be",
        "is often recommended",
        "often recommended",
        "is recommended",
        "recommended",
        "may be",
        "may",
        "in many systems",
        "typically",
        "generally",
    ]
    for phrase in soft_phrases:
        s = s.replace(phrase, "")

    s = s.replace("first into", "")
    s = s.replace("then into", "")
    s = s.replace("and then into", "to")
    s = s.replace("and then to", "to")

    s = re.sub(r"[^\w\s\.\-]", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def load_source_registry() -> dict:
    data = load_yaml(SOURCE_REGISTRY_PATH)
    sources = data.get("sources", [])
    return {item["source_id"]: item for item in sources if "source_id" in item}


def is_trusted_source(source_id: str, registry: dict) -> bool:
    entry = registry.get(source_id)
    if not entry:
        return False
    return str(entry.get("trust_status", "")).lower() == "trusted"


def get_policy() -> dict:
    data = load_yaml(PROMOTION_POLICY_PATH)

    # Sensible defaults if file structure differs
    min_distinct_sources = 2
    if "promotion" in data and isinstance(data["promotion"], dict):
        min_distinct_sources = data["promotion"].get("min_distinct_sources", 2)
    elif "promotion_rules" in data and isinstance(data["promotion_rules"], dict):
        accepted = data["promotion_rules"].get("accepted", {})
        min_distinct_sources = accepted.get("min_distinct_sources", 2)

    return {
        "min_distinct_sources": min_distinct_sources
    }


def existing_normalized(bucket: dict) -> set:
    return {normalize_statement(f.get("statement", "")) for f in bucket.get("facts", [])}


def next_fact_id(bucket: dict, prefix: str) -> str:
    return f"{prefix}_{len(bucket.get('facts', [])) + 1:04d}"


def promote_bucket(
    accepted_path: Path,
    provisional_path: Path,
    accepted_prefix: str,
    registry: dict,
    min_distinct_sources: int,
    promotion_log: list,
) -> dict:
    accepted = load_json_bucket(accepted_path)
    provisional = load_json_bucket(provisional_path)

    accepted_norm = existing_normalized(accepted)
    provisional_facts = provisional.get("facts", [])

    # Group provisional facts by normalized statement
    grouped = {}
    for fact in provisional_facts:
        statement = fact.get("statement", "")
        norm = normalize_statement(statement)
        if not norm:
            continue
        grouped.setdefault(norm, []).append(fact)

    promoted_norms = set()
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")

    counts = {
        "promoted": 0,
        "skipped_existing_accepted": 0,
        "skipped_not_enough_sources": 0,
        "skipped_untrusted_sources": 0
    }

    for norm, group in grouped.items():
        if norm in accepted_norm:
            counts["skipped_existing_accepted"] += 1
            continue

        source_ids = sorted({
            item.get("source_metadata", {}).get("source_id")
            for item in group
            if item.get("source_metadata", {}).get("source_id")
        })

        trusted_source_ids = [sid for sid in source_ids if is_trusted_source(sid, registry)]

        if len(trusted_source_ids) < len(source_ids):
            counts["skipped_untrusted_sources"] += 1
            continue

        if len(set(trusted_source_ids)) < min_distinct_sources:
            counts["skipped_not_enough_sources"] += 1
            continue

        # Choose the first record as the base record
        base = group[0]
        promoted_record = {
            "fact_id": next_fact_id(accepted, accepted_prefix),
            "statement": base.get("statement"),
            "domain": base.get("domain"),
            "type": base.get("type"),
            "confidence": "high",
            "status": "accepted",
            "source_metadata": {
                "source_id": "multi_source_corroborated",
                "section_id": None,
                "source_type": "promoted_from_provisional"
            },
            "promotion_metadata": {
                "promoted_at_utc": timestamp,
                "corroboration_count": len(set(trusted_source_ids)),
                "source_ids": trusted_source_ids,
                "provisional_reasons": sorted({
                    item.get("provisional_reason", "unknown")
                    for item in group
                }),
                "promoted_from_file": provisional_path.name
            }
        }

        accepted["facts"].append(promoted_record)
        accepted_norm.add(norm)
        promoted_norms.add(norm)
        counts["promoted"] += 1

        promotion_log.append({
            "promoted_at_utc": timestamp,
            "accepted_file": accepted_path.name,
            "provisional_file": provisional_path.name,
            "statement": base.get("statement"),
            "normalized_statement": norm,
            "source_ids": trusted_source_ids,
            "corroboration_count": len(set(trusted_source_ids))
        })

    # Keep only non-promoted provisional facts
    remaining = []
    for fact in provisional_facts:
        norm = normalize_statement(fact.get("statement", ""))
        if norm not in promoted_norms:
            remaining.append(fact)

    provisional["facts"] = remaining

    save_json_bucket(accepted_path, accepted)
    save_json_bucket(provisional_path, provisional)

    return counts


def load_promotion_log() -> list:
    if not PROMOTION_LOG_PATH.exists():
        return []
    with open(PROMOTION_LOG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    return []


def save_promotion_log(log: list) -> None:
    with open(PROMOTION_LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=2)


def main():
    registry = load_source_registry()
    policy = get_policy()
    min_distinct_sources = policy["min_distinct_sources"]

    promotion_log = load_promotion_log()

    summary = {
        "core": promote_bucket(
            CORE_PATH, PROV_CORE_PATH, "CORE", registry, min_distinct_sources, promotion_log
        ),
        "parameters": promote_bucket(
            PARAMS_PATH, PROV_PARAMS_PATH, "PARAM", registry, min_distinct_sources, promotion_log
        ),
        "guidance": promote_bucket(
            GUIDANCE_PATH, PROV_GUIDANCE_PATH, "GUIDE", registry, min_distinct_sources, promotion_log
        ),
        "warnings": promote_bucket(
            WARNINGS_PATH, PROV_WARNINGS_PATH, "WARN", registry, min_distinct_sources, promotion_log
        ),
    }

    save_promotion_log(promotion_log)

    print(f"Promotion policy: min_distinct_sources={min_distinct_sources}")
    print(json.dumps(summary, indent=2))
    print(f"Saved promotion log to: {PROMOTION_LOG_PATH}")


if __name__ == "__main__":
    main()