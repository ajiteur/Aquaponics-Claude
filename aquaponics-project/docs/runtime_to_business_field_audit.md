# Runtime to Business Field Audit

Status: `draft`

## Purpose

- Provide a read-only Phase 1 audit of runtime-to-business field coverage for the first narrow business slice.
- Clarify mapping readiness before further integration work.
- Treat missing numeric business assumptions as separate from field-mapping readiness.

## Scope

- This audit is limited to first-slice field coverage and mapping readiness.
- It reviews current business-layer contract and first-slice business files against current runtime or simulation outputs.
- It does not redesign schemas, populate price or cost rates, or change canonical biology or model files.

## Current Objective

- Build one narrow, reviewable first vertical slice from runtime outputs to business interpretation.

## Chosen First Slice

- `basil bulk kg wholesale`

## Why This Slice Was Chosen

- `price_basil_bulk_kg` and `rule_basil_bulk_kg` already define an active direct-mass path.
- It avoids head-based, bunch-based, timing-heavy, and architecture-advisory logic.
- `tilapia kg wholesale` still carries an extra fish price-basis ambiguity in `pricing_models.json` on top of the same harvested-mass gap.
- `channel_wholesale` is already framed as the cleanest first-pass channel for bulk kg pricing.

## Sources Reviewed

- `docs/business_layer_contract.md`
- `data/knowledge/business/pricing_models.json`
- `data/knowledge/business/cost_models.json`
- `data/knowledge/business/labor_models.json`
- `data/knowledge/business/yield_to_revenue_rules.json`
- `data/knowledge/business/channel_assumptions.json`
- Runtime or simulation samples:
  - `data/simulation/scenarios/starter_tilapia_basil_system_day_1_day_2_day_3_day_4_day_5_day_6_day_7.json`
  - `data/simulation/day_logs/day_log_7_20260411T034837Z.json`
  - `data/simulation/multi_day_summary.json`

## Mapping Categories

- `present_directly`: the exact business-facing field is already present in current runtime output.
- `derivable_by_simple_mapping`: the field can be obtained by flattening a nested object, renaming a field, summing daily values, or using a fixed slice configuration value.
- `missing`: no current runtime source was found.
- `allowed_null_or_deferred_for_first_slice`: useful later, but not required to prove the first narrow slice now, or intentionally deferred in current business rules.

## Field-by-Field Audit Table

