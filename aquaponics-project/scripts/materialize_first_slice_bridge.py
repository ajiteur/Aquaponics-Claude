#!/usr/bin/env python3
"""Materialize the first-slice bridge field into the basil baseline scenario.

This helper is intentionally narrow:
- reads only configs/first_slice_bridge_baselines.yaml
- looks up only starter_tilapia_basil_system
- writes only crop_system_type into
  data/simulation/scenarios/starter_tilapia_basil_system.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = PROJECT_ROOT / "configs" / "first_slice_bridge_baselines.yaml"
SCENARIO_KEY = "starter_tilapia_basil_system"
SCENARIO_PATH = (
    PROJECT_ROOT / "data" / "simulation" / "scenarios" / "starter_tilapia_basil_system.json"
)
BRIDGE_FIELD = "crop_system_type"
EXPECTED_VALUE = "architecture_dwc_raft"


def load_bridge_value(config_path: Path) -> str:
    if not config_path.exists():
        raise FileNotFoundError(f"Bridge config not found: {config_path}")

    current_key: str | None = None
    found_key = False
    bridge_value: str | None = None

    for raw_line in config_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if not line.startswith((" ", "\t")) and stripped.endswith(":"):
            current_key = stripped[:-1].strip()
            continue

        if current_key != SCENARIO_KEY:
            continue

        found_key = True
        if ":" not in stripped:
            continue

        field_name, raw_value = stripped.split(":", 1)
        field_name = field_name.strip()
        value = raw_value.strip()

        if field_name == BRIDGE_FIELD:
            bridge_value = value
            break

    if not found_key:
        raise KeyError(f"Missing config key: {SCENARIO_KEY}")

    if bridge_value is None:
        raise KeyError(f"Missing field '{BRIDGE_FIELD}' under config key: {SCENARIO_KEY}")

    return bridge_value


def load_scenario(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Scenario file not found: {path}")

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in scenario file: {path}") from exc

    if not isinstance(data, dict):
        raise ValueError(f"Scenario file must contain a JSON object: {path}")

    return data


def with_bridge_field_after_scenario_id(scenario: dict, bridge_value: str) -> dict:
    reordered: dict = {}
    inserted = False

    for key, value in scenario.items():
        if key == BRIDGE_FIELD:
            continue

        reordered[key] = value
        if key == "scenario_id":
            reordered[BRIDGE_FIELD] = bridge_value
            inserted = True

    if not inserted:
        reordered[BRIDGE_FIELD] = bridge_value

    return reordered


def main() -> int:
    try:
        bridge_value = load_bridge_value(CONFIG_PATH)
        scenario = load_scenario(SCENARIO_PATH)
    except (FileNotFoundError, KeyError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    scenario_id = scenario.get("scenario_id")
    if scenario_id != SCENARIO_KEY:
        print(
            f"error: scenario id mismatch in {SCENARIO_PATH}: expected '{SCENARIO_KEY}', found '{scenario_id}'",
            file=sys.stderr,
        )
        return 2

    if bridge_value != EXPECTED_VALUE:
        print(
            f"error: unexpected bridge value for {SCENARIO_KEY}: expected '{EXPECTED_VALUE}', found '{bridge_value}'",
            file=sys.stderr,
        )
        return 2

    current_value = scenario.get(BRIDGE_FIELD)
    if current_value == bridge_value:
        print(f"No change needed: {SCENARIO_PATH} already has {BRIDGE_FIELD}={bridge_value}")
        return 0

    updated = with_bridge_field_after_scenario_id(scenario, bridge_value)
    SCENARIO_PATH.write_text(json.dumps(updated, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {SCENARIO_PATH}: set {BRIDGE_FIELD}={bridge_value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
