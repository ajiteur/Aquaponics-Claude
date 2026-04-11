from pathlib import Path
import json
from datetime import datetime, UTC
from typing import Iterable

PROJECT_ROOT = Path(__file__).resolve().parent.parent

VAULT_ROOT = PROJECT_ROOT / "knowledge-vault"
COMPONENT_LIBRARY_PATH = PROJECT_ROOT / "data" / "simulation" / "components" / "component_library.json"

ATOMIC_FACT_CANDIDATE_PATHS = [
    PROJECT_ROOT / "data" / "knowledge" / "atomic_facts" / "atomic_facts_core.json",
    PROJECT_ROOT / "data" / "knowledge" / "atomic_facts" / "parameter_ranges.json",
    PROJECT_ROOT / "data" / "knowledge" / "atomic_facts" / "warnings_and_cautions.json",
    PROJECT_ROOT / "data" / "knowledge" / "atomic_facts" / "operational_guidance.json",
    PROJECT_ROOT / "data" / "simulation" / "atomic_facts_core.json",
    PROJECT_ROOT / "data" / "simulation" / "atomic_facts_parameters.json",
    PROJECT_ROOT / "data" / "simulation" / "atomic_facts_warnings_and_cautions.json",
    PROJECT_ROOT / "data" / "simulation" / "atomic_facts_operational_guidance.json",
]

UPDATE_LOGS_DIR = PROJECT_ROOT / "data" / "logs" / "update_logs"
RESEARCH_REPORT_PREFIX = "research_to_tuning_cycle_report_"
COMPARE_REPORT_PREFIX = "compare_lettuce_vs_basil_"
VIABLE_REPORT_PREFIX = "viable_scenarios_report_"

GENERATED_AT = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_json(path: Path, default=None):
    if not path.exists():
        return {} if default is None else default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def find_existing_atomic_fact_files() -> list[Path]:
    existing = []
    seen = set()
    for path in ATOMIC_FACT_CANDIDATE_PATHS:
        if path.exists():
            resolved = str(path.resolve())
            if resolved not in seen:
                existing.append(path)
                seen.add(resolved)
    return existing


def to_bullet_list(items: list[str], indent: int = 0) -> str:
    prefix = "  " * indent
    return "\n".join(f"{prefix}- {item}" for item in items) if items else f"{prefix}- None"


def note_path_to_wiki_link(note_path: str, display_text: str | None = None) -> str:
    if display_text:
        return f"[[{note_path}|{display_text}]]"
    return f"[[{note_path}]]"


def render_link_list(links: list[tuple[str, str | None]]) -> str:
    if not links:
        return "- None"
    return "\n".join(
        f"- {note_path_to_wiki_link(path, display)}"
        for path, display in links
    )


def append_related_notes(lines: list[str], links: list[tuple[str, str | None]]) -> None:
    lines.append("## Related Notes")
    lines.append("")
    lines.append(render_link_list(links))
    lines.append("")


def sanitize_note_name(name: str) -> str:
    return name.replace("/", " ").replace("\\", " ").strip()


def slugify_note_name(name: str) -> str:
    safe = sanitize_note_name(name)
    for char in [":", "*", "?", "\"", "<", ">", "|"]:
        safe = safe.replace(char, "")
    return safe


def find_latest_matching_file(prefix: str) -> Path | None:
    files = sorted(
        UPDATE_LOGS_DIR.glob(f"{prefix}*.json"),
        key=lambda path: path.stat().st_mtime,
        reverse=True
    )
    return files[0] if files else None


