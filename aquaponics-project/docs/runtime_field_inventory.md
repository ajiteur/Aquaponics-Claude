# Runtime Field Inventory

Status: `draft`

## Purpose

- Provide a reusable census of current runtime-facing outputs under `data/simulation/**`.
- Separate stable runtime observations from inconsistent metadata, one-off result files, and fields still missing for the first business slice.
- Support adapter prep for the current first vertical slice objective without treating derived runtime files as canonical business truth.

## Scope

- Focus on runtime-facing derived outputs:
  - `data/simulation/scenarios/*.json`
  - `data/simulation/day_logs/*.json`
  - `data/simulation/multi_day_summary.json`
  - `data/simulation/tradeoff_matrix_results.json`
- Exclude support/config/reference families by default:
  - `data/simulation/components/**`
  - `data/simulation/models/**`
  - `data/simulation/parameters/**`
  - `data/simulation/species/**`
  - `data/simulation/species_evidence/**`
  - `data/simulation/_sync_backups/**`
- This note inventories current runtime shape only. It does not redesign schemas or promote derived fields into canonical business inputs.

## Files Reviewed

- Runtime-facing files scanned: `758`
  - `740` day logs
  - `16` scenario snapshots
  - `1` multi-day summary file with `7` flattened daily rows
  - `1` tradeoff-matrix file with `60` parameter-sweep rows
- Support/config/reference files present but excluded from the main census:
  - `2` support component files
  - `2` support model files
  - `2` support parameter files
  - `3` support species files
  - `5` support species-evidence files
  - `2` support misc files
  - `12` backup files
- Reusable helper used for the census:
  - `scripts/runtime_field_inventory.py`

## Runtime File Shape Summary

### `scenario_snapshot`

- Count: `16`
- Stable top-level shape:
  - `scenario_id`
  - `crop_system_type` on the current basil scenario path
  - `time`
  - `system`
  - `water_state`
  - `plant_crop`
  - `fish_batch`
  - `feeding`
  - `equipment`
  - `economics`
  - `operations_policy`
  - `nitrogen_model`
  - `derived`
  - `notes`
- Main use for adapter prep:
  - richest single-file source for scenario identity, plant state, fish state, water chemistry, and daily derived metrics
- Main caveat:
  - metadata and some `derived.*` fields are inconsistent in the two base scenario files versus the later day-by-day rollup snapshots

### `day_log`

- Count: `740`
- Stable top-level shape:
  - `day`
  - `scenario_file`
  - `saved_scenario_file`
  - `water_state_after`
  - `plant_crop_after`
  - `fish_batch_after`
  - `derived`
  - `overlap_assessment`
- Main use for adapter prep:
  - stable end-of-day observations with qualitative overlap/risk proxies
- Main caveat:
  - uses absolute Windows paths for file references and does not emit business-ready harvest or event rollups

### `multi_day_summary`

- Count: `1` file, `7` rows
- Shape:
  - flat per-day rows with `day`, `scenario_file`, pH/TAN/NH3/nitrate, fish biomass, plant biomass, daily operating cost, and stability score
- Main use:
  - quick summary/visualization input
- Main caveat:
  - currently lettuce-only and too flattened for the first adapter by itself

### `tradeoff_results`

- Count: `1` file, `60` rows
- Shape:
  - flat parameter-sweep rows over pH/temperature/mode scoring
- Main use:
  - research/tuning support
- Main caveat:
  - not a scenario-output family and not suitable as a first business adapter source

## Field Inventory by Category

### Scenario Identity and File Framing

| Field path | Label | Notes |
|---|---|---|
| `scenario_snapshot.scenario_id` | `common_stable` | Present in all `16` scenario snapshots. |
| `day_log.scenario_file` | `common_stable` | Absolute path to the pre-day scenario snapshot. Adapter should normalize basename only. |
| `day_log.saved_scenario_file` | `common_stable` | Absolute path to the post-day scenario snapshot. Useful for pairing logs to snapshots. |
| `multi_day_summary[].scenario_file` | `rare` | Present in all `7` rows, but only in one summary file and currently lettuce-only. |
| `scenario_snapshot.updated_at_utc` | `common_but_inconsistent` | Present in `15/16` snapshots. Missing from the basil base scenario file. |
| `scenario_snapshot.generated_at_utc` | `rare` | Present in `8/16` snapshots and only on the lettuce scenario family. |
| `run_id` | `missing_for_first_slice` | No explicit runtime field. Must be adapter-derived from file naming or invocation context. |
| `scenario_name` | `missing_for_first_slice` | No explicit human-readable scenario name. |

