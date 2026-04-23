#!/usr/bin/env python3
"""Build a read-only first-slice adapter payload from one runtime scenario snapshot."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCRIPT_NAME = "scripts/build_first_slice_adapter_payload.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Emit a reviewable first-slice business payload from one runtime scenario snapshot."
    )
    parser.add_argument(
        "input_path",
        help="Path to one runtime scenario snapshot JSON file.",
    )
    parser.add_argument(
        "--overrides",
        help="Optional JSON file with explicit slice-config values and manual review overrides.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print the emitted JSON payload.",
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


def build_run_id(input_path: Path) -> str:
    return input_path.stem


def build_payload(input_path: Path, source: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    scenario_id = source.get("scenario_id")
    crop_system_type = source.get("crop_system_type")
    crop_system_type_status = (
        "direct rename/flattening" if crop_system_type is not None else "missing"
    )
    plant_crop = source.get("plant_crop") if isinstance(source.get("plant_crop"), dict) else {}
    water_state = source.get("water_state") if isinstance(source.get("water_state"), dict) else {}
    derived = source.get("derived") if isinstance(source.get("derived"), dict) else {}
    time_block = source.get("time") if isinstance(source.get("time"), dict) else {}

    payload = {
        "metadata": {
            "input_path": normalize_path(input_path),
            "generated_by": SCRIPT_NAME,
            "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "missing_or_deferred_fields": [],
            "proxy_only_do_not_promote": {
                "water_use_l": "operations_policy.water_top_up_l_per_day",
            },
            "field_statuses": {
                "run_id": "inconsistent",
                "scenario_name": "slice-config required",
                "time_basis": "slice-config required",
                "product_id": "slice-config required",
                "channel_id": "slice-config required",
                "saleable_harvest_mass_kg": "missing",
                "cull_or_unsaleable_mass_kg": "deferred",
                "harvest_event_count": "deferred",
                "first_harvest_utc": "deferred",
                "last_harvest_utc": "deferred",
                "water_use_l": "deferred",
                "supplement_input_records": "deferred",
                "adjustment_event_count": "deferred",
                "quality_risk_event_records": "deferred",
                "out_of_range_event_records": "deferred",
                "downtime_event_count": "deferred",
                "disease_or_pathogen_event_records": "deferred",
                "planting_count": "proxy_only_do_not_promote",
                "crop_system_type": crop_system_type_status,
                "growing_area_m2": "missing",
                "period_start_utc": "deferred",
                "period_end_utc": "deferred",
            },
        },
        "scenario_id": scenario_id,
        "run_id": build_run_id(input_path),
        "scenario_name": overrides.get("scenario_name"),
        "time_basis": overrides.get("time_basis", "scenario_rollup"),
        "period_start_utc": None,
        "period_end_utc": None,
        "crop_id": plant_crop.get("species_id"),
        "crop_system_type": crop_system_type,
        "growing_area_m2": None,
        "planting_count": None,
        "live_plant_count_end": plant_crop.get("plant_count"),
        "product_id": overrides.get("product_id", "basil"),
        "channel_id": overrides.get("channel_id", "channel_wholesale"),
        "saleable_harvest_mass_kg": overrides.get("saleable_harvest_mass_kg"),
        "cull_or_unsaleable_mass_kg": None,
        "harvest_event_count": None,
        "first_harvest_utc": None,
        "last_harvest_utc": None,
        "energy_kwh": derived.get("daily_energy_kwh"),
        "water_use_l": None,
        "supplement_input_records": None,
        "observed_pH": water_state.get("pH"),
        "observed_tan_mg_l": water_state.get("tan_mg_L"),
        "observed_unionized_nh3_mg_l": water_state.get("unionized_nh3_mg_L"),
        "observed_nitrate_mg_l": water_state.get("nitrate_mg_L"),
        "operating_day_count": time_block.get("day"),
        "adjustment_event_count": None,
        "quality_risk_event_records": None,
        "out_of_range_event_records": None,
        "downtime_event_count": None,
        "disease_or_pathogen_event_records": None,
    }

    missing_or_deferred_fields = [
        key
        for key, value in payload.items()
        if key != "metadata"
        and value is None
        and key
        in {
            "scenario_name",
            "time_basis",
            "product_id",
            "channel_id",
            "saleable_harvest_mass_kg",
            "period_start_utc",
            "period_end_utc",
            "crop_system_type",
            "growing_area_m2",
            "planting_count",
            "cull_or_unsaleable_mass_kg",
            "harvest_event_count",
            "first_harvest_utc",
            "last_harvest_utc",
            "water_use_l",
            "supplement_input_records",
            "adjustment_event_count",
            "quality_risk_event_records",
            "out_of_range_event_records",
            "downtime_event_count",
            "disease_or_pathogen_event_records",
        }
    ]
    payload["metadata"]["missing_or_deferred_fields"] = missing_or_deferred_fields
    return payload


def main() -> int:
    args = parse_args()
    input_path = Path(args.input_path)
    if not input_path.exists() or not input_path.is_file():
        print(f"error: input path does not exist or is not a file: {input_path}", file=sys.stderr)
        return 2

    try:
        source = load_json(input_path)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if not isinstance(source, dict):
        print("error: input JSON must be an object-shaped runtime scenario snapshot", file=sys.stderr)
        return 2

    overrides: dict[str, Any] = {}
    if args.overrides:
        overrides_path = Path(args.overrides)
        if not overrides_path.exists() or not overrides_path.is_file():
            print(f"error: overrides path does not exist or is not a file: {overrides_path}", file=sys.stderr)
            return 2
        try:
            loaded_overrides = load_json(overrides_path)
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
        if not isinstance(loaded_overrides, dict):
            print("error: overrides JSON must be an object", file=sys.stderr)
            return 2
        overrides = loaded_overrides

    payload = build_payload(input_path, source, overrides)
    if args.pretty:
        json.dump(payload, sys.stdout, indent=2)
    else:
        json.dump(payload, sys.stdout, separators=(",", ":"))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