def render_component_note(component: dict) -> str:
    lines = []
    note_name = slugify_note_name(component.get("name", component.get("component_id", "Unknown Component")))
    category = component.get("category", "unknown")
    lines.append(f"# {component.get('name', component.get('component_id', 'Unknown Component'))}")
    lines.append("")
    lines.append(f"Generated at: `{GENERATED_AT}`")
    lines.append("")
    lines.append(f"- Component ID: `{component.get('component_id', 'unknown')}`")
    lines.append(f"- Category: `{component.get('category', 'unknown')}`")
    lines.append(f"- Role: {component.get('role', 'unknown')}")
    lines.append(f"- Status: `{component.get('status', 'unknown')}`")
    lines.append(f"- CAPEX: `{component.get('capex', 'unknown')}`")
    lines.append(f"- Power (W): `{component.get('power_w', 'unknown')}`")
    lines.append(f"- Maintenance interval (days): `{component.get('maintenance_interval_days', 'unknown')}`")
    lines.append(f"- Upgrade tier: `{component.get('upgrade_tier', 'unknown')}`")
    lines.append("")
    lines.append("## Affects Variables")
    lines.append("")
    lines.append(to_bullet_list(component.get("affects_variables", [])))
    lines.append("")
    lines.append("## Failure Modes")
    lines.append("")
    lines.append(to_bullet_list(component.get("failure_modes", [])))
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append(to_bullet_list(component.get("notes", [])))
    lines.append("")
    append_related_notes(lines, [
        ("Home", "Home"),
        ("Components/Components", "Components"),
        ("Sources/Source Register", "Source Register"),
        ("Learnings/Simulation Learnings", "Simulation Learnings"),
        ("Atomic Truths/Parameter Atomic Truths", "Parameter Atomic Truths"),
    ])
    return "\n".join(lines).strip() + "\n"


def render_components_index_note(component_library: dict) -> str:
    lines = []
    lines.append("# Components")
    lines.append("")
    lines.append(f"Generated at: `{GENERATED_AT}`")
    lines.append("")
    lines.append(f"Library version: `{component_library.get('version', 'unknown')}`")
    lines.append(f"Library status: `{component_library.get('status', 'unknown')}`")
    lines.append("")

    notes = component_library.get("notes", [])
    if notes:
        lines.append("## Library Notes")
        lines.append("")
        lines.append(to_bullet_list(notes))
        lines.append("")

    sections = [
        ("Water Loop", "water_loop_components", "Water Loop"),
        ("Grow", "grow_components", "Grow"),
        ("Equipment", "equipment_components", "Equipment"),
        ("Sensors", "sensor_components", "Sensors"),
    ]

    for heading, key, folder_name in sections:
        components = component_library.get(key, [])
        lines.append(f"## {heading}")
        lines.append("")
        lines.append(f"Count: **{len(components)}**")
        lines.append("")
        if components:
            for component in components:
                note_name = slugify_note_name(component.get("name", component.get("component_id", "Unknown Component")))
                lines.append(f"- {note_path_to_wiki_link(f'Components/{folder_name}/{note_name}', component.get('name', note_name))}")
        else:
            lines.append("- None")
        lines.append("")

    append_related_notes(lines, [
        ("Home", "Home"),
        ("Sources/Source Register", "Source Register"),
        ("Learnings/Simulation Learnings", "Simulation Learnings"),
        ("Atomic Truths/Atomic Truths", "Atomic Truths"),
    ])
    return "\n".join(lines).strip() + "\n"


def render_source_register_note() -> str:
    lines = []
    lines.append("# Source Register")
    lines.append("")
    lines.append(f"Generated at: `{GENERATED_AT}`")
    lines.append("")
    lines.append("Starter register for evidence, report digests, and source tracking.")
    lines.append("Fill this note later from report digests, species evidence JSON, and external source metadata.")
    lines.append("")
    lines.append("## Planned Inputs")
    lines.append("")
    lines.append("- `data/knowledge/report_digests/*.json`")
    lines.append("- `data/simulation/species_evidence/*.json`")
    lines.append("- `data/logs/update_logs/*.json`")
    lines.append("")
    lines.append("## Suggested Fields")
    lines.append("")
    lines.append("- Source ID")
    lines.append("- Source type")
    lines.append("- Topic")
    lines.append("- Reliability notes")
    lines.append("- Last seen in report")
    lines.append("- Follow-up actions")
    lines.append("")
    append_related_notes(lines, [
        ("Home", "Home"),
        ("Components/Components", "Components"),
        ("Learnings/Simulation Learnings", "Simulation Learnings"),
        ("Atomic Truths/Atomic Truths", "Atomic Truths"),
    ])
    return "\n".join(lines).strip() + "\n"


