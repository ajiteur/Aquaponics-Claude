# MVP Benchmark Scenario Dataset Design

## 1. Purpose

This document designs the first benchmark scenario dataset for the pre-customer
Aquaponics MVP proof path.

The dataset design is for:

- showing how the current Mode A + P1 + P1.5 + P2a spine can accept a
  source-backed benchmark scenario
- making source metadata, readiness, uncertainty, and blocked claims explicit
- preparing a later seed-demo report

This pass does not create JSON or data files. It does not implement
calculations. It does not promote benchmark assumptions into canon.

## 2. Relationship to seed-goal reset and data contract

This design follows the current pathway:

1. unit-economics seed-goal reset
2. unit-economics data contract
3. benchmark scenario dataset
4. seed-demo report
5. later expert/customer validation when accessible

Use `docs/mvp_unit_economics_seed_goal_reset.md` for the strategic boundary and
`docs/mvp_unit_economics_data_contract.md` for field classifications, metadata,
readiness levels, minimum field sets, and blocked outputs.

This benchmark design supports pre-customer evidence-backed demo credibility
only. It is not customer validation, commercial proof, real-world operating
proof, or canonical truth.

## 3. Benchmark scenario name and role

Scenario name:

`uvi_like_tilapia_basil_dwc_raft_benchmark_v0`

Role:

- first benchmark-shaped scenario for a bounded tilapia + basil DWC/raft unit
- UVI-like in architecture and evidence family, not a claim of exact UVI system
  replication
- source-backed where evidence exists
- explicitly labeled where values are scenario assumptions
- gap-labeled where source support is insufficient

This is the first benchmark because the current MVP already uses tilapia +
basil DWC/raft framing, and UVI/SRAC/FAO/extension-style materials are a
reasonable public evidence family for pre-customer scenario design.

## 4. Source basis and evidence hierarchy

Use this evidence hierarchy for later dataset population:

1. direct benchmark system source with matching tilapia + basil DWC/raft scope
2. institutional aquaponics guidance from UVI, SRAC, FAO, or extension sources
3. existing repo research packs for tilapia feed, tank/TAN-to-NH3 context,
   aeration/solids, operating economics, and basil harvest/saleability
4. supplier price evidence with date, geography, unit, and source metadata
5. explicit scenario assumptions labeled `scenario_input`
6. unresolved items labeled `source_gap`, `expert_question_candidate`, or
   `blocked_until_observed`

Relevant present source families include:

- UVI-like DWC/raft architecture anchors
- SRAC/FAO/extension aquaponics and RAS guidance
- `data/sources/research_reports/markdown/Tilapia feed-regime and stocking-input research pack for a first fish-feed-to-water-quality MVP.md`
- `data/sources/research_reports/markdown/Tank Volume, Exchange and TAN-to-NH3 Risk Research Pack.md`
- `data/sources/research_reports/markdown/Aeration Capacity and Solids Load Translation Research Pack for the Aquaponics MVP.md`
- `data/sources/research_reports/markdown/Operating Economics Input Research Pack for the Aquaponics MVP.md`
- `data/sources/research_reports/markdown/Defensible First-Pass External Reference Standard for Harvest-Readiness and Saleability of Fresh Basil Sold as Basil Bulk Kg Wholesale.md`
- supplier price evidence, if later collected with metadata

Do not use a benchmark source to fill observed customer/operator fields.

## 5. Data readiness and field table format

Use these readiness levels:

- `L0_blocked_or_unavailable`
- `L1_scenario_input`
- `L2_benchmark_assumption_with_source`
- `L3_measured_internal_or_pilot_data`
- `L4_observed_customer_or_operator_data`
- `L5_reviewed_or_validated_commercial_data`

For this benchmark design, most usable fields should be
`L1_scenario_input` or `L2_benchmark_assumption_with_source`. Do not imply
`L4` or `L5` validation.

Every field table uses this format:

| field_name | category | required_for | classification | readiness_level | unit | source_basis | metadata_required | example_value_or_placeholder | validation_rule | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 6. Scenario metadata fields

