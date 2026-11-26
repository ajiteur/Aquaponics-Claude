#!/usr/bin/env python3
"""Assemble an aquaponics system from catalog parts and report cost of production per kg.

You pick a region, a fish, a plant, a grow architecture, one part per category
and a target (grow area or plant output). The configurator sizes the system
with the sizing rules in the component catalog, prices each part, spreads build
cost over its lifetime, adds running costs, and reports:

    cost per kg of plant output, split by component (with each line's share)
    plant and fish output, feed, water, energy, and minimum area
    cheaper (or dearer) alternatives in each category, with their trade-offs
    every input that is missing, so gaps stay visible

Optionally it runs the crop-cycle simulator on the sized system as a cross-check.

All output is a scenario estimate, not validated. It is a cost-of-production
estimate from candidate inputs: not profit, viability or a quote. Missing
inputs are left out of the totals and listed; they are never filled in.

Usage (from the aquaponics-project folder):
    python scripts/configure_system.py <build.json> [--out result.json]
    python run.py <run name>          (a run file with a "configurator" block)
Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import math
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_COMPONENTS = PROJECT_ROOT / "data" / "catalog" / "components_v0.json"
DEFAULT_SPECIES = PROJECT_ROOT / "data" / "catalog" / "species_sizing_v0.json"
DEFAULT_LOCATIONS = PROJECT_ROOT / "data" / "scenarios" / "unit_configuration_candidates_v0.json"
CROP_CYCLE_SCRIPT = PROJECT_ROOT / "src" / "simulate_crop_cycle.py"
BASE_SIM_SCENARIO = PROJECT_ROOT / "data" / "simulation" / "scenarios" / "basil_raft_crop_cycle.json"

CASES = ("low_cost", "mid", "high_cost")
LABEL = "Scenario estimate, not validated."
SCOPE_NOTE = (
    "Cost of production from candidate inputs. Build cost is spread straight-line over each part's "
    "life with no interest. Logistics, packaging, marketing, land, permits, insurance and financing "
    "are not included. Not profit, viability or a quote."
)


class ConfigError(Exception):
    """A problem in a build file or catalog that the user can fix."""


# --- helpers ----------------------------------------------------------------

def project_path(p: str | Path) -> Path:
    path = Path(p)
    return path if path.is_absolute() else PROJECT_ROOT / path


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return str(path)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ConfigError(f"File not found: {rel(path)}")
    except json.JSONDecodeError as exc:
        raise ConfigError(f"{rel(path)} is not valid JSON (line {exc.lineno}): {exc.msg}")


def as_range(value: Any) -> dict | None:
    """Accept a number, a {low, high} dict or None. Returns {low, high, ...} or None."""
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return {"low": float(value), "high": float(value)}
    if isinstance(value, dict):
        if "value" in value and "low" not in value:
            return as_range(value["value"]) if value["value"] is not None else None
        if value.get("low") is None or value.get("high") is None:
            return None
        return value
    raise ConfigError(f"Expected a number or {{low, high}}, got {value!r}")


def pick(rng: dict | None, case: str, favourable: str | None) -> float | None:
    """Value for a case. favourable='low' means a lower value lowers cost per kg."""
    if rng is None:
        return None
    lo, hi = float(rng["low"]), float(rng["high"])
    if case == "mid" or favourable is None:
        return (lo + hi) / 2
    good = lo if favourable == "low" else hi
    bad = hi if favourable == "low" else lo
    return good if case == "low_cost" else bad


def r(x: float | None, nd: int = 2) -> float | None:
    return None if x is None else round(x, nd)


# --- catalog access ---------------------------------------------------------

class Catalog:
    def __init__(self, components: dict, species: dict, locations: dict):
        self.components_doc = components
        self.species_doc = species
        self.locations = locations.get("locations", {})
        self.location_sources = locations.get("sources", {})
        self.by_id = {}
        for c in components.get("components", []):
            if c["component_id"] in self.by_id:
                raise ConfigError(f"Duplicate component_id in catalog: {c['component_id']}")
            self.by_id[c["component_id"]] = c
        self.rules = components.get("design_rules", {})
        self.running = {}
        for item in components.get("running_inputs", []):
            self.running[(item["input_id"], item["region"])] = item
        self.labour_regimes = {x["regime_id"]: x for x in components.get("labour_regimes", [])}
        self.fish = {f["species_key"]: f for f in species.get("fish", [])}
        self.plants = {p["species_key"]: p for p in species.get("plants", [])}

    def component(self, cid: str) -> dict:
        if cid not in self.by_id:
            raise ConfigError(f"Unknown component '{cid}'. See data/catalog/components_v0.json for ids.")
        return self.by_id[cid]

    def alternatives(self, comp: dict, region: str, architecture: str) -> list[dict]:
        out = []
        for c in self.by_id.values():
            if c["component_id"] == comp["component_id"] or c["category"] != comp["category"]:
                continue
            if c.get("role", c["category"]) != comp.get("role", comp["category"]):
                continue
            if c["region"] not in (region, "any"):
                continue
            arch = c.get("architectures")
            if arch and architecture not in arch:
                continue
            out.append(c)
        return out


# --- sizing -----------------------------------------------------------------

def rule_value(catalog: Catalog, build: dict, key: str, case: str) -> float | None:
    """A design rule: build overrides win; otherwise the catalog's sourced range."""
    overrides = build.get("design_overrides", {})
    if key in overrides:
        return pick(as_range(overrides[key]), case, None)
    rule = catalog.rules.get(key)
    if rule is None:
        return None
    return pick(as_range(rule), case, rule.get("favourable"))