| Business field | Slice relevance | Current source or candidate source | Status | Mapping note | Blocks first slice? | Notes |
|---|---|---|---|---|---|---|
| `scenario_id` | required_now | scenario file `scenario_id` | `present_directly` | Already emitted exactly. | no | Use the scenario artifact as the primary source. |
| `run_id` | required_now | day-log basename timestamp or `saved_scenario_file` basename | `derivable_by_simple_mapping` | Needs one deterministic adapter rule for run identity. | no | Current runtime does not emit a normalized run field directly. |
| `scenario_name` | useful_now | humanized `scenario_id` | `derivable_by_simple_mapping` | No explicit scenario name field was found. | no | Keep as adapter label only. |
| `time_basis` | required_now | `time.timestep` or adapter-fixed `scenario_rollup` | `derivable_by_simple_mapping` | Current files say `daily`, but a 7-day scenario file behaves like a rollup snapshot. | no | Later integration should choose one normalized meaning and use it consistently. |
| `period_start_utc` | useful_now | no direct runtime source found | `allowed_null_or_deferred_for_first_slice` | Current simulation tracks day counts, not explicit UTC period bounds. | no | Do not misuse `updated_at_utc` as simulated period start. |
| `period_end_utc` | useful_now | `updated_at_utc` is save time only | `allowed_null_or_deferred_for_first_slice` | Save time is not the same thing as business period end. | no | Add later when runtime emits explicit period framing or adapter metadata. |
| `crop_id` | required_now | `plant_crop.species_id = plant_basil` | `derivable_by_simple_mapping` | Flatten the nested plant record from the primary scenario snapshot. | no | Current runtime species ID already matches the canonical plant identifier pattern. |
| `product_id` | required_now | `crop_id = plant_basil` -> `basil` | `derivable_by_simple_mapping` | Needed to select `price_basil_bulk_kg`. | no | Use an explicit mapping table rather than stripping prefixes implicitly everywhere. |
| `channel_id` | required_now | fixed slice choice `channel_wholesale` | `derivable_by_simple_mapping` | This is chosen by the first-slice configuration, not by runtime output. | no | Keep it explicit instead of inferring it from scenario data. |
| `crop_system_type` | useful_now | scenario file `crop_system_type` | `present_directly` | Already emitted directly on the current basil scenario path. | no | Context field only; architecture-conditioned business rules remain deferred. |
| `growing_area_m2` | useful_now | no runtime source found | `missing` | Needed later for area-normalized reporting and some labor or CAPEX views. | no | Not a blocker for the first kg-based revenue path. |
| `planting_count` | useful_now | `plant_crop.plant_count` | `derivable_by_simple_mapping` | Works only as a first-pass proxy because current runtime does not separate transplanted vs surviving plants. | no | Relevant later if `cost_plant_inputs_basil` is populated. |
| `live_plant_count_end` | useful_now | `plant_crop.plant_count` | `derivable_by_simple_mapping` | Current plant count behaves like end-of-period live count. | no | This meaning is cleaner than using the same value as guaranteed planting count. |
| `saleable_harvest_mass_kg` | required_now | no runtime source found | `missing` | Both `rule_basil_bulk_kg` and `price_basil_bulk_kg` depend on saleable harvested kg. | yes | Main blocker. Current runtime emits standing biomass and daily gain, not harvest mass. |
| `cull_or_unsaleable_mass_kg` | useful_now | no runtime source found | `allowed_null_or_deferred_for_first_slice` | Optional in the current basil kg revenue rule. | no | Add later with harvest rollups. |
| `harvest_event_count` | useful_now | no runtime source found; `harvest_policy: manual` is not an event count | `allowed_null_or_deferred_for_first_slice` | Optional in the current basil kg rule. | no | Needed later for harvest labor and timing analysis. |
| `first_harvest_utc` | useful_now | no runtime source found | `allowed_null_or_deferred_for_first_slice` | Optional in the current basil kg rule. | no | Leave null for the first slice. |
| `last_harvest_utc` | useful_now | no runtime source found | `allowed_null_or_deferred_for_first_slice` | Optional in the current basil kg rule. | no | Leave null for the first slice. |
| `energy_kwh` | useful_now | `derived.daily_energy_kwh` or sum of day logs | `derivable_by_simple_mapping` | Straight rename plus one period-aggregation choice. | no | Active `cost_electricity` can use this once rates are populated. |
| `water_use_l` | useful_now | `operations_policy.water_top_up_l_per_day` only as proxy | `allowed_null_or_deferred_for_first_slice` | Current runtime does not emit observed water-use totals. | no | Do not silently equate top-up policy with actual use unless the adapter documents that proxy explicitly. |
| `supplement_input_records` | useful_now | no direct source; only `pH_control_enabled` and `base_dosing_enabled` policy flags | `allowed_null_or_deferred_for_first_slice` | No dose quantities or dose event records were found. | no | Current `cost_supplements_and_buffering` cannot be mapped cleanly yet. |
| `observed_pH` | required_now | `water_state.pH` | `derivable_by_simple_mapping` | Flatten the nested water-state object from the primary scenario snapshot. | no | Naming change only. |
| `observed_tan_mg_l` | required_now | `water_state.tan_mg_L` | `derivable_by_simple_mapping` | Rename and normalize `mg_L` vs `mg_l`. | no | Same physical unit, naming mismatch only. |
| `observed_unionized_nh3_mg_l` | required_now | `water_state.unionized_nh3_mg_L` | `derivable_by_simple_mapping` | Rename and normalize case. | no | Same physical unit, naming mismatch only. |
| `observed_nitrate_mg_l` | required_now | `water_state.nitrate_mg_L` | `derivable_by_simple_mapping` | Rename and normalize case. | no | Same physical unit, naming mismatch only. |
| `operating_day_count` | useful_now | `time.day` on rollup file or count of day logs | `derivable_by_simple_mapping` | Not a contract field, but needed by active shared labor records. | no | Helps `labor_system_monitoring_and_checks` if that path is included early. |
| `adjustment_event_count` | useful_now | no runtime source found | `allowed_null_or_deferred_for_first_slice` | Active water-quality adjustment labor has no current runtime event counter. | no | Leave null until actual dose or adjustment events are recorded. |
| `quality_risk_event_records` | deferred | no runtime source found | `allowed_null_or_deferred_for_first_slice` | Risk-penalty activation is still deferred on purpose. | no | Do not infer these from overlap scores yet. |
| `out_of_range_event_records` | deferred | no runtime source found | `allowed_null_or_deferred_for_first_slice` | Current day logs show assessments, not explicit event records. | no | Keep null for the first slice. |
| `downtime_event_count` | deferred | no runtime source found | `allowed_null_or_deferred_for_first_slice` | No explicit downtime rollup was found. | no | Keep null for the first slice. |
| `disease_or_pathogen_event_records` | deferred | no runtime source found | `allowed_null_or_deferred_for_first_slice` | No explicit disease or pathogen event stream was found. | no | Keep null for the first slice. |