| field_name | category | required_for | classification | readiness_level | unit | source_basis | metadata_required | example_value_or_placeholder | validation_rule | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `scenario_id` | scenario_metadata | dataset identity | scenario_input, required | L1_scenario_input | label | dataset design | date, author/status, notes | `uvi_like_tilapia_basil_dwc_raft_benchmark_v0` | must be unique and stable | yes | Identifier only, not evidence. |
| `scenario_name` | scenario_metadata | dataset identity | scenario_input, required | L1_scenario_input | text | dataset design | date, notes | `UVI-like tilapia basil DWC raft benchmark v0` | non-empty | yes | Display name. |
| `benchmark_version` | scenario_metadata | dataset traceability | scenario_input, required | L1_scenario_input | label | dataset design | date, notes | `v0` | must change when record shape or source basis changes | yes | Version of benchmark scenario, not app version. |
| `benchmark_status` | scenario_metadata | all benchmark use | benchmark_assumption, required | L2_benchmark_assumption_with_source | label | data contract | source_basis, confidence, notes | `benchmark_assumption_with_source` | must not be actual/customer status | yes | Prevents validation overclaim. |
| `readiness_level` | scenario_metadata | all benchmark use | benchmark_assumption, required | L2_benchmark_assumption_with_source | label | data contract | source_basis, confidence, notes | `L2_benchmark_assumption_with_source` | must not be L4/L5 | yes | Dataset-level readiness ceiling. |
| `architecture_context` | scenario_metadata | current engine context | benchmark_assumption, required | L2_benchmark_assumption_with_source | label | UVI-like DWC/raft architecture anchor | source family, date, notes | `tilapia_basil_dwc_raft` | non-empty; not a pricing selector | yes | Context, not canon. |
| `system_type` | scenario_metadata | source filtering | benchmark_assumption, required | L2_benchmark_assumption_with_source | label | UVI/SRAC/FAO/extension source | source family, date, notes | `coupled_aquaponics_dwc_or_raft_benchmark` | context must be explicit | yes | Do not flatten with media bed/NFT. |
| `source_family` | scenario_metadata | source traceability | benchmark_assumption, required | L2_benchmark_assumption_with_source | label list | source hierarchy | source title/reference, date, geography, confidence | `<UVI/SRAC/FAO/extension/source_family>` | at least one source family required | yes | Use durable labels. |
| `source_reference` | scenario_metadata | source traceability | benchmark_assumption, required | L2_benchmark_assumption_with_source | text/list | source hierarchy | title, URL/path if available, access date, notes | `<source_reference>` | must be reviewable | yes | Do not paste unsupported values. |
| `source_geography` | scenario_metadata | applicability | benchmark_assumption, required | L2_benchmark_assumption_with_source | label | source metadata | geography, date, notes | `<source_geography>` | must state source geography or unknown | yes | Avoids universalizing source context. |
| `applicability_notes` | scenario_metadata | seed-demo report | benchmark_assumption, required | L2_benchmark_assumption_with_source | text | reviewer | source limits, confidence, notes | `<context_differences_and_limits>` | must mention non-validation status | yes | Required for seed-demo honesty. |
| `customer_validation_status` | scenario_metadata | blocked-claim guardrail | blocked_until_observed, required | L0_blocked_or_unavailable | label | data contract | notes | `not_customer_validated` | must remain not customer validated | yes | No customer access yet. |

## 7. Fish/feed input fields

| field_name | category | required_for | classification | readiness_level | unit | source_basis | metadata_required | example_value_or_placeholder | validation_rule | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `fish_species` | fish_feed_input | benchmark identity | benchmark_assumption, required | L2_benchmark_assumption_with_source | species label | UVI-like tilapia source or source_gap | source family, date, confidence | `tilapia` or `<source_gap>` | must match tilapia scope | yes | Species does not prove safety or yield. |
| `feed_kg_day` | fish_feed_input | Mode A load path | benchmark_assumption or scenario_input, required | L1_scenario_input or L2_benchmark_assumption_with_source | kg/day | tilapia feed research pack, benchmark source, or explicit scenario | unit, source, date, confidence | `<source-backed or scenario daily feed>` | non-negative number when implemented later | yes | Root input for current engine. |
| `protein_fraction` | fish_feed_input | Mode A load path | benchmark_assumption or scenario_input, required | L1_scenario_input or L2_benchmark_assumption_with_source | fraction | tilapia feed research pack, feed label, or explicit scenario | unit, source, date, confidence | `<source-backed or scenario protein fraction>` | 0 to 1 inclusive | yes | Do not promote one universal protein value into canon. |
| `feed_class` | fish_feed_input | report context | benchmark_assumption or scenario_input, optional | L1_scenario_input or L2_benchmark_assumption_with_source | label | feed source or scenario | source, date, notes | `<grow_out_or_source_gap>` | non-empty if supplied | no | Context only. |
| `fish_count` | fish_feed_input | benchmark scale context | benchmark_assumption, optional | L2_benchmark_assumption_with_source | fish | UVI-like source, SRAC/extension, or source_gap | unit, source, date, confidence | `<source-backed fish count>` or `source_gap` | non-negative integer when supplied | no | Not needed for Mode A load path. |
| `average_fish_weight_kg` | fish_feed_input | benchmark scale context | benchmark_assumption, optional | L2_benchmark_assumption_with_source | kg/fish | UVI-like source, stocking pack, or source_gap | unit, source, date, confidence | `<source-backed average weight>` or `source_gap` | non-negative number when supplied | no | Do not derive Mode A feed from this. |
| `fish_biomass_kg` | fish_feed_input | benchmark scale context | benchmark_assumption, optional | L2_benchmark_assumption_with_source | kg | source-backed count and weight or direct source | unit, source, date, confidence | `<source-backed biomass>` or `source_gap` | explicit source or explicit derivation from sourced count and weight | no | Not a basil-saleability proxy. |
| `fcr_if_used` | fish_feed_input | later sensitivity only | benchmark_assumption, optional | L2_benchmark_assumption_with_source | kg feed/kg gain | tilapia feed research pack or source_gap | unit, source, date, confidence | `<source-backed FCR band>` or `source_gap` | positive if supplied | no | Not used by current Mode A engine. |
| `mortality_context` | fish_feed_input | future real-world gaps | benchmark_assumption, optional | L2_benchmark_assumption_with_source | label or count | benchmark source or source_gap | unit if numeric, source, date, confidence | `source_gap` | must not imply observed mortality | no | Save for later expert/customer review. |

