#!/usr/bin/env python3
"""Build a gross revenue range for the basil bulk kg wholesale slice.

Combines simulated harvests (from src/simulate_crop_cycle.py result files) with
the price and saleability cases in a working-input file. Output is a scenario
estimate, not validated: it covers gross revenue only, never costs, margin or
profit.

Usage:
    python scripts/build_basil_revenue_range.py RESULT.json [RESULT.json ...]
        [--inputs scripts/example_first_slice_working_inputs.json]
        [--crops-per-year 13] [--out data/simulation/results/basil_revenue_range.json]

--crops-per-year defaults to 13, the staggered-production crop count reported for
the UVI basil trial (Rakocy et al. 2004).
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUTS = PROJECT_ROOT / "scripts" / "example_first_slice_working_inputs.json"
DEFAULT_OUT = PROJECT_ROOT / "data" / "simulation" / "results" / "basil_revenue_range.json"
DEFAULT_CROPS_PER_YEAR = 13
CASE_NAMES = ("conservative", "base", "optimistic")


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return str(path)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def harvest_basis(result: dict, result_path: Path) -> dict:
    """Mean harvested mass per m2 per harvest across a run's basil harvest events."""
    events = [e for e in result.get("harvest_events", []) if e.get("species_id") == "plant_basil"]
    if not events:
        raise ValueError(f"{rel(result_path)} has no basil harvest events")
    per_m2 = [e["harvested_mass_kg_per_m2"] for e in events]
    return {
        "result_file": rel(result_path),
        "scenario_id": result.get("scenario_id"),
        "harvest_event_count": len(events),
        "grow_area_m2": events[0]["grow_area_m2_at_anchor_density"],
        "harvested_kg_per_m2_per_harvest": round(sum(per_m2) / len(per_m2), 3),
        "harvested_kg_per_harvest": round(sum(e["harvested_mass_kg"] for e in events) / len(events), 3),
        "output_basis": events[0].get("output_basis"),
        "water_state_context": {
            "max_tan_mg_L": max((d["tan_mg_L"] for d in result.get("daily", [])), default=None),
            "max_unionized_nh3_mg_L": max((d["unionized_nh3_mg_L"] for d in result.get("daily", [])), default=None),
            "min_nitrate_mg_L": min((d["nitrate_mg_L"] for d in result.get("daily", [])), default=None),
            "note": "Context only. Not a fish-safety or system-safety assessment.",
        },
    }


def case_inputs(inputs: dict) -> dict[str, dict]:
    cases = {}
    for name in CASE_NAMES:
        case = inputs.get("cases", {}).get(name, {})
        price = case.get("price_per_saleable_kg")
        saleability = case.get("saleability_rate")
        provenance = case.get("provenance", {})
        cases[name] = {
            "price_per_saleable_kg": price,
            "saleability_rate": saleability,
            "currency_code": provenance.get("currency_code"),
            "price_basis": {
                "market_level": provenance.get("market_level"),
                "price_date_basis": provenance.get("price_date_basis"),
                "price_tax_treatment": provenance.get("price_tax_treatment"),
            },
            "saleability_basis": provenance.get("saleability_basis"),
            "input_status": "provisional working assumption from the inputs file",
            # AGENTS.md 1C: price and saleability must be user-approved for this scope.
            "approval": case.get("approval") or inputs.get("metadata", {}).get("approval"),
        }
        cases[name]["approval_status"] = "approved" if cases[name]["approval"] else "pending_user_approval"
    return cases


def revenue_rows(basis: dict, cases: dict[str, dict], crops_per_year: int) -> dict[str, dict]:
    rows = {}
    for name, case in cases.items():
        price, saleability = case["price_per_saleable_kg"], case["saleability_rate"]
        if price is None or saleability is None:
            rows[name] = {"missing_inputs": [k for k in ("price_per_saleable_kg", "saleability_rate") if case[k] is None]}
            continue
        saleable_kg_m2 = basis["harvested_kg_per_m2_per_harvest"] * saleability
        rev_m2_harvest = saleable_kg_m2 * price
        rows[name] = {
            "saleable_kg_per_m2_per_harvest": round(saleable_kg_m2, 3),
            "gross_revenue_per_m2_per_harvest": round(rev_m2_harvest, 2),
            "gross_revenue_per_m2_per_year": round(rev_m2_harvest * crops_per_year, 2),
            "gross_revenue_per_harvest_for_scenario_area": round(rev_m2_harvest * basis["grow_area_m2"], 2),
            "gross_revenue_per_year_for_scenario_area": round(rev_m2_harvest * basis["grow_area_m2"] * crops_per_year, 2),
        }
    return rows


def build(result_paths: list[Path], inputs_path: Path, crops_per_year: int) -> dict:
    inputs = load_json(inputs_path)
    cases = case_inputs(inputs)
    scenarios = []
    for path in result_paths:
        basis = harvest_basis(load_json(path), path)
        scenarios.append({"harvest_basis": basis, "cases": revenue_rows(basis, cases, crops_per_year)})

    annual = [
        row["gross_revenue_per_m2_per_year"]
        for s in scenarios
        for row in s["cases"].values()
        if "gross_revenue_per_m2_per_year" in row
    ]
    currencies = {c["currency_code"] for c in cases.values()}
    pending = sorted(n for n, c in cases.items() if c["approval_status"] != "approved")
    return {
        "estimate_status": "scenario_estimate",
        "label": "Scenario estimate, not validated. Gross revenue only: no costs, margin or profit.",
        "slice_id": "basil_bulk_kg_wholesale",
        "generated_by": "scripts/build_basil_revenue_range.py",
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "inputs_file": rel(inputs_path),
        "crops_per_year": crops_per_year,
        "crops_per_year_basis": "Rakocy et al. 2004 (Acta Hort 648), Results: the staggered trial is described as 13 crops per year, versus nine in an earlier study; consistent with 23.4 kg/m2/yr / 1.8 kg/m2 per harvest"
        if crops_per_year == DEFAULT_CROPS_PER_YEAR
        else "user-supplied",
        "currency_code": currencies.pop() if len(currencies) == 1 else sorted(c for c in currencies if c),
        "input_approval_status": "approved" if not pending else "pending_user_approval",
        "cases_pending_input_approval": pending,
        "case_inputs": cases,
        "scenarios": scenarios,
        "range_gross_revenue_per_m2_per_year": {"low": min(annual), "high": max(annual)} if annual else None,
        "limits": [
            "Harvested mass is runtime-native simulation output calibrated to the UVI yield anchor, not observed harvest data.",
            "Saleable mass = harvested mass x saleability_rate, where saleability_rate is a provisional working assumption.",
            "Prices are provisional Dutch wholesale examples; tax treatment is not normalized.",
            "Costs are out of scope here, so this says nothing about margin, profitability or viability.",
            "Each scenario carries its water-state range as context. High TAN or NH3 in a scenario means its harvest may not be reachable in practice; that is not assessed here.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("results", nargs="+", help="simulate_crop_cycle.py result files")
    parser.add_argument("--inputs", default=str(DEFAULT_INPUTS))
    parser.add_argument("--crops-per-year", type=int, default=DEFAULT_CROPS_PER_YEAR)
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    def resolve(p: str) -> Path:
        path = Path(p)
        return path if path.is_absolute() else PROJECT_ROOT / path

    output = build([resolve(p) for p in args.results], resolve(args.inputs), args.crops_per_year)
    out = resolve(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(json.dumps({"saved_to": rel(out), "range_gross_revenue_per_m2_per_year": output["range_gross_revenue_per_m2_per_year"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
