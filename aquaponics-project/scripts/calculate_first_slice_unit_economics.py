#!/usr/bin/env python3
"""Read-only calculator for first-slice basil wholesale unit economics."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCRIPT_NAME = "scripts/calculate_first_slice_unit_economics.py"
CASE_NAMES = ("conservative", "base", "optimistic")
HARVESTED_COMPONENT_FIELDS = (
    "direct_labor_cost_per_harvested_kg",
    "electricity_cost_per_harvested_kg",
    "packaging_handling_cost_per_harvested_kg",
    "other_variable_cost_per_harvested_kg",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calculate narrow first-slice unit economics from a working input JSON."
    )
    parser.add_argument("input_path", help="Path to the working input JSON file.")
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print the emitted JSON result.",
    )
    return parser.parse_args()


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"failed to read {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc


def normalize_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(Path.cwd().resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def as_number(value: Any) -> float | None:
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    return None


def valid_saleability(value: float | None) -> bool:
    return value is not None and 0.0 < value <= 1.0


def derive_variable_cost(case_data: dict[str, Any], saleability_rate: float | None) -> tuple[float | None, str, list[str], list[str]]:
    """Return derived variable cost per saleable kg, path used, notes, and missing inputs."""

    notes: list[str] = []
    missing_inputs: list[str] = []

    direct_saleable = as_number(case_data.get("variable_cost_per_saleable_kg"))
    if direct_saleable is not None:
        return direct_saleable, "direct_variable_cost_per_saleable_kg", notes, missing_inputs

    direct_harvested = as_number(case_data.get("variable_cost_per_harvested_kg"))
    if direct_harvested is not None:
        if valid_saleability(saleability_rate):
            return direct_harvested / saleability_rate, "variable_cost_per_harvested_kg", notes, missing_inputs
        missing_inputs.append("saleability_rate")
        notes.append("variable_cost_per_harvested_kg was provided, but saleability_rate is missing or invalid.")
        return None, "variable_cost_per_harvested_kg", notes, missing_inputs

    component_values: dict[str, float | None] = {
        field: as_number(case_data.get(field)) for field in HARVESTED_COMPONENT_FIELDS
    }
    present_components = [field for field, value in component_values.items() if value is not None]
    if present_components:
        missing_components = [field for field, value in component_values.items() if value is None]
        if missing_components:
            missing_inputs.extend(missing_components)
            notes.append("Not all harvested-kg variable-cost components were supplied.")
            return None, "harvested_component_sum", notes, missing_inputs
        if valid_saleability(saleability_rate):
            harvested_total = sum(component_values[field] or 0.0 for field in HARVESTED_COMPONENT_FIELDS)
            return harvested_total / saleability_rate, "harvested_component_sum", notes, missing_inputs
        missing_inputs.append("saleability_rate")
        notes.append("Harvested-kg variable-cost components were supplied, but saleability_rate is missing or invalid.")
        return None, "harvested_component_sum", notes, missing_inputs

    missing_inputs.append("variable_cost_per_saleable_kg_or_equivalent")
    notes.append("No direct saleable-kg variable cost, harvested-kg variable cost, or full harvested-kg component set was supplied.")
    return None, "unavailable", notes, missing_inputs


def calculate_case(case_name: str, case_data: dict[str, Any]) -> tuple[dict[str, Any], list[str], list[str]]:
    price = as_number(case_data.get("price_per_saleable_kg"))
    saleability_rate = as_number(case_data.get("saleability_rate"))
    fixed_batch_cost = as_number(case_data.get("fixed_batch_cost"))
    saleable_harvest_mass_kg = as_number(case_data.get("saleable_harvest_mass_kg"))

    notes: list[str] = []
    missing_inputs: list[str] = []
    provisional_inputs = case_data.get("provisional_inputs", [])
    if not isinstance(provisional_inputs, list):
        provisional_inputs = []

    variable_cost_per_saleable_kg, variable_cost_path, variable_cost_notes, variable_cost_missing = derive_variable_cost(
        case_data, saleability_rate
    )
    notes.extend(variable_cost_notes)
    missing_inputs.extend(variable_cost_missing)

    contribution_margin_per_saleable_kg: float | None = None
    if price is None:
        missing_inputs.append("price_per_saleable_kg")
        notes.append("price_per_saleable_kg is required to calculate contribution margin.")
    elif variable_cost_per_saleable_kg is not None:
        contribution_margin_per_saleable_kg = price - variable_cost_per_saleable_kg

    break_even_saleable_kg: float | None = None
    if fixed_batch_cost is None:
        missing_inputs.append("fixed_batch_cost")
        notes.append("break_even_saleable_kg is null because fixed_batch_cost was not supplied.")
    elif contribution_margin_per_saleable_kg is None:
        notes.append("break_even_saleable_kg is null because contribution margin could not be calculated.")
    elif contribution_margin_per_saleable_kg <= 0:
        notes.append("break_even_saleable_kg is null because contribution margin per saleable kg is zero or negative.")
    else:
        break_even_saleable_kg = fixed_batch_cost / contribution_margin_per_saleable_kg

    required_harvested_kg: float | None = None
    if valid_saleability(saleability_rate):
        # Normalized to one saleable kilogram for unit-economics review.
        required_harvested_kg = 1.0 / saleability_rate
    else:
        missing_inputs.append("saleability_rate")
        notes.append("required_harvested_kg is null because saleability_rate is missing or outside (0, 1].")

    if saleable_harvest_mass_kg is None:
        notes.append("saleable_harvest_mass_kg is null; no realized-output comparison is attempted.")

    result = {
        "price_per_saleable_kg": price,
        "variable_cost_per_saleable_kg": variable_cost_per_saleable_kg,
        "variable_cost_path": variable_cost_path,
        "saleability_rate": saleability_rate,
        "fixed_batch_cost": fixed_batch_cost,
        "saleable_harvest_mass_kg": saleable_harvest_mass_kg,
        "contribution_margin_per_saleable_kg": contribution_margin_per_saleable_kg,
        "break_even_saleable_kg": break_even_saleable_kg,
        "required_harvested_kg": required_harvested_kg,
        "provenance": case_data.get("provenance", {}),
        "provisional_inputs": provisional_inputs,
        "notes": notes,
    }
    return result, provisional_inputs, sorted(set(missing_inputs))


def build_output(input_path: Path, payload: dict[str, Any]) -> dict[str, Any]:
    metadata = payload.get("metadata", {}) if isinstance(payload.get("metadata"), dict) else {}
    cases = payload.get("cases", {}) if isinstance(payload.get("cases"), dict) else {}

    result_cases: dict[str, Any] = {}
    provisional_inputs: dict[str, list[str]] = {}
    missing_inputs: dict[str, list[str]] = {}

    for case_name in CASE_NAMES:
        case_data = cases.get(case_name)
        if not isinstance(case_data, dict):
            result_cases[case_name] = {
                "contribution_margin_per_saleable_kg": None,
                "break_even_saleable_kg": None,
                "required_harvested_kg": None,
                "notes": ["Case data is missing."],
            }
            provisional_inputs[case_name] = []
            missing_inputs[case_name] = ["case_definition"]
            continue

        case_result, case_provisional, case_missing = calculate_case(case_name, case_data)
        result_cases[case_name] = case_result
        provisional_inputs[case_name] = case_provisional
        missing_inputs[case_name] = case_missing

    return {
        "metadata": {
            "input_path": normalize_path(input_path),
            "generated_by": SCRIPT_NAME,
            "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "provisional_inputs": provisional_inputs,
            "missing_inputs": missing_inputs,
            "calculation_limits": [
                "This working output is non-canonical and must not be promoted automatically into data/knowledge/business/**.",
                "The calculator does not derive saleable_harvest_mass_kg from standing biomass, growth rate, or runtime proxies.",
                "Contribution margin requires either variable_cost_per_saleable_kg, variable_cost_per_harvested_kg, or a full explicit set of harvested-kg cost components.",
                "Break-even saleable kg is emitted only when fixed_batch_cost is supplied and contribution margin per saleable kg is positive.",
                "required_harvested_kg is normalized to harvested kilograms needed for one saleable kilogram.",
            ],
        },
        "slice_id": metadata.get("slice_id", "basil_bulk_kg_wholesale"),
        "benchmark_geography": metadata.get("benchmark_geography", "netherlands"),
        "benchmark_status": metadata.get(
            "benchmark_status", "first_working_research_benchmark_only"
        ),
        "cases": result_cases,
    }


def main() -> int:
    args = parse_args()
    input_path = Path(args.input_path)
    if not input_path.exists() or not input_path.is_file():
        print(f"error: input path does not exist or is not a file: {input_path}", file=sys.stderr)
        return 2

    try:
        payload = load_json(input_path)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if not isinstance(payload, dict):
        print("error: input JSON must be an object", file=sys.stderr)
        return 2

    output = build_output(input_path, payload)
    if args.pretty:
        json.dump(output, sys.stdout, indent=2)
    else:
        json.dump(output, sys.stdout, separators=(",", ":"))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
