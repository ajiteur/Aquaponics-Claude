"""Audit that every catalog price and rate is tied to a market: region, currency and price year.

Reads data/catalog/components_v0.json and the locations block of
data/scenarios/unit_configuration_candidates_v0.json, and prints one line per priced item plus
the flags: a missing market tag, a currency that differs from the item's own, a price year
that is not recorded, or a price taken from one place and used for a whole region.

Usage:
    python scripts/audit_market_tags.py [--json]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
DEFAULT_COMPONENTS = PROJECT_ROOT / "data" / "catalog" / "components_v0.json"
DEFAULT_LOCATIONS = PROJECT_ROOT / "data" / "scenarios" / "unit_configuration_candidates_v0.json"
LOCATION_RATES = ("wage_per_hour", "electricity_per_kwh")


def year_text(year: dict | None) -> str:
    if not year:
        return "not recorded"
    lo, hi = year.get("low"), year.get("high")
    if lo == hi:
        return str(lo) if lo is not None else "not recorded"
    return f"{lo if lo is not None else '?'}-{hi if hi is not None else '?'}"


def audit(components_path: Path = DEFAULT_COMPONENTS, locations_path: Path = DEFAULT_LOCATIONS) -> dict:
    catalog = json.loads(components_path.read_text(encoding="utf-8"))
    locations = json.loads(locations_path.read_text(encoding="utf-8")).get("locations", {})
    rows, flags = [], []

    def add(kind, item_id, region, currency, market, own_currency):
        row = {"kind": kind, "id": item_id, "region": region, "currency_code": currency,
               "price_year": year_text((market or {}).get("price_year")),
               "price_year_basis": (market or {}).get("price_year_basis"), "place": (market or {}).get("place")}
        rows.append(row)
        if market is None:
            flags.append(f"{kind} {item_id}: no market tag")
            return
        if market.get("price_year_basis") == "not_a_price":
            return
        if market.get("region") != region:
            flags.append(f"{kind} {item_id}: market region {market.get('region')} differs from item region {region}")
        if market.get("currency_code") != own_currency:
            flags.append(f"{kind} {item_id}: market currency {market.get('currency_code')} differs from {own_currency}")
        if "not recorded" in row["price_year"] or "?" in row["price_year"]:
            flags.append(f"{kind} {item_id} ({region}): price year {row['price_year']}")
        if market.get("place"):
            flags.append(f"{kind} {item_id} ({region}): priced for {market['place']} only")

    for c in catalog.get("components", []):
        cp = c.get("capex_per_unit")
        if cp is None:
            flags.append(f"component {c['component_id']} ({c['region']}): no price")
            continue
        add("component", c["component_id"], c["region"], c.get("currency_code"), cp.get("market"), c.get("currency_code"))
    for r in catalog.get("running_inputs", []):
        add("running_input", r["input_id"], r["region"], r.get("currency_code"), r.get("market"), r.get("currency_code"))
    for name, loc in locations.items():
        cur = loc.get("currency_code")
        if not cur:
            flags.append(f"location {name}: no currency_code")
        for key in LOCATION_RATES:
            rate = loc.get(key)
            if not isinstance(rate, dict):
                continue
            market = {"region": name, "currency_code": cur, "price_year": rate.get("price_year"),
                      "price_year_basis": rate.get("price_year_basis", "not_recorded")}
            add("location_rate", f"{name}.{key}", name, cur, market, cur)
    return {"rows": rows, "flags": flags,
            "counts": {"items": len(rows), "flags": len(flags)}}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--json", action="store_true", help="print the full result as JSON")
    args = parser.parse_args(argv)
    result = audit()
    if args.json:
        print(json.dumps(result, indent=2))
        return 0
    print(f"MARKET TAG AUDIT  {result['counts']['items']} priced items and rates, {result['counts']['flags']} flags")
    for r in result["rows"]:
        if r["price_year_basis"] == "not_a_price":
            continue
        place = f"  [{r['place']}]" if r["place"] else ""
        print(f"  {r['kind']:<14} {r['id']:<48} {r['region']:<20} {str(r['currency_code']):<5} {r['price_year']:<13} {r['price_year_basis']}{place}")
    print("\nFLAGS")
    for f in result["flags"]:
        print(f"  - {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
