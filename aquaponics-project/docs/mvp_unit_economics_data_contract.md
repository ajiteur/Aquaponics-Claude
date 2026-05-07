# MVP Unit-Economics Data Contract

## 1. Purpose

This contract defines the data required to evaluate one bounded tilapia + basil
DWC/raft aquaponics unit for future commercial unit economics using real
measured data, explicitly supplied scenario data, or clearly labeled benchmark
assumptions.

This is a strategic/data-contract document only. It is not a product spec, not
an implementation plan, and not approval to calculate revenue, profitability,
total operating cost, commercial operability, fish/system safety, or basil
saleable harvest mass.

The contract exists to bridge:

- the current Mode A + P1 + P1.5 + P2a technical spine
- future benchmark scenario datasets
- future seed-demo reports
- later real-world unit-economics evaluation when observed or reviewed data is
  available

## 2. Relationship to the seed-goal reset

This contract implements the next step from
`docs/mvp_unit_economics_seed_goal_reset.md`:

1. unit-economics seed-goal reset
2. unit-economics data contract
3. benchmark scenario dataset
4. seed-demo report
5. later expert/customer validation when accessible

The contract supports pre-customer benchmark-backed proof discipline, but
benchmark scenarios must not be treated as customer validation, commercial
proof, or real-world operating proof.

## 3. Field classification system

Use these classifications in field definitions and later datasets:

- `measured`: observed directly from a meter, record, harvest, invoice, or
  operator log.
- `scenario_input`: explicitly supplied by the scenario author for a run.
- `benchmark_assumption`: sourced from public datasets, institutional reports,
  extension examples, supplier evidence, or benchmark systems.
- `derived`: calculated from allowed inputs after required inputs are present.
- `blocked_until_observed`: cannot be populated from proxy fields or benchmark
  assumptions.
- `optional`: useful but not required for the named output.
- `required`: required for the named output or field set.

Classifications may be combined, such as `scenario_input, required` or
`blocked_until_observed, required`.

## 4. Data readiness levels

| readiness_level | meaning | allowed use |
| --- | --- | --- |
| `L0_blocked_or_unavailable` | Missing, unresolved, or blocked by guardrail. | Keep null and explain the blocker. |
| `L1_scenario_input` | Manually supplied scenario value with no external source requirement. | Demo and what-if context only. |
| `L2_benchmark_assumption_with_source` | Public or supplier-backed benchmark value with metadata. | Benchmark scenario dataset and seed-demo context only. |
| `L3_measured_internal_or_pilot_data` | Internal measurement or pilot data, not yet customer/operator validated. | Internal evidence and later review. |
| `L4_observed_customer_or_operator_data` | Observed data from customer/operator setting. | Real-world evaluation input after provenance review. |
| `L5_reviewed_or_validated_commercial_data` | Reviewed commercial data suitable for decision support. | Future commercial evaluation, still scoped to evidence. |

Readiness level is not a claim strength shortcut. A field at `L2` can be useful
for benchmark scenarios, but it remains benchmark evidence, not validation.

## 5. Required metadata standard

Every field should carry or inherit this metadata:

- `unit`
- `source_basis`
- `date`
- `geography` where relevant
- `currency` where relevant
- measured/scenario/benchmark status
- `confidence`
- `notes`

For benchmark assumptions, metadata must also identify the source family,
applicability limits, and any context differences from the bounded tilapia +
basil DWC/raft unit.

For revenue-related future fields, metadata must include explicit quantity,
price, currency, date, geography, buyer/channel, sale unit, and
actual-versus-scenario status before any future revenue calculation is allowed.

## 6. Field table format

Every field table in this contract uses these columns:

| field_name | category | required_for | classification | readiness_level | unit | source_basis | data_status | metadata_required | validation_rule | allowed_to_derive | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`allowed_to_derive` means the field itself may be derived. It does not mean the
field may be inferred from unrelated proxies.

## 7. Biological and fish/feed inputs