def species_value(entry: dict, key: str, case: str, build: dict, kind: str) -> float | None:
    overrides = build.get("species_overrides", {}).get(kind, {})
    if key in overrides:
        return pick(as_range(overrides[key]), case, None)
    spec = entry.get("sizing", {}).get(key)
    if spec is None:
        return None
    return pick(as_range(spec), case, spec.get("favourable"))


def size_system(catalog: Catalog, build: dict, case: str, gaps: set) -> dict:
    arch = build["grow_architecture"]
    plant = catalog.plants[build["plant"]]
    fish = catalog.fish[build["fish"]]
    target = build.get("target", {})

    yld = species_value(plant, "yield_kg_per_m2_yr", case, build, "plant")
    applies = plant["sizing"].get("yield_kg_per_m2_yr", {}).get("applies_to_architectures")
    yield_basis = "sourced for this architecture"
    if applies and arch not in applies and "yield_kg_per_m2_yr" not in build.get("species_overrides", {}).get("plant", {}):
        # No direct yield for this architecture: use a sourced yield ratio against the reference
        # architecture, if the catalog has one. Missing ratio means missing yield.
        rel_spec = plant["sizing"].get("yield_relative_to_reference_architecture", {})
        ratio = rel_spec.get("values", {}).get(arch)
        if yld is not None and ratio is not None and ratio.get("low") is not None:
            yld = yld * pick(as_range(ratio), case, ratio.get("favourable", "high"))
            yield_basis = f"{rel_spec.get('reference_architecture', applies[0])} yield x sourced ratio for {arch}"
        else:
            yld = None
    if yld is None:
        gaps.add(f"plant yield for {build['plant']} in {arch} (no sourced value; set species_overrides.plant.yield_kg_per_m2_yr)")

    if target.get("grow_area_m2"):
        area = float(target["grow_area_m2"])
    elif target.get("plant_output_kg_per_year"):
        if not yld:
            raise ConfigError("Target is plant output, but there is no yield for this plant and architecture.")
        area = float(target["plant_output_kg_per_year"]) / yld
    else:
        raise ConfigError("Set target.grow_area_m2 or target.plant_output_kg_per_year in the build.")

    frr = species_value(plant, "feeding_rate_ratio_g_per_m2_day", case, build, "plant")
    arch_factor = (catalog.rules.get("feeding_rate_architecture_factor", {}).get("values", {}).get(arch))
    if build.get("design_overrides", {}).get("feeding_rate_architecture_factor") is not None:
        arch_factor = float(build["design_overrides"]["feeding_rate_architecture_factor"])
    if frr is None or arch_factor is None:
        gaps.add("feeding rate ratio for this plant/architecture")
        feed_kg_day = None
    else:
        feed_kg_day = area * frr * arch_factor / 1000.0

    fcr = species_value(fish, "fcr", case, build, "fish")
    prod_density = species_value(fish, "annual_production_kg_per_m3_tank", case, build, "fish")
    harvest_kg = species_value(fish, "harvest_weight_kg", case, build, "fish")
    survival = species_value(fish, "survival_fraction", case, build, "fish")

    feed_kg_yr = feed_kg_day * 365 if feed_kg_day is not None else None
    fish_kg_yr = feed_kg_yr / fcr if feed_kg_yr is not None and fcr else None
    tank_m3 = fish_kg_yr / prod_density if fish_kg_yr is not None and prod_density else None
    fingerlings_yr = (fish_kg_yr / harvest_kg / survival) if fish_kg_yr and harvest_kg and survival else None

    retention_h = rule_value(catalog, build, "fish_tank_retention_h", case)
    flow_lph = tank_m3 * 1000 / retention_h if tank_m3 is not None and retention_h else None
    hrt_min = rule_value(catalog, build, "clarifier_hrt_min", case)
    clarifier_m3 = flow_lph * hrt_min / 60 / 1000 if flow_lph is not None and hrt_min else None

    air_per_feed = rule_value(catalog, build, "air_lpm_per_kg_feed_day", case)
    fish_air = feed_kg_day * air_per_feed if feed_kg_day is not None and air_per_feed else None
    raft_share = rule_value(catalog, build, "raft_air_share_of_fish_air", case) if arch == "dwc_raft" else 0.0
    air_lpm = fish_air * (1 + raft_share) if fish_air is not None and raft_share is not None else fish_air

    hydro_m3 = liner_m2 = media_m3 = channel_m = wall_face_m2 = None
    if arch == "dwc_raft":
        depth = rule_value(catalog, build, "raft_water_depth_m", case)
        width = rule_value(catalog, build, "raft_trough_width_m", case)
        hydro_m3 = area * depth if depth else None
        liner_m2 = area * (1 + 2 * depth / width) if depth and width else None
        # Wall face of the troughs (both long sides, water depth high), the same geometry as the
        # liner's side area. Ends and freeboard are not counted, so this undercounts slightly.
        wall_face_m2 = area * 2 * depth / width if depth and width else None
    elif arch == "media_bed":
        bed_depth = rule_value(catalog, build, "media_bed_depth_m", case)
        media_m3 = area * bed_depth if bed_depth else None
    elif arch == "nft":
        per_m2 = rule_value(catalog, build, "nft_channel_m_per_m2", case)
        channel_m = area * per_m2 if per_m2 else None
        if per_m2 is None:
            gaps.add("NFT channel metres per m2 of grow area (no sourced layout; set design_overrides.nft_channel_m_per_m2)")

    needs_biofilter = arch in catalog.rules.get("separate_biofilter_needed_for", {}).get("values", [])
    loading = rule_value(catalog, build, "mbbr_loading_kg_feed_per_m3_day", case)
    biofilter_m3 = feed_kg_day / loading if needs_biofilter and feed_kg_day is not None and loading else 0.0

    parts = [tank_m3, clarifier_m3, hydro_m3, biofilter_m3]
    system_water_m3 = sum(p for p in parts if p) if tank_m3 is not None else None
    if arch != "dwc_raft":
        gaps.add(f"water held in the {arch} grow unit (not sourced; system water counts tanks and filters only)")
    makeup = rule_value(catalog, build, "makeup_water_fraction_per_day", case)
    makeup_m3_yr = system_water_m3 * makeup * 365 if system_water_m3 is not None and makeup is not None else None

    plants_m2 = species_value(plant, "planting_density_plants_per_m2", case, build, "plant")
    heads = species_value(plant, "heads_per_m2_yr", case, build, "plant")
    if heads is not None:
        plants_yr = area * heads
    elif plants_m2 is not None:
        cycle = species_value(plant, "cycle_days", case, build, "plant")
        cuts = species_value(plant, "harvests_per_planting", case, build, "plant")
        plants_yr = area * plants_m2 * 365 / (cycle * cuts) if cycle and cuts else None
    else:
        plants_yr = None

    return {
        "grow_area_m2": area,
        "raft_area_m2": area if arch == "dwc_raft" else 0.0,
        "liner_area_m2": liner_m2,
        "trough_wall_face_m2": wall_face_m2,
        "system_count": 1.0,
        "media_volume_m3": media_m3,
        "nft_channel_length_m": channel_m,
        "hydro_volume_m3": hydro_m3,
        "feed_kg_day": feed_kg_day,
        "feed_kg_yr": feed_kg_yr,
        "fish_kg_yr": fish_kg_yr,
        "fish_tank_volume_m3": tank_m3,
        "fingerlings_per_yr": fingerlings_yr,
        "recirculation_flow_lph": flow_lph,
        "clarifier_volume_m3": clarifier_m3,
        "biofilter_media_m3": biofilter_m3,
        "air_flow_lpm": air_lpm,
        "system_water_m3": system_water_m3,
        "makeup_water_m3_yr": makeup_m3_yr,
        "plant_kg_yr": area * yld if yld else None,
        "plant_yield_basis": yield_basis if yld else None,
        "plants_started_per_yr": plants_yr,
    }