## 8. Water-quality input fields

| field_name | category | required_for | classification | readiness_level | unit | source_basis | metadata_required | example_value_or_placeholder | validation_rule | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `effective_water_volume_l` | water_quality_input | P1 TAN-N concentration context | benchmark_assumption or scenario_input, required | L1_scenario_input or L2_benchmark_assumption_with_source | L | tank-volume/TAN-to-NH3 pack, UVI-like source, or scenario | unit, source, date, confidence | `<source-backed fish-tank/effective volume>` | positive number when implemented later | yes | Must state scope. |
| `total_system_volume_l` | water_quality_input | benchmark context | benchmark_assumption, optional | L2_benchmark_assumption_with_source | L | UVI-like source or source_gap | unit, source, date, confidence | `<source-backed total volume>` or `source_gap` | positive number if supplied | no | Not a substitute for fish-tank scope. |
| `accumulation_period_day` | water_quality_input | P1 TAN-N concentration context | scenario_input, required | L1_scenario_input | day | scenario design | unit, notes | `<explicit period>` | positive number | yes | Time basis only. |
| `concentration_scope` | water_quality_input | P1 TAN-N concentration context | scenario_input, required | L1_scenario_input | label | current helper boundary | notes | `fish_tank` | must match supported scope | yes | Prevents whole-system ambiguity. |
| `ph` | water_quality_input | P1 NH3 chemistry context | benchmark_assumption or scenario_input, required | L1_scenario_input or L2_benchmark_assumption_with_source | pH | tank/TAN-to-NH3 pack or scenario | unit, source, date, confidence | `<source-backed or scenario pH>` | 0 to 14 inclusive | yes | Not a safety threshold. |
| `water_temp_c` | water_quality_input | P1 NH3 chemistry context | benchmark_assumption or scenario_input, required | L1_scenario_input or L2_benchmark_assumption_with_source | deg C | tank/TAN-to-NH3 pack or scenario | unit, source, date, confidence | `<source-backed or scenario temperature>` | finite number | yes | Not a safety claim. |
| `freshwater_assumption` | water_quality_input | P1 NH3 chemistry context | scenario_input or benchmark_assumption, required | L1_scenario_input or L2_benchmark_assumption_with_source | boolean/label | scenario or source | source, notes | `<freshwater_status>` | explicit true/false or salinity basis | yes | Do not hide salinity context. |
| `water_exchange_or_replacement_context` | water_quality_input | later benchmark context | benchmark_assumption or source_gap, optional | L2_benchmark_assumption_with_source or L0_blocked_or_unavailable | L/day or label | UVI/SRAC/FAO/extension source or source_gap | unit, source, date, confidence | `source_gap` | explicit basis if supplied | no | Current P1 is no-removal/upper-bound context. |
| `biofilter_state_context` | water_quality_input | later benchmark context | benchmark_assumption or source_gap, optional | L2_benchmark_assumption_with_source or L0_blocked_or_unavailable | label | benchmark source or source_gap | source, date, notes | `source_gap` | must state assumed/unknown | no | Do not use for safety or removal proof. |

## 9. Engineering/equipment input fields

| field_name | category | required_for | classification | readiness_level | unit | source_basis | metadata_required | example_value_or_placeholder | validation_rule | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `equipment_power_records` | engineering_equipment_input | P2a power cost | benchmark_assumption or scenario_input, required if power cost is included | L1_scenario_input or L2_benchmark_assumption_with_source | record list | supplier evidence, UVI-like source, or scenario | device role, kW, runtime, basis, source, date | `<source-backed equipment records>` | each record must include role, kW, runtime, load fraction, and power basis | yes for power cost | Does not prove aeration adequacy. |
| `device_id` | engineering_equipment_input | power record identity | scenario_input, required per device | L1_scenario_input | label | scenario design | notes | `<device_id>` | unique within record list | yes | Identifier only. |
| `device_role` | engineering_equipment_input | power record context | scenario_input or benchmark_assumption, required per device | L1_scenario_input or L2_benchmark_assumption_with_source | label | supplier evidence or scenario | source, notes | `<pump_or_blower_role>` | non-empty | yes | Role is not capacity. |
| `device_kw` | engineering_equipment_input | P2a power cost | benchmark_assumption or scenario_input, required per device | L1_scenario_input or L2_benchmark_assumption_with_source | kW | nameplate, meter, supplier evidence, or source_gap | unit, source, date, confidence | `<source-backed device kW>` | non-negative number | yes for device power cost | Must state measured/nameplate basis. |
| `runtime_h_day` | engineering_equipment_input | P2a power cost | benchmark_assumption or scenario_input, required per device | L1_scenario_input or L2_benchmark_assumption_with_source | h/day | operating assumption, benchmark source, or source_gap | unit, source, date, confidence | `<source-backed or scenario runtime>` | 0 to 24 | yes for device power cost | Runtime is not reliability proof. |
| `load_fraction` | engineering_equipment_input | P2a power cost | benchmark_assumption or scenario_input, required per device | L1_scenario_input or L2_benchmark_assumption_with_source | fraction | equipment/source assumption | unit, source, notes | `<load_fraction_or_source_gap>` | 0 to 1 inclusive | yes for device power cost | Avoid silent full-load assumptions. |
| `power_basis` | engineering_equipment_input | seed-demo transparency | scenario_input or benchmark_assumption, required per device | L1_scenario_input or L2_benchmark_assumption_with_source | label | meter/nameplate/supplier/source | source, notes | `<nameplate_kw_or_measured_or_source_gap>` | must state basis | yes | Required to avoid fake precision. |
| `backup_power_status` | engineering_equipment_input | future risk context | benchmark_assumption or source_gap, optional | L2_benchmark_assumption_with_source or L0_blocked_or_unavailable | label | benchmark source or source_gap | source, date, notes | `source_gap` | must not imply safety | no | Not a current cost category. |