| field_name | category | required_for | classification | readiness_level | unit | source_basis | data_status | metadata_required | validation_rule | allowed_to_derive | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `fish_species` | biological_fish_feed | benchmark dataset, real-world report | scenario_input or benchmark_assumption, required | L1-L4 | species id/name | scenario, benchmark source, or observed stock record | explicit | unit, source_basis, date, geography, status, confidence, notes | non-empty; context must match tilapia scope | no | yes for unit-specific evaluation | Do not use species alone to claim safety or yield. |
| `fish_count` | biological_fish_feed | benchmark dataset, real-world report | measured or scenario_input or benchmark_assumption, optional for current demo | L1-L4 | fish | stocking record or benchmark assumption | explicit | unit, source_basis, date, status, confidence, notes | non-negative integer | no | no for current demo; yes for population economics | Needed for stocking and mortality context. |
| `average_fish_weight_kg` | biological_fish_feed | benchmark dataset, real-world report | measured or scenario_input or benchmark_assumption, optional | L1-L4 | kg/fish | scale record or benchmark assumption | explicit | unit, source_basis, date, status, confidence, notes | non-negative number | no | no for current Mode A | Do not derive feed from this in Mode A unless a later Mode B pass is approved. |
| `fish_biomass_kg` | biological_fish_feed | benchmark dataset, future real-world report | measured or benchmark_assumption, optional | L1-L4 | kg | stocking/weight record or benchmark assumption | explicit or derived from count and weight if both explicit | unit, source_basis, date, status, confidence, notes | non-negative number; if derived, count and average weight must be explicit | yes, from explicit count * explicit weight only | no for current Mode A | Not a source for basil saleable harvest. |
| `feed_kg_day` | biological_fish_feed | current demo, benchmark dataset, seed-demo report | scenario_input, required | L1-L4 | kg/day | scenario input, operator log, or benchmark assumption | explicit | unit, source_basis, date, status, confidence, notes | non-negative number | no | yes for Mode A load path | Current Mode A root input. |
| `protein_fraction` | biological_fish_feed | current demo, benchmark dataset, seed-demo report | scenario_input, required | L1-L4 | fraction | feed label, scenario, or benchmark source | explicit | unit, source_basis, date, status, confidence, notes | 0 to 1 inclusive | no | yes for Mode A load path | Current load calculation input. |
| `feed_class` | biological_fish_feed | current demo context, benchmark dataset | scenario_input or benchmark_assumption, optional | L1-L4 | label | scenario or feed record | explicit | source_basis, date, status, confidence, notes | non-empty if supplied | no | no | Context only. |
| `fcr_if_used` | biological_fish_feed | future benchmark or real-world evaluation | scenario_input or benchmark_assumption or measured, optional | L1-L5 | kg feed/kg gain | source record or benchmark | explicit | unit, source_basis, date, geography, status, confidence, notes | positive number if supplied | no | no for current Mode A | Do not use to replace Mode A without approval. |
| `mortality_count` | biological_fish_feed | future real-world unit economics | measured or benchmark_assumption, optional until fish outputs exist | L0-L5 | fish | operator log, pilot data, benchmark assumption | explicit | unit, source_basis, date, status, confidence, notes | non-negative integer | no | yes for mortality-adjusted fish output | Must stay separate from safety claims. |

## 8. Water-quality inputs

| field_name | category | required_for | classification | readiness_level | unit | source_basis | data_status | metadata_required | validation_rule | allowed_to_derive | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `fish_tank_volume_l` | water_quality | P1 context, benchmark dataset | scenario_input or measured, required for P1 concentration context | L1-L4 | L | scenario, system record, or measurement | explicit | unit, source_basis, date, status, confidence, notes | positive number | no | yes for TAN-N concentration context | Current P1 uses effective water volume, not whole-system proof. |
| `total_system_volume_l` | water_quality | future real-world report | measured or benchmark_assumption, optional | L1-L4 | L | system record or benchmark | explicit | unit, source_basis, date, status, confidence, notes | positive number if supplied | no | no for current demo | Context; not a substitute for concentration scope. |
| `accumulation_period_day` | water_quality | P1 context, benchmark dataset | scenario_input, required for P1 concentration context | L1-L4 | day | scenario or operating record | explicit | unit, source_basis, date, status, confidence, notes | positive number | no | yes for TAN-N concentration context | Defines accumulation basis only. |
| `concentration_scope` | water_quality | P1 context | scenario_input, required | L1-L4 | label | scenario or measurement protocol | explicit | source_basis, date, status, confidence, notes | allowed scope must be explicit | no | yes for P1 context | Current first helper supports fish-tank scope. |
| `ph` | water_quality | P1 NH3 chemistry context | measured or scenario_input or benchmark_assumption, required for NH3 context | L1-L4 | pH | meter record, scenario, or benchmark | explicit | unit, source_basis, date, status, confidence, notes | 0 to 14 inclusive | no | yes for NH3 chemistry context | Does not imply safety. |
| `water_temp_c` | water_quality | P1 NH3 chemistry context | measured or scenario_input or benchmark_assumption, required for NH3 context | L1-L4 | deg C | thermometer record, scenario, or benchmark | explicit | unit, source_basis, date, status, confidence, notes | finite number in plausible water range | no | yes for NH3 chemistry context | Does not imply safety. |
| `measured_do_mg_l` | water_quality | P1.5 context | measured or scenario_input or benchmark_assumption, optional | L1-L4 | mg/L | meter record, scenario, or benchmark | explicit | unit, source_basis, date, status, confidence, notes | non-negative number | no | no | Context only; not aeration adequacy or future safety proof. |
| `alkalinity_mg_l_as_caco3` | water_quality | future real-world report | measured or benchmark_assumption, optional | L1-L4 | mg CaCO3/L | test record or benchmark | explicit | unit, source_basis, date, status, confidence, notes | non-negative number if supplied | no | no for current demo | Separate from derived alkalinity demand. |
| `water_replacement_or_exchange_l_day` | water_quality | future real-world report | measured or scenario_input or benchmark_assumption, optional | L1-L4 | L/day | meter/log/benchmark | explicit | unit, source_basis, date, status, confidence, notes | non-negative number | no | no for current demo | Needed later for water cost and dilution context. |
| `freshwater_or_salinity_assumption` | water_quality | P1 NH3 context, benchmark dataset | scenario_input or measured, required for current freshwater chemistry | L1-L4 | label or ppt | scenario, meter, or benchmark | explicit | unit if numeric, source_basis, date, status, confidence, notes | explicit freshwater boolean or salinity value | no | yes for current NH3 context | Do not hide salinity assumptions. |
| `biofilter_state` | water_quality | future real-world report | measured or benchmark_assumption, optional | L0-L4 | label | operator record or benchmark | explicit | source_basis, date, status, confidence, notes | label must state observed, assumed, or unknown | no | no for current demo | Context only; not a safety verdict. |