# --- costing ----------------------------------------------------------------

def component_override(build: dict | None, comp: dict, key: str):
    """A per-part value the user set in the build (component_overrides.<id>.<key>), or None."""
    return ((build or {}).get("component_overrides", {}).get(comp["component_id"], {}) or {}).get(key)


def quantity(comp: dict, drivers: dict, build: dict | None = None) -> float | None:
    fixed = component_override(build, comp, "quantity")
    if fixed is not None:
        return float(fixed)
    s = comp["sizing"]
    d = drivers.get(s["driver"])
    if d is None:
        return None
    if s.get("mode", "discrete") == "continuous":
        return d * float(s.get("per_driver_unit", 1.0))
    cap = float(s["capacity_per_unit"])
    n = math.ceil(d / cap - 1e-9) if d > 0 else 0
    return max(n, int(s.get("min_units", 0)))


def duty_hours(comp: dict, build: dict | None) -> float | None:
    """Hours per day a part runs. A part with no energy block runs 24 h by default; a part whose
    catalog entry sets duty_hours_per_day to null (lights) needs the user to set it in the build."""
    override = component_override(build, comp, "duty_hours_per_day")
    if override is not None:
        return float(override)
    energy = comp.get("energy") or {}
    if "duty_hours_per_day" in energy:
        return None if energy["duty_hours_per_day"] is None else float(energy["duty_hours_per_day"])
    return 24.0


def cost_component(comp: dict, drivers: dict, case: str, power_price: float | None, gaps: set,
                   build: dict | None = None) -> dict:
    qty = quantity(comp, drivers, build)
    capex_unit = pick(as_range(comp.get("capex_per_unit")), case, "low")
    life = pick(as_range(comp.get("lifetime_years")), case, "high")
    hours = duty_hours(comp, build)
    if life is None and comp.get("lifetime_hours") and hours:
        # Rated burning hours (lights, UV lamps) turn into years only once the hours per day are known.
        rated = pick(as_range(comp["lifetime_hours"]), case, "high")
        life = rated / (hours * 365) if rated else None
    line = {
        "component_id": comp["component_id"],
        "category": comp["category"],
        "name": comp["name"],
        "quantity": r(qty, 3),
        "quantity_unit": comp["sizing"].get("unit_label", "units"),
        "capex_total": None,
        "capex_per_year": None,
        "electricity_kwh_yr": None,
        "electricity_cost_per_year": None,
        "missing": [],
    }
    if qty is None:
        line["missing"].append(f"sizing driver {comp['sizing']['driver']}")
    if capex_unit is None:
        line["missing"].append("price")
    if life is None:
        line["missing"].append("lifetime")
    if qty is not None and capex_unit is not None:
        line["capex_total"] = r(qty * capex_unit)
        if life:
            line["capex_per_year"] = r(qty * capex_unit / life)
    energy = comp.get("energy")
    if energy:
        w = pick(as_range(energy.get("power_w_per_unit")), case, "low")
        if hours is None:
            line["missing"].append("duty hours per day (set component_overrides.<id>.duty_hours_per_day)")
        elif w is not None and qty is not None:
            kwh = qty * w * hours * 365 / 1000
            line["electricity_kwh_yr"] = r(kwh, 1)
            if power_price is not None:
                line["electricity_cost_per_year"] = r(kwh * power_price)
        else:
            line["missing"].append("power rating")
    for m in line["missing"]:
        gaps.add(f"{comp['component_id']}: {m}")
    return line


