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
                "confidence": alt.get("price_reliability", {}).get("confidence"),
                "confidence_reason": alt.get("price_reliability", {}).get("confidence_reason"),
                "labour": alt.get("labour_effect"),
                # A zero-cost placeholder has no meaningful life to compare.
                "lifetime_years": None if ((alt.get("capex_per_unit") or {}).get("market") or {}).get("price_year_basis") == "not_a_price"
                else {"base": comp.get("lifetime_years"), "swap": alt.get("lifetime_years")},
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
            "confidence": sw.get("confidence"),
            "confidence_reason": sw.get("confidence_reason"),
            "labour": sw.get("labour"),
            "risk": sw.get("risk"),
            "lifetime_years": sw.get("lifetime_years"),
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


# --- plain-language trade-off report ---------------------------------------

def _money(v: float | None, cur: str, nd: int = 2) -> str:
    return "n/a" if v is None else f"{cur} {abs(v):,.{nd}f}"


def _life(rng: dict | None) -> str:
    if not rng or rng.get("low") is None:
        return "not sourced"
    lo, hi = rng["low"], rng["high"]
    if lo == hi:
        return f"{lo:g} year" if lo == 1 else f"{lo:g} years"
    return f"{lo:g}-{hi:g} years"


def tradeoff_entry(row: dict, cur: str) -> list[str]:
    """Gain, give-up and confidence lines for one swap, from its numbers and catalog notes."""
    if row["status"] != "ran":
        return [f"- **Not run:** {row['reason']}"]
    m = row["mid"]
    gains, losses = [], []

    def compare(key: str, text: str, unit: str = "", nd: int = 0, money: bool = False, lower_is_better: bool = True):
        ch = m[key]["change"]
        if ch is None or abs(ch) < 10 ** -max(nd, 1):
            return
        val = _money(ch, cur, nd) if money else f"{abs(ch):,.{nd}f}{unit}"
        (gains if (ch < 0) == lower_is_better else losses).append(f"{val} {'less' if ch < 0 else 'more'} {text}")

    compare("cost_per_kg_plant", "cost per kg of basil", nd=2, money=True)
    if m["cost_per_kg_plant"]["change"] is None:
        compare("cost_per_m2_grow_yr", "cost per m2 of grow area per year", nd=0, money=True)
    compare("capex_total", "to build", nd=0, money=True)
    compare("plant_kg_yr", "basil per year", " kg", lower_is_better=False)
    compare("fish_kg_yr", "fish per year", " kg", lower_is_better=False)
    compare("electricity_kwh_yr", "electricity per year", " kWh")
    compare("makeup_water_m3_yr", "top-up water per year", " m3")
    compare("minimum_area_m2", "floor area", " m2", nd=1)
    if m["plant_kg_yr"]["swap"] is None:
        losses.append("no sourced basil yield, so no cost per kg")
    lt = row.get("lifetime_years")
    if isinstance(lt, dict) and ("base" in lt or "swap" in lt):
        b, sw_ = _life(lt.get("base")), _life(lt.get("swap"))
        if b != sw_:
            losses.append(f"lifetime {sw_} instead of {b}") if (sw_ == "not sourced" or (lt.get("swap") or {}).get("high", 0) < (lt.get("base") or {}).get("low", 0)) \
                else gains.append(f"lifetime {sw_} instead of {b}")
    lines = [f"- **You gain:** {'; '.join(gains) if gains else 'nothing measurable in the model'}.",
             f"- **You give up:** {'; '.join(losses) if losses else 'nothing measurable in the model'}."]
    notes = [t for t in (row.get("risk"), row.get("labour")) if t] + row.get("trade_offs", [])[:2]
    if notes:
        lines.append(f"- **Risk, labour and practice:** {' '.join(n.rstrip('.') + '.' for n in notes)}")
    if row["new_gaps"] and not row["like_for_like"]:
        cost_gaps = [g for g in row["new_gaps"] if "footprint not recorded" not in g]
        lines.append(f"- **Left out of the cost (not like-for-like):** {'; '.join(cost_gaps)}.")
    conf = row.get("confidence") or "not rated"
    reason = f" {row['confidence_reason']}" if row.get("confidence_reason") else ""
    lines.append(f"- **Confidence:** {conf}.{reason}")
    return lines


def tradeoff_markdown(results: list[tuple[str, dict]]) -> str:
    out = [
        "# Swap Trade-offs",
        "",
        "Generated by `python scripts/compare_swaps.py --vault` from the swap runs (`runs/swaps_basil_nl.json`, "
        "`runs/swaps_basil_karnataka.json`). Do not edit by hand.",
        "",
        "**Scenario estimate, not validated.** Each swap changes one choice in a 100 m2 tilapia + basil raft build "
        "(owner labour, mid case) and is compared with that base. Gains and losses come from the configurator's numbers; "
        "risk and labour notes come from the catalog. Missing values stay missing. Values marked pending are candidates awaiting approval.",
        "",
    ]
    for title, res in results:
        cur = res["currency_code"] or ""
        b = res["base"]
        rng = b["cost_per_kg_plant_range"]
        out += [f"## {title}", "",
                f"Base: {cur} {rng['low_cost']:,.2f} / {rng['mid']:,.2f} / {rng['high_cost']:,.2f} per kg of basil (low / mid / high cost).", ""]
        for row in res["swaps"]:
            out += [f"### {row['label']}", ""] + tradeoff_entry(row, cur)
            if row.get("note"):
                out.append(f"- **Note:** {row['note']}")
            out.append("")
    out += ["## Related Notes", "", "- [[Project/How to Add Components|How to Add Components]]",
            "- [[Learnings/Simulation Findings Log|Simulation Findings Log]]", ""]
    return "\n".join(out)


VAULT_NOTE = PROJECT_ROOT / "knowledge-vault" / "Learnings" / "Swap Trade-offs.md"
VAULT_RUNS = (("Netherlands (heated glasshouse)", "runs/swaps_basil_nl.json"),
              ("Karnataka (polyhouse)", "runs/swaps_basil_karnataka.json"))


def write_vault_note(path: Path = VAULT_NOTE) -> Path:
    results = []
    for title, run in VAULT_RUNS:
        spec = cs.load_json(PROJECT_ROOT / run)
        results.append((title, compare_swaps(spec["swaps"])))
    path.write_text(tradeoff_markdown(results), encoding="utf-8")
    return path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("spec", nargs="?", help="run file with a 'swaps' block, or a bare swaps spec")
    parser.add_argument("--vault", action="store_true",
                        help="write the plain-language trade-off note for the NL and Karnataka swap runs to the vault")
    parser.add_argument("--out", help="write the full result JSON here")
    args = parser.parse_args(argv)
    if args.vault:
        print(f"Wrote {write_vault_note().relative_to(PROJECT_ROOT)}")
        return 0
    if not args.spec:
        parser.error("give a run file, or --vault")
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