## 9. Engineering and equipment inputs

| field_name | category | required_for | classification | readiness_level | unit | source_basis | data_status | metadata_required | validation_rule | allowed_to_derive | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `pump_records` | engineering_equipment | P2a power cost, benchmark dataset | scenario_input or measured or benchmark_assumption, required if pump power is costed | L1-L4 | record list | scenario, equipment log, supplier spec, or benchmark | explicit | source_basis, date, geography, status, confidence, notes | each record must name device, role, kW, runtime, and basis | no | yes for pump power cost | Record list, not a safety claim. |
| `blower_or_aeration_records` | engineering_equipment | P2a power cost, P1.5 context | scenario_input or measured or benchmark_assumption, required if aeration power is costed | L1-L4 | record list | scenario, equipment log, supplier spec, or benchmark | explicit | source_basis, date, geography, status, confidence, notes | each record must name device, role, kW, runtime, and basis | no | yes for aeration power cost | Does not prove aeration adequacy. |
| `device_kw` | engineering_equipment | P2a power cost | scenario_input or measured or benchmark_assumption, required per device | L1-L4 | kW | nameplate, meter, supplier spec, or benchmark | explicit | unit, source_basis, date, status, confidence, notes | non-negative number | no | yes for power kWh/day | Must state nameplate vs measured basis. |
| `runtime_h_day` | engineering_equipment | P2a power cost | scenario_input or measured or benchmark_assumption, required per device | L1-L4 | h/day | timer, operator log, scenario, or benchmark | explicit | unit, source_basis, date, status, confidence, notes | 0 to 24 inclusive per day | no | yes for power kWh/day | Use duty cycle status if not continuous. |
| `power_basis` | engineering_equipment | P2a power cost | scenario_input or measured, required | L1-L4 | label | meter, nameplate, supplier spec, or scenario | explicit | source_basis, date, status, confidence, notes | one of measured, nameplate, duty_cycle, estimated, benchmark | no | yes for seed-demo transparency | Required to avoid fake precision. |
| `backup_power_status` | engineering_equipment | future real-world risk/cost | measured or scenario_input or benchmark_assumption, optional | L0-L4 | label | operator record, design record, or benchmark | explicit | source_basis, date, status, confidence, notes | label must state present, absent, unknown, or scenario | no | no for current P2a | Do not convert to safety or reliability proof. |
| `dwc_root_zone_aeration_status` | engineering_equipment | P1.5 context, future report | measured or scenario_input or benchmark_assumption, optional | L0-L4 | label | design record, operator record, or benchmark | explicit | source_basis, date, status, confidence, notes | label must state observed, assumed, absent, or unknown | no | no for current demo | Context only. |
| `filter_or_clarifier_type` | engineering_equipment | future solids/labor context | scenario_input or measured or benchmark_assumption, optional | L1-L4 | label | design record or benchmark | explicit | source_basis, date, status, confidence, notes | non-empty if supplied | no | no for current demo | Does not prove solids-removal capacity. |
| `solids_removal_schedule` | engineering_equipment | future labor/maintenance | measured or scenario_input or benchmark_assumption, optional | L1-L4 | schedule | operator log, SOP, or benchmark | explicit | unit/frequency, source_basis, date, status, confidence, notes | frequency and basis must be explicit | no | no for current demo | Needed before labor/cost claims. |

## 10. Operating-cost inputs

| field_name | category | required_for | classification | readiness_level | unit | source_basis | data_status | metadata_required | validation_rule | allowed_to_derive | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `feed_price_per_kg` | operating_cost | P2a feed cost, benchmark dataset | scenario_input or benchmark_assumption or measured, required if feed cost is calculated | L1-L5 | currency/kg | supplier quote, invoice, scenario, or benchmark | explicit | unit, currency, source_basis, date, geography, status, confidence, notes | non-negative number with currency | no | yes for feed cost | Scenario or benchmark price is not canon. |
| `electricity_price_per_kwh` | operating_cost | P2a power cost, benchmark dataset | scenario_input or benchmark_assumption or measured, required if power cost is calculated | L1-L5 | currency/kWh | tariff, invoice, scenario, or benchmark | explicit | unit, currency, source_basis, date, geography, status, confidence, notes | non-negative number with currency | no | yes for power cost | Scenario or benchmark tariff is not canon. |
| `buffer_material_price` | operating_cost | future operating cost | scenario_input or benchmark_assumption or measured, optional | L0-L5 | currency/unit | supplier quote, invoice, or benchmark | explicit | unit, currency, source_basis, date, geography, status, confidence, notes | non-negative number with unit and currency | no | no for current P2a | Future field only; no current total cost. |
| `water_tariff` | operating_cost | future operating cost | scenario_input or benchmark_assumption or measured, optional | L0-L5 | currency/m3 or currency/L | tariff, invoice, scenario, or benchmark | explicit | unit, currency, source_basis, date, geography, status, confidence, notes | non-negative number with unit and currency | no | no for current P2a | Requires water-use field before cost. |
| `discharge_cost` | operating_cost | future operating cost | scenario_input or benchmark_assumption or measured, optional | L0-L5 | currency/unit | tariff, invoice, scenario, or benchmark | explicit | unit, currency, source_basis, date, geography, status, confidence, notes | non-negative number with unit and currency | no | no for current P2a | Keep separate from water tariff. |
| `labor_rate` | operating_cost | labor cost, future unit economics | scenario_input or benchmark_assumption or measured, optional until labor is included | L0-L5 | currency/hour | wage record, scenario, or benchmark | explicit | unit, currency, source_basis, date, geography, status, confidence, notes | non-negative number with currency | no | yes if labor cost is claimed | May also appear in labor table; use one source basis. |
| `disposal_fees` | operating_cost | future operating cost | scenario_input or benchmark_assumption or measured, optional | L0-L5 | currency/unit | invoice, tariff, scenario, or benchmark | explicit | unit, currency, source_basis, date, geography, status, confidence, notes | non-negative number with unit and currency | no | no for current P2a | Future field only. |

