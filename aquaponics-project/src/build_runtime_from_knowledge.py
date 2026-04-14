from __future__ import annotations

import argparse
import copy
import difflib
import json
import shutil
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_ROOT = PROJECT_ROOT / "data" / "knowledge"
SIMULATION_ROOT = PROJECT_ROOT / "data" / "simulation"
BACKUP_ROOT = SIMULATION_ROOT / "_sync_backups"

OWNERSHIP_NOTE = "data/knowledge is canonical; data/simulation is a derived runtime mirror."
SCOPES = ("parameters", "species", "species_evidence")


@dataclass
class PlannedChange:
    scope: str
    source_path: Path
    target_path: Path
    before_text: str
    after_text: str

    @property
    def is_new(self) -> bool:
        return not self.target_path.exists()

    @property
    def changed(self) -> bool:
        return self.before_text != self.after_text


def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def dump_json(data: dict) -> str:
    return json.dumps(data, indent=2, ensure_ascii=True) + "\n"


def now_utc() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_stamp() -> str:
    return datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")


def discover_knowledge_files(scope: str) -> list[Path]:
    root = KNOWLEDGE_ROOT / scope
    return sorted(root.rglob("*.json"))


def default_target_path(scope: str, source_path: Path) -> Path:
    relative_path = source_path.relative_to(KNOWLEDGE_ROOT / scope)
    return SIMULATION_ROOT / scope / relative_path


def resolve_target_path(scope: str, source_path: Path, payload: dict) -> Path:
    derived_path = payload.get("source_basis", {}).get("derived_from_simulation_path")
    if derived_path:
        return PROJECT_ROOT / Path(derived_path)
    return default_target_path(scope, source_path)


