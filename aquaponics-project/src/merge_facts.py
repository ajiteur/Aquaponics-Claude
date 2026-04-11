import json
from pathlib import Path
from datetime import datetime, UTC

PROJECT_ROOT = Path(__file__).resolve().parent.parent
REVIEW_DIR = PROJECT_ROOT / "data" / "logs" / "review_runs"
FACTS_DIR = PROJECT_ROOT / "data" / "knowledge" / "atomic_facts"
FACTS_DIR.mkdir(parents=True, exist_ok=True)

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

review_files = sorted(REVIEW_DIR.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
if not review_files:
    raise FileNotFoundError(f"No review files found in {REVIEW_DIR}")

latest_review = review_files[0]

with open(latest_review, "r", encoding="utf-8") as f:
    review_package = json.load(f)

summary = review_package.get("summary")
approved_claims = review_package.get("approved_claims")
provisional_claims = review_package.get("provisional_claims", [])
source_metadata = review_package.get("source_metadata", {})
source_registry_status = review_package.get("source_registry_status", {})

if summary is None:
    raise ValueError("Review file missing 'summary'")
if approved_claims is None or not isinstance(approved_claims, list):
    raise ValueError("Review file missing valid 'approved_claims'")
if not isinstance(provisional_claims, list):
    raise ValueError("Review file has invalid 'provisional_claims'")

source_id = source_metadata.get("source_id")
source_gate = source_registry_status.get("source_gate")
source_gate_reason = source_registry_status.get("reason")

if not source_id:
    raise ValueError("Review file missing source_metadata.source_id")

if source_gate == "blocked":
    raise ValueError(
        f"Merge blocked: source '{source_id}' is blocked "
        f"(source_gate={source_gate}, reason={source_gate_reason})"
    )

def load_bucket(path: Path) -> dict:
    if not path.exists():
        return {"facts": []}

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        return {"facts": []}

    if "facts" not in data or not isinstance(data["facts"], list):
        data["facts"] = []

    return data

def existing_statements(bucket: dict) -> set:
    return {fact.get("statement", "").strip().lower() for fact in bucket.get("facts", [])}

# Accepted buckets
core_bucket = load_bucket(CORE_PATH)
params_bucket = load_bucket(PARAMS_PATH)
guidance_bucket = load_bucket(GUIDANCE_PATH)
warnings_bucket = load_bucket(WARNINGS_PATH)

# Provisional buckets
prov_core_bucket = load_bucket(PROV_CORE_PATH)
prov_params_bucket = load_bucket(PROV_PARAMS_PATH)
prov_guidance_bucket = load_bucket(PROV_GUIDANCE_PATH)
prov_warnings_bucket = load_bucket(PROV_WARNINGS_PATH)

core_seen = existing_statements(core_bucket)
params_seen = existing_statements(params_bucket)
guidance_seen = existing_statements(guidance_bucket)
warnings_seen = existing_statements(warnings_bucket)

prov_core_seen = existing_statements(prov_core_bucket)
prov_params_seen = existing_statements(prov_params_bucket)
prov_guidance_seen = existing_statements(prov_guidance_bucket)
prov_warnings_seen = existing_statements(prov_warnings_bucket)

timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")

def classify_bucket(claim: dict) -> str:
    statement = (claim.get("statement") or "").lower()
    claim_type = (claim.get("claim_type") or "").lower()

    if claim_type == "parameter":
        return "parameters"

    if claim_type == "risk":
        return "warnings"

    if any(term in statement for term in ["warning", "caution", "toxic", "toxicity", "harm"]):
        return "warnings"

    if any(term in statement for term in ["should", "recommended", "may", "discouraged", "necessary", "often"]):
        return "guidance"

    return "core"

def add_fact(bucket: dict, seen: set, claim: dict, bucket_name: str, lifecycle_status: str, provisional_reason: str | None = None) -> tuple[bool, str | None]:
    statement = (claim.get("statement") or "").strip()
    if not statement:
        return False, "missing_statement"

    key = statement.lower()
    if key in seen:
        return False, "duplicate"

    fact_list = bucket.get("facts", [])
    if not isinstance(fact_list, list):
        bucket["facts"] = []
        fact_list = bucket["facts"]

    record = {
        "fact_id": f"{bucket_name.upper()}_{len(fact_list) + 1:04d}",
        "statement": statement,
        "domain": claim.get("domain"),
        "type": claim.get("claim_type"),
        "confidence": claim.get("confidence"),
        "status": lifecycle_status,
        "source_metadata": {
            "source_id": source_metadata.get("source_id"),
            "section_id": source_metadata.get("section_id"),
            "source_type": source_metadata.get("source_type")
        },
        "review_metadata": {
            "reviewed_from_file": latest_review.name,
            "source_gate": source_gate,
            "source_gate_reason": source_gate_reason
        },
        "merged_at_utc": timestamp
    }

    if provisional_reason is not None:
        record["provisional_reason"] = provisional_reason

    bucket["facts"].append(record)
    seen.add(key)
    return True, None

counts = {
    "accepted_core": 0,
    "accepted_parameters": 0,
    "accepted_guidance": 0,
    "accepted_warnings": 0,
    "provisional_core": 0,
    "provisional_parameters": 0,
    "provisional_guidance": 0,
    "provisional_warnings": 0,
    "duplicates_skipped": 0
}

# Only trusted sources can add accepted facts
if source_gate == "trusted":
    for claim in approved_claims:
        bucket_name = classify_bucket(claim)

        if bucket_name == "core":
            added, reason = add_fact(core_bucket, core_seen, claim, "core", "accepted")
            if added:
                counts["accepted_core"] += 1
            elif reason == "duplicate":
                counts["duplicates_skipped"] += 1

        elif bucket_name == "parameters":
            added, reason = add_fact(params_bucket, params_seen, claim, "param", "accepted")
            if added:
                counts["accepted_parameters"] += 1
            elif reason == "duplicate":
                counts["duplicates_skipped"] += 1

        elif bucket_name == "guidance":
            added, reason = add_fact(guidance_bucket, guidance_seen, claim, "guide", "accepted")
            if added:
                counts["accepted_guidance"] += 1
            elif reason == "duplicate":
                counts["duplicates_skipped"] += 1

        elif bucket_name == "warnings":
            added, reason = add_fact(warnings_bucket, warnings_seen, claim, "warn", "accepted")
            if added:
                counts["accepted_warnings"] += 1
            elif reason == "duplicate":
                counts["duplicates_skipped"] += 1

# Trusted and conditional sources can add provisional facts
if source_gate in {"trusted", "conditional"}:
    for item in provisional_claims:
        claim = item.get("claim", {})
        provisional_reason = item.get("reason", "unknown_provisional_reason")
        bucket_name = classify_bucket(claim)

        if bucket_name == "core":
            added, reason = add_fact(prov_core_bucket, prov_core_seen, claim, "prov_core", "provisional", provisional_reason)
            if added:
                counts["provisional_core"] += 1
            elif reason == "duplicate":
                counts["duplicates_skipped"] += 1

        elif bucket_name == "parameters":
            added, reason = add_fact(prov_params_bucket, prov_params_seen, claim, "prov_param", "provisional", provisional_reason)
            if added:
                counts["provisional_parameters"] += 1
            elif reason == "duplicate":
                counts["duplicates_skipped"] += 1

        elif bucket_name == "guidance":
            added, reason = add_fact(prov_guidance_bucket, prov_guidance_seen, claim, "prov_guide", "provisional", provisional_reason)
            if added:
                counts["provisional_guidance"] += 1
            elif reason == "duplicate":
                counts["duplicates_skipped"] += 1

        elif bucket_name == "warnings":
            added, reason = add_fact(prov_warnings_bucket, prov_warnings_seen, claim, "prov_warn", "provisional", provisional_reason)
            if added:
                counts["provisional_warnings"] += 1
            elif reason == "duplicate":
                counts["duplicates_skipped"] += 1

with open(CORE_PATH, "w", encoding="utf-8") as f:
    json.dump(core_bucket, f, indent=2)

with open(PARAMS_PATH, "w", encoding="utf-8") as f:
    json.dump(params_bucket, f, indent=2)

with open(GUIDANCE_PATH, "w", encoding="utf-8") as f:
    json.dump(guidance_bucket, f, indent=2)

with open(WARNINGS_PATH, "w", encoding="utf-8") as f:
    json.dump(warnings_bucket, f, indent=2)

with open(PROV_CORE_PATH, "w", encoding="utf-8") as f:
    json.dump(prov_core_bucket, f, indent=2)

with open(PROV_PARAMS_PATH, "w", encoding="utf-8") as f:
    json.dump(prov_params_bucket, f, indent=2)

with open(PROV_GUIDANCE_PATH, "w", encoding="utf-8") as f:
    json.dump(prov_guidance_bucket, f, indent=2)

with open(PROV_WARNINGS_PATH, "w", encoding="utf-8") as f:
    json.dump(prov_warnings_bucket, f, indent=2)

print(f"Read review file: {latest_review.name}")
print(f"Source gate: {source_gate} ({source_gate_reason})")
print(json.dumps(counts, indent=2))
print("Saved categorized facts to:")
print(f" - {CORE_PATH}")
print(f" - {PARAMS_PATH}")
print(f" - {GUIDANCE_PATH}")
print(f" - {WARNINGS_PATH}")
print("Saved provisional categorized facts to:")
print(f" - {PROV_CORE_PATH}")
print(f" - {PROV_PARAMS_PATH}")
print(f" - {PROV_GUIDANCE_PATH}")
print(f" - {PROV_WARNINGS_PATH}")
