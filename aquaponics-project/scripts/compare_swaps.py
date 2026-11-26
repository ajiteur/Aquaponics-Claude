"""Compare swaps side by side: change one choice in a configurator build and see what moves.

A swap is a patch on the base build (scripts/configure_system.py). It can change the grow
architecture (raft, NFT, media bed), the heating source (gas boiler or heat pump), one part
(a tank, pump or structure) or any other build field. Each swap is run through the same
configurator, and the report gives the change against the base in cost per kg, cost per m2
of grow area, yield, water, area, electricity and build cost, plus the gaps the swap opens
or closes.

Scenario estimate, not validated. Missing values stay missing: a swap with no sourced yield
shows cost per kg as n/a and lists the gap, and nothing is filled in.

Usage:
    python scripts/compare_swaps.py runs/swaps_basil_nl.json [--out result.json]
"""
from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

_spec = importlib.util.spec_from_file_location("configure_system", SCRIPT_DIR / "configure_system.py")
cs = importlib.util.module_from_spec(_spec)
sys.modules.setdefault("configure_system", cs)
_spec.loader.exec_module(cs)

ConfigError = cs.ConfigError

# Metrics compared for each swap: (key, label, where it lives in a case result, decimals)
METRICS = [
    ("cost_per_kg_plant", "cost per kg plant", "case", 3),
    ("cost_per_m2_grow_yr", "cost per m2 grow area per yr", "case", 2),
    ("annual_cost_counted", "annual cost counted", "case", 0),
    ("capex_total", "build cost (total)", "case", 0),
    ("electricity_kwh_yr", "electricity kWh/yr", "case", 0),
    ("plant_kg_yr", "plant output kg/yr", "sizing", 0),
    ("fish_kg_yr", "fish output kg/yr", "sizing", 0),
    ("feed_kg_yr", "feed kg/yr", "sizing", 0),
    ("system_water_m3", "system water m3", "sizing", 1),
    ("makeup_water_m3_yr", "make-up water m3/yr", "sizing", 0),
    ("minimum_area_m2", "minimum area m2", "sizing", 1),
    ("planning_area_m2_uvi_ratio", "planning area m2", "sizing", 1),
]


def deep_merge(base: dict, patch: dict) -> dict:
    """Dicts merge key by key; any other value (list, number, string, null) replaces."""
    out = copy.deepcopy(base)
    for key, value in patch.items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = deep_merge(out[key], value)
        else:
            out[key] = copy.deepcopy(value)
    return out


def metric(case: dict, key: str, where: str) -> float | None:
    return case["sizing"].get(key) if where == "sizing" else case.get(key)


def delta(a: float | None, b: float | None) -> float | None:
    return None if a is None or b is None else b - a


def component_swaps(catalog: Any, build: dict) -> list[dict]:
    """One swap per catalog alternative of each chosen part (same category, role and region)."""
    out = []
    comps = build.get("components", {})
    for comp in cs.resolve_components(catalog, build):
        for alt in catalog.alternatives(comp, build["region"], build["grow_architecture"]):
            cat = comp["category"]
            current = comps[cat]
            new = [alt["component_id"] if x == comp["component_id"] else x for x in current] \
                if isinstance(current, list) else alt["component_id"]
            out.append({
                "swap_id": f"part_{alt['component_id']}",
                "kind": "component",
                "label": f"{cat}: {alt['name']} instead of {comp['component_id']}",
                "patch": {"components": {cat: new}},
                "trade_offs": alt.get("trade_offs", []),
                "auto": True,
            })
    return out


def compare_swaps(spec: dict, components_path: Path = cs.DEFAULT_COMPONENTS,
                  species_path: Path = cs.DEFAULT_SPECIES, locations_path: Path = cs.DEFAULT_LOCATIONS) -> dict:
    def run_build(build: dict) -> dict:
        return cs.build_result(build, components_path, species_path, locations_path, run_simulation=False)

    base_build = spec.get("base")
    if not isinstance(base_build, dict):
        raise ConfigError("The swaps block needs a 'base' build (see runs/swaps_basil_nl.json).")
    base_build = copy.deepcopy(base_build)
    base = run_build(base_build)
    catalog = cs.Catalog(cs.load_json(components_path), cs.load_json(species_path), cs.load_json(locations_path))
    swaps = list(spec.get("options", []))
    if spec.get("include_component_alternatives", True):
        explicit = {json.dumps(s.get("patch", {}), sort_keys=True) for s in swaps}
        swaps += [s for s in component_swaps(catalog, base_build)
                  if json.dumps(s["patch"], sort_keys=True) not in explicit]

    base_gaps = set(base["gaps"])
    rows = []
    for sw in swaps:
        if "swap_id" not in sw or "patch" not in sw:
            raise ConfigError("Each entry in 'options' needs 'swap_id' and 'patch'.")
        build = deep_merge(base_build, sw["patch"])
        build["build_id"] = f"{base_build.get('build_id', 'base')}__{sw['swap_id']}"
        row = {
            "swap_id": sw["swap_id"],
            "kind": sw.get("kind", "custom"),
            "label": sw.get("label", sw["swap_id"]),
            "patch": sw["patch"],
            "note": sw.get("note"),
            "trade_offs": sw.get("trade_offs", []),
        }
        try:
            res = run_build(build)
        except ConfigError as exc:
            row.update({"status": "not_run", "reason": str(exc)})
            rows.append(row)
            continue
        mid, bmid = res["cases"]["mid"], base["cases"]["mid"]
        row["status"] = "ran"
        row["mid"] = {}
        for key, _, where, nd in METRICS:
            a, b = metric(bmid, key, where), metric(mid, key, where)
            row["mid"][key] = {"base": a, "swap": b, "change": cs.r(delta(a, b), nd)}
        row["cost_per_kg_plant_range"] = {c: res["cases"][c]["cost_per_kg_plant"] for c in cs.CASES}
        row["cost_per_m2_grow_yr_range"] = {c: res["cases"][c]["cost_per_m2_grow_yr"] for c in cs.CASES}
        gaps = set(res["gaps"])
        row["new_gaps"] = sorted(gaps - base_gaps)
        row["closed_gaps"] = sorted(base_gaps - gaps)
        # A swap that opens gaps leaves some of its costs out, so its change is not like-for-like.
        # Footprint gaps only affect the area figures, not cost.
        row["like_for_like"] = not [g for g in row["new_gaps"] if "footprint not recorded" not in g]
        rows.append(row)

    return {
        "estimate_status": "scenario_estimate",
        "label": f"{cs.LABEL} {cs.SCOPE_NOTE}",
        "generated_by": "scripts/compare_swaps.py",
        "currency_code": base["currency_code"],
        "base_build_id": base_build.get("build_id"),
        "base": {
            "cost_per_kg_plant_range": {c: base["cases"][c]["cost_per_kg_plant"] for c in cs.CASES},
            "cost_per_m2_grow_yr_range": {c: base["cases"][c]["cost_per_m2_grow_yr"] for c in cs.CASES},
            "mid": {key: metric(base["cases"]["mid"], key, where) for key, _, where, _ in METRICS},
            "gaps": base["gaps"],
        },
        "how_to_read": ("Each change is swap minus base, mid case. Cost lines that a swap cannot price are left out "
                        "and listed under new_gaps, so a swap with new gaps can look cheaper than it is."),
        "swaps": rows,
    }


