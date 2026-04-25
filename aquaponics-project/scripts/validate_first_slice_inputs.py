#!/usr/bin/env python3
"""Validate first-slice tracked config and example JSON/YAML files.

This helper is intentionally narrow:
- reads the current first-slice tracked bridge config
- validates the current example override JSON files
- validates the current example working-input JSON file
- checks only syntax, required keys, and a few first-slice-safe value shapes
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parent.parent

BRIDGE_CONFIG_PATH = PROJECT_ROOT / "configs" / "first_slice_bridge_baselines.yaml"
EXAMPLE_OVERRIDES_PATH = PROJECT_ROOT / "scripts" / "example_first_slice_overrides.json"
REVIEWED_MANUAL_OVERRIDES_PATH = (
    PROJECT_ROOT / "scripts" / "example_first_slice_reviewed_manual_overrides.json"
)
WORKING_INPUTS_PATH = PROJECT_ROOT / "scripts" / "example_first_slice_working_inputs.json"

SCENARIO_KEY = "starter_tilapia_basil_system"
BRIDGE_FIELD = "crop_system_type"
EXPECTED_BRIDGE_VALUE = "architecture_dwc_raft"

OVERRIDE_REQUIRED_KEYS = (
    "product_id",
    "channel_id",
    "scenario_name",
    "time_basis",
    "saleable_harvest_mass_kg",
)

WORKING_INPUT_CASES = ("conservative", "base", "optimistic")
WORKING_INPUT_CASE_REQUIRED_KEYS = (
    "price_per_saleable_kg",
    "variable_cost_per_saleable_kg",
    "saleability_rate",
    "fixed_batch_cost",
    "saleable_harvest_mass_kg",
    "provenance",
)
PROVENANCE_REQUIRED_KEYS = (
    "currency_code",
    "market_level",
    "price_date_basis",
    "price_tax_treatment",
    "assumption_status",
)


class ValidationError(Exception):
    """Raised when a required first-slice input is invalid."""


def load_json_object(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ValidationError(f"missing file: {path.as_posix()}")

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValidationError(f"failed to read {path.as_posix()}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError(f"invalid JSON in {path.as_posix()}: {exc}") from exc

    if not isinstance(data, dict):
        raise ValidationError(f"top-level JSON object required: {path.as_posix()}")

    return data


def parse_first_slice_yaml(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        raise ValidationError(f"missing file: {path.as_posix()}")

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise ValidationError(f"failed to read {path.as_posix()}: {exc}") from exc

    data: dict[str, dict[str, str]] = {}
    current_top_key: str | None = None

    for lineno, raw_line in enumerate(lines, start=1):
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if raw_line.startswith("\t"):
            raise ValidationError(f"tabs are not allowed in {path.as_posix()}:{lineno}")

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        if indent == 0:
            if not stripped.endswith(":"):
                raise ValidationError(
                    f"invalid top-level YAML mapping in {path.as_posix()}:{lineno}"
                )
            current_top_key = stripped[:-1].strip()
            if not current_top_key:
                raise ValidationError(f"empty top-level key in {path.as_posix()}:{lineno}")
            data[current_top_key] = {}
            continue

        if indent != 2:
            raise ValidationError(
                f"unsupported indentation in {path.as_posix()}:{lineno}; expected 2 spaces"
            )

        if current_top_key is None:
            raise ValidationError(
                f"nested YAML entry without top-level key in {path.as_posix()}:{lineno}"
            )

        if ":" not in stripped:
            raise ValidationError(f"invalid YAML key/value in {path.as_posix()}:{lineno}")

        key, raw_value = stripped.split(":", 1)
        key = key.strip()
        value = raw_value.strip()

        if not key:
            raise ValidationError(f"empty nested key in {path.as_posix()}:{lineno}")

        if (
            len(value) >= 2
            and value[0] == value[-1]
            and value[0] in {"'", '"'}
        ):
            value = value[1:-1]

        data[current_top_key][key] = value

    if not data:
        raise ValidationError(f"empty YAML mapping: {path.as_posix()}")

    return data


def require_keys(mapping: dict[str, Any], keys: tuple[str, ...], path_label: str) -> None:
    for key in keys:
        if key not in mapping:
            raise ValidationError(f"missing required key '{key}' in {path_label}")


def validate_optional_mass(value: Any, path_label: str) -> None:
    if value is None:
        return
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValidationError(f"{path_label} must be null or numeric")
    if value < 0:
        raise ValidationError(f"{path_label} must be non-negative")


def validate_bridge_config() -> str:
    data = parse_first_slice_yaml(BRIDGE_CONFIG_PATH)
    if SCENARIO_KEY not in data:
        raise ValidationError(
            f"missing top-level key '{SCENARIO_KEY}' in {BRIDGE_CONFIG_PATH.as_posix()}"
        )

    scenario_config = data[SCENARIO_KEY]
    if not isinstance(scenario_config, dict):
        raise ValidationError(
            f"'{SCENARIO_KEY}' must map to a nested object in {BRIDGE_CONFIG_PATH.as_posix()}"
        )

    require_keys(scenario_config, (BRIDGE_FIELD,), BRIDGE_CONFIG_PATH.as_posix())

    bridge_value = scenario_config[BRIDGE_FIELD]
    if bridge_value != EXPECTED_BRIDGE_VALUE:
        raise ValidationError(
            f"{BRIDGE_CONFIG_PATH.as_posix()} {SCENARIO_KEY}.{BRIDGE_FIELD} must be "
            f"'{EXPECTED_BRIDGE_VALUE}', found '{bridge_value}'"
        )

    return f"OK {BRIDGE_CONFIG_PATH.as_posix()}: {SCENARIO_KEY}.{BRIDGE_FIELD}={bridge_value}"


def validate_overrides_file(path: Path) -> str:
    data = load_json_object(path)
    require_keys(data, OVERRIDE_REQUIRED_KEYS, path.as_posix())

    if data["product_id"] != "basil":
        raise ValidationError(f"{path.as_posix()} product_id must be 'basil'")
    if data["channel_id"] != "channel_wholesale":
        raise ValidationError(f"{path.as_posix()} channel_id must be 'channel_wholesale'")
    if data["time_basis"] != "scenario_rollup":
        raise ValidationError(f"{path.as_posix()} time_basis must be 'scenario_rollup'")
    if not isinstance(data["scenario_name"], str) or not data["scenario_name"].strip():
        raise ValidationError(f"{path.as_posix()} scenario_name must be a non-empty string")

    validate_optional_mass(
        data["saleable_harvest_mass_kg"],
        f"{path.as_posix()} saleable_harvest_mass_kg",
    )

    return f"OK {path.as_posix()}"


def validate_working_inputs() -> str:
    data = load_json_object(WORKING_INPUTS_PATH)
    require_keys(data, ("metadata", "cases"), WORKING_INPUTS_PATH.as_posix())

    metadata = data["metadata"]
    cases = data["cases"]
    if not isinstance(metadata, dict):
        raise ValidationError(f"{WORKING_INPUTS_PATH.as_posix()} metadata must be an object")
    if not isinstance(cases, dict):
        raise ValidationError(f"{WORKING_INPUTS_PATH.as_posix()} cases must be an object")

    require_keys(
        metadata,
        ("slice_id", "benchmark_geography", "benchmark_status"),
        f"{WORKING_INPUTS_PATH.as_posix()} metadata",
    )

    if metadata["slice_id"] != "basil_bulk_kg_wholesale":
        raise ValidationError(
            f"{WORKING_INPUTS_PATH.as_posix()} metadata.slice_id must be "
            f"'basil_bulk_kg_wholesale'"
        )

    for case_name in WORKING_INPUT_CASES:
        if case_name not in cases:
            raise ValidationError(
                f"missing case '{case_name}' in {WORKING_INPUTS_PATH.as_posix()}"
            )

        case_data = cases[case_name]
        if not isinstance(case_data, dict):
            raise ValidationError(
                f"{WORKING_INPUTS_PATH.as_posix()} cases.{case_name} must be an object"
            )

        require_keys(
            case_data,
            WORKING_INPUT_CASE_REQUIRED_KEYS,
            f"{WORKING_INPUTS_PATH.as_posix()} cases.{case_name}",
        )

        provenance = case_data["provenance"]
        if not isinstance(provenance, dict):
            raise ValidationError(
                f"{WORKING_INPUTS_PATH.as_posix()} cases.{case_name}.provenance must be an object"
            )

        require_keys(
            provenance,
            PROVENANCE_REQUIRED_KEYS,
            f"{WORKING_INPUTS_PATH.as_posix()} cases.{case_name}.provenance",
        )

        for numeric_key in (
            "price_per_saleable_kg",
            "variable_cost_per_saleable_kg",
            "saleability_rate",
            "fixed_batch_cost",
        ):
            value = case_data[numeric_key]
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise ValidationError(
                    f"{WORKING_INPUTS_PATH.as_posix()} cases.{case_name}.{numeric_key} must be numeric"
                )

        saleability = case_data["saleability_rate"]
        if saleability < 0 or saleability > 1:
            raise ValidationError(
                f"{WORKING_INPUTS_PATH.as_posix()} cases.{case_name}.saleability_rate must be between 0 and 1"
            )

        validate_optional_mass(
            case_data["saleable_harvest_mass_kg"],
            f"{WORKING_INPUTS_PATH.as_posix()} cases.{case_name}.saleable_harvest_mass_kg",
        )

    return f"OK {WORKING_INPUTS_PATH.as_posix()}: metadata and {len(WORKING_INPUT_CASES)} cases"


def main() -> int:
    try:
        messages = [
            validate_bridge_config(),
            validate_overrides_file(EXAMPLE_OVERRIDES_PATH),
            validate_overrides_file(REVIEWED_MANUAL_OVERRIDES_PATH),
            validate_working_inputs(),
        ]
    except ValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    for message in messages:
        print(message)

    print(f"Validation passed: {len(messages)} file(s) checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
