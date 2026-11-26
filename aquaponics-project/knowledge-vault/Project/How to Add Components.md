# How to Add Components

The configurator builds an aquaponics system from parts, like picking bases in a game, and reports the cost of production per kg. This note says how to add a part, a species or a region. Run it with `run.bat configure_basil_dwc_nl` (see [[Project/How to Run Locally|How to Run Locally]]).

Everything in the catalog is a **candidate** until you approve it. Results are **scenario estimates, not validated**.

## Where things live

| What | File |
|---|---|
| Parts (tanks, grow units, pumps, air, filters, structures) | `data/catalog/components_v0.json` → `components` |
| Running costs (feed, fingerlings, seeds, water, gas) | same file → `running_inputs` |
| Labour options | same file → `labour_regimes` |
| Sizing rules (retention time, air per kg feed, make-up water...) | same file → `design_rules` |
| Fish and plant sizing numbers | `data/catalog/species_sizing_v0.json` (biology stays in `data/knowledge/species/`) |
| Wage and electricity by location | `data/scenarios/unit_configuration_candidates_v0.json` → `locations` |
| Field rules | `schemas/component_catalog.schema.json` |
| A build you can edit | `runs/configure_basil_dwc_nl.json`, `runs/configure_basil_dwc_karnataka.json` |

## Add a part

1. Copy an existing part in the same `category` and give it a new `component_id` (lowercase, underscores).
2. Set `region` (`netherlands`, `india`, or `any`) and `currency_code`.
3. Set `sizing`: which `driver` it is sized on (for example `fish_tank_volume_m3`, `recirculation_flow_lph`, `air_flow_lpm`, `liner_area_m2`, `structure_area_m2`), and either `capacity_per_unit` (one item covers this much, so the count is rounded up) or `mode: continuous` (paid per m2 or per m).
4. Fill `capex_per_unit` and `lifetime_years` as `{low, high}`, with `price_basis` (incl. or excl. VAT, date read) and `source_ids`. Add the source to `sources` with its tier.
5. Add `energy.power_w_per_unit` if it uses power, and `footprint_m2_per_unit` if it stands on the floor.
6. Write the `trade_offs` in plain words: what you gain and what you give up.
7. Fill `price_reliability`: tier, source gate and reason, confidence and reason, corroboration.
8. Leave a number `null` if you don't have it. The configurator shows it as a gap. It never guesses.

Then run `python -m unittest tests.test_configure_system`. The catalog test checks the reliability fields and source ids.

## Add a species

Add an entry under `fish` or `plants` in `species_sizing_v0.json` with `canon_ref` pointing at its profile in `data/knowledge/species/`. A fish needs FCR, production per m3 of tank per year, harvest weight and survival. A plant needs yield per m2 per year (per architecture), feeding rate ratio, and planting density or heads per m2 per year.

## Add a region

A new country is data only. No code changes are needed, and `tests/test_multi_market.py` proves it with a stub third market.

1. Add a `locations.<name>` block in `unit_configuration_candidates_v0.json` with `currency_code`, `wage_per_hour` and `electricity_per_kwh`. Give each rate a `price_year` ({low, high}) and a `price_year_basis`.
2. Add parts and running inputs with that `region`, its `currency_code`, and a `market` block next to each price: `{"region", "currency_code", "price_year": {"low", "high"}, "price_year_basis": "stated_in_source" | "retail_listing_read_date" | "not_recorded" | "not_a_price"}`. Add `place` when the price comes from one city or utility but stands in for the whole region.
3. Run `python scripts/audit_market_tags.py`. It lists every price with its market and year, and flags anything untagged. A build refuses parts or prices in another currency, because no exchange rate is applied inside a build. Its report lists market flags (missing years, single-city prices) above the gaps.

## Compare swaps

`runs/swaps_basil_nl.json` and `runs/swaps_basil_karnataka.json` hold a base build and a list of `options`. Each option is a patch on the base: dicts merge, and lists and values replace. For example, `{"grow_architecture": "nft", "components": {"grow_unit": ["nft_channel_upvc_100x50_in"]}}` swaps the raft for NFT, and `{"heating": {"enabled": true, "source": "heat_pump"}, "components": {"heating": "heating_heat_pump_air_water_nl"}}` swaps gas for a heat pump. Every catalog alternative of each chosen part is added automatically. A new part with a price and life shows up as a swap with no other changes. The report marks a swap with (*) when it opens a cost gap.

## Reliability check (every new value)

Check the source and look for a second one. Tier 1 is peer-reviewed or official, tier 2 is research notes and extension packs, tier 3 is shop listings and anecdote. Tier 3 or single-source values stay candidate.

## Related Notes

- [[Project/Project|Project]]
- [[Learnings/Simulation Findings Log|Simulation Findings Log]]