def running_value(catalog: Catalog, input_id: str, region: str, case: str, build: dict) -> tuple[float | None, dict | None]:
    overrides = build.get("running_overrides", {})
    if input_id in overrides:
        return pick(as_range(overrides[input_id]), case, None), {"origin": "user_supplied_in_build_file"}
    item = catalog.running.get((input_id, region))
    if item is None:
        return None, None
    favourable = item.get("favourable", "low")
    return pick(as_range(item.get("value")), case, favourable), item


def location_value(catalog: Catalog, build: dict, key: str, case: str) -> float | None:
    overrides = build.get("running_overrides", {})
    if key in overrides:
        return pick(as_range(overrides[key]), case, None)
    loc = catalog.locations.get(build["location"])
    if loc is None:
        raise ConfigError(f"Unknown location '{build['location']}'. Known: {', '.join(catalog.locations)}")
    return pick(as_range(loc.get(key)), case, "low")


def evaluate_case(catalog: Catalog, build: dict, case: str, components: list[dict]) -> dict:
    gaps: set = set()
    drivers = size_system(catalog, build, case, gaps)
    region = build["region"]
    power_price = location_value(catalog, build, "electricity_per_kwh", case)
    wage = location_value(catalog, build, "wage_per_hour", case)

    # Structure covers the whole minimum footprint, so work that out first.
    equip_footprint = 0.0
    for comp in components:
        if not comp.get("occupies_floor"):
            continue
        q = quantity(comp, drivers, build)
        fp = comp.get("footprint_m2_per_unit")
        if q and fp:
            equip_footprint += q * float(fp)
        elif q:
            gaps.add(f"{comp['component_id']}: footprint not recorded (minimum area undercounts it)")
    min_area = drivers["grow_area_m2"] + equip_footprint
    ratio = rule_value(catalog, build, "land_to_grow_area_ratio_uvi", case)
    drivers["equipment_footprint_m2"] = equip_footprint
    drivers["minimum_area_m2"] = min_area
    drivers["planning_area_m2_uvi_ratio"] = drivers["grow_area_m2"] * ratio if ratio else None
    structure_basis = build.get("structure_area_basis", "planning_area_m2_uvi_ratio")
    drivers["structure_area_m2"] = drivers.get(structure_basis) or min_area

    # Backup power is sized on the load that must keep running in an outage: pumps and aeration.
    critical_w = 0.0
    for comp in components:
        if comp["category"] not in ("water_pump", "aeration"):
            continue
        q = quantity(comp, drivers, build)
        w = pick(as_range((comp.get("energy") or {}).get("power_w_per_unit")), case, "low")
        if q and w:
            critical_w += q * w
    drivers["critical_load_w"] = critical_w

    lines = [cost_component(c, drivers, case, power_price, gaps, build) for c in components]
    if (drivers.get("biofilter_media_m3") or 0) > 0 and not any(c["category"] == "biofilter" for c in components):
        gaps.add(f"biofilter: {build['grow_architecture']} needs a separate biofilter, but none is chosen, so its cost is left out")
    if not any(c["category"] == "grow_unit" for c in components):
        gaps.add(f"grow unit: no part chosen (none priced for {build['grow_architecture']} in {region}), so its build cost is left out")

    running = []

    def add_running(line_id: str, label: str, qty: float | None, unit: str, input_id: str):
        price, item = running_value(catalog, input_id, region, case, build)
        row = {"line_id": line_id, "label": label, "quantity": r(qty, 2), "quantity_unit": unit,
               "unit_price": r(price, 4), "cost_per_year": None, "input_id": input_id}
        if qty is None:
            gaps.add(f"{label}: quantity")
        elif price is None:
            gaps.add(f"{label}: price ({input_id} for {region})")
        else:
            row["cost_per_year"] = r(qty * price)
        running.append(row)

    add_running("feed", "Fish feed", drivers["feed_kg_yr"], "kg/yr", "fish_feed_price_per_kg")
    add_running("fingerlings", "Fingerlings", drivers["fingerlings_per_yr"], "fish/yr", "fingerling_price_each")
    add_running("seeds", "Seeds / plant starts", drivers["plants_started_per_yr"], "plants/yr", f"{build['plant']}_seed_price_each")
    add_running("water", "Make-up water", drivers["makeup_water_m3_yr"], "m3/yr", "water_price_per_m3")
    if build.get("propagation", {}).get("enabled"):
        # Plugs or tray cells used once per plant start (opt-in, so older builds are unchanged).
        add_running("propagation", "Propagation plugs or tray cells", drivers["plants_started_per_yr"],
                    "plants/yr", "propagation_cell_price_each")

    heating = build.get("heating", {})
    heat_pump_kwh = 0.0
    heating_source = heating.get("source", "gas_boiler")
    if heating.get("enabled"):
        # Heat demand is recorded as m3 of gas a boiler-heated greenhouse burns per m2 per year.
        demand, _ = running_value(catalog, "greenhouse_heat_demand_m3_gas_per_m2_yr", region, case, build)
        gas_qty = drivers["structure_area_m2"] * demand if demand is not None else None
        if heating_source == "gas_boiler":
            add_running("heating", "Heating gas", gas_qty, "m3 gas/yr", "natural_gas_price_per_m3")
            if not any(c["category"] == "heating" for c in components):
                gaps.add("gas boiler and heating installation: no catalog price (the glasshouse price excludes heating)")
        elif heating_source == "heat_pump":
            # Same heat, delivered by an electric heat pump: heat (kWh) = gas m3 x heat per m3 of gas;
            # electricity = heat / seasonal COP.
            heat_per_m3, _ = running_value(catalog, "gas_heat_kwh_per_m3", region, case, build)
            cop, _ = running_value(catalog, "heat_pump_seasonal_cop", region, case, build)
            heat_kwh = gas_qty * heat_per_m3 if gas_qty is not None and heat_per_m3 is not None else None
            drivers["heat_demand_kwh_yr"] = heat_kwh
            if heat_kwh is None:
                gaps.add("heat pump: heat demand in kWh (needs greenhouse_heat_demand and gas_heat_kwh_per_m3)")
            elif cop is None:
                gaps.add(f"heat pump: seasonal COP (heat_pump_seasonal_cop for {region})")
            else:
                heat_pump_kwh = heat_kwh / cop
                if power_price is None:
                    gaps.add("heat pump: electricity price")
                running.append({
                    "line_id": "heating", "label": "Heat pump electricity", "quantity": r(heat_pump_kwh, 0),
                    "quantity_unit": "kWh/yr", "unit_price": r(power_price, 4),
                    "cost_per_year": r(heat_pump_kwh * power_price) if power_price is not None else None,
                    "input_id": "heat_pump_seasonal_cop",
                })
            if not any(c["category"] == "heating" for c in components):
                gaps.add("heat pump: no heating component chosen, so its build cost is left out")
        else:
            raise ConfigError(f"Unknown heating.source '{heating_source}'. Known: gas_boiler, heat_pump")

    regime_id = build.get("labour_regime")
    labour = {"regime_id": regime_id, "hours_per_year": None, "cost_per_year": None, "costed": False}
    if regime_id:
        regime = catalog.labour_regimes.get(regime_id)
        if regime is None:
            raise ConfigError(f"Unknown labour_regime '{regime_id}'. Known: {', '.join(catalog.labour_regimes)}")
        per_m2 = pick(as_range(regime.get("hours_per_m2_yr")), case, "low")
        per_kg = pick(as_range(regime.get("hours_per_kg_output")), case, "low")
        hours = None
        if per_m2 is not None:
            hours = per_m2 * drivers["grow_area_m2"]
        elif per_kg is not None and drivers["plant_kg_yr"] is not None:
            hours = per_kg * (drivers["plant_kg_yr"] + (drivers["fish_kg_yr"] or 0))
        labour["hours_per_year"] = r(hours, 0)
        labour["costed"] = bool(regime.get("costed", True))
        if hours is not None and labour["costed"]:
            labour["cost_per_year"] = r(hours * wage) if wage is not None else None
        labour["label"] = regime["label"]
    else:
        gaps.add("labour regime not chosen")

    # Plumbing, valves, fittings and small parts are not itemised in the catalog. UVI's build
    # spent a sourced share of hardware cost on them, so add that share as its own line.
    frac = rule_value(catalog, build, "plumbing_misc_fraction_of_hardware_capex", case)
    misc_life = rule_value(catalog, build, "plumbing_misc_lifetime_years", case)
    hardware = sum(l["capex_total"] or 0 for l in lines if l["category"] != "structure")
    if frac is not None and hardware:
        misc_total = hardware * frac
        lines.append({
            "component_id": "allowance_plumbing_misc", "category": "plumbing_misc",
            "name": "Plumbing, valves, fittings and small parts (UVI share of hardware cost)",
            "quantity": None, "quantity_unit": "allowance", "capex_total": r(misc_total),
            "capex_per_year": r(misc_total / misc_life) if misc_life else None,
            "electricity_kwh_yr": None, "electricity_cost_per_year": None, "missing": [],
        })

    elec_kwh = sum(l["electricity_kwh_yr"] or 0 for l in lines) + heat_pump_kwh
    capex_total = sum(l["capex_total"] or 0 for l in lines)
    cost_rows = []
    for l in lines:
        if l["capex_per_year"] is not None:
            cost_rows.append((f"build: {l['category']} ({l['component_id']})", l["capex_per_year"]))
        if l["electricity_cost_per_year"] is not None:
            cost_rows.append((f"electricity: {l['category']} ({l['component_id']})", l["electricity_cost_per_year"]))
    for row in running:
        if row["cost_per_year"] is not None:
            cost_rows.append((f"running: {row['label']}", row["cost_per_year"]))
    if labour["cost_per_year"] is not None:
        cost_rows.append(("running: labour", labour["cost_per_year"]))
    total = sum(v for _, v in cost_rows)
    plant_kg = drivers["plant_kg_yr"]
    fish_kg = drivers["fish_kg_yr"] or 0
    breakdown = [
        {"line": name, "cost_per_year": r(v), "per_kg_plant": r(v / plant_kg, 3) if plant_kg else None,
         "share": r(v / total, 4) if total else None}
        for name, v in sorted(cost_rows, key=lambda x: -x[1])
    ]
    return {
        "case": case,
        "sizing": {k: (r(v, 3) if not isinstance(v, str) else v) for k, v in drivers.items()},
        "components": lines,
        "running": running,
        "labour": labour,
        "electricity_kwh_yr": r(elec_kwh, 0),
        "electricity_price_used": power_price,
        "wage_used": wage,
        "capex_total": r(capex_total),
        "annual_cost_counted": r(total),
        "cost_per_kg_plant": r(total / plant_kg, 3) if plant_kg else None,
        "cost_per_kg_all_output": r(total / (plant_kg + fish_kg), 3) if plant_kg else None,
        "cost_per_m2_grow_yr": r(total / drivers["grow_area_m2"], 3) if drivers["grow_area_m2"] else None,
        "heating_source": heating_source if heating.get("enabled") else None,
        "breakdown": breakdown,
        "gaps": sorted(gaps),
    }