## 10. Aeration and solids input fields

| field_name | category | required_for | classification | readiness_level | unit | source_basis | metadata_required | example_value_or_placeholder | validation_rule | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `include_aeration_solids_context` | aeration_solids_input | P1.5 report section | scenario_input, required for P1.5 context | L1_scenario_input | boolean | scenario design | notes | `<true_or_false>` | boolean | yes for P1.5 context | Enables context, not adequacy. |
| `measured_do_mg_l` | aeration_solids_input | measured DO context | benchmark_assumption or scenario_input, optional | L1_scenario_input or L2_benchmark_assumption_with_source | mg/L | aeration/solids pack, benchmark source, or scenario | unit, source, date, confidence | `<source-backed or scenario DO>` or `source_gap` | non-negative number if supplied | no | Context only, not future safety proof. |
| `dry_solids_coefficient` | aeration_solids_input | dry-solids potential | benchmark_assumption or scenario_input, optional | L1_scenario_input or L2_benchmark_assumption_with_source | fraction | aeration/solids pack or scenario | unit, source, date, confidence | `<source-backed solids coefficient>` or `source_gap` | 0 to 1 inclusive if supplied | no | Not wet sludge, TSS, or removal capacity. |
| `dry_solids_basis` | aeration_solids_input | seed-demo transparency | benchmark_assumption or scenario_input, required if coefficient supplied | L1_scenario_input or L2_benchmark_assumption_with_source | label | source or scenario | source, notes | `benchmark_assumption_not_canon` | must state not canon | yes if coefficient supplied | Keeps source boundary visible. |
| `aeration_capacity_context_available` | aeration_solids_input | blocked-label context | scenario_input or source_gap, optional | L1_scenario_input or L0_blocked_or_unavailable | boolean | source review | source, notes | `false` or `source_gap` | boolean if supplied | no | Do not use as capacity proof. |
| `oxygen_transfer_basis_available` | aeration_solids_input | blocked-label context | scenario_input or source_gap, optional | L1_scenario_input or L0_blocked_or_unavailable | boolean | source review | source, notes | `false` or `source_gap` | boolean if supplied | no | Needed before capacity comparison. |
| `dwc_root_zone_aeration_context_available` | aeration_solids_input | DWC context | benchmark_assumption or source_gap, optional | L2_benchmark_assumption_with_source or L0_blocked_or_unavailable | boolean/label | UVI-like or extension source | source, date, notes | `source_gap` | explicit if supplied | no | Separate from fish-tank aeration. |
| `solids_removal_capacity_context_available` | aeration_solids_input | solids context | benchmark_assumption or source_gap, optional | L2_benchmark_assumption_with_source or L0_blocked_or_unavailable | boolean/label | aeration/solids source | source, date, notes | `source_gap` | explicit if supplied | no | Not solids-removal capacity proof. |
| `clarifier_retention_context_available` | aeration_solids_input | solids context | benchmark_assumption or source_gap, optional | L2_benchmark_assumption_with_source or L0_blocked_or_unavailable | boolean/label | benchmark source | source, date, notes | `source_gap` | explicit if supplied | no | Future report context only. |

## 11. Operating-cost input fields