### Time Basis and Period Framing

| Field path | Label | Notes |
|---|---|---|
| `scenario_snapshot.time.day` | `common_stable` | Present in all scenario snapshots. |
| `scenario_snapshot.time.timestep` | `common_stable` | Present in all scenario snapshots. Current value is `daily`. |
| `scenario_snapshot.time.subdaily_safety_checks` | `common_stable` | Present in all scenario snapshots. |
| `day_log.day` | `common_stable` | Present in all day logs. |
| `multi_day_summary[].day` | `rare` | Stable inside the one summary file. |
| `period_start_utc` | `missing_for_first_slice` | No runtime output emits explicit simulated period start. |
| `period_end_utc` | `missing_for_first_slice` | `updated_at_utc` is save time metadata, not a simulated period end. |
| `time_basis` | `common_but_inconsistent` | Source artifacts mix `time.timestep = daily` with cumulative day-rollup file names. Adapter normalization is required. |

### Crop Identity, Biomass, and Growth

| Field path | Label | Notes |
|---|---|---|
| `scenario_snapshot.plant_crop.species_id` | `common_stable` | Stable crop identifier source. |
| `scenario_snapshot.plant_crop.plant_count` | `common_stable` | Standing plant count, not explicit planting count. |
| `scenario_snapshot.plant_crop.average_biomass_g` | `common_stable` | Standing biomass per plant, not saleable harvest mass. |
| `scenario_snapshot.plant_crop.days_since_transplant` | `common_stable` | Useful operational context only. |
| `scenario_snapshot.plant_crop.growth_stage` | `common_stable` | Useful context, not directly a business field. |
| `day_log.plant_crop_after.*` | `common_stable` | End-of-day equivalents of the scenario snapshot crop state. |
| `scenario_snapshot.derived.daily_plant_biomass_gain_g_per_plant` | `common_but_inconsistent` | Missing in the two base scenario files, present from day 1 onward. |
| `crop_system_type` | `common_but_inconsistent` | Present on the current basil scenario path as a context field, but not yet guaranteed across every runtime family. |
| `growing_area_m2` | `missing_for_first_slice` | No runtime field found. |
| `saleable_harvest_mass_kg` | `missing_for_first_slice` | Main first-slice blocker. No harvest rollup exists. |
| `harvest_event_count` / `first_harvest_utc` / `last_harvest_utc` | `missing_for_first_slice` | Only `operations_policy.harvest_policy = manual` exists, which is policy only. |

### Fish Identity, Counts, and Biomass

| Field path | Label | Notes |
|---|---|---|
| `scenario_snapshot.fish_batch.species_id` | `common_stable` | Stable fish identifier source. |
| `scenario_snapshot.fish_batch.count` | `common_stable` | Standing count, not harvested count. |
| `scenario_snapshot.fish_batch.total_biomass_kg` | `common_stable` | Standing biomass only. |
| `scenario_snapshot.fish_batch.average_weight_g` | `common_stable` | Stable per-fish weight field. |
| `scenario_snapshot.fish_batch.mortality_count` | `common_stable` | Useful later for fish-side business interpretation. |
| `day_log.fish_batch_after.*` | `common_stable` | End-of-day equivalents of the scenario snapshot fish state. |
| `scenario_snapshot.derived.daily_fish_biomass_gain_kg` | `common_but_inconsistent` | Missing in the two base scenario files, present from day 1 onward. |
| `multi_day_summary[].fish_biomass_kg` / `avg_fish_weight_g` | `rare` | Stable within the one summary file only. |
| `harvested_fish_biomass_kg` / `mortality_biomass_kg` | `missing_for_first_slice` | No fish harvest or mortality biomass rollups found. |

### Water Chemistry and Environment