def summarize_research_report(report: dict, report_path: Path) -> list[str]:
    recommendation = report.get("recommendation", {})
    baseline = report.get("baseline_summary", {})
    tuned = report.get("tuned_summary", {})

    return [
        f"### Research to Tuning: `{report_path.name}`",
        "",
        f"- Recommendation: `{recommendation.get('decision', 'unknown')}`",
        f"- Reason: {recommendation.get('reason', 'No reason provided.')}",
        f"- Baseline NH3: `{baseline.get('unionized_nh3_mg_L', 'unknown')}`",
        f"- Tuned NH3: `{tuned.get('unionized_nh3_mg_L', 'unknown')}`",
        f"- Baseline stability: `{baseline.get('system_stability_score', 'unknown')}`",
        f"- Tuned stability: `{tuned.get('system_stability_score', 'unknown')}`",
        "",
    ]


def summarize_compare_report(report: dict, report_path: Path) -> list[str]:
    comparison = report.get("final_day_comparison", {})
    return [
        f"### Scenario Comparison: `{report_path.name}`",
        "",
        f"- Lettuce NH3 risk band: `{comparison.get('unionized_nh3_risk_band', {}).get('lettuce', 'unknown')}`",
        f"- Basil NH3 risk band: `{comparison.get('unionized_nh3_risk_band', {}).get('basil', 'unknown')}`",
        f"- Plant biomass delta (basil - lettuce): `{comparison.get('plant_avg_biomass_g', {}).get('difference_basil_minus_lettuce', 'unknown')}`",
        f"- Nitrate delta (basil - lettuce): `{comparison.get('nitrate_mg_L', {}).get('difference_basil_minus_lettuce', 'unknown')}`",
        f"- Stability delta (basil - lettuce): `{comparison.get('system_stability_score', {}).get('difference_basil_minus_lettuce', 'unknown')}`",
        "",
    ]


def summarize_viable_report(report: dict, report_path: Path) -> list[str]:
    counts = report.get("counts", {})
    top = report.get("top_10_viable", [])
    best = top[0] if top else {}
    settings = best.get("settings", {})
    final_day = best.get("final_day", {})

    return [
        f"### Viable Scenarios: `{report_path.name}`",
        "",
        f"- Tested scenarios: `{counts.get('tested', 'unknown')}`",
        f"- Viable scenarios: `{counts.get('viable', 'unknown')}`",
        f"- Best composite score: `{best.get('composite_score', 'unknown')}`",
        f"- Best NH3: `{final_day.get('unionized_nh3_mg_L', 'unknown')}`",
        f"- Best settings: feed=`{settings.get('feed_rate_percent_body_weight_per_day', 'unknown')}`, plants=`{settings.get('plant_count', 'unknown')}`, biofilter=`{settings.get('biofilter_maturity', 'unknown')}`, water=`{settings.get('water_volume_l', 'unknown')}`, mode=`{settings.get('mode', 'unknown')}`",
        "",
    ]


def render_simulation_learnings_note() -> str:
    lines = []
    lines.append("# Simulation Learnings")
    lines.append("")
    lines.append(f"Generated at: `{GENERATED_AT}`")
    lines.append("")
    lines.append("Summary from the latest relevant simulation update logs, when present.")
    lines.append("")

    latest_research = find_latest_matching_file(RESEARCH_REPORT_PREFIX)
    latest_compare = find_latest_matching_file(COMPARE_REPORT_PREFIX)
    latest_viable = find_latest_matching_file(VIABLE_REPORT_PREFIX)

    if latest_research:
        lines.extend(summarize_research_report(load_json(latest_research, default={}), latest_research))
    if latest_compare:
        lines.extend(summarize_compare_report(load_json(latest_compare, default={}), latest_compare))
    if latest_viable:
        lines.extend(summarize_viable_report(load_json(latest_viable, default={}), latest_viable))

    if not any([latest_research, latest_compare, latest_viable]):
        lines.append("- No relevant update-log reports were found.")
        lines.append("")

    append_related_notes(lines, [
        ("Home", "Home"),
        ("Sources/Source Register", "Source Register"),
        ("Components/Components", "Components"),
        ("Atomic Truths/Atomic Truths", "Atomic Truths"),
    ])
    return "\n".join(lines).strip() + "\n"