| field_name | category | required_for | classification | readiness_level | unit | source_basis | metadata_required | example_value_or_placeholder | validation_rule | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `include_operating_cost_pressure` | operating_cost_input | P2a report section | scenario_input, required for P2a | L1_scenario_input | boolean | scenario design | notes | `<true_or_false>` | boolean | yes for P2a context | Enables selected cost pressure only. |
| `feed_price_per_kg` | operating_cost_input | scenario feed cost | benchmark_assumption or scenario_input, required if feed cost included | L1_scenario_input or L2_benchmark_assumption_with_source | currency/kg | supplier evidence, operating economics pack, or scenario | unit, currency, source, date, geography, confidence | `<source-backed feed price>` or `source_gap` | non-negative number with currency | yes for feed cost | Not canon or market truth. |
| `feed_price_currency` | operating_cost_input | scenario feed cost | scenario_input or benchmark_assumption, required if feed cost included | L1_scenario_input or L2_benchmark_assumption_with_source | currency code | price source | currency, source, date | `<currency>` | non-empty | yes | Needed for subtotal compatibility. |
| `feed_price_date` | operating_cost_input | scenario feed cost | benchmark_assumption or scenario_input, required if feed cost included | L1_scenario_input or L2_benchmark_assumption_with_source | date | supplier/source metadata | date, source | `<price_date>` | valid date or source date | yes | No stale price without date. |
| `feed_price_geography` | operating_cost_input | scenario feed cost | benchmark_assumption or scenario_input, required if feed cost included | L1_scenario_input or L2_benchmark_assumption_with_source | label | supplier/source metadata | geography, source | `<price_geography>` | non-empty | yes | Avoids universal price claims. |
| `feed_price_source_type` | operating_cost_input | scenario feed cost | benchmark_assumption or scenario_input, required if feed cost included | L1_scenario_input or L2_benchmark_assumption_with_source | label | source metadata | source, notes | `<supplier_quote_or_benchmark_or_scenario>` | non-empty | yes | Must preserve status. |
| `electricity_price_per_kwh` | operating_cost_input | scenario power cost | benchmark_assumption or scenario_input, required if power cost included | L1_scenario_input or L2_benchmark_assumption_with_source | currency/kWh | tariff, supplier, operating economics pack, or scenario | unit, currency, source, date, geography, confidence | `<source-backed tariff>` or `source_gap` | non-negative number with currency | yes for power cost | Not canon. |
| `electricity_price_currency` | operating_cost_input | scenario power cost | scenario_input or benchmark_assumption, required if power cost included | L1_scenario_input or L2_benchmark_assumption_with_source | currency code | tariff/source metadata | currency, source, date | `<currency>` | non-empty | yes | Must match or explicitly convert with feed currency. |
| `electricity_tariff_date` | operating_cost_input | scenario power cost | benchmark_assumption or scenario_input, required if power cost included | L1_scenario_input or L2_benchmark_assumption_with_source | date | tariff/source metadata | date, source | `<tariff_date>` | valid date or source date | yes | No tariff without date. |
| `electricity_price_geography` | operating_cost_input | scenario power cost | benchmark_assumption or scenario_input, required if power cost included | L1_scenario_input or L2_benchmark_assumption_with_source | label | tariff/source metadata | geography, source | `<tariff_geography>` | non-empty | yes | Avoids universal tariff claims. |
| `electricity_tariff_source_type` | operating_cost_input | scenario power cost | benchmark_assumption or scenario_input, required if power cost included | L1_scenario_input or L2_benchmark_assumption_with_source | label | source metadata | source, notes | `<tariff_or_benchmark_or_scenario>` | non-empty | yes | Must preserve status. |
| `buffer_water_labor_cost_placeholders` | operating_cost_input | future total-cost gap map | source_gap or scenario_input, optional | L0_blocked_or_unavailable or L1_scenario_input | mixed | operating economics pack or source_gap | unit, currency where relevant, source, date, notes | `source_gap` | must not roll into total operating cost | no | Placeholders only. |

## 12. Labor and maintenance placeholders

| field_name | category | required_for | classification | readiness_level | unit | source_basis | metadata_required | example_value_or_placeholder | validation_rule | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `clarifier_purge_frequency` | labor_maintenance_placeholder | future labor gap map | source_gap or benchmark_assumption, optional | L0_blocked_or_unavailable or L2_benchmark_assumption_with_source | events/day or schedule | operating economics pack, extension source, or source_gap | unit, source, date, confidence | `source_gap` | explicit frequency if supplied | no | Placeholder, not cost. |
| `filter_cleaning_frequency` | labor_maintenance_placeholder | future labor gap map | source_gap or benchmark_assumption, optional | L0_blocked_or_unavailable or L2_benchmark_assumption_with_source | events/day or schedule | operating economics pack, extension source, or source_gap | unit, source, date, confidence | `source_gap` | explicit frequency if supplied | no | Placeholder, not cost. |
| `task_hours_per_event` | labor_maintenance_placeholder | future labor gap map | source_gap or benchmark_assumption, optional | L0_blocked_or_unavailable or L2_benchmark_assumption_with_source | hours/event | operating economics pack or source_gap | unit, source, date, confidence | `source_gap` | non-negative if supplied | no | Do not calculate labor cost yet. |
| `labor_rate` | labor_maintenance_placeholder | future labor gap map | source_gap or benchmark_assumption, optional | L0_blocked_or_unavailable or L2_benchmark_assumption_with_source | currency/hour | supplier/labor source or source_gap | unit, currency, source, date, geography | `source_gap` | non-negative if supplied | no | No total operating cost. |
| `maintenance_notes` | labor_maintenance_placeholder | seed-demo gap map | scenario_input or source_gap, optional | L1_scenario_input or L0_blocked_or_unavailable | text | benchmark review | source, notes | `<notes_or_source_gap>` | must state status | no | Qualitative only. |

## 13. Fish output placeholders

