from __future__ import annotations

import argparse
import copy
import difflib
import json
import shutil
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


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


@dataclass
class ScopeSummary:
    scope: str
    files_scanned: int = 0
    files_changed: int = 0
    files_unchanged: int = 0
    validation_passed: int = 0
    validation_failed: int = 0


class ValidationError(ValueError):
    def __init__(self, scope: str, source_path: Path, field_path: str, reason: str):
        self.scope = scope
        self.source_path = source_path
        self.field_path = field_path
        self.reason = reason
        message = (
            f"Validation failed: scope={scope}; "
            f"source={source_path}; "
            f"path={field_path}; "
            f"reason={reason}"
        )
        super().__init__(message)


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


def fail_validation(scope: str, source_path: Path, field_path: str, reason: str) -> None:
    raise ValidationError(scope, source_path, field_path, reason)


def require_dict(value: Any, scope: str, source_path: Path, label: str) -> dict:
    if not isinstance(value, dict):
        fail_validation(scope, source_path, label, "must be an object")
    return value


def require_list(value: Any, scope: str, source_path: Path, label: str) -> list:
    if not isinstance(value, list):
        fail_validation(scope, source_path, label, "must be a list")
    return value


def require_string(value: Any, scope: str, source_path: Path, label: str) -> str:
    if not isinstance(value, str) or not value:
        fail_validation(scope, source_path, label, "must be a non-empty string")
    return value


def validate_runtime_sync(payload: dict, scope: str, source_path: Path, target_path: Path) -> None:
    runtime_sync = require_dict(payload.get("runtime_sync"), scope, source_path, "runtime_sync")
    require_string(runtime_sync.get("scope"), scope, source_path, "runtime_sync.scope")
    require_string(runtime_sync.get("generated_at_utc"), scope, source_path, "runtime_sync.generated_at_utc")
    require_string(runtime_sync.get("canonical_source"), scope, source_path, "runtime_sync.canonical_source")
    require_string(runtime_sync.get("runtime_target"), scope, source_path, "runtime_sync.runtime_target")
    require_string(runtime_sync.get("ownership"), scope, source_path, "runtime_sync.ownership")

    if runtime_sync["scope"] != scope:
        fail_validation(scope, source_path, "runtime_sync.scope", f"must equal {scope}")

    expected_source = str(source_path.relative_to(PROJECT_ROOT)).replace("\\", "/")
    expected_target = str(target_path.relative_to(PROJECT_ROOT)).replace("\\", "/")

    if runtime_sync["canonical_source"] != expected_source:
        fail_validation(scope, source_path, "runtime_sync.canonical_source", f"must equal {expected_source}")
    if runtime_sync["runtime_target"] != expected_target:
        fail_validation(scope, source_path, "runtime_sync.runtime_target", f"must equal {expected_target}")


def validate_parameters_payload(payload: dict, source_path: Path, target_path: Path) -> None:
    require_string(payload.get("version"), "parameters", source_path, "parameters.version")
    require_string(payload.get("status"), "parameters", source_path, "parameters.status")
    require_list(payload.get("records"), "parameters", source_path, "parameters.records")
    if "source_basis" in payload:
        require_dict(payload.get("source_basis"), "parameters", source_path, "parameters.source_basis")
    validate_runtime_sync(payload, "parameters", source_path, target_path)

    for index, record in enumerate(payload["records"]):
        record = require_dict(record, "parameters", source_path, f"parameters.records[{index}]")
        require_string(record.get("parameter_id"), "parameters", source_path, f"parameters.records[{index}].parameter_id")
        require_string(record.get("name"), "parameters", source_path, f"parameters.records[{index}].name")
        require_string(record.get("kind"), "parameters", source_path, f"parameters.records[{index}].kind")
        require_string(record.get("status"), "parameters", source_path, f"parameters.records[{index}].status")
        if "context_tags" in record:
            require_list(record["context_tags"], "parameters", source_path, f"parameters.records[{index}].context_tags")
        if "notes" in record:
            require_list(record["notes"], "parameters", source_path, f"parameters.records[{index}].notes")
        if "simulation_use" in record:
            require_dict(record["simulation_use"], "parameters", source_path, f"parameters.records[{index}].simulation_use")
        if "values" in record:
            require_dict(record["values"], "parameters", source_path, f"parameters.records[{index}].values")


def validate_species_payload(payload: dict, source_path: Path, target_path: Path) -> None:
    require_string(payload.get("species_id"), "species", source_path, "species.species_id")
    require_string(payload.get("scientific_name"), "species", source_path, "species.scientific_name")
    require_string(payload.get("common_name"), "species", source_path, "species.common_name")
    require_string(payload.get("category"), "species", source_path, "species.category")
    require_string(payload.get("status"), "species", source_path, "species.status")

    if "source_basis" in payload:
        require_dict(payload.get("source_basis"), "species", source_path, "species.source_basis")

    validate_runtime_sync(payload, "species", source_path, target_path)

    environment = require_dict(payload.get("environment"), "species", source_path, "species.environment")
    require_dict(environment.get("preferred_pH"), "species", source_path, "species.environment.preferred_pH")
    require_dict(environment.get("preferred_temp_c"), "species", source_path, "species.environment.preferred_temp_c")

    if "nutrient_response" in payload:
        require_dict(payload["nutrient_response"], "species", source_path, "species.nutrient_response")

    for field_name in ("growth_notes", "stress_notes", "evidence"):
        if field_name in payload:
            require_list(payload[field_name], "species", source_path, f"species.{field_name}")