def render_atomic_facts_index_note(atomic_fact_files: list[Path]) -> str:
    lines = []
    lines.append("# Atomic Truths")
    lines.append("")
    lines.append(f"Generated at: `{GENERATED_AT}`")
    lines.append("")
    lines.append("This index links the currently exported atomic-truth notes.")
    lines.append("")

    if not atomic_fact_files:
        lines.append("- No atomic fact files were found.")
        lines.append("")
        return "\n".join(lines)

    for path in atomic_fact_files:
        title = title_from_atomic_fact_filename(path.name)
        note_name = sanitize_note_name(title)
        lines.append(f"- {note_path_to_wiki_link(f'Atomic Truths/{note_name}')}")

    lines.append("")
    append_related_notes(lines, [
        ("Home", "Home"),
        ("Components/Components", "Components"),
        ("Sources/Source Register", "Source Register"),
        ("Learnings/Simulation Learnings", "Simulation Learnings"),
    ])
    return "\n".join(lines)


def title_from_atomic_fact_filename(filename: str) -> str:
    stem = filename.replace(".json", "")
    mapping = {
        "atomic_facts_core": "Core Atomic Truths",
        "parameter_ranges": "Parameter Atomic Truths",
        "warnings_and_cautions": "Warnings and Cautions Atomic Truths",
        "operational_guidance": "Operational Guidance Atomic Truths",
    }
    return mapping.get(stem, stem.replace("_", " ").title())


def render_atomic_facts_note(title: str, facts_doc: dict, source_path: Path) -> str:
    facts = facts_doc.get("facts", [])
    related_links = [
        ("Home", "Home"),
        ("Atomic Truths/Atomic Truths", "Atomic Truths"),
        ("Sources/Source Register", "Source Register"),
        ("Learnings/Simulation Learnings", "Simulation Learnings"),
    ]

    if "Parameter" in title:
        related_links.append(("Components/Components", "Components"))
    elif "Operational Guidance" in title or "Warnings" in title:
        related_links.append(("Components/Components", "Components"))

    lines = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"Generated at: `{GENERATED_AT}`")
    lines.append("")
    lines.append(f"Source JSON: `{source_path}`")
    lines.append("")
    lines.append(f"Fact count: **{len(facts)}**")
    lines.append("")

    if not facts:
        lines.append("- No facts found in this file.")
        lines.append("")
        return "\n".join(lines)

    for fact in facts:
        fact_id = fact.get("fact_id", "unknown")
        statement = fact.get("statement", "")
        domain = fact.get("domain", "unknown")
        fact_type = fact.get("type", "unknown")
        confidence = fact.get("confidence", "unknown")
        status = fact.get("status", "unknown")
        provisional_reason = fact.get("provisional_reason")
        source_metadata = fact.get("source_metadata", {})
        review_metadata = fact.get("review_metadata", {})

        lines.append(f"## {fact_id}")
        lines.append("")
        lines.append(f"- Statement: {statement}")
        lines.append(f"- Domain: `{domain}`")
        lines.append(f"- Type: `{fact_type}`")
        lines.append(f"- Confidence: `{confidence}`")
        lines.append(f"- Status: `{status}`")

        if provisional_reason:
            lines.append(f"- Provisional reason: `{provisional_reason}`")

        if source_metadata:
            lines.append("- Source metadata:")
            lines.append(f"  - Source ID: `{source_metadata.get('source_id', 'unknown')}`")
            lines.append(f"  - Section ID: `{source_metadata.get('section_id', 'unknown')}`")
            lines.append(f"  - Source type: `{source_metadata.get('source_type', 'unknown')}`")

        if review_metadata:
            lines.append("- Review metadata:")
            for k, v in review_metadata.items():
                lines.append(f"  - {k}: `{v}`")

        lines.append("")

    append_related_notes(lines, related_links)
    return "\n".join(lines).strip() + "\n"


