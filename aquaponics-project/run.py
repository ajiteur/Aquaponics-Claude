#!/usr/bin/env python3
"""Run a named local scenario: a crop-cycle simulation and/or the unit-economics comparison.

A "run" is a small JSON file in runs/ that says which simulation scenario to run,
for how many days, which unit configurations and locations to compare, and any
values you want to change (price, labour h/kg, wage, electricity, feed rate ...).

Usage (from the aquaponics-project folder):
    python run.py                 list the runs in runs/
    python run.py <name>          run runs/<name>.json
    python run.py path/to/x.json  run any run file

Output goes to data/simulation/results/local_runs/<name>/ :
    summary.txt, simulation_daily.csv, unit_economics.csv, plus the raw JSON.
Those files are ignored by git, so local runs never clutter the repo.

All results are scenario estimates, not validated. Unit economics covers labour +
electricity only; it is not total operating cost, profit or viability.
Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import copy
import csv
import importlib.util
import json
import sys
import tempfile
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent
RUNS_DIR = PROJECT_ROOT / "runs"
OUT_ROOT = PROJECT_ROOT / "data" / "simulation" / "results" / "local_runs"
COMPARE_SCRIPT = PROJECT_ROOT / "scripts" / "compare_unit_configurations.py"
CROP_CYCLE_SCRIPT = PROJECT_ROOT / "src" / "simulate_crop_cycle.py"
LABEL = "Scenario estimate, not validated."


class RunError(Exception):
    """A problem in a run file that the user can fix."""


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def project_path(p: str) -> Path:
    path = Path(p)
    return path if path.is_absolute() else PROJECT_ROOT / path


def rel(path: Path) -> str:
    """Path relative to the project folder when possible, for readable output."""
    try:
        return path.resolve().relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return str(path)


def find_run_file(name: str) -> Path:
    candidates = [Path(name), RUNS_DIR / name, RUNS_DIR / f"{name}.json"]
    for c in candidates:
        if c.is_file():
            return c.resolve()
    raise RunError(f"No run called '{name}'. Run 'python run.py' to list them.")


def list_runs() -> int:
    files = sorted(RUNS_DIR.glob("*.json"))
    if not files:
        print("No run files in runs/.")
        return 0
    print("Runs you can start with: python run.py <name>\n")
    for f in files:
        try:
            label = json.loads(f.read_text(encoding="utf-8")).get("label", "")
        except json.JSONDecodeError as exc:
            label = f"(cannot read: {exc})"
        print(f"  {f.stem:<28} {label}")
    return 0


# --- overrides -------------------------------------------------------------

def _step(node: Any, key: str, path: str) -> Any:
    """One step down a dotted path. In a list, match the item whose id is `key`."""
    if isinstance(node, dict):
        if key not in node:
            raise RunError(f"Override '{path}': '{key}' not found. Known keys: {', '.join(map(str, node))}")
        return node[key]
    if isinstance(node, list):
        for item in node:
            if isinstance(item, dict) and key in (item.get("config_id"), item.get("id")):
                return item
        ids = [str(i.get("config_id") or i.get("id")) for i in node if isinstance(i, dict)]
        raise RunError(f"Override '{path}': no item '{key}'. Known ids: {', '.join(ids)}")
    raise RunError(f"Override '{path}': cannot go into '{key}' (it is a plain value).")


def apply_overrides(data: Any, overrides: dict[str, Any]) -> list[str]:
    """Set each dotted path in `overrides` on `data`. Returns notes for the summary."""
    notes = []
    for path, value in (overrides or {}).items():
        if path.startswith("_"):
            continue  # comments
        parts = path.split(".")
        node = data
        for key in parts[:-1]:
            node = _step(node, key, path)
        last = parts[-1]
        if isinstance(node, dict):
            if last not in node:
                notes.append(f"new key added: {path}")
            node[last] = value
        elif isinstance(node, list):
            raise RunError(f"Override '{path}': ends on a list item; name a field inside it.")
        else:
            raise RunError(f"Override '{path}': parent is a plain value.")
        notes.append(f"{path} = {json.dumps(value)}")
    return notes


# --- simulation ------------------------------------------------------------

def run_simulation(spec: dict, out_dir: Path) -> tuple[dict, list[str]]:
    scenario_path = project_path(spec["scenario"])
    if not scenario_path.is_file():
        raise RunError(f"Simulation scenario not found: {spec['scenario']}")
    days = int(spec.get("days", 28))
    scenario = json.loads(scenario_path.read_text(encoding="utf-8"))
    notes = apply_overrides(scenario, spec.get("overrides", {}))

    crop_cycle = load_module(CROP_CYCLE_SCRIPT, "simulate_crop_cycle")
    with tempfile.TemporaryDirectory() as tmp:
        working = Path(tmp) / scenario_path.name
        working.write_text(json.dumps(scenario, indent=2), encoding="utf-8")
        result = crop_cycle.run_cycle(working, days)
    result["scenario_source"] = rel(scenario_path)
    result["overrides_applied"] = notes

    (out_dir / "simulation_result.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    daily = result["daily"]
    if daily:
        with open(out_dir / "simulation_daily.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(daily[0]))
            writer.writeheader()
            writer.writerows(daily)

    s, last = result["summary"], (daily[-1] if daily else {})
    lines = [
        f"SIMULATION  {result['scenario_id']}  ({days} days)  [{LABEL}]",
        f"  scenario file:            {result['scenario_source']}",
        f"  harvest events:           {s['harvest_event_count']}",
        f"  harvested mass (kg):      {s['total_harvested_mass_kg']}  (cut mass, not saleable mass)",
        f"  mean plant growth score:  {s['mean_plant_growth_score']}   (min {s['min_plant_growth_score']})",
        f"  final water:  TAN {last.get('tan_mg_L')} mg/L | NH3 {last.get('unionized_nh3_mg_L')} mg/L"
        f" | nitrate {last.get('nitrate_mg_L')} mg/L | pH {last.get('pH')}",
        "  (water values are model context, not a fish-safety check)",
    ]
    if notes:
        lines.append("  changes from the base scenario: " + "; ".join(notes))
    return result, lines


# --- unit economics --------------------------------------------------------

def run_unit_economics(spec: dict, area_m2: float | None, out_dir: Path) -> tuple[dict | None, list[str]]:
    if not COMPARE_SCRIPT.is_file():
        return None, [
            "UNIT ECONOMICS  skipped: scripts/compare_unit_configurations.py is not in this copy yet.",
            "  It arrives with the unit-economics pull request (#10). Merge it, then 'git pull'.",
        ]
    inputs_path = project_path(spec.get("inputs", "data/scenarios/unit_configuration_candidates_v0.json"))
    if not inputs_path.is_file():
        raise RunError(f"Unit-economics inputs not found: {rel(inputs_path)}")
    data = json.loads(inputs_path.read_text(encoding="utf-8"))
    notes = apply_overrides(data, spec.get("overrides", {}))

    wanted_configs = spec.get("configs") or [c["config_id"] for c in data["configurations"]]
    known = {c["config_id"] for c in data["configurations"]}
    unknown = [c for c in wanted_configs if c not in known]
    if unknown:
        raise RunError(f"Unknown config(s): {', '.join(unknown)}. Known: {', '.join(sorted(known))}")
    wanted_locations = spec.get("locations") or list(data["locations"])
    unknown = [loc for loc in wanted_locations if loc not in data["locations"]]
    if unknown:
        raise RunError(f"Unknown location(s): {', '.join(unknown)}. Known: {', '.join(data['locations'])}")

    data["configurations"] = [c for c in data["configurations"] if c["config_id"] in wanted_configs]
    for c in data["configurations"]:
        allowed = c.get("locations")
        c["locations"] = [loc for loc in wanted_locations if allowed is None or loc in allowed]

    compare = load_module(COMPARE_SCRIPT, "compare_unit_configurations")
    with tempfile.TemporaryDirectory() as tmp:
        tmp_inputs = Path(tmp) / "inputs.json"
        tmp_inputs.write_text(json.dumps(data), encoding="utf-8")
        output = compare.build(tmp_inputs)
    output["inputs_file"] = rel(inputs_path)
    output["overrides_applied"] = notes
    output["farm_area_m2"] = area_m2
    (out_dir / "unit_economics_result.json").write_text(json.dumps(output, indent=2), encoding="utf-8")

    rows = []
    for r in output["results"]:
        for case in compare.CASES:
            c = r["cases"].get(case)
            row = {
                "estimate_status": "scenario_estimate",
                "config_id": r["config_id"],
                "location": r["location"],
                "currency": r["currency_code"],
                "case": case,
                "missing_inputs": ";".join(r["missing_inputs"]),
                "verdict": r.get("verdict", "gap"),
            }
            if c:
                row.update({
                    "revenue_per_m2_yr": c["revenue_per_m2_yr"],
                    "labour_cost_per_m2_yr": c["labour_cost_per_m2_yr"],
                    "electricity_cost_per_m2_yr": c["electricity_cost_per_m2_yr"],
                    "headroom_per_m2_yr": c["headroom_per_m2_yr"],
                    "headroom_for_farm_area_yr": round(c["headroom_per_m2_yr"] * area_m2, 0) if area_m2 else "",
                    "labour_h_per_harvested_unit": c["labour_h_per_harvested_unit"],
                    "breakeven_labour_h_per_harvested_unit": c["breakeven_labour_h_per_harvested_unit"],
                })
            rows.append(row)
            if not c:
                break
    fields = list(dict.fromkeys(k for row in rows for k in row))
    with open(out_dir / "unit_economics.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        f"UNIT ECONOMICS  [{LABEL} Labour + electricity only; not total cost, profit or viability.]",
        f"  inputs file: {output['inputs_file']}",
        "  Headroom = revenue minus labour and electricity, per m2 per year (low / mid / high case).",
        "  It still has to pay for heating, building cost, consumables and any unpaid owner time.",
        "",
    ]
    head = f"  {'config':<42} {'location':<16} {'headroom per m2/yr (low / mid / high)':<40} {'verdict'}"
    if area_m2:
        head += f"   | for {area_m2:g} m2 (mid)"
    lines += [head, "  " + "-" * (len(head) - 2)]
    for r in output["results"]:
        if r["missing_inputs"]:
            lines.append(f"  {r['config_id']:<42} {r['location']:<16} missing: {', '.join(r['missing_inputs'])}")
            continue
        c = r["cases"]
        vals = " / ".join(f"{c[k]['headroom_per_m2_yr']:,.0f}" for k in compare.CASES)
        line = f"  {r['config_id']:<42} {r['location']:<16} {r['currency_code'] + ' ' + vals:<40} {r['verdict']}"
        if area_m2:
            line += f"   | {r['currency_code']} {c['mid']['headroom_per_m2_yr'] * area_m2:,.0f}"
        lines.append(line)
    if notes:
        lines += ["", "  changes from the inputs file: " + "; ".join(notes)]
    return output, lines


# --- main ------------------------------------------------------------------

def run(run_file: Path) -> int:
    try:
        spec = json.loads(run_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RunError(f"{run_file.name} is not valid JSON (line {exc.lineno}, column {exc.colno}): {exc.msg}")
    name = run_file.stem
    out_dir = OUT_ROOT / name
    out_dir.mkdir(parents=True, exist_ok=True)
    area = spec.get("farm_area_m2")
    area = float(area) if area else None

    lines = [f"RUN  {name}: {spec.get('label', '')}", f"estimate_status: scenario_estimate ({LABEL})", ""]
    if spec.get("simulation") is not None:
        _, sim_lines = run_simulation(spec["simulation"], out_dir)
        lines += sim_lines + [""]
    if spec.get("unit_economics") is not None:
        _, ue_lines = run_unit_economics(spec["unit_economics"], area, out_dir)
        lines += ue_lines + [""]
    if spec.get("simulation") is None and spec.get("unit_economics") is None:
        raise RunError("The run file needs a 'simulation' block, a 'unit_economics' block, or both.")

    lines.append(f"Files written to {rel(out_dir)}/")
    text = "\n".join(lines)
    (out_dir / "summary.txt").write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("name", nargs="?", help="run name in runs/ (leave out to list them)")
    args = parser.parse_args(argv)
    try:
        if not args.name or args.name == "list":
            return list_runs()
        return run(find_run_file(args.name))
    except RunError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