def build_runtime_sync_block(scope: str, source_path: Path, target_path: Path, generated_at_utc: str) -> dict:
    return {
        "scope": scope,
        "generated_at_utc": generated_at_utc,
        "canonical_source": str(source_path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "runtime_target": str(target_path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "ownership": OWNERSHIP_NOTE,
    }


def maybe_add_alias(container: dict, canonical_key: str, alias_key: str) -> None:
    if canonical_key in container and alias_key not in container:
        container[alias_key] = copy.deepcopy(container[canonical_key])


def deep_preserve_missing(existing: object, generated: object) -> object:
    if isinstance(existing, dict) and isinstance(generated, dict):
        merged = copy.deepcopy(generated)
        for key, existing_value in existing.items():
            if key not in merged:
                merged[key] = copy.deepcopy(existing_value)
            else:
                merged[key] = deep_preserve_missing(existing_value, merged[key])
        return merged

    return copy.deepcopy(generated)


def match_evidence_record(record: dict) -> tuple[str | None, str | None, str | None]:
    return (
        record.get("field"),
        record.get("normalized_field_name"),
        record.get("source_id"),
    )


def preserve_parameter_runtime_fields(existing_payload: dict, generated_payload: dict) -> dict:
    merged_payload = deep_preserve_missing(existing_payload, generated_payload)
    existing_records = {
        record.get("parameter_id"): record
        for record in existing_payload.get("records", [])
        if record.get("parameter_id")
    }

    merged_records: list[dict] = []
    for generated_record in generated_payload.get("records", []):
        parameter_id = generated_record.get("parameter_id")
        existing_record = existing_records.get(parameter_id)
        if existing_record is None:
            merged_records.append(generated_record)
            continue
        merged_records.append(deep_preserve_missing(existing_record, generated_record))

    merged_payload["records"] = merged_records
    return merged_payload


def preserve_species_runtime_fields(existing_payload: dict, generated_payload: dict) -> dict:
    return deep_preserve_missing(existing_payload, generated_payload)


def preserve_species_evidence_runtime_fields(existing_payload: dict, generated_payload: dict) -> dict:
    merged_payload = deep_preserve_missing(existing_payload, generated_payload)
    existing_records = {
        match_evidence_record(record): record
        for record in existing_payload.get("evidence_records", [])
    }

    merged_records: list[dict] = []
    for generated_record in generated_payload.get("evidence_records", []):
        existing_record = existing_records.get(match_evidence_record(generated_record))
        if existing_record is None:
            merged_records.append(generated_record)
            continue
        merged_records.append(deep_preserve_missing(existing_record, generated_record))

    merged_payload["evidence_records"] = merged_records
    return merged_payload


def preserve_runtime_only_fields(scope: str, existing_payload: dict | None, generated_payload: dict) -> dict:
    if existing_payload is None:
        return generated_payload
    if scope == "parameters":
        return preserve_parameter_runtime_fields(existing_payload, generated_payload)
    if scope == "species":
        return preserve_species_runtime_fields(existing_payload, generated_payload)
    if scope == "species_evidence":
        return preserve_species_evidence_runtime_fields(existing_payload, generated_payload)
    raise ValueError(f"Unsupported scope: {scope}")


def normalize_parameter_record(record: dict) -> dict:
    normalized = copy.deepcopy(record)
    unit = normalized.get("unit")
    kind = normalized.get("kind")

    if kind == "range" and "range" in normalized:
        normalized.setdefault("values", {})
        normalized["values"]["min"] = normalized["range"].get("min")
        normalized["values"]["max"] = normalized["range"].get("max")
        if unit is not None:
            normalized["values"]["unit"] = unit

    if kind == "scalar" and "value" in normalized:
        normalized.setdefault("values", {})
        normalized["values"]["value"] = normalized.get("value")
        if unit is not None:
            normalized["values"]["unit"] = unit

    if "threshold" in normalized and isinstance(normalized["threshold"], dict):
        threshold = normalized["threshold"]
        normalized.setdefault("operator", threshold.get("operator"))
        normalized.setdefault("value", threshold.get("value"))
        normalized.setdefault("values", {})
        operator = threshold.get("operator")
        threshold_value = threshold.get("value")
        if operator in (">", ">="):
            normalized["values"]["min"] = threshold_value
        if operator in ("<", "<="):
            normalized["values"]["max"] = threshold_value
        if unit is not None:
            normalized["values"]["unit"] = unit

    if "thresholds" in normalized and isinstance(normalized["thresholds"], list):
        for threshold in normalized["thresholds"]:
            nested_threshold = threshold.get("threshold")
            if isinstance(nested_threshold, dict):
                threshold.setdefault("operator", nested_threshold.get("operator"))
                threshold.setdefault("value", nested_threshold.get("value"))
                threshold.pop("threshold", None)
            if unit is not None:
                threshold.setdefault("unit", threshold.get("unit", unit))

    if "threshold_range" in normalized and isinstance(normalized["threshold_range"], dict):
        normalized.setdefault("values", {})
        normalized["values"]["min"] = normalized["threshold_range"].get("min")
        normalized["values"]["max"] = normalized["threshold_range"].get("max")
        if unit is not None:
            normalized["values"]["unit"] = unit

    return normalized


def transform_parameters(payload: dict) -> dict:
    runtime_payload = copy.deepcopy(payload)
    records = runtime_payload.get("records", [])
    runtime_payload["records"] = [normalize_parameter_record(record) for record in records]
    return runtime_payload


def add_species_aliases(runtime_payload: dict) -> None:
    nutrient_response = runtime_payload.get("nutrient_response")
    if isinstance(nutrient_response, dict):
        maybe_add_alias(nutrient_response, "aquaponics_nitrateN_anchor_mg_L", "aquaponics_nitrate_n_anchor_mg_L")
        maybe_add_alias(nutrient_response, "pH_operating_aquaponics", "aquaponics_operating_pH")

    validation = runtime_payload.get("validation_benchmarks", {})
    aquaponics_context = validation.get("aquaponics_context")
    if isinstance(aquaponics_context, dict):
        maybe_add_alias(aquaponics_context, "pH_operating_aquaponics", "operating_pH_range")
        maybe_add_alias(aquaponics_context, "aquaponics_nitrateN_anchor_mg_L", "nitrate_n_anchor_mg_L")

    future_fields = runtime_payload.get("future_fields")
    if isinstance(future_fields, dict):
        maybe_add_alias(future_fields, "pH_operating_aquaponics_context", "aquaponics_operating_pH_context")
        maybe_add_alias(future_fields, "disease_downy_mildew_triggers", "downy_mildew_triggers")
        maybe_add_alias(
            future_fields,
            "stress_multi_harvest_root_disease_and_deficiency",
            "multi_harvest_stress",
        )


def transform_species(payload: dict) -> dict:
    runtime_payload = copy.deepcopy(payload)
    add_species_aliases(runtime_payload)
    return runtime_payload


def add_evidence_aliases(runtime_payload: dict) -> None:
    target_fields = runtime_payload.get("target_fields")
    if isinstance(target_fields, list):
        additions: list[str] = []
        if "pH_operating_aquaponics" in target_fields and "aquaponics_operating_pH" not in target_fields:
            additions.append("aquaponics_operating_pH")
        if "aquaponics_nitrateN_anchor_mg_L" in target_fields and "aquaponics_nitrate_n_anchor_mg_L" not in target_fields:
            additions.append("aquaponics_nitrate_n_anchor_mg_L")
        target_fields.extend(additions)

    for record in runtime_payload.get("evidence_records", []):
        field_name = record.get("field")
        if field_name == "pH_operating_aquaponics":
            record.setdefault("legacy_field_alias", "aquaponics_operating_pH")
        elif field_name == "aquaponics_nitrateN_anchor_mg_L":
            record.setdefault("legacy_field_alias", "aquaponics_nitrate_n_anchor_mg_L")


def transform_species_evidence(payload: dict) -> dict:
    runtime_payload = copy.deepcopy(payload)
    add_evidence_aliases(runtime_payload)
    return runtime_payload


def transform_payload(scope: str, payload: dict) -> dict:
    if scope == "parameters":
        return transform_parameters(payload)
    if scope == "species":
        return transform_species(payload)
    if scope == "species_evidence":
        return transform_species_evidence(payload)
    raise ValueError(f"Unsupported scope: {scope}")


def add_runtime_metadata(scope: str, source_path: Path, target_path: Path, payload: dict, generated_at_utc: str) -> dict:
    runtime_payload = copy.deepcopy(payload)
    runtime_payload["runtime_sync"] = build_runtime_sync_block(
        scope=scope,
        source_path=source_path,
        target_path=target_path,
        generated_at_utc=generated_at_utc,
    )
    return runtime_payload


def plan_scope(scope: str, generated_at_utc: str) -> list[PlannedChange]:
    planned_changes: list[PlannedChange] = []
    for source_path in discover_knowledge_files(scope):
        canonical_payload = load_json(source_path)
        target_path = resolve_target_path(scope, source_path, canonical_payload)
        runtime_payload = transform_payload(scope, canonical_payload)
        existing_payload = load_json(target_path) if target_path.exists() else None
        runtime_payload = preserve_runtime_only_fields(scope, existing_payload, runtime_payload)
        runtime_payload = add_runtime_metadata(scope, source_path, target_path, runtime_payload, generated_at_utc)

        before_text = ""
        if target_path.exists():
            before_text = target_path.read_text(encoding="utf-8")
        after_text = dump_json(runtime_payload)

        planned_changes.append(
            PlannedChange(
                scope=scope,
                source_path=source_path,
                target_path=target_path,
                before_text=before_text,
                after_text=after_text,
            )
        )
    return [change for change in planned_changes if change.changed]


def build_diff(change: PlannedChange) -> str:
    before_lines = change.before_text.splitlines(keepends=True)
    after_lines = change.after_text.splitlines(keepends=True)
    relative_source = str(change.source_path.relative_to(PROJECT_ROOT)).replace("\\", "/")
    relative_target = str(change.target_path.relative_to(PROJECT_ROOT)).replace("\\", "/")
    diff_lines = difflib.unified_diff(
        before_lines,
        after_lines,
        fromfile=f"current/{relative_target}",
        tofile=f"proposed/{relative_target}",
        n=3,
    )
    header = f"## {change.scope}: {relative_source} -> {relative_target}\n"
    return header + "".join(diff_lines)


def backup_path_for(target_path: Path, stamp: str) -> Path:
    relative_target = target_path.relative_to(SIMULATION_ROOT)
    return BACKUP_ROOT / stamp / relative_target


def apply_changes(changes: list[PlannedChange]) -> tuple[int, int]:
    stamp = backup_stamp()
    backups_created = 0
    writes = 0

    for change in changes:
        if change.target_path.exists():
            backup_path = backup_path_for(change.target_path, stamp)
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(change.target_path, backup_path)
            backups_created += 1

        change.target_path.parent.mkdir(parents=True, exist_ok=True)
        change.target_path.write_text(change.after_text, encoding="utf-8")
        writes += 1

    return backups_created, writes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build simulation runtime files from canonical knowledge files.",
    )
    parser.add_argument(
        "--scope",
        action="append",
        choices=SCOPES,
        help="Limit the sync to one or more scopes. Default: all scopes.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply the proposed runtime updates after showing the diff and creating backups.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes only. This is the default behavior when --apply is not set.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    scopes = args.scope or list(SCOPES)
    generated_at_utc = now_utc()

    changes: list[PlannedChange] = []
    for scope in scopes:
        changes.extend(plan_scope(scope, generated_at_utc))

    if not changes:
        print("No runtime changes proposed.")
        return

    print("Proposed runtime sync changes:")
    print(f"- Mode: {'apply' if args.apply else 'dry-run'}")
    print(f"- Ownership: {OWNERSHIP_NOTE}")
    print(f"- Files to update: {len(changes)}")
    print("")

    for change in changes:
        print(build_diff(change))

    if not args.apply:
        print("")
        print("Dry run only. No files were written.")
        return

    backups_created, writes = apply_changes(changes)
    print("")
    print(f"Applied {writes} runtime updates.")
    print(f"Created {backups_created} backups under {BACKUP_ROOT.relative_to(PROJECT_ROOT)}.")


if __name__ == "__main__":
    main()