def resolve_components(catalog: Catalog, build: dict) -> list[dict]:
    chosen = []
    for category, ids in build.get("components", {}).items():
        if category.startswith("_") or ids in (None, [], ""):
            continue
        for cid in ids if isinstance(ids, list) else [ids]:
            comp = catalog.component(cid)
            if comp["category"] != category:
                raise ConfigError(f"Component '{cid}' is a {comp['category']}, not a {category}.")
            if comp["region"] not in (build["region"], "any"):
                raise ConfigError(f"Component '{cid}' is priced for {comp['region']}, not {build['region']}.")
            arch = comp.get("architectures")
            if arch and build["grow_architecture"] not in arch:
                raise ConfigError(f"Component '{cid}' does not fit a {build['grow_architecture']} system.")
            chosen.append(comp)
    return chosen


def validate_build(catalog: Catalog, build: dict) -> None:
    for key in ("region", "location", "fish", "plant", "grow_architecture"):
        if not build.get(key):
            raise ConfigError(f"The build needs '{key}'.")
    if build["fish"] not in catalog.fish:
        raise ConfigError(f"Unknown fish '{build['fish']}'. Known: {', '.join(catalog.fish)}")
    if build["plant"] not in catalog.plants:
        raise ConfigError(f"Unknown plant '{build['plant']}'. Known: {', '.join(catalog.plants)}")
    archs = catalog.rules.get("architectures", {}).get("values", ["dwc_raft", "nft", "media_bed"])
    if build["grow_architecture"] not in archs:
        raise ConfigError(f"Unknown grow_architecture '{build['grow_architecture']}'. Known: {', '.join(archs)}")


