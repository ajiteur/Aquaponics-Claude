#!/usr/bin/env python3
"""Print a deterministic Mode A feed-load report from explicit JSON inputs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.mvp_mode_a_feed_load_report import (  # noqa: E402
    ModeAFeedLoadReportValidationError,
    build_mode_a_feed_load_report,
)


REQUIRED_INPUT_FIELDS = (
    "scenario_id",
    "input_mode",
    "feed_kg_day",
    "protein_fraction",
)

OPTIONAL_CONTEXT_FIELDS = (
    "feed_class",
    "protein_basis",
    "feeding_frequency_per_day",
    "fcr_band",
    "architecture_context",
    "water_volume_context_available",
    "time_basis_context_available",
    "exchange_or_retention_context_available",
    "ph_context_available",
    "temperature_context_available",
    "feed_price_context_available",
    "tank_volume_context_available",
    "stocking_density_context_available",
    "biofilter_capacity_context_available",
)

SUPPORTED_INPUT_FIELDS = REQUIRED_INPUT_FIELDS + OPTIONAL_CONTEXT_FIELDS


class DemoInputError(ValueError):
    """Raised when demo input JSON cannot be used to build a report."""


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print a Mode A MVP feed-load report JSON to stdout."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to a JSON object containing explicit Mode A feed-load inputs.",
    )
    return parser.parse_args(argv)


def load_input_payload(input_path: Path) -> dict[str, Any]:
    if not input_path.exists() or not input_path.is_file():
        raise DemoInputError(f"input path does not exist or is not a file: {input_path}")

    try:
        payload = json.loads(input_path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise DemoInputError(f"failed to read input JSON: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise DemoInputError(f"invalid input JSON: {exc}") from exc

    if not isinstance(payload, dict):
        raise DemoInputError("input JSON must be an object")

    missing_fields = [
        field for field in REQUIRED_INPUT_FIELDS if field not in payload
    ]
    if missing_fields:
        raise DemoInputError(
            "missing required input field(s): " + ", ".join(missing_fields)
        )

    unsupported_fields = [
        field for field in payload if field not in SUPPORTED_INPUT_FIELDS
    ]
    if unsupported_fields:
        raise DemoInputError(
            "unsupported input field(s): " + ", ".join(sorted(unsupported_fields))
        )

    return payload


def build_report_from_input_payload(payload: dict[str, Any]) -> dict[str, Any]:
    kwargs = {
        field: payload[field]
        for field in SUPPORTED_INPUT_FIELDS
        if field in payload
    }
    try:
        return build_mode_a_feed_load_report(**kwargs)
    except ModeAFeedLoadReportValidationError as exc:
        raise DemoInputError(str(exc)) from exc


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    input_path = Path(args.input)

    try:
        payload = load_input_payload(input_path)
        report = build_report_from_input_payload(payload)
    except DemoInputError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    json.dump(_normalize_float_noise(report), sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


def _normalize_float_noise(value: Any) -> Any:
    if isinstance(value, float):
        return round(value, 10)
    if isinstance(value, dict):
        return {key: _normalize_float_noise(child) for key, child in value.items()}
    if isinstance(value, list):
        return [_normalize_float_noise(child) for child in value]
    return value


if __name__ == "__main__":
    raise SystemExit(main())