| Field path | Label | Notes |
|---|---|---|
| `scenario_snapshot.water_state.pH` | `common_stable` | Direct candidate for `observed_pH` after flattening. |
| `scenario_snapshot.water_state.tan_mg_L` | `common_stable` | Direct candidate for `observed_tan_mg_l` after unit-string normalization. |
| `scenario_snapshot.water_state.unionized_nh3_mg_L` | `common_stable` | Direct candidate for `observed_unionized_nh3_mg_l`. |
| `scenario_snapshot.water_state.nitrate_mg_L` | `common_stable` | Direct candidate for `observed_nitrate_mg_l`. |
| `scenario_snapshot.water_state.nitrite_mg_L` | `common_stable` | Useful later, not required for the first slice contract. |
| `scenario_snapshot.water_state.dissolved_oxygen_mg_L` | `common_stable` | Useful later for risk or operations. |
| `scenario_snapshot.water_state.alkalinity_mg_L_as_CaCO3` | `common_stable` | Useful later for chemistry control. |
| `day_log.water_state_after.*` | `common_stable` | End-of-day equivalents of the scenario snapshot chemistry state. |
| `multi_day_summary[].pH` / `tan_mg_L` / `unionized_nh3_mg_L` / `nitrate_mg_L` | `rare` | Stable within the summary file, but flattened and lettuce-only. |
| `overlap_assessment.*` | `common_stable` | Runtime quality proxy only. See risk notes below. |

### Energy, Feed, and Derived Daily Metrics

| Field path | Label | Notes |
|---|---|---|
| `scenario_snapshot.derived.daily_energy_kwh` | `common_stable` | Present in all snapshots, but `null` in both base scenario files before day 1. |
| `scenario_snapshot.derived.daily_feed_kg` | `common_stable` | Present in all snapshots, but `null` in both base scenario files before day 1. |
| `scenario_snapshot.derived.daily_tan_input_mg_L_equivalent` | `common_stable` | Stable derived chemistry load input. |
| `scenario_snapshot.derived.system_stability_score` | `common_stable` | Stable score field, but not itself a business output. |
| `scenario_snapshot.derived.daily_operating_cost` | `common_but_inconsistent` | Missing in the two base scenario files and should not be promoted into canonical business costing. |
| `day_log.derived.*` | `common_stable` | Stable daily derived metrics across all day logs. |
| `multi_day_summary[].daily_operating_cost` | `rare` | Present only in the single summary file and should not be treated as canonical business cost. |

### Water Use, Supplements, and Dosing

| Field path | Label | Notes |
|---|---|---|
| `scenario_snapshot.operations_policy.water_top_up_l_per_day` | `common_stable` | `proxy_only_do_not_promote`. Policy/setting, not observed water use. |
| `scenario_snapshot.operations_policy.pH_control_enabled` | `common_stable` | Indicates control enabled, not actual dosing records. |
| `scenario_snapshot.operations_policy.base_dosing_enabled` | `common_stable` | Indicates control enabled, not actual supplementation quantities. |
| `water_use_l` | `missing_for_first_slice` | No observed water-use rollup found. |
| `supplement_input_records` | `missing_for_first_slice` | No actual dose event or dose quantity records found. |

### Harvest, Events, Downtime, and Quality/Risk

| Field path | Label | Notes |
|---|---|---|
| `scenario_snapshot.operations_policy.harvest_policy` | `common_stable` | `proxy_only_do_not_promote`. Policy only, not harvest observations. |
| `day_log.overlap_assessment.balance_score` | `common_stable` | `proxy_only_do_not_promote` for business risk/event outputs. |
| `day_log.overlap_assessment.nitrification_assessment.*` | `common_stable` | Qualitative status proxy, not event records. |
| `day_log.overlap_assessment.plant_tradeoff_warning.triggered/messages` | `common_stable` | Warning proxy only. |
| `quality_risk_event_records` | `missing_for_first_slice` | No explicit event record stream found. |
| `out_of_range_event_records` | `missing_for_first_slice` | No explicit out-of-range rollup found. |
| `downtime_event_count` | `missing_for_first_slice` | No explicit downtime field found. |
| `disease_or_pathogen_event_records` | `missing_for_first_slice` | No disease/pathogen event stream found. |

