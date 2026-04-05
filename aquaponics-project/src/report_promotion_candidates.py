import json
import re
from pathlib import Path
from collections import defaultdict

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FACTS_DIR = PROJECT_ROOT / "aquaponics-knowledge" / "03_atomic_facts"
REPORT_PATH = PROJECT_ROOT / "aquaponics-knowledge" / "06_evidence_maps" / "promotion_candidates_report.json"

PROVISIONAL_FILES = {
    "core": FACTS_DIR / "provisional_core_candidates.json",
    "parameters": FACTS_DIR / "provisional_parameter_ranges.json",
    "guidance": FACTS_DIR / "provisional_operational_guidance.json",
    "warnings": FACTS_DIR / "provisional_warnings_and_cautions.json",
}

MIN_DISTINCT_SOURCES = 2


def load_bucket(path: Path) -> dict:
    if not path.exists():
        return {"facts": []}
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict) or "facts" not in data or not isinstance(data["facts"], list):
        return {"facts": []}
    return data


def normalize_statement(text: str) -> str:
    s = (text or "").lower().strip()

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

    s = re.sub(r"[^\w\s\.\-<>/]", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def main():
    report = {
        "min_distinct_sources_required": MIN_DISTINCT_SOURCES,
        "categories": {}
    }

    for category, path in PROVISIONAL_FILES.items():
        bucket = load_bucket(path)
        grouped = defaultdict(list)

        for fact in bucket["facts"]:
            norm = normalize_statement(fact.get("statement", ""))
            if norm:
                grouped[norm].append(fact)

        items = []
        for norm, facts in grouped.items():
            source_ids = sorted({
                f.get("source_metadata", {}).get("source_id")
                for f in facts
                if f.get("source_metadata", {}).get("source_id")
            })

            items.append({
                "normalized_statement": norm,
                "example_statement": facts[0].get("statement"),
                "distinct_source_count": len(source_ids),
                "source_ids": source_ids,
                "needs_additional_sources": max(0, MIN_DISTINCT_SOURCES - len(source_ids)),
                "provisional_reasons": sorted({
                    f.get("provisional_reason", "unknown")
                    for f in facts
                }),
                "count_records": len(facts)
            })

        items.sort(key=lambda x: (x["needs_additional_sources"], -x["count_records"], x["example_statement"]))
        report["categories"][category] = items

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"Saved promotion candidate report to: {REPORT_PATH}")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()