## 11. Labor and maintenance inputs

| field_name | category | required_for | classification | readiness_level | unit | source_basis | data_status | metadata_required | validation_rule | allowed_to_derive | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `clarifier_purge_frequency` | labor_maintenance | future labor/maintenance cost | measured or scenario_input or benchmark_assumption, optional | L0-L5 | events/day or schedule | operator log, SOP, scenario, or benchmark | explicit | unit, source_basis, date, status, confidence, notes | non-negative frequency or explicit schedule | no | no for current demo | Requires task hours before labor cost. |
| `filter_cleaning_frequency` | labor_maintenance | future labor/maintenance cost | measured or scenario_input or benchmark_assumption, optional | L0-L5 | events/day or schedule | operator log, SOP, scenario, or benchmark | explicit | unit, source_basis, date, status, confidence, notes | non-negative frequency or explicit schedule | no | no for current demo | Keep separate from solids capacity. |
| `task_hours_per_event` | labor_maintenance | future labor cost | measured or scenario_input or benchmark_assumption, required if labor cost is calculated | L0-L5 | hours/event | time log, scenario, or benchmark | explicit | unit, source_basis, date, status, confidence, notes | non-negative number | no | yes if labor cost is claimed | Must name task type. |
| `labor_rate` | labor_maintenance | future labor cost | measured or scenario_input or benchmark_assumption, required if labor cost is calculated | L0-L5 | currency/hour | wage record, scenario, or benchmark | explicit | unit, currency, source_basis, date, geography, status, confidence, notes | non-negative number with currency | no | yes if labor cost is claimed | Same economic input as operating-cost labor rate. |
| `maintenance_notes` | labor_maintenance | seed-demo context, future real-world report | measured or scenario_input or benchmark_assumption, optional | L0-L5 | text | operator note, SOP, scenario, or benchmark | explicit | source_basis, date, status, confidence, notes | text must state source and status | no | no | Qualitative context only. |

## 12. Fish output inputs

| field_name | category | required_for | classification | readiness_level | unit | source_basis | data_status | metadata_required | validation_rule | allowed_to_derive | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `fish_harvest_date` | fish_output | future fish revenue, real-world report | measured or scenario_input or benchmark_assumption, required if fish revenue is calculated | L0-L5 | date | harvest record, scenario, or benchmark | explicit | unit, source_basis, date, status, confidence, notes | valid date | no | yes for fish revenue timing | Date alone does not imply sale. |
| `harvested_fish_count` | fish_output | future fish output | measured or scenario_input or benchmark_assumption, optional depending sale unit | L0-L5 | fish | harvest record, scenario, or benchmark | explicit | unit, source_basis, date, status, confidence, notes | non-negative integer | no | yes if fish sale unit is count | Keep separate from stocked count. |
| `harvested_fish_mass_kg` | fish_output | future fish revenue | measured or scenario_input or benchmark_assumption, required if fish is sold by kg | L0-L5 | kg | scale record, scenario, or benchmark | explicit | unit, source_basis, date, status, confidence, notes | non-negative number | no | yes if fish sale unit is kg | Must state live/whole/processed basis. |
| `fish_mortalities` | fish_output | future unit economics | measured or benchmark_assumption, optional until risk/mortality used | L0-L5 | fish or kg | mortality log or benchmark | explicit | unit, source_basis, date, status, confidence, notes | non-negative; basis must be count or mass | no | yes for mortality-adjusted output | Not a safety claim. |
| `rejected_or_downgraded_fish` | fish_output | future fish revenue/risk | measured or benchmark_assumption, optional | L0-L5 | fish or kg | harvest/QA record or benchmark | explicit | unit, source_basis, date, status, confidence, notes | non-negative; reason labels explicit if supplied | no | no until fish revenue uses grades | Do not price as first-quality output without explicit status. |
| `fish_sale_price` | fish_output | future fish revenue | scenario_input or benchmark_assumption or measured, required if fish revenue is calculated | L0-L5 | currency/sale unit | invoice, quote, scenario, or benchmark | explicit | unit, currency, source_basis, date, geography, buyer/channel, status, confidence, notes | non-negative number with sale unit and currency | no | yes for fish revenue | Future input only; no current revenue claim. |
| `fish_buyer_channel` | fish_output | future fish revenue | scenario_input or benchmark_assumption or measured, required if fish revenue is calculated | L0-L5 | label | buyer record, scenario, or benchmark | explicit | source_basis, date, geography, status, confidence, notes | non-empty if fish revenue is calculated | no | yes for fish revenue | Needed to avoid generic price claims. |