def summary_lines(result: dict) -> list[str]:
    cur = result["currency_code"] or ""

    def fmt(v, nd=2, sign=False):
        if v is None:
            return "n/a"
        return f"{v:+,.{nd}f}" if sign else f"{v:,.{nd}f}"

    b = result["base"]
    rng = b["cost_per_kg_plant_range"]
    lines = [
        f"SWAPS  {result['base_build_id']}  [{cs.LABEL}]",
        f"  Base: {cur} {fmt(rng['low_cost'])} / {fmt(rng['mid'])} / {fmt(rng['high_cost'])} per kg plant (low / mid / high cost)"
        f" | {cur} {fmt(b['mid']['cost_per_m2_grow_yr'])} per m2 grow area per yr (mid)",
        f"  {result['how_to_read']}",
        "",
        f"  {'swap':<46} {'cost/kg':>9} {'cost/m2':>9} {'yield kg':>9} {'water m3':>9} {'top-up':>8} {'area m2':>8} {'kWh/yr':>9} {'build':>10}",
    ]
    for row in result["swaps"]:
        if row["status"] != "ran":
            lines.append(f"  {row['swap_id']:<46} not run: {row['reason']}")
            continue
        m = row["mid"]
        name = row["swap_id"] if row["like_for_like"] else f"{row['swap_id']} (*)"
        lines.append(
            f"  {name[:46]:<46} {fmt(m['cost_per_kg_plant']['change'], 2, True):>9}"
            f" {fmt(m['cost_per_m2_grow_yr']['change'], 1, True):>9} {fmt(m['plant_kg_yr']['change'], 0, True):>9}"
            f" {fmt(m['system_water_m3']['change'], 1, True):>9} {fmt(m['makeup_water_m3_yr']['change'], 0, True):>8}"
            f" {fmt(m['minimum_area_m2']['change'], 1, True):>8} {fmt(m['electricity_kwh_yr']['change'], 0, True):>9}"
            f" {fmt(m['capex_total']['change'], 0, True):>10}"
        )
        lines.append(f"  {'':<4}{row['label']}")
        if row["cost_per_kg_plant_range"]["mid"] is None:
            lines.append(f"  {'':<4}cost per kg n/a (no sourced yield); cost per m2 range"
                         f" {fmt(row['cost_per_m2_grow_yr_range']['low_cost'], 1)} / {fmt(row['cost_per_m2_grow_yr_range']['mid'], 1)}"
                         f" / {fmt(row['cost_per_m2_grow_yr_range']['high_cost'], 1)}")
        else:
            rr = row["cost_per_kg_plant_range"]
            lines.append(f"  {'':<4}cost per kg after swap: {fmt(rr['low_cost'])} / {fmt(rr['mid'])} / {fmt(rr['high_cost'])}")
        for g in row["new_gaps"]:
            lines.append(f"  {'':<4}new gap: {g}")
        for g in row["closed_gaps"]:
            lines.append(f"  {'':<4}closes gap: {g}")
        if row.get("note"):
            lines.append(f"  {'':<4}note: {row['note']}")
        if row["trade_offs"]:
            lines.append(f"  {'':<4}trade-off: {row['trade_offs'][0]}")
    lines += ["", "  (*) the swap opens cost gaps (listed under it), so some of its costs are left out and the change is not like-for-like.",
              f"  Columns are changes against the base (mid case, {cur}): cost per kg of plant, cost per m2 of grow area",
              "  per yr, plant output, system water, make-up water per yr, minimum area, electricity, total build cost.",
              f"  Not included: {cs.SCOPE_NOTE}"]
    return lines


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("spec", help="run file with a 'swaps' block, or a bare swaps spec")
    parser.add_argument("--out", help="write the full result JSON here")
    args = parser.parse_args(argv)
    try:
        spec = cs.load_json(cs.project_path(args.spec))
        if isinstance(spec.get("swaps"), dict):
            spec = spec["swaps"]
        result = compare_swaps(spec)
    except ConfigError as exc:
        print(f"Error: {exc}")
        return 2
    if args.out:
        out = cs.project_path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print("\n".join(summary_lines(result)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