## Required Now vs Later vs Deferred

### Required Now for the First Slice

- `scenario_id`
- adapter-stable `run_id`
- `time_basis`
- `crop_id`
- `product_id`
- fixed `channel_id = channel_wholesale`
- `saleable_harvest_mass_kg`
- `observed_pH`
- `observed_tan_mg_l`
- `observed_unionized_nh3_mg_l`
- `observed_nitrate_mg_l`
- `energy_kwh`
- `operating_day_count` if early shared monitoring labor is included

### Useful but Not Required Yet

- `scenario_name`
- `period_start_utc`
- `period_end_utc`
- `crop_system_type`
- `growing_area_m2`
- `planting_count`
- `live_plant_count_end`
- `water_use_l`
- `supplement_input_records`
- `adjustment_event_count`
- `cull_or_unsaleable_mass_kg`
- `harvest_event_count`
- `first_harvest_utc`
- `last_harvest_utc`

### Intentionally Deferred

- risk-event rollups used by `risk_penalty_models.json`
- count-based or bunch-based sale-unit paths
- delivery timing, order timing, and cash-timing fields
- architecture-conditioned output-form guidance
- fish-side product fields for the later tilapia or joint-product slice

## Main Blockers

- `saleable_harvest_mass_kg` is missing entirely from current runtime outputs, and that is the main blocker for the basil kg pricing path.
- Current simulation outputs are state snapshots and day-log assessments, not explicit harvest rollups.
- `growing_area_m2` is absent, although it does not block the narrow basil wholesale proof.
- `crop_system_type` is now present as a context field, although it still does not block the narrow basil wholesale proof.
- `water_use_l` and `supplement_input_records` do not exist as observed rollups yet, so shared operating-cost coverage remains partial.
- Active shared labor can use `operating_day_count`, but `adjustment_event_count` is still missing.

## Recommended Next Action

- Keep `basil bulk kg wholesale` as the first slice.
- Build one thin translation layer that maps current basil scenario or day-log fields into normalized business-field names and fixed slice config values.
- Decide one explicit source for `saleable_harvest_mass_kg` next. That source should be an adapter-side or derived harvest rollup, not an invented value inside canonical biology or model files.
- Keep water, supplement, and risk-event fields null or deferred in the first implementation unless a clear upstream rollup already exists.

## Notes and Cautions

- Current runtime `economics.*` values and `daily_operating_cost` should not be treated as canonical business inputs. Canonical pricing, cost, and labor assumptions still live under `data/knowledge/business/**`.
- `water_top_up_l_per_day` is a policy or scenario setting, not automatically the same thing as observed `water_use_l`.
- `plant_count` is not automatically the same thing as `planting_count` once harvests or losses start. It is only a practical first-pass proxy in the current starter scenario shape.
- The current runtime-facing files use nested objects such as scenario-snapshot `water_state`, `plant_crop`, and `fish_batch`, plus day-log variants like `water_state_after` and `plant_crop_after`, so a flattening and renaming layer is expected.
- This audit judges mapping readiness only. It does not judge whether price rates, labor rates, or cost rates are populated enough for full economics yet.