def compare_alternatives(catalog: Catalog, build: dict, components: list[dict], base_mid: dict) -> list[dict]:
    out = []
    base = base_mid["cost_per_kg_plant"]
    for comp in components:
        for alt in catalog.alternatives(comp, build["region"], build["grow_architecture"]):
            swapped = [alt if c is comp else c for c in components]
            res = evaluate_case(catalog, build, "mid", swapped)
            alt_line = next(l for l in res["components"] if l["component_id"] == alt["component_id"])
            out.append({
                "category": comp["category"],
                "instead_of": comp["component_id"],
                "alternative": alt["component_id"],
                "alternative_name": alt["name"],
                "cost_per_kg_plant_mid": res["cost_per_kg_plant"],
                "change_per_kg_plant_mid": r(res["cost_per_kg_plant"] - base, 3)
                if res["cost_per_kg_plant"] is not None and base is not None else None,
                "alternative_missing": alt_line["missing"],
                "trade_offs": alt.get("trade_offs", []),
            })
    return sorted(out, key=lambda x: (x["category"], x["change_per_kg_plant_mid"] if x["change_per_kg_plant_mid"] is not None else 1e9))


# --- optional simulator cross-check ----------------------------------------

def simulation_check(catalog: Catalog, build: dict, mid: dict, days: int) -> dict:
    plant = catalog.plants[build["plant"]]
    if not plant.get("simulation_supported") or build["grow_architecture"] != "dwc_raft":
        return {"status": "not_available",
                "reason": "The crop-cycle simulator is calibrated for basil in a DWC raft only."}
    s = mid["sizing"]
    if s.get("feed_kg_day") is None or s.get("fish_tank_volume_m3") is None:
        return {"status": "not_available", "reason": "Sizing is incomplete (feed or tank volume missing)."}
    scenario = json.loads(BASE_SIM_SCENARIO.read_text(encoding="utf-8"))
    rate = scenario["feeding"]["feed_rate_percent_body_weight_per_day"] / 100.0
    biomass = s["feed_kg_day"] / rate
    avg_kg = scenario["fish_batch"]["average_weight_g"] / 1000.0
    area = s["grow_area_m2"]
    density = species_value(plant, "planting_density_plants_per_m2", "mid", build, "plant") or 8.0
    scenario["scenario_id"] = f"configurator_{build.get('build_id', 'build')}"
    # Basil now uses growth-based N uptake (PR #11), which already scales with volume. The legacy
    # placeholder fallback is in mg/L per plant per day, so rescale it to keep mg per plant constant.
    base_volume_l = scenario["system"]["water_volume_l"]
    new_volume_l = s["system_water_m3"] * 1000
    nm = scenario.get("nitrogen_model", {})
    if nm.get("plant_nitrate_uptake_mode") == "placeholder" and "nitrate_uptake_mg_l_per_plant_day" in nm:
        nm["nitrate_uptake_mg_l_per_plant_day"] = round(nm["nitrate_uptake_mg_l_per_plant_day"] * base_volume_l / new_volume_l, 6)
    scenario["system"]["water_volume_l"] = round(new_volume_l, 1)
    scenario["system"]["fish_tank_volume_l"] = round(s["fish_tank_volume_m3"] * 1000, 1)
    scenario["system"]["plant_zone_volume_l"] = round((s.get("hydro_volume_m3") or 0) * 1000, 1)
    scenario["system"]["recirculation_rate_lph"] = round(s["recirculation_flow_lph"], 1)
    scenario["system"]["nitrification_surfaces"]["raft_grow_area_m2"] = round(area, 2)
    scenario["system"]["nitrification_surfaces"]["basis"] = "configurator: sized from catalog design rules"
    scenario["fish_batch"]["total_biomass_kg"] = round(biomass, 2)
    scenario["fish_batch"]["count"] = max(1, round(biomass / avg_kg))
    scenario["plant_crop"]["plant_count"] = max(1, round(area * density))
    scenario["operations_policy"]["water_top_up_l_per_day"] = round((s["makeup_water_m3_yr"] or 0) / 365 * 1000, 1)

    spec = importlib.util.spec_from_file_location("simulate_crop_cycle", CROP_CYCLE_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "configurator_scenario.json"
        path.write_text(json.dumps(scenario, indent=2), encoding="utf-8")
        result = module.run_cycle(path, days)
    last = result["daily"][-1] if result["daily"] else {}
    harvested = result["summary"]["total_harvested_mass_kg"]
    return {
        "status": "ran",
        "days": days,
        "note": "Simulator cross-check of the sized system (one growing period). Model context only: not a fish-safety, aeration or yield proof.",
        "fish_biomass_kg_simulated": round(biomass, 1),
        "harvested_kg": harvested,
        "harvested_kg_per_m2": round(harvested / area, 3) if area else None,
        "catalog_yield_per_cut_kg_per_m2": r(s["plant_kg_yr"] / area / (365 / 28), 3) if s.get("plant_kg_yr") else None,
        "mean_plant_growth_score": result["summary"]["mean_plant_growth_score"],
        "final_tan_mg_L": last.get("tan_mg_L"),
        "final_unionized_nh3_mg_L": last.get("unionized_nh3_mg_L"),
        "final_nitrate_mg_L": last.get("nitrate_mg_L"),
        "final_pH": last.get("pH"),
    }


# --- entry points -----------------------------------------------------------

def market_check(catalog: Catalog, build: dict, components: list[dict]) -> dict:
    """Tie every price the build uses to its market (region, currency, price year).

    A currency that differs from the location's currency is an error, since no exchange rate is
    applied inside a build. A price with no recorded year, or one taken from another place in the
    same region, is reported as a flag rather than hidden.
    """
    loc = catalog.locations.get(build["location"], {})
    currency = loc.get("currency_code")
    tags, flags = [], []

    def check(kind: str, item_id: str, market: dict | None, cur: str | None):
        if cur is not None and currency is not None and cur != currency:
            raise ConfigError(f"{kind} '{item_id}' is priced in {cur}, but location '{build['location']}' uses {currency}.")
        if market is None:
            flags.append(f"{item_id}: no market tag (region, currency, price year)")
            return
        if market.get("price_year_basis") == "not_a_price":
            return
        tags.append({"kind": kind, "id": item_id, **market})
        if market.get("price_year_basis") == "not_recorded" or not market.get("price_year"):
            flags.append(f"{item_id}: price year not recorded")
        if market.get("place"):
            flags.append(f"{item_id}: priced for {market['place']}, used for location '{build['location']}'")

    for comp in components:
        cp = comp.get("capex_per_unit")
        if cp is not None:
            check("component", comp["component_id"], cp.get("market"), comp.get("currency_code"))
    overrides = build.get("running_overrides", {})
    for (input_id, region), item in sorted(catalog.running.items()):
        if region == build["region"] and input_id not in overrides:
            check("running_input", input_id, item.get("market"), item.get("currency_code"))
    for key in ("wage_per_hour", "electricity_per_kwh"):
        rate = loc.get(key)
        if isinstance(rate, dict) and key not in overrides:
            year = rate.get("price_year")
            if not year:
                flags.append(f"location {build['location']}.{key}: price year not recorded")
            elif None in (year.get("low"), year.get("high")):
                flags.append(f"location {build['location']}.{key}: price year recorded for one end of the range only")
    return {"currency_code": currency, "tags": tags, "flags": sorted(set(flags))}


def build_result(build: dict, components_path: Path = DEFAULT_COMPONENTS,
                 species_path: Path = DEFAULT_SPECIES, locations_path: Path = DEFAULT_LOCATIONS,
                 run_simulation: bool | None = None) -> dict:
    catalog = Catalog(load_json(components_path), load_json(species_path), load_json(locations_path))
    validate_build(catalog, build)
    components = resolve_components(catalog, build)
    market = market_check(catalog, build, components)
    cases = {case: evaluate_case(catalog, build, case, components) for case in CASES}
    currency = catalog.locations.get(build["location"], {}).get("currency_code")
    result = {
        "estimate_status": "scenario_estimate",
        "label": f"{LABEL} {SCOPE_NOTE}",
        "generated_by": "scripts/configure_system.py",
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "build": build,
        "currency_code": currency,
        "catalog_files": [rel(components_path), rel(species_path), rel(locations_path)],
        "case_definitions": {
            "low_cost": "cheapest end of every price, longest life, highest yield, lowest labour",
            "mid": "midpoint of every range",
            "high_cost": "dearest end of every price, shortest life, lowest yield, highest labour",
        },
        "cases": cases,
        "alternatives_mid": compare_alternatives(catalog, build, components, cases["mid"]),
        "gaps": sorted(set().union(*(set(c["gaps"]) for c in cases.values()))),
        "market": market,
        "not_included": SCOPE_NOTE,
    }
    sim = build.get("simulation_check") if run_simulation is None else ({"days": 28} if run_simulation else None)
    if sim:
        result["simulation_check"] = simulation_check(catalog, build, cases["mid"], int(sim.get("days", 28)))
    return result


def summary_lines(result: dict) -> list[str]:
    cur = result["currency_code"] or ""
    b = result["build"]
    c = result["cases"]
    mid = c["mid"]
    s = mid["sizing"]

    def three(key: str, nd: int = 2) -> str:
        vals = [c[k].get(key) for k in CASES]
        return " / ".join("n/a" if v is None else f"{v:,.{nd}f}" for v in vals)

    def fmt(v, nd=1):
        return "n/a" if v is None else f"{v:,.{nd}f}"

    lines = [
        f"CONFIGURATOR  {b.get('build_id', '')}  [{LABEL}]",
        f"  {b['fish']} + {b['plant']}, {b['grow_architecture']}, {b['region']} (prices for {b['location']}, {cur})",
        f"  labour: {mid['labour'].get('label', 'not chosen')}",
        "",
        f"  Cost per kg of plant output (low cost / mid / high cost): {cur} {three('cost_per_kg_plant')}",
        f"  Cost per kg of all output, fish included:                 {cur} {three('cost_per_kg_all_output')}",
        f"  Annual cost counted:  {cur} {three('annual_cost_counted', 0)}     Build cost (total): {cur} {three('capex_total', 0)}",
        "",
        "  SYSTEM (mid case)",
        f"    grow area {fmt(s['grow_area_m2'])} m2 | minimum area {fmt(s['minimum_area_m2'])} m2 (grow + equipment)"
        f" | planning area {fmt(s.get('planning_area_m2_uvi_ratio'))} m2 (UVI land ratio)",
        f"    plant output {fmt(s['plant_kg_yr'], 0)} kg/yr | fish output {fmt(s['fish_kg_yr'], 0)} kg/yr"
        f" | feed {fmt(s['feed_kg_yr'], 0)} kg/yr ({fmt(s['feed_kg_day'], 2)} kg/day)",
        f"    fish tanks {fmt(s['fish_tank_volume_m3'], 1)} m3 | system water {fmt(s['system_water_m3'], 1)} m3"
        f" | make-up water {fmt(s['makeup_water_m3_yr'], 0)} m3/yr | electricity {fmt(mid['electricity_kwh_yr'], 0)} kWh/yr",
        f"    pump flow {fmt(s['recirculation_flow_lph'], 0)} L/h | air {fmt(s['air_flow_lpm'], 0)} L/min"
        f" | fingerlings {fmt(s['fingerlings_per_yr'], 0)}/yr | plant starts {fmt(s['plants_started_per_yr'], 0)}/yr",
        "",
        f"  WHERE THE MONEY GOES (mid case, {cur} per kg of plant output, share of counted cost)",
    ]
    for row in mid["breakdown"]:
        lines.append(f"    {row['line']:<62} {fmt(row['per_kg_plant'], 3):>9}  {row['share'] * 100:5.1f}%")
    if mid["labour"].get("hours_per_year") and not mid["labour"].get("costed"):
        lines.append(f"    owner hours needed (not costed): {mid['labour']['hours_per_year']:,.0f} h/yr")
    alts = result["alternatives_mid"]
    if alts:
        lines += ["", f"  ALTERNATIVES (swap one part, mid case, change in {cur} per kg of plant output)"]
        for a in alts:
            change = a["change_per_kg_plant_mid"]
            ch = "n/a" if change is None else f"{change:+,.3f}"
            miss = f"  [missing: {', '.join(a['alternative_missing'])}]" if a["alternative_missing"] else ""
            lines.append(f"    {a['category']:<14} {a['alternative']:<44} {ch:>9}{miss}")
            if a["trade_offs"]:
                lines.append(f"    {'':<14} trade-off: {a['trade_offs'][0]}")
    sim = result.get("simulation_check")
    if sim:
        lines += ["", "  SIMULATOR CROSS-CHECK (mid case)"]
        if sim["status"] == "ran":
            lines.append(
                f"    {sim['days']} days: harvested {sim['harvested_kg']} kg ({sim['harvested_kg_per_m2']} kg/m2;"
                f" catalog yield implies {sim['catalog_yield_per_cut_kg_per_m2']} kg/m2 per cut)"
            )
            lines.append(
                f"    final TAN {sim['final_tan_mg_L']} mg/L | NH3 {sim['final_unionized_nh3_mg_L']} mg/L"
                f" | nitrate {sim['final_nitrate_mg_L']} mg/L | pH {sim['final_pH']} (model context, not a fish-safety check)"
            )
        else:
            lines.append(f"    not run: {sim['reason']}")
    flags = result.get("market", {}).get("flags", [])
    if flags:
        lines += ["", "  MARKET FLAGS (prices used but not fully tied to this market and year)"]
        lines += [f"    - {f}" for f in flags]
    if result["gaps"]:
        lines += ["", "  GAPS (left out of the totals, never filled in)"]
        lines += [f"    - {g}" for g in result["gaps"]]
    lines += ["", f"  Not included: {SCOPE_NOTE}"]
    return lines


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("build", help="build JSON file")
    parser.add_argument("--out", help="write the full result JSON here")
    parser.add_argument("--no-simulation", action="store_true", help="skip the simulator cross-check")
    args = parser.parse_args(argv)
    try:
        build = load_json(project_path(args.build))
        result = build_result(build, run_simulation=False if args.no_simulation else None)
    except ConfigError as exc:
        print(f"Error: {exc}")
        return 2
    if args.out:
        out = project_path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print("\n".join(summary_lines(result)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