## 13. Basil output inputs

| field_name | category | required_for | classification | readiness_level | unit | source_basis | data_status | metadata_required | validation_rule | allowed_to_derive | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `planted_area_m2_or_site_count` | basil_output | future basil context, benchmark dataset | measured or scenario_input or benchmark_assumption, optional | L0-L5 | m2 or sites | planting record, scenario, or benchmark | explicit | unit, source_basis, date, status, confidence, notes | non-negative number with basis | no | no for current MVP | Context only; not saleable mass. |
| `basil_harvest_date` | basil_output | future basil revenue | measured or scenario_input or benchmark_assumption, required if basil revenue is calculated | L0-L5 | date | harvest record, scenario, or benchmark | explicit | unit, source_basis, date, status, confidence, notes | valid date | no | yes for basil revenue timing | Date alone does not imply sale. |
| `gross_harvested_basil_mass_kg` | basil_output | future harvest review | measured or scenario_input or benchmark_assumption, optional | L0-L5 | kg | scale record, scenario, or benchmark | explicit | unit, source_basis, date, status, confidence, notes | non-negative number | no | no for current MVP | Must not be treated as saleable mass. |
| `observed_saleable_harvest_mass_kg` | basil_output | future saleable harvest source | measured or reviewed, required before basil revenue | L0, L3-L5 | kg | observed acceptance, QA review, buyer acceptance, or reviewed manual input | blocked unless observed/reviewed | unit, source_basis, date, geography, buyer/channel if relevant, status, confidence, notes | non-negative number only when observed or reviewed | no | yes for basil revenue | May later source `saleable_harvest_mass_kg`; no proxy inference. |
| `saleable_harvest_mass_kg` | basil_output | business-required basil kg revenue field | blocked_until_observed, required | L0 until observed/reviewed; L3-L5 after approval | kg | observed runtime output or explicit reviewed manual input only | null/unresolved until backed | unit, source_basis, date, geography, buyer/channel if relevant, status, confidence, notes | must remain null unless backed by observed/reviewed source | no | yes for basil revenue | Null means unresolved, not zero. |
| `rejected_or_cull_basil_mass_kg` | basil_output | future basil review/risk | measured or reviewed or benchmark_assumption, optional | L0-L5 | kg | QA record, harvest record, scenario, or benchmark | explicit if supplied | unit, source_basis, date, status, confidence, notes | non-negative number | no | no unless cull economics are claimed | Must not be inferred from gross minus saleable unless both are explicit and same lot. |
| `basil_rejection_reasons` | basil_output | future QA/review context | measured or reviewed, optional | L0-L5 | label list | QA record, buyer feedback, reviewed manual input | explicit if supplied | source_basis, date, status, confidence, notes | labels must be reviewed/observed, not automatic | no | no | Ontology labels are review context, not calculations. |
| `basil_sale_price` | basil_output | future basil revenue | scenario_input or benchmark_assumption or measured, required if basil revenue is calculated | L0-L5 | currency/sale unit | invoice, quote, scenario, or benchmark | explicit | unit, currency, source_basis, date, geography, buyer/channel, status, confidence, notes | non-negative number with sale unit and currency | no | yes for basil revenue | Future input only; no current revenue claim. |
| `basil_buyer_channel` | basil_output | future basil revenue | scenario_input or benchmark_assumption or measured, required if basil revenue is calculated | L0-L5 | label | buyer record, scenario, or benchmark | explicit | source_basis, date, geography, status, confidence, notes | non-empty if basil revenue is calculated | no | yes for basil revenue | Needed to avoid generic price claims. |

## 14. Revenue inputs

Revenue inputs are future contract fields only. They do not authorize current
revenue, projected revenue, profitability, commercial operability, or economic
viability claims.

