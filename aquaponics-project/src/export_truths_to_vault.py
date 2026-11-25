"""Export atomic facts to Obsidian as one note per truth.

Reads every fact file in data/knowledge/atomic_facts/ (except backups) and writes:

    knowledge-vault/Truths/Truths.md                      hub: counts and links
    knowledge-vault/Truths/<Domain>/<Domain>.md           domain index
    knowledge-vault/Truths/<Domain>/<ID> <statement>.md   one note per truth

The JSON files stay the source of truth. This script only rewrites files inside
knowledge-vault/Truths/, and removes truth notes there whose fact no longer
exists. It never touches other vault notes.

Usage:
    python src/export_truths_to_vault.py [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FACTS_DIR = PROJECT_ROOT / "data" / "knowledge" / "atomic_facts"
VAULT_ROOT = PROJECT_ROOT / "knowledge-vault"
TRUTHS_ROOT = VAULT_ROOT / "Truths"

SKIP_FILES = {"approved_facts_backup.json"}

DOMAIN_FOLDERS = {
    "water_chemistry": "Water Chemistry",
    "biology": "Biology",
    "system_design": "System Design",
    "operations": "Operations",
    "risk": "Risk",
    "business": "Business",
}

# Terms linked to existing explainer notes on first mention in a statement.
EXPLAINER_LINKS = [
    (r"\bnitrification\b", "Reference/Explainers/Nitrification"),
    (r"\bunionized ammonia\b|\bNH3\b", "Reference/Explainers/Unionized Ammonia NH3"),
    (r"\bTAN\b", "Reference/Explainers/TAN"),
    (r"\bpH\b", "Reference/Explainers/pH"),
]

STATUS_LABELS = {
    "accepted": "Accepted",
    "provisional": "Candidate",
}

INVALID_FILENAME_CHARS = r'[\\/:*?"<>|#^\[\]]'


def note_title(fact: dict, max_len: int = 70) -> str:
    statement = fact.get("statement", "").replace("/", " per ")
    statement = re.sub(INVALID_FILENAME_CHARS, "", statement)
    statement = re.sub(r"\s+", " ", statement).strip().rstrip(".")
    if len(statement) > max_len:
        statement = statement[:max_len].rsplit(" ", 1)[0]
    return f"{fact['fact_id']} {statement}".strip()


def link_explainers(statement: str) -> str:
    """Link the first mention of each explainer term, skipping text already inside a link."""
    for pattern, target in EXPLAINER_LINKS:
        link_spans = [m.span() for m in re.finditer(r"\[\[.*?\]\]", statement)]
        for match in re.finditer(pattern, statement):
            if any(start <= match.start() < end for start, end in link_spans):
                continue
            text = match.group(0)
            statement = statement[: match.start()] + f"[[{target}|{text}]]" + statement[match.end():]
            break
    return statement


def yaml_value(value) -> str:
    if value is None:
        return "null"
    return json.dumps(str(value), ensure_ascii=False)


def load_facts() -> list[tuple[dict, Path]]:
    loaded = []
    seen_ids = set()
    for path in sorted(FACTS_DIR.glob("*.json")):
        if path.name in SKIP_FILES:
            continue
        doc = json.loads(path.read_text(encoding="utf-8"))
        for fact in doc.get("facts", []):
            fact_id = fact.get("fact_id")
            if not fact_id or fact_id in seen_ids:
                continue
            seen_ids.add(fact_id)
            loaded.append((fact, path))
    return loaded


def domain_folder(fact: dict) -> str:
    domain = fact.get("domain", "unknown")
    return DOMAIN_FOLDERS.get(domain, domain.replace("_", " ").title())


def format_corroboration(value) -> str:
    """Corroborating source ids, or the recorded status (e.g. single_source)."""
    if not value:
        return "not recorded"
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        ids = value.get("source_ids") or []
        status = value.get("status")
        parts = [status] if status else []
        if ids:
            parts.append(", ".join(f"`{i}`" for i in ids))
        return "; ".join(parts) or "not recorded"
    return ", ".join(f"`{i}`" for i in value)


def render_truth(fact: dict, source_path: Path) -> str:
    folder = domain_folder(fact)
    status = fact.get("status", "unknown")
    source = fact.get("source_metadata", {})
    review = fact.get("review_metadata", {})
    lines = [
        "---",
        f"fact_id: {yaml_value(fact.get('fact_id'))}",
        f"domain: {yaml_value(fact.get('domain'))}",
        f"type: {yaml_value(fact.get('type'))}",
        f"confidence: {yaml_value(fact.get('confidence'))}",
        f"status: {yaml_value(status)}",
        f"source_id: {yaml_value(source.get('source_id'))}",
        f"source_tier: {yaml_value(source.get('source_tier'))}",
        f"source_gate: {yaml_value(review.get('source_gate'))}",
        f"source_file: {yaml_value(source_path.relative_to(PROJECT_ROOT).as_posix())}",
        "tags:",
        "  - truth",
        f"  - {fact.get('domain', 'unknown')}",
        f"  - {STATUS_LABELS.get(status, status).lower()}",
        "---",
        "",
        f"# {fact['fact_id']}",
        "",
        f"> {link_explainers(fact.get('statement', ''))}",
        "",
    ]
    if status == "provisional":
        reason = fact.get("provisional_reason", "not recorded")
        lines += [f"**Candidate truth.** Not yet approved (`{reason}`).", ""]
    if fact.get("note"):
        lines += [f"Note: {fact['note']}", ""]
    context = fact.get("context")
    if context:
        lines.append("## Context")
        lines.append("")
        lines += [f"- {k.replace('_', ' ')}: {v}" for k, v in context.items()]
        lines.append("")
    lines += [
        "## Source",
        "",
        f"- Source ID: `{source.get('source_id', 'unknown')}`",
        f"- Section: `{source.get('section_id', 'unknown')}`",
        f"- Source type: `{source.get('source_type', 'unknown')}`",
        "",
        "## Reliability",
        "",
        f"- Source tier: {source.get('source_tier') or 'not recorded'}",
        f"- Source gate: {review.get('source_gate') or 'not recorded'}"
        + (f" ({review['source_gate_reason']})" if review.get("source_gate_reason") else ""),
        f"- Confidence: {fact.get('confidence') or 'not recorded'}"
        + (f". Reason: {review['confidence_reason']}" if review.get("confidence_reason") else ". Reason: not recorded"),
        f"- Corroboration: {format_corroboration(review.get('corroboration'))}",
        "",
        "## Related Notes",
        "",
        f"- [[Truths/{folder}/{folder}|{folder}]]",
        "- [[Truths/Truths|Truths]]",
        "- [[Sources/Source Register|Source Register]]",
        "",
    ]
    return "\n".join(lines)


def render_domain_index(folder: str, entries: list[tuple[dict, str]]) -> str:
    lines = [f"# {folder}", "", "Generated by `src/export_truths_to_vault.py`. Do not edit by hand.", ""]
    for label_status, label in (("accepted", "Accepted truths"), ("provisional", "Candidate truths")):
        group = [(f, t) for f, t in entries if f.get("status") == label_status]
        if not group:
            continue
        lines += [f"## {label} ({len(group)})", ""]
        lines += [f"- [[Truths/{folder}/{t}|{f['fact_id']}]]: {f.get('statement', '')}" for f, t in group]
        lines.append("")
    other = [(f, t) for f, t in entries if f.get("status") not in ("accepted", "provisional")]
    if other:
        lines += [f"## Other ({len(other)})", ""]
        lines += [f"- [[Truths/{folder}/{t}|{f['fact_id']}]] ({f.get('status')})" for f, t in other]
        lines.append("")
    lines += ["## Related Notes", "", "- [[Truths/Truths|Truths]]", ""]
    return "\n".join(lines)


def render_hub(by_folder: dict[str, list[tuple[dict, str]]]) -> str:
    total = sum(len(v) for v in by_folder.values())
    accepted = sum(1 for v in by_folder.values() for f, _ in v if f.get("status") == "accepted")
    lines = [
        "# Truths",
        "",
        "Generated by `src/export_truths_to_vault.py`. Do not edit by hand: change the JSON in",
        "`data/knowledge/atomic_facts/` and re-run the export.",
        "",
        f"**{total} truths**: {accepted} accepted, {total - accepted} candidate or other.",
        "",
        "Accepted truths are evidence-backed and reviewed. Candidate truths are sourced but",
        "wait for review. Simulation results and decisions are not truths: see",
        "[[Learnings/Simulation Findings Log|Simulation Findings Log]] and",
        "[[Project/Decisions Log|Decisions Log]].",
        "",
        "## By domain",
        "",
    ]
    for folder in sorted(by_folder):
        entries = by_folder[folder]
        n_acc = sum(1 for f, _ in entries if f.get("status") == "accepted")
        lines.append(f"- [[Truths/{folder}/{folder}|{folder}]]: {len(entries)} ({n_acc} accepted)")
    lines += ["", "## Related Notes", "", "- [[Home|Home]]", "- [[Sources/Source Register|Source Register]]", ""]
    return "\n".join(lines)


def build_outputs() -> dict[Path, str]:
    outputs: dict[Path, str] = {}
    by_folder: dict[str, list[tuple[dict, str]]] = {}
    for fact, path in load_facts():
        folder = domain_folder(fact)
        title = note_title(fact)
        by_folder.setdefault(folder, []).append((fact, title))
        outputs[TRUTHS_ROOT / folder / f"{title}.md"] = render_truth(fact, path)
    for folder, entries in by_folder.items():
        outputs[TRUTHS_ROOT / folder / f"{folder}.md"] = render_domain_index(folder, entries)
    outputs[TRUTHS_ROOT / "Truths.md"] = render_hub(by_folder)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description="Export atomic facts as one Obsidian note per truth.")
    parser.add_argument("--dry-run", action="store_true", help="List what would change without writing.")
    args = parser.parse_args()

    outputs = build_outputs()
    existing = set(TRUTHS_ROOT.rglob("*.md")) if TRUTHS_ROOT.exists() else set()
    stale = sorted(existing - set(outputs))
    changed = [p for p, text in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != text]

    if not args.dry_run:
        for path in changed:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(outputs[path], encoding="utf-8")
        for path in stale:
            path.unlink()

    print(json.dumps({
        "mode": "dry_run" if args.dry_run else "apply",
        "notes_total": len(outputs),
        "notes_written" if not args.dry_run else "notes_to_write": len(changed),
        "stale_notes_removed" if not args.dry_run else "stale_notes_to_remove": [str(p.relative_to(VAULT_ROOT)) for p in stale],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