def validate_species_evidence_payload(payload: dict, source_path: Path, target_path: Path) -> None:
    require_string(payload.get("species_id"), "species_evidence", source_path, "species_evidence.species_id")
    require_string(payload.get("status"), "species_evidence", source_path, "species_evidence.status")
    require_list(payload.get("target_fields"), "species_evidence", source_path, "species_evidence.target_fields")
    require_list(payload.get("evidence_records"), "species_evidence", source_path, "species_evidence.evidence_records")

    if "source_basis" in payload:
        require_dict(payload.get("source_basis"), "species_evidence", source_path, "species_evidence.source_basis")

    validate_runtime_sync(payload, "species_evidence", source_path, target_path)

    for index, record in enumerate(payload["evidence_records"]):
        record = require_dict(record, "species_evidence", source_path, f"species_evidence.evidence_records[{index}]")
        require_string(record.get("field"), "species_evidence", source_path, f"species_evidence.evidence_records[{index}].field")

        if "normalized_field_name" in record and record["normalized_field_name"] is not None:
            require_string(
                record["normalized_field_name"],
                "species_evidence",
                source_path,
                f"species_evidence.evidence_records[{index}].normalized_field_name",
            )

        if "source_id" in record and record["source_id"] is not None:
            require_string(
                record["source_id"],
                "species_evidence",
                source_path,
                f"species_evidence.evidence_records[{index}].source_id",
            )

        if "context_tags" in record:
            require_list(
                record["context_tags"],
                "species_evidence",
                source_path,
                f"species_evidence.evidence_records[{index}].context_tags",
            )

        if "notes" in record:
            notes = record["notes"]
            if not isinstance(notes, (str, list)):
                fail_validation(
                    "species_evidence",
                    source_path,
                    f"species_evidence.evidence_records[{index}].notes",
                    "must be a string or list",
                )


def validate_generated_payload(scope: str, payload: dict, source_path: Path, target_path: Path) -> None:
    if scope == "parameters":
        validate_parameters_payload(payload, source_path, target_path)
        return
    if scope == "species":
        validate_species_payload(payload, source_path, target_path)
        return
    if scope == "species_evidence":
        validate_species_evidence_payload(payload, source_path, target_path)
        return
    raise ValidationError(scope, source_path, scope, "unsupported scope")


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


def validate_alias_consistency(scope: str, payload: dict, source_path: Path) -> None:
    alias_pairs: list[tuple[str, str, dict | None]] = []

    nutrient_response = payload.get("nutrient_response")
    if isinstance(nutrient_response, dict):
        alias_pairs.extend(
            [
                (
                    "nutrient_response.aquaponics_nitrateN_anchor_mg_L",
                    "nutrient_response.aquaponics_nitrate_n_anchor_mg_L",
                    nutrient_response,
                ),
                (
                    "nutrient_response.pH_operating_aquaponics",
                    "nutrient_response.aquaponics_operating_pH",
                    nutrient_response,
                ),
            ]
        )

    future_fields = payload.get("future_fields")
    if isinstance(future_fields, dict):
        alias_pairs.extend(
            [
                (
                    "future_fields.pH_operating_aquaponics_context",
                    "future_fields.aquaponics_operating_pH_context",
                    future_fields,
                ),
                (
                    "future_fields.disease_downy_mildew_triggers",
                    "future_fields.downy_mildew_triggers",
                    future_fields,
                ),
                (
                    "future_fields.stress_multi_harvest_root_disease_and_deficiency",
                    "future_fields.multi_harvest_stress",
                    future_fields,
                ),
            ]
        )

    for canonical_path, alias_path, container in alias_pairs:
        if not container:
            continue
        canonical_key = canonical_path.split(".")[-1]
        alias_key = alias_path.split(".")[-1]
        if canonical_key in container and alias_key in container and container[canonical_key] != container[alias_key]:
            fail_validation(scope, source_path, alias_path, f"must mirror canonical value at {canonical_path}")


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


def payload_without_runtime_timestamp(payload: dict) -> dict:
    cloned = copy.deepcopy(payload)
    runtime_sync = cloned.get("runtime_sync")
    if isinstance(runtime_sync, dict):
        runtime_sync.pop("generated_at_utc", None)
    return cloned


def stabilize_runtime_sync_timestamp(existing_payload: dict | None, runtime_payload: dict) -> dict:
    if existing_payload is None:
        return runtime_payload

    existing_sync = existing_payload.get("runtime_sync")
    new_sync = runtime_payload.get("runtime_sync")

    if not isinstance(existing_sync, dict) or not isinstance(new_sync, dict):
        return runtime_payload

    if payload_without_runtime_timestamp(existing_payload) == payload_without_runtime_timestamp(runtime_payload):
        existing_timestamp = existing_sync.get("generated_at_utc")
        if isinstance(existing_timestamp, str) and existing_timestamp:
            runtime_payload["runtime_sync"]["generated_at_utc"] = existing_timestamp

    return runtime_payload