| field_name | category | required_for | classification | readiness_level | unit | source_basis | data_status | metadata_required | validation_rule | allowed_to_derive | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `fish_revenue_quantity` | revenue_input | future fish revenue | measured or scenario_input or benchmark_assumption, required | L0-L5 | kg, fish, or sale unit | harvest/sale record, scenario, or benchmark | explicit | unit, source_basis, date, geography, buyer/channel, status, confidence, notes | non-negative; sale unit must match price unit | no | yes for fish revenue | Must identify live, whole, or processed basis if by mass. |
| `fish_sale_price` | revenue_input | future fish revenue | measured or scenario_input or benchmark_assumption, required | L0-L5 | currency/sale unit | invoice, quote, scenario, or benchmark | explicit | unit, currency, source_basis, date, geography, buyer/channel, status, confidence, notes | non-negative with currency and sale unit | no | yes for fish revenue | Benchmark price must remain benchmark-labeled. |
| `basil_revenue_quantity` | revenue_input | future basil revenue | blocked_until_observed or scenario_input with explicit status, required | L0-L5 | kg or sale unit | observed/reviewed saleable mass, sale record, scenario, or benchmark | explicit or blocked | unit, source_basis, date, geography, buyer/channel, status, confidence, notes | must not be inferred from gross mass, plant count, or biomass | no | yes for basil revenue | Actual basil revenue requires observed/reviewed saleable quantity. |
| `basil_sale_price` | revenue_input | future basil revenue | measured or scenario_input or benchmark_assumption, required | L0-L5 | currency/sale unit | invoice, quote, scenario, or benchmark | explicit | unit, currency, source_basis, date, geography, buyer/channel, status, confidence, notes | non-negative with currency and sale unit | no | yes for basil revenue | Benchmark price must remain benchmark-labeled. |
| `sale_unit` | revenue_input | future revenue | measured or scenario_input or benchmark_assumption, required | L0-L5 | label | invoice, quote, scenario, or benchmark | explicit | unit, source_basis, date, geography, status, confidence, notes | unit must match quantity and price | no | yes for any revenue calculation | Examples: kg, fish, bunch, tray, batch. |
| `currency` | revenue_input | future revenue | measured or scenario_input or benchmark_assumption, required | L0-L5 | ISO/code label | invoice, quote, scenario, tariff, or benchmark | explicit | currency, source_basis, date, geography, status, confidence, notes | all combined money fields must share currency or state conversion basis | no | yes for revenue and cost comparisons | No silent currency mixing. |
| `price_date` | revenue_input | future revenue | measured or scenario_input or benchmark_assumption, required | L0-L5 | date | invoice, quote, scenario, or benchmark | explicit | date, source_basis, geography, status, confidence, notes | valid date | no | yes for revenue | Needed for price relevance. |
| `price_geography` | revenue_input | future revenue | measured or scenario_input or benchmark_assumption, required | L0-L5 | label | invoice, quote, scenario, or benchmark | explicit | geography, source_basis, date, status, confidence, notes | non-empty if revenue is calculated | no | yes for revenue | Avoids generic market claims. |
| `buyer_channel` | revenue_input | future revenue | measured or scenario_input or benchmark_assumption, required | L0-L5 | label | buyer record, channel assumption, scenario, or benchmark | explicit | source_basis, date, geography, status, confidence, notes | non-empty if revenue is calculated | no | yes for revenue | Channel-specific pricing must stay explicit. |
| `actual_vs_scenario_status` | revenue_input | future revenue | measured or scenario_input or benchmark_assumption, required | L0-L5 | label | sale record, scenario metadata, or benchmark metadata | explicit | source_basis, date, status, confidence, notes | must be actual_sale, scenario_input, benchmark_assumption, or reviewed_manual | no | yes for any revenue output | Prevents benchmark revenue from sounding actual. |

## 15. Derived outputs allowed later

These outputs may be calculated later only when their required inputs exist and
the output label preserves its status. This section does not implement or
authorize new calculations.

| field_name | category | required_for | classification | readiness_level | unit | source_basis | data_status | metadata_required | validation_rule | allowed_to_derive | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `tan_n_load` | derived_output | current demo | derived, required | L1-L4 from inputs | kg/day or g/day | explicit `feed_kg_day` and `protein_fraction` | available in current MVP | unit, source_basis, date, status, confidence, notes | requires feed and protein inputs | yes | yes for Mode A loads | TAN-N load, not concentration or safety. |
| `tan_n_concentration_context` | derived_output | P1 context | derived, optional outside P1 | L1-L4 from inputs | mg/L | TAN-N load, volume, period, scope | available when complete inputs exist | unit, source_basis, date, status, confidence, notes | requires complete P1 group | yes | yes for P1 context | Fish-tank context only. |
| `nh3_chemistry_context` | derived_output | P1 context | derived, optional outside P1 | L1-L4 from inputs | fraction, mg/L | TAN-N concentration, pH, temperature, freshwater/salinity basis | available when complete inputs exist | unit, source_basis, date, status, confidence, notes | requires complete chemistry inputs | yes | yes for NH3 context | Not toxicity or safety. |
| `nitrification_oxygen_demand` | derived_output | current demo, P1.5 context | derived, required for current loads | L1-L4 from inputs | g/day | TAN-N load and basis factor | available in current MVP | unit, source_basis, date, status, confidence, notes | requires TAN-N load | yes | yes for current loads | Not aeration capacity or total oxygen demand. |
| `alkalinity_demand` | derived_output | current demo | derived, required for current loads | L1-L4 from inputs | g CaCO3/day | TAN-N load and basis factor | available in current MVP | unit, source_basis, date, status, confidence, notes | requires TAN-N load | yes | yes for current loads | Demand context only. |
| `dry_solids_potential` | derived_output | P1.5 context | derived, optional | L1-L4 from inputs | kg/day | feed and explicit dry-solids coefficient | available when supplied | unit, source_basis, date, status, confidence, notes | requires feed and coefficient | yes | no for current demo | Not wet sludge, TSS, or removal capacity. |
| `selected_operating_cost_pressure` | derived_output | P2a context | derived, optional | L1-L5 from explicit cost inputs | currency/day | explicit feed and/or power cost inputs | available when supplied money fields share currency | unit, currency, source_basis, date, geography, status, confidence, notes | requires explicit selected cost categories and compatible currency | yes | no for current load path | Not total operating cost or profitability. |
| `fish_revenue` | derived_output | future report only | derived, blocked until explicit revenue inputs | L0 until required inputs; L1-L5 after status-labeled inputs | currency/period | explicit fish quantity, price, currency, date, geography, buyer/channel, status | blocked now | unit, currency, source_basis, date, geography, buyer/channel, status, confidence, notes | requires complete fish revenue input set | yes, later only | yes | No current revenue claim; benchmark output must be labeled benchmark scenario. |
| `basil_revenue` | derived_output | future report only | derived, blocked until explicit saleable quantity and price inputs | L0 until observed/reviewed or explicitly status-labeled scenario inputs | currency/period | explicit saleable quantity, price, currency, date, geography, buyer/channel, status | blocked now | unit, currency, source_basis, date, geography, buyer/channel, status, confidence, notes | requires saleable quantity not inferred from proxies | yes, later only | yes | Actual basil revenue requires observed/reviewed saleable mass. |
| `unit_economics_scenario_outputs` | derived_output | future scenario report | derived, blocked until complete-enough status-labeled inputs | L0 until contract fields complete | mixed | explicit cost, revenue, labor, utilization, risk, and status labels | blocked now | unit, currency, source_basis, date, geography, status, confidence, notes | must expose nulls and missing inputs | yes, later only | yes | Must not imply profitability or commercial operability without approved scope. |