def main():
    VAULT_ROOT.mkdir(parents=True, exist_ok=True)

    components_root = VAULT_ROOT / "Components"
    components_index_path = components_root / "Components.md"
    sources_index_path = VAULT_ROOT / "Sources" / "Source Register.md"
    learnings_index_path = VAULT_ROOT / "Learnings" / "Simulation Learnings.md"

    component_library = load_json(COMPONENT_LIBRARY_PATH, default={})
    atomic_fact_files = find_existing_atomic_fact_files()

    component_sections = [
        ("Water Loop", "water_loop_components"),
        ("Grow", "grow_components"),
        ("Equipment", "equipment_components"),
        ("Sensors", "sensor_components"),
    ]

    write_text(components_index_path, render_components_index_note(component_library))
    component_notes_exported = 0
    for folder_name, key in component_sections:
        for component in component_library.get(key, []):
            component_name = slugify_note_name(component.get("name", component.get("component_id", "Unknown Component")))
            component_path = components_root / folder_name / f"{component_name}.md"
            write_text(component_path, render_component_note(component))
            component_notes_exported += 1

    write_text(sources_index_path, render_source_register_note())
    write_text(learnings_index_path, render_simulation_learnings_note())

    atomic_index_path = VAULT_ROOT / "Atomic Truths" / "Atomic Truths.md"
    write_text(atomic_index_path, render_atomic_facts_index_note(atomic_fact_files))

    for fact_path in atomic_fact_files:
        title = title_from_atomic_fact_filename(fact_path.name)
        note_name = sanitize_note_name(title) + ".md"
        facts_doc = load_json(fact_path, default={})
        note_path = VAULT_ROOT / "Atomic Truths" / note_name
        write_text(note_path, render_atomic_facts_note(title, facts_doc, fact_path))

    home_lines = [
        "# Aquaponics Knowledge Vault",
        "",
        f"Generated at: `{GENERATED_AT}`",
        "",
        "## Sections",
        "",
        f"- {note_path_to_wiki_link('Components/Components', 'Components')}",
        f"- {note_path_to_wiki_link('Atomic Truths/Atomic Truths', 'Atomic Truths')}",
        f"- {note_path_to_wiki_link('Sources/Source Register', 'Source Register')}",
        f"- {note_path_to_wiki_link('Learnings/Simulation Learnings', 'Simulation Learnings')}",
        "",
        "## Notes",
        "",
        "- This vault is generated from local JSON source files.",
        "- Treat the JSON files as source of truth.",
        "- Treat these Markdown files as human-readable exports.",
        "",
    ]
    append_related_notes(home_lines, [
        ("Components/Components", "Components"),
        ("Atomic Truths/Atomic Truths", "Atomic Truths"),
        ("Sources/Source Register", "Source Register"),
        ("Learnings/Simulation Learnings", "Simulation Learnings"),
    ])
    write_text(VAULT_ROOT / "Home.md", "\n".join(home_lines))

    print(f"Exported Obsidian vault content to: {VAULT_ROOT}")
    print(json.dumps({
        "vault_root": str(VAULT_ROOT),
        "components_index_note": str(components_index_path),
        "component_notes_exported": component_notes_exported,
        "source_register_note": str(sources_index_path),
        "simulation_learnings_note": str(learnings_index_path),
        "atomic_truth_index_note": str(atomic_index_path),
        "atomic_truth_files_exported": len(atomic_fact_files),
    }, indent=2))


if __name__ == "__main__":
    main()