## Common Fields Across Runtime Outputs

These are the strongest cross-family adapter candidates, but they still need normalization because the same concept appears under different shapes.

| Concept | Scenario snapshots | Day logs | Multi-day summary | Label | Notes |
|---|---|---|---|---|---|
| Scenario reference | `scenario_id` | `scenario_file`, `saved_scenario_file` | `scenario_file` | `common_but_inconsistent` | Scenario snapshots use IDs; logs and summaries use absolute paths. |
| Day index | `time.day` | `day` | `day` | `common_but_inconsistent` | Same concept, different nesting. |
| pH | `water_state.pH` | `water_state_after.pH` | `pH` | `common_but_inconsistent` | Strong adapter candidate after flattening. |
| TAN | `water_state.tan_mg_L` | `water_state_after.tan_mg_L` | `tan_mg_L` | `common_but_inconsistent` | Strong adapter candidate after flattening and case normalization. |
| Unionized NH3 | `water_state.unionized_nh3_mg_L` | `water_state_after.unionized_nh3_mg_L` | `unionized_nh3_mg_L` | `common_but_inconsistent` | Strong adapter candidate after flattening and case normalization. |
| Nitrate | `water_state.nitrate_mg_L` | `water_state_after.nitrate_mg_L` | `nitrate_mg_L` | `common_but_inconsistent` | Strong adapter candidate after flattening and case normalization. |
| Plant biomass | `plant_crop.average_biomass_g` | `plant_crop_after.average_biomass_g` | `plant_avg_biomass_g` | `common_but_inconsistent` | Standing biomass only, not saleable harvest. |
| Daily energy | `derived.daily_energy_kwh` | `derived.daily_energy_kwh` | none | `common_stable` for scenario/day_log only | Usable for the first slice if the adapter picks one runtime family consistently. |

## Inconsistent or One-Off Fields

- `scenario_snapshot.updated_at_utc`: `15/16`
  - missing from the basil base scenario file
- `scenario_snapshot.generated_at_utc`: `8/16`
  - only the lettuce scenario family carries this metadata
- `scenario_snapshot.derived.daily_operating_cost`: `14/16`
  - absent from the two base scenario files
- `scenario_snapshot.derived.daily_fish_biomass_gain_kg`: `14/16`
  - absent from the two base scenario files
- `scenario_snapshot.derived.daily_plant_biomass_gain_g_per_plant`: `14/16`
  - absent from the two base scenario files
- `scenario_snapshot.derived.nitrate_availability_score`: `14/16`
  - absent from the two base scenario files
- `scenario_snapshot.derived.risk_score`: `2/16`
  - effectively a one-off field on the two base scenario files only
- `multi_day_summary`: one-off family
  - only one file exists and it is currently lettuce-only
- `tradeoff_matrix_results`: one-off family
  - stable internal shape, but it is a parameter sweep rather than a scenario-output family

## Missing Harvest/Event Rollup Observations

These are the most important gaps for the first business slice.

- No `saleable_harvest_mass_kg`
- No `cull_or_unsaleable_mass_kg`
- No `harvest_event_count`
- No `first_harvest_utc`
- No `last_harvest_utc`
- No observed `water_use_l`
- No `supplement_input_records`
- No `adjustment_event_count`
- No explicit `quality_risk_event_records`
- No explicit `out_of_range_event_records`
- No explicit `downtime_event_count`
- No explicit `disease_or_pathogen_event_records`

## Key Implications for Downstream Business Use

- The strongest adapter source family for the first slice is the cumulative `scenario_snapshot` family, because it contains scenario identity, crop state, fish state, chemistry, and daily derived metrics in one file.
- `day_log` files are stable and useful, but they add path-based run framing and qualitative overlap/risk proxies rather than solving the harvest-output gap.
- `multi_day_summary` and `tradeoff_matrix_results` are useful read-only analysis artifacts, but they should not be treated as the main adapter source for the first basil wholesale slice.
- Several runtime-side economics fields exist, but they are derived placeholders and `proxy_only_do_not_promote` for business-layer canon.
- The main first-slice blocker is not chemistry, identity, or energy; it is the missing harvest rollup needed to produce `saleable_harvest_mass_kg`.