## 16. Blocked outputs and claims

These outputs and claims remain blocked in the current MVP:

- `saleable_harvest_mass_kg` unless backed by observed runtime output or
  explicit reviewed manual input
- fish safety
- system safety
- aeration adequacy
- total oxygen demand
- total operating cost
- profitability
- commercial operability
- customer validation
- benchmark scenario as customer validation
- benchmark scenario as commercial proof
- benchmark scenario as real-world operating proof

If a later dataset contains benchmark quantities or benchmark prices, any
derived money output must be explicitly labeled as benchmark scenario output.
It must not be described as actual revenue, projected revenue, profitability, or
economic viability.

## 17. Minimum field set: current technical demo

Minimum fields for the current four-level technical demo:

- Mode A: `scenario_id`, `input_mode`, `feed_kg_day`, `protein_fraction`,
  `feed_class`, `architecture_context`
- P1: `effective_water_volume_l`, `accumulation_period_day`,
  `concentration_scope`, `ph`, `water_temp_c`, `freshwater_assumption`
- P1.5: `include_aeration_solids_context`, `measured_do_mg_l`,
  `dry_solids_coefficient`, `dry_solids_basis`, and context-availability flags
- P2a: `include_operating_cost_pressure`, `feed_price_per_kg`,
  `feed_price_currency`, `feed_price_date`, `feed_price_geography`,
  `feed_price_source_type`, `electricity_price_per_kwh`,
  `electricity_price_currency`, `electricity_tariff_date`,
  `electricity_price_geography`, `electricity_tariff_class`,
  `electricity_tariff_source_type`, and `equipment_power_records`

This field set supports the current technical demo only. It does not support
revenue, profitability, total operating cost, safety, commercial operability, or
saleable basil harvest claims.

## 18. Minimum field set: benchmark scenario dataset

Minimum fields for a benchmark scenario dataset:

- scenario identity: `scenario_id`, `scenario_name`, `benchmark_version`,
  `architecture_context`, `system_type`, `crop_species`, `fish_species`
- source metadata: source family, source title/reference, source date,
  geography, applicability notes, confidence, and benchmark status
- Mode A/P1/P1.5/P2a fields listed in the current technical demo minimum set
- benchmark-specific context: fish count or biomass where sourced, planted
  area or site count where sourced, and benchmark scale notes
- cost metadata: feed price, electricity tariff, currency, geography, date, and
  source basis
- explicit null/blocked fields: `saleable_harvest_mass_kg: null` unless
  observed/reviewed; revenue fields absent or null unless explicitly supplied
  with benchmark status labels
- blocked-claim flags: no customer validation, no commercial proof, no
  real-world operating proof

Benchmark datasets may support seed-demo credibility and gap analysis. They are
not canon and not field validation.

## 19. Minimum viable benchmark dataset fields

Smallest field set for `uvi_like_tilapia_basil_dwc_raft_benchmark_v0`:

- `scenario_id: uvi_like_tilapia_basil_dwc_raft_benchmark_v0`
- `scenario_name`
- `benchmark_status: benchmark_assumption_with_source`
- `readiness_level: L2_benchmark_assumption_with_source`
- `architecture_context: tilapia_basil_dwc_raft`
- `system_type: coupled_aquaponics_dwc_or_raft_benchmark`
- `fish_species`
- `crop_species: basil`
- `product_form_scope: basil_bulk_kg_wholesale_context_or_unresolved`
- `source_family`
- `source_reference`
- `source_date_or_access_date`
- `source_geography`
- `applicability_notes`
- `confidence`
- `feed_kg_day`
- `protein_fraction`
- `feed_class`
- `effective_water_volume_l`
- `accumulation_period_day`
- `concentration_scope`
- `ph`
- `water_temp_c`
- `freshwater_assumption`
- `measured_do_mg_l` or `do_context_status`
- `dry_solids_coefficient`
- `dry_solids_basis: benchmark_assumption_not_canon`
- `feed_price_per_kg`
- `feed_price_currency`
- `feed_price_date`
- `feed_price_geography`
- `feed_price_source_type`
- `electricity_price_per_kwh`
- `electricity_price_currency`
- `electricity_tariff_date`
- `electricity_price_geography`
- `electricity_tariff_source_type`
- `equipment_power_records`
- `saleable_harvest_mass_kg: null`
- `saleable_harvest_mass_status: blocked_until_observed_or_reviewed`
- `revenue_status: not_calculated`
- `profitability_status: not_calculated`
- `commercial_operability_status: not_claimed`
- `customer_validation_status: not_customer_validated`

Optional but useful if public evidence supports it:

- `fish_count`
- `average_fish_weight_kg`
- `fish_biomass_kg`
- `planted_area_m2_or_site_count`
- `filter_or_clarifier_type`
- `solids_removal_schedule`

The benchmark remains a scenario dataset even if every value is sourced.

## 20. Minimum field set: seed-demo report

Minimum fields for a seed-demo report:

- current technical demo input set and outputs
- integrity snapshot result and commit reference
- benchmark scenario dataset identifier and source metadata
- readiness level for each major field group
- gap map for missing real-world fields
- explicit null status for `saleable_harvest_mass_kg`
- selected cost pressure as selected cost pressure only
- blocked-claim section: no safety, no total operating cost, no revenue, no
  profitability, no commercial operability, no customer validation
- next data needed before unit-economics evaluation

The seed-demo report may show a disciplined pathway to evaluation. It must not
claim that evaluation is complete.

## 21. Minimum field set: future real-world unit-economics report

Minimum fields for a future real-world unit-economics report:

- observed run identity, time basis, and operating period
- measured or reviewed feed, water, equipment, labor, harvest, cost, and price
  inputs
- fish harvest quantity, sale unit, sale price, currency, date, geography, and
  buyer/channel
- basil observed/reviewed saleable quantity, sale unit, sale price, currency,
  date, geography, and buyer/channel
- cull/rejection/mortality records where they affect revenue or cost
- labor task records and labor rate
- energy records, water use, supplements, packaging, disposal, and other
  selected cost records
- CAPEX/useful-life/utilization fields if payback or asset intensity is in
  scope
- risk/event records if risk-adjusted outputs are in scope
- explicit actual-versus-scenario status for every quantity and price
- null propagation for any missing required field

Even this future report must keep claims scoped to the data supplied and review
state. It should not imply universal commercial operability.

## 22. Scenario assumptions versus canon

Keep these scenario-based, not canon, unless a later explicit canon pass
approves otherwise:

- benchmark feed amount, protein fraction, fish count, biomass, water volume,
  pH, temperature, DO, and dry-solids coefficient
- feed and electricity prices used in demo or benchmark scenarios
- equipment kW, runtime, and power basis when sourced from a scenario or
  benchmark
- labor rates, task hours, water tariffs, discharge costs, buffer prices, and
  disposal fees
- benchmark yields, fish harvest quantities, basil harvest quantities, prices,
  utilization, CAPEX, risk penalties, and loss rates
- UVI/SRAC/FAO/extension-derived values adapted to the bounded unit
- supplier quotes and manually created scenario records

Scenario assumptions may be used for transparent sensitivity or benchmark
context. They must not be promoted into canonical biology, canonical business
truth, runtime truth, or customer validation by implication.

## 23. Validation checks for future implementation

For a later data-contract implementation or schema pass, validate:

- only explicitly allowed files changed
- no `configs/**`, `data/knowledge/**`, `data/simulation/**`, `src/**`,
  `scripts/**`, `tests/**`, ontology, or knowledge-vault files changed unless
  the user explicitly allowed that exact scope
- required metadata fields exist for every numeric or money field
- every field has a classification and readiness level
- benchmark fields are labeled `benchmark_assumption` and do not claim customer
  validation, commercial proof, or real-world operating proof
- `saleable_harvest_mass_kg` remains null unless observed or explicitly
  reviewed
- gross, modeled, observed saleable, and rejected basil masses remain separate
- revenue outputs require explicit quantity, price, currency, date, geography,
  buyer/channel, and actual-versus-scenario status
- profitability and commercial operability remain blocked unless a later pass
  explicitly approves the complete required input set and output scope
- selected operating-cost pressure is not renamed or treated as total operating
  cost
- missing required inputs propagate nulls and missing-input explanations
- `python scripts/check_mvp_integrity.py --quick` passes at minimum; use full
  integrity before external-facing report use

## 24. Recommended next action

Create a docs-only benchmark scenario dataset design for
`uvi_like_tilapia_basil_dwc_raft_benchmark_v0`. The design should populate no
values yet unless the user explicitly requests a sourced dataset pass. It should
define record shape, source metadata, readiness labels, blocked-claim fields,
and the gap map needed for a later seed-demo report.