| field_name | category | required_for | classification | readiness_level | unit | source_basis | metadata_required | example_value_or_placeholder | validation_rule | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `fish_harvest_date` | fish_output_placeholder | future unit economics | source_gap or benchmark_assumption, optional | L0_blocked_or_unavailable or L2_benchmark_assumption_with_source | date | benchmark source or source_gap | source, date, confidence | `source_gap` | valid date if supplied | no | Placeholder only. |
| `harvested_fish_count` | fish_output_placeholder | future fish revenue | source_gap or benchmark_assumption, optional | L0_blocked_or_unavailable or L2_benchmark_assumption_with_source | fish | benchmark source or source_gap | unit, source, date, confidence | `source_gap` | non-negative integer if supplied | no | Do not claim fish revenue. |
| `harvested_fish_mass_kg` | fish_output_placeholder | future fish revenue | source_gap or benchmark_assumption, optional | L0_blocked_or_unavailable or L2_benchmark_assumption_with_source | kg | benchmark source or source_gap | unit, source, date, confidence | `source_gap` | non-negative if supplied | no | Must state live/whole/processed basis. |
| `fish_mortalities` | fish_output_placeholder | future risk/economics | source_gap or benchmark_assumption, optional | L0_blocked_or_unavailable or L2_benchmark_assumption_with_source | fish or kg | benchmark source or source_gap | unit, source, date, confidence | `source_gap` | non-negative if supplied | no | Not fish safety. |
| `fish_sale_price_placeholder` | fish_output_placeholder | future fish revenue | source_gap, optional | L0_blocked_or_unavailable | currency/sale unit | supplier or market evidence needed | currency, unit, date, geography, buyer/channel, source | `source_gap` | must not be used without explicit quantity and status | no | Revenue remains not calculated. |

## 14. Basil output placeholders

| field_name | category | required_for | classification | readiness_level | unit | source_basis | metadata_required | example_value_or_placeholder | validation_rule | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `planted_area_m2_or_site_count` | basil_output_placeholder | benchmark scale context | benchmark_assumption or source_gap, optional | L2_benchmark_assumption_with_source or L0_blocked_or_unavailable | m2 or sites | UVI-like source or source_gap | unit, source, date, confidence | `source_gap` | non-negative if supplied | no | Context only. |
| `basil_harvest_date` | basil_output_placeholder | future basil revenue | source_gap, optional | L0_blocked_or_unavailable | date | observed/reviewed data needed | source, date, notes | `source_gap` | valid date if supplied later | no | No observed harvest now. |
| `gross_harvested_basil_mass_kg` | basil_output_placeholder | future review | source_gap or benchmark_assumption, optional | L0_blocked_or_unavailable or L2_benchmark_assumption_with_source | kg | benchmark source or source_gap | unit, source, date, confidence | `source_gap` | non-negative if supplied | no | Must not become saleable mass. |
| `observed_saleable_harvest_mass_kg` | basil_output_placeholder | future saleable source | blocked_until_observed, required before actual basil revenue | L0_blocked_or_unavailable | kg | observed/reviewed data only | unit, source, date, reviewer/buyer/channel, confidence | `null` | must remain null until observed or reviewed | yes | Do not infer from gross mass or plant count. |
| `saleable_harvest_mass_kg` | basil_output_placeholder | business-required basil revenue field | blocked_until_observed, required before basil revenue | L0_blocked_or_unavailable | kg | observed runtime output or explicit reviewed manual input only | unit, source, date, reviewer/buyer/channel, confidence | `null` | must remain null until backed | yes | Null means unresolved, not zero. |
| `rejected_or_cull_basil_mass_kg` | basil_output_placeholder | future review | blocked_until_observed or source_gap, optional | L0_blocked_or_unavailable | kg | observed/reviewed data needed | unit, source, date, reviewer, notes | `source_gap` | no inference from saleability labels | no | Keep separate from saleable mass. |
| `basil_rejection_reasons` | basil_output_placeholder | future review | blocked_until_observed or source_gap, optional | L0_blocked_or_unavailable | label list | QA/buyer/reviewer data needed | source, date, reviewer, confidence | `expert_question_candidate` | reviewed labels only | no | Ontology labels are not automatic logic. |
| `basil_sale_price_placeholder` | basil_output_placeholder | future basil revenue | source_gap, optional | L0_blocked_or_unavailable | currency/sale unit | supplier/market evidence needed | currency, unit, date, geography, buyer/channel, source | `source_gap` | must not be used without saleable quantity and status | no | Revenue remains not calculated. |

## 15. Revenue placeholders

| field_name | category | required_for | classification | readiness_level | unit | source_basis | metadata_required | example_value_or_placeholder | validation_rule | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `fish_revenue_status` | revenue_placeholder | blocked-claim guardrail | blocked_until_observed, required | L0_blocked_or_unavailable | label | data contract | notes | `not_calculated` | must remain not calculated | yes | No fish revenue in benchmark design. |
| `basil_revenue_status` | revenue_placeholder | blocked-claim guardrail | blocked_until_observed, required | L0_blocked_or_unavailable | label | data contract | notes | `not_calculated` | must remain not calculated | yes | No basil revenue without saleable mass. |
| `sale_unit` | revenue_placeholder | future revenue | source_gap, optional | L0_blocked_or_unavailable | label | future source needed | source, date, buyer/channel, notes | `source_gap` | must match quantity and price later | no | Placeholder only. |
| `currency` | revenue_placeholder | future revenue/cost comparison | scenario_input or benchmark_assumption, optional | L1_scenario_input or L2_benchmark_assumption_with_source | currency code | source metadata | currency, date, geography, source | `<currency_if_cost_inputs_supplied>` | no silent currency mixing | no | Cost-pressure currency only unless revenue inputs exist. |
| `buyer_channel` | revenue_placeholder | future revenue | source_gap, optional | L0_blocked_or_unavailable | label | future customer/operator/source data needed | source, geography, notes | `expert_question_candidate` | non-empty before future revenue | no | Do not invent buyer channel. |
| `actual_vs_scenario_status` | revenue_placeholder | future revenue | scenario_input, required if any price placeholder exists | L1_scenario_input | label | dataset metadata | source, notes | `benchmark_assumption_or_scenario_input` | cannot be actual_sale | yes | Prevents benchmark revenue overclaim. |

