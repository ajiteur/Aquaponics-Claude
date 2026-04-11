import json
import re
from pathlib import Path
from datetime import datetime, UTC
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RUNS_DIR = PROJECT_ROOT / "data" / "logs" / "extraction_runs"
REVIEW_DIR = PROJECT_ROOT / "data" / "logs" / "review_runs"
CONFIG_DIR = PROJECT_ROOT / "configs"

REVIEW_DIR.mkdir(parents=True, exist_ok=True)

SOURCE_REGISTRY_PATH = CONFIG_DIR / "source_registry.yaml"

if not SOURCE_REGISTRY_PATH.exists():
    raise FileNotFoundError(f"Missing source registry: {SOURCE_REGISTRY_PATH}")

with open(SOURCE_REGISTRY_PATH, "r", encoding="utf-8") as f:
    registry_data = yaml.safe_load(f) or {}

registry_sources = registry_data.get("sources", [])
registry_by_id = {item["source_id"]: item for item in registry_sources if "source_id" in item}

json_files = sorted(RUNS_DIR.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
if not json_files:
    raise FileNotFoundError(f"No extraction run files found in {RUNS_DIR}")

latest_file = json_files[0]

with open(latest_file, "r", encoding="utf-8") as f:
    package = json.load(f)

source_metadata = package.get("source_metadata", {})
extraction = package.get("extraction", {})

source_id = source_metadata.get("source_id")
registry_entry = registry_by_id.get(source_id)

claims = extraction.get("claims", [])
entities = extraction.get("entities", [])
parameters = extraction.get("parameters", [])
processes = extraction.get("processes", [])
risks = extraction.get("risks", [])
unresolved_items = extraction.get("unresolved_items", [])

approved_claims = []
provisional_claims = []
rejected_claims = []
contradictions = []
missing_context = []

VALID_CONFIDENCE = {"high", "medium", "low"}
VALID_CLAIM_TYPES = {"definition", "process", "dependency", "risk", "parameter"}
VALID_DOMAINS = {"biology", "water_chemistry", "system_design", "operations", "risk"}

GUIDELINE_TERMS = {
    "should", "recommended", "often recommended", "may", "discouraged",
    "necessary", "can be necessary", "in many systems", "often", "typically",
    "optimal", "compromise", "best", "ideal", "set point", "begins to slow"
}

VAGUE_TERMS = {
    "important", "efficient", "good", "bad", "helps", "supports", "improves"
}

def normalize_statement(text: str) -> str:
    s = text.lower().strip()
    s = s.replace("first into", "")
    s = s.replace("then into", "")
    s = s.replace("and then to", "to")
    s = s.replace("and then into", "to")
    s = s.replace("first", "")
    s = re.sub(r"[^\w\s]", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def contains_guideline_language(statement: str) -> bool:
    s = statement.lower()
    return any(term in s for term in GUIDELINE_TERMS)

def is_vague(statement: str) -> bool:
    s = statement.lower()
    return any(term in s for term in VAGUE_TERMS) and len(statement.split()) < 14

def contains_numeric_threshold(statement: str) -> bool:
    s = statement.lower()
    return bool(re.search(r"\b\d+(\.\d+)?\b", s)) or any(sym in s for sym in ["<", ">", "≤", "≥"])

def get_source_profile(entry: dict | None) -> dict:
    if entry is None:
        return {
            "trust_status": "unknown",
            "trust_tier": None,
            "evidence_level": None,
            "source_type": None
        }

    return {
        "trust_status": str(entry.get("trust_status", "")).strip().lower(),
        "trust_tier": str(entry.get("trust_tier", "")).strip().lower(),
        "evidence_level": str(entry.get("evidence_level", "")).strip().upper(),
        "source_type": str(entry.get("source_type", "")).strip().lower()
    }

def evaluate_source(entry: dict | None) -> tuple[str, str]:
    if entry is None:
        return "unknown", "source_not_in_registry"

    trust_status = str(entry.get("trust_status", "")).strip().lower()
    evidence_level = str(entry.get("evidence_level", "")).strip().upper()

    if trust_status == "blocked":
        return "blocked", "source_blocked"

    if trust_status == "conditional":
        return "conditional", "source_conditional"

    if trust_status == "trusted":
        if evidence_level in {"E5", "E4", "E3"}:
            return "trusted", "trusted_source"
        return "conditional", "trusted_but_low_evidence_source"

    return "unknown", "unrecognized_source_status"

source_gate, source_gate_reason = evaluate_source(registry_entry)

source_profile = get_source_profile(registry_entry)

seen_normalized = set()

for claim in claims:
    statement = claim.get("statement", "").strip()
    confidence = claim.get("confidence", "").strip().lower()
    claim_type = claim.get("claim_type", "").strip().lower()
    domain = claim.get("domain", "").strip().lower()

    if not statement:
        rejected_claims.append({
            "reason": "missing_statement",
            "claim": claim
        })
        continue

    normalized = normalize_statement(statement)

    if normalized in seen_normalized:
        rejected_claims.append({
            "reason": "duplicate_or_near_duplicate_statement",
            "claim": claim
        })
        continue

    seen_normalized.add(normalized)

    if is_vague(statement):
        provisional_claims.append({
            "reason": "vague_statement",
            "claim": claim
        })
        continue

    if confidence not in VALID_CONFIDENCE:
        provisional_claims.append({
            "reason": "invalid_confidence_label",
            "claim": claim
        })
        continue

    if claim_type not in VALID_CLAIM_TYPES:
        provisional_claims.append({
            "reason": "invalid_claim_type",
            "claim": claim
        })
        continue

    if domain not in VALID_DOMAINS:
        provisional_claims.append({
            "reason": "invalid_domain",
            "claim": claim
        })
        continue

    if source_gate == "blocked":
        rejected_claims.append({
            "reason": source_gate_reason,
            "claim": claim
        })
        continue

    if source_gate in {"unknown", "conditional"}:
        provisional_claims.append({
            "reason": source_gate_reason,
            "claim": claim
        })
        continue

        # Tier 3 / commercial handling:
    # keep as provisional unless corroborated elsewhere
    if source_profile["trust_tier"] == "tier_3" or source_profile["source_type"] == "commercial_manual":
        if contains_numeric_threshold(statement):
            provisional_claims.append({
                "reason": "tier3_numeric_requires_corroboration",
                "claim": claim
            })
        else:
            provisional_claims.append({
                "reason": "commercial_secondary_only",
                "claim": claim
            })
        continue

    if confidence == "low":
        provisional_claims.append({
            "reason": "low_confidence",
            "claim": claim
        })
        continue

    if confidence == "medium":
        provisional_claims.append({
            "reason": "medium_confidence_requires_confirmation",
            "claim": claim
        })
        continue

    if contains_guideline_language(statement):
        provisional_claims.append({
            "reason": "guideline_or_recommendation_language",
            "claim": claim
        })
        continue

    approved_claims.append(claim)

review_timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
review_package = {
    "review_id": f"review_{source_id or 'unknown'}_{review_timestamp}",
    "reviewed_from_file": latest_file.name,
    "source_metadata": source_metadata,
    "source_registry_status": {
        "source_id": source_id,
        "found_in_registry": registry_entry is not None,
        "source_gate": source_gate,
        "reason": source_gate_reason,
        "evidence_level": registry_entry.get("evidence_level") if registry_entry else None,
        "trust_tier": registry_entry.get("trust_tier") if registry_entry else None,
        "trust_status": registry_entry.get("trust_status") if registry_entry else None
    },
    "summary": {
        "approved_claim_count": len(approved_claims),
        "provisional_claim_count": len(provisional_claims),
        "rejected_claim_count": len(rejected_claims),
        "entity_count": len(entities),
        "parameter_count": len(parameters),
        "process_count": len(processes),
        "risk_count": len(risks),
        "unresolved_item_count": len(unresolved_items)
    },
    "approved_claims": approved_claims,
    "provisional_claims": provisional_claims,
    "rejected_claims": rejected_claims,
    "contradictions": contradictions,
    "missing_context": missing_context,
    "entities": entities,
    "parameters": parameters,
    "processes": processes,
    "risks": risks,
    "unresolved_items": unresolved_items
}

output_path = REVIEW_DIR / f"{review_package['review_id']}.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(review_package, f, indent=2)

print(f"Reviewed latest extraction file: {latest_file.name}")
print(f"Source gate: {source_gate} ({source_gate_reason})")
print(f"Saved review output to: {output_path}")
print(json.dumps(review_package["summary"], indent=2))