def plan_scope(scope: str, generated_at_utc: str) -> list[PlannedChange]:
    return plan_scope_with_summary(scope, generated_at_utc)[0]


def plan_scope_with_summary(scope: str, generated_at_utc: str) -> tuple[list[PlannedChange], ScopeSummary]:
    planned_changes: list[PlannedChange] = []
    summary = ScopeSummary(scope=scope)

    for source_path in discover_knowledge_files(scope):
        summary.files_scanned += 1

        canonical_payload = load_json(source_path)
        target_path = resolve_target_path(scope, source_path, canonical_payload)
        existing_payload = load_json(target_path) if target_path.exists() else None

        runtime_payload = transform_payload(scope, canonical_payload)
        runtime_payload = preserve_runtime_only_fields(scope, existing_payload, runtime_payload)
        runtime_payload = add_runtime_metadata(scope, source_path, target_path, runtime_payload, generated_at_utc)
        runtime_payload = stabilize_runtime_sync_timestamp(existing_payload, runtime_payload)

        try:
            validate_generated_payload(scope, runtime_payload, source_path, target_path)
            validate_alias_consistency(scope, runtime_payload, source_path)
        except ValidationError:
            summary.validation_failed += 1
            raise

        summary.validation_passed += 1

        before_text = target_path.read_text(encoding="utf-8") if target_path.exists() else ""
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

    changed = [change for change in planned_changes if change.changed]
    summary.files_changed = len(changed)
    summary.files_unchanged = summary.files_scanned - summary.files_changed
    return changed, summary


def build_summary(changes: list[PlannedChange], mode: str, scope_summaries: list[ScopeSummary]) -> dict:
    by_scope: dict[str, dict[str, int]] = {}

    for item in scope_summaries:
        scoped_changes = [change for change in changes if change.scope == item.scope]
        by_scope[item.scope] = {
            "files_scanned": item.files_scanned,
            "files_changed": item.files_changed,
            "files_unchanged": item.files_unchanged,
            "new_files": sum(1 for change in scoped_changes if change.is_new),
            "updated_files": sum(1 for change in scoped_changes if not change.is_new),
            "validation_passed": item.validation_passed,
            "validation_failed": item.validation_failed,
        }

    return {
        "mode": mode,
        "ownership": OWNERSHIP_NOTE,
        "files_scanned": sum(item.files_scanned for item in scope_summaries),
        "files_with_proposed_changes": len(changes),
        "files_unchanged": sum(item.files_unchanged for item in scope_summaries),
        "validation_passed_count": sum(item.validation_passed for item in scope_summaries),
        "validation_failed_count": sum(item.validation_failed for item in scope_summaries),
        "scopes_processed": [item.scope for item in scope_summaries],
        "scopes": by_scope,
        "targets": [
            {
                "scope": change.scope,
                "source": str(change.source_path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
                "target": str(change.target_path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
                "status": "create" if change.is_new else "update",
            }
            for change in changes
        ],
    }


def render_summary(summary: dict) -> str:
    lines = [
        f"{summary['mode'].capitalize()} summary report:",
        f"- Mode: {summary['mode']}",
        f"- Ownership: {summary['ownership']}",
        f"- Files scanned: {summary['files_scanned']}",
        f"- Files with proposed changes: {summary['files_with_proposed_changes']}",
        f"- Files unchanged: {summary['files_unchanged']}",
        f"- Scopes processed: {', '.join(summary['scopes_processed'])}",
        f"- Validation passed count: {summary['validation_passed_count']}",
        f"- Validation failed count: {summary['validation_failed_count']}",
    ]

    for scope in summary["scopes_processed"]:
        scope_summary = summary["scopes"][scope]
        lines.append(
            f"- {scope}: scanned={scope_summary['files_scanned']}, "
            f"changed={scope_summary['files_changed']}, "
            f"unchanged={scope_summary['files_unchanged']}, "
            f"new={scope_summary['new_files']}, "
            f"updated={scope_summary['updated_files']}, "
            f"validation_passed={scope_summary['validation_passed']}, "
            f"validation_failed={scope_summary['validation_failed']}"
        )

    return "\n".join(lines)


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
    mode = "apply" if args.apply else "dry-run"

    changes: list[PlannedChange] = []
    scope_summaries: list[ScopeSummary] = []

    try:
        for scope in scopes:
            scoped_changes, scoped_summary = plan_scope_with_summary(scope, generated_at_utc)
            changes.extend(scoped_changes)
            scope_summaries.append(scoped_summary)
    except ValidationError as error:
        print("Validation failed during runtime sync planning.")
        print(str(error))
        raise SystemExit(1)

    summary = build_summary(changes, mode=mode, scope_summaries=scope_summaries)
    print(render_summary(summary))
    print("")

    if not changes:
        print("No runtime changes proposed.")
        return

    print("Proposed runtime sync changes:")
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