## 16. Expected derived outputs from current engine

| field_name | category | required_for | classification | readiness_level | unit | source_basis | metadata_required | example_value_or_placeholder | validation_rule | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `tan_n_load` | expected_current_output | Mode A | derived, required | L1/L2 input-dependent | kg/day and g/day | current engine from feed/protein | input status, units, notes | `<current_engine_output>` | requires `feed_kg_day` and `protein_fraction` | yes | Load only, not concentration. |
| `nitrification_oxygen_demand` | expected_current_output | Mode A/P1.5 | derived, required | L1/L2 input-dependent | g/day | current engine from TAN-N load | input status, units, notes | `<current_engine_output>` | requires TAN-N load | yes | Not total oxygen demand or aeration capacity. |
| `alkalinity_demand` | expected_current_output | Mode A | derived, required | L1/L2 input-dependent | g CaCO3/day | current engine from TAN-N load | input status, units, notes | `<current_engine_output>` | requires TAN-N load | yes | Demand context only. |
| `tan_n_concentration_context` | expected_current_output | P1 | derived, optional | L1/L2 input-dependent | mg/L | current engine from complete P1 inputs | input status, units, notes | `<current_engine_output>` | requires volume, period, scope | yes | Fish-tank context, not safety. |
| `nh3_chemistry_context` | expected_current_output | P1 | derived, optional | L1/L2 input-dependent | fraction and mg/L | current engine from complete chemistry inputs | input status, units, notes | `<current_engine_output>` | requires TAN-N concentration, pH, temperature, freshwater basis | yes | Not toxicity or safety. |
| `measured_do_context` | expected_current_output | P1.5 | scenario_input or benchmark_assumption, optional | L1/L2 | mg/L | supplied input carried as context | source, units, notes | `<input_context>` | explicit value and source if supplied | no | Not future safety proof. |
| `dry_solids_potential` | expected_current_output | P1.5 | derived, optional | L1/L2 input-dependent | kg/day | current engine from feed and coefficient | input status, units, notes | `<current_engine_output>` | requires feed and coefficient | no | Not wet sludge, TSS, or removal capacity. |
| `scenario_feed_cost` | expected_current_output | P2a | derived, optional | L1/L2 input-dependent | currency/day | current engine from feed and price | currency, date, geography, source | `<current_engine_output>` | requires explicit feed price inputs | no | Scenario cost only. |
| `scenario_power_cost` | expected_current_output | P2a | derived, optional | L1/L2 input-dependent | currency/day | current engine from equipment and tariff | currency, date, geography, source | `<current_engine_output>` | requires equipment records and tariff | no | Scenario cost only. |
| `selected_operating_cost_pressure_subtotal` | expected_current_output | P2a | derived, optional | L1/L2 input-dependent | currency/day | current engine from selected cost categories | currency, date, geography, source | `<current_engine_output>` | requires compatible supplied money fields | no | Not total operating cost. |

## 17. Fields that remain null or blocked

| field_name | category | required_for | classification | readiness_level | unit | source_basis | metadata_required | example_value_or_placeholder | validation_rule | blocked_if_missing | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `saleable_harvest_mass_kg` | blocked_field | basil revenue | blocked_until_observed, required later | L0_blocked_or_unavailable | kg | observed/reviewed input only | source, date, reviewer/buyer, notes | `null` | must remain null | yes | Do not infer from biomass, plant count, or benchmark yield. |
| `total_operating_cost` | blocked_field | future economics | blocked_until_observed, required later | L0_blocked_or_unavailable | currency/period | complete cost contract needed | currency, date, geography, source | `not_calculated` | must remain not calculated | yes | P2a is selected pressure only. |
| `revenue` | blocked_field | future economics | blocked_until_observed, required later | L0_blocked_or_unavailable | currency/period | complete quantity and price inputs needed | quantity, price, currency, date, geography, buyer/channel, status | `not_calculated` | must remain not calculated | yes | No revenue in benchmark design. |
| `profitability` | blocked_field | future economics | blocked_until_observed, required later | L0_blocked_or_unavailable | label/currency | complete revenue and cost scope needed | source, assumptions, notes | `not_calculated` | must remain not calculated | yes | No profitability claim. |
| `commercial_operability` | blocked_field | future validation | blocked_until_observed, required later | L0_blocked_or_unavailable | label | customer/operator/real-world evidence needed | source, validation status, notes | `not_claimed` | must remain not claimed | yes | Benchmark cannot prove this. |
| `fish_system_safety` | blocked_field | safety claims | blocked_until_observed, required later | L0_blocked_or_unavailable | label | safety design and evidence needed | source, thresholds, review status | `not_claimed` | must remain not claimed | yes | TAN/NH3/DO context is not safety. |
| `aeration_adequacy` | blocked_field | aeration claims | blocked_until_observed, required later | L0_blocked_or_unavailable | label | oxygen-transfer/capacity proof needed | source, equipment, transfer basis | `not_claimed` | must remain not claimed | yes | Device kW is not aeration capacity. |
| `solids_removal_capacity` | blocked_field | solids claims | blocked_until_observed, required later | L0_blocked_or_unavailable | label | filter design/performance evidence needed | source, design, validation status | `not_claimed` | must remain not claimed | yes | Dry solids potential is not removal capacity. |

## 18. Uncertainty labels

Use these labels in the later dataset:

- `benchmark_assumption`
- `scenario_input`
- `not_customer_validated`
- `not_canon`
- `not_commercial_proof`
- `not_real_world_operating_proof`
- `not_total_operating_cost`
- `not_profitability`
- `source_gap`
- `expert_question_candidate`
- `blocked_until_observed`

Labels must travel with the field or record they qualify. Do not put them only
in surrounding prose.

## 19. Claims allowed

The benchmark scenario may claim:

- this is a designed benchmark scenario record shape
- the scenario is UVI-like in DWC/raft architecture framing if sources support
  that classification
- the current engine can consume explicit Mode A, P1, P1.5, and P2a inputs
- the current engine can output load, chemistry context, solids context, and
  selected operating-cost pressure when required inputs are present
- source gaps are explicit
- benchmark assumptions are not canon
- the scenario can support a future seed-demo report once values are sourced

## 20. Claims forbidden

The benchmark scenario must not claim or imply:

- customer validation
- commercial proof
- real-world operating proof
- canonical biology, business, or runtime truth
- fish safety
- system safety
- aeration adequacy
- solids-removal capacity
- total operating cost
- revenue
- profitability
- commercial operability
- known basil saleable harvest output
- `saleable_harvest_mass_kg` inferred from gross harvest, plant count, biomass,
  daily gain, readiness labels, saleability labels, or benchmark yield

## 21. Source gaps and expert/customer question candidates

Use `source_gap` when a desired value lacks sufficient public/source support.
Use `expert_question_candidate` when public evidence cannot safely answer the
question.

Current likely gaps:

- exact UVI-like tilapia + basil DWC/raft source values that map cleanly to
  this one bounded scenario
- local feed price and electricity tariff if no supplier/tariff evidence is
  selected
- equipment records with defensible kW, runtime, load fraction, and power basis
- DO context if no source-backed value is chosen
- solids coefficient if source support is too broad for the intended scenario
- clarifier/filter cleaning frequency and task hours
- fish harvest mass, sale unit, price, and buyer/channel
- basil gross harvest mass, observed saleable mass, cull mass, rejection
  reasons, sale price, and buyer/channel
- whether benchmark sources are representative enough for seed-demo reviewers

Expert/customer question candidates:

- Which UVI/SRAC/FAO/extension benchmark is most comparable to this bounded
  tilapia + basil DWC/raft scenario?
- Which source is acceptable for feed price and electricity tariff metadata?
- Should equipment power be nameplate, metered, duty-cycle adjusted, or
  supplier-estimated for the first seed-demo report?
- What observed basil handling or buyer acceptance record is sufficient before
  `saleable_harvest_mass_kg` can be non-null?
- Which labor and maintenance activities matter most before total operating
  cost is even designed?
- Which fish sale unit and channel should be represented first when customer
  access exists?

## 22. Future dataset implementation guidance

Recommended future dataset location:

`data/benchmarks/uvi_like_tilapia_basil_dwc_raft_benchmark_v0.json`

Do not create that file in this design pass.

Future implementation guidance:

- keep one top-level scenario record
- include dataset-level readiness and uncertainty labels
- include source metadata beside each benchmark assumption or in a linked
  source block referenced by field ids
- keep current-engine input fields separate from future placeholder fields
- keep expected outputs separate from source inputs
- keep blocked fields explicit as null or not calculated
- require `saleable_harvest_mass_kg: null` unless an observed/reviewed source
  exists in a later approved pass
- include `not_customer_validated`, `not_commercial_proof`, and
  `not_real_world_operating_proof` labels at dataset and blocked-output level
- do not store benchmark values in canonical knowledge files

## 23. Validation checks for later implementation

For a later dataset implementation pass, validate:

- only the explicitly approved dataset file is created or modified
- no `configs/**`, `data/knowledge/**`, `data/simulation/**`, `src/**`,
  `scripts/**`, `tests/**`, ontology, or knowledge-vault files change unless
  explicitly allowed
- every field has classification, readiness level, source basis, and required
  metadata
- benchmark fields are labeled `L2_benchmark_assumption_with_source`
- scenario-only fields are labeled `L1_scenario_input`
- no field claims L4/L5 customer/commercial validation
- `saleable_harvest_mass_kg` is null unless observed or explicitly reviewed
- revenue, profitability, commercial operability, total operating cost, safety,
  aeration adequacy, and solids-removal capacity remain blocked
- selected operating-cost pressure remains distinct from total operating cost
- all source gaps are labeled `source_gap` or `expert_question_candidate`
- `python scripts/check_mvp_integrity.py --quick` passes after dataset creation
- `git --no-pager diff --name-only -- configs data/knowledge data/simulation src scripts tests knowledge-vault` stays empty unless scope is explicitly widened

## 24. Recommended next action

Run a Deep Research or source-review request to fill the source plan for
`uvi_like_tilapia_basil_dwc_raft_benchmark_v0`. The output should identify
source-backed candidate values, source gaps, and expert/customer questions, but
it should not create the JSON dataset or promote any assumptions into canon.
