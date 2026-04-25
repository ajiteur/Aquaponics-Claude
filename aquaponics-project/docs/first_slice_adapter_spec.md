# First Slice Adapter Spec

Status: `draft`

## Purpose

- Define the smallest viable adapter-prep target for the first business slice without changing canonical biology, simulation, or business files.
- Make the minimum required adapter outputs explicit for `basil bulk kg wholesale`.
- Separate direct renames and flattenings from slice-config inputs, missing fields, and fields that must remain null or deferred.

## First Slice Chosen

- `basil bulk kg wholesale`

## Required Adapter Outputs for First Slice

These are the minimum outputs the adapter should aim to emit for a reviewable first slice.

| Business field | Status | Notes |
|---|---|---|
| `scenario_id` | `direct rename/flattening` | Available directly from `scenario_snapshot.scenario_id`. |
| `run_id` | `inconsistent` | Must be adapter-derived. No explicit runtime field exists. |
| `scenario_name` | `slice-config required` | Humanized label only. No runtime field exists. |
| `time_basis` | `inconsistent` | Runtime says `daily`, but cumulative scenario files behave like rollup snapshots. |
| `crop_id` | `direct rename/flattening` | From `plant_crop.species_id` or `plant_crop_after.species_id`. |
| `product_id` | `slice-config required` | For this slice: `basil`. |
| `channel_id` | `slice-config required` | For this slice: `channel_wholesale`. |
| `saleable_harvest_mass_kg` | `missing` | Main blocker. No current runtime output provides this. |
| `observed_pH` | `direct rename/flattening` | From `water_state.pH` or `water_state_after.pH`. |
| `observed_tan_mg_l` | `direct rename/flattening` | From `water_state.tan_mg_L` or `water_state_after.tan_mg_L`. |
| `observed_unionized_nh3_mg_l` | `direct rename/flattening` | From `water_state.unionized_nh3_mg_L` or `water_state_after.unionized_nh3_mg_L`. |
| `observed_nitrate_mg_l` | `direct rename/flattening` | From `water_state.nitrate_mg_L` or `water_state_after.nitrate_mg_L`. |
| `energy_kwh` | `direct rename/flattening` | From `derived.daily_energy_kwh`. |
| `operating_day_count` | `direct rename/flattening` | Adapter convenience field from `time.day` or `day`. Useful if early shared labor is included. |

## Candidate Runtime Source Fields

### Preferred primary source family

- Use the cumulative basil `scenario_snapshot` file as the primary adapter input.
- Example:
  - `data/simulation/scenarios/starter_tilapia_basil_system_day_1_day_2_day_3_day_4_day_5_day_6_day_7.json`

Why this is the smallest viable source:

- it already contains `scenario_id`
- it contains the current crop/fish/water state in one file
- it exposes the daily derived energy/feed/gain metrics needed for the narrow slice
- it avoids depending on day-log-only path pairing unless later needed for run framing

### Optional paired source

- A matching `day_log` can still be paired later if the adapter wants:
  - a deterministic timestamp-like token from the log filename for `run_id`
  - overlap/risk proxy inspection for future diagnostics

## Fields That Are Direct Renames/Flattenings

| Adapter output | Current runtime source | Notes |
|---|---|---|
| `scenario_id` | `scenario_snapshot.scenario_id` | Already emitted exactly. |
| `crop_id` | `scenario_snapshot.plant_crop.species_id` | No translation needed beyond flattening. |
| `live_plant_count_end` | `scenario_snapshot.plant_crop.plant_count` | Usable as standing end-of-period count only. |
| `observed_pH` | `scenario_snapshot.water_state.pH` | Direct flattening. |
| `observed_tan_mg_l` | `scenario_snapshot.water_state.tan_mg_L` | Normalize `mg_L` to business-layer naming. |
| `observed_unionized_nh3_mg_l` | `scenario_snapshot.water_state.unionized_nh3_mg_L` | Normalize case only. |
| `observed_nitrate_mg_l` | `scenario_snapshot.water_state.nitrate_mg_L` | Normalize case only. |
| `energy_kwh` | `scenario_snapshot.derived.daily_energy_kwh` | Direct flattening from the chosen rollup snapshot. |
| `operating_day_count` | `scenario_snapshot.time.day` | Convenience adapter output, not a contract field. |
| `crop_system_type` | `scenario_snapshot.crop_system_type` | Direct carry-through context field only. |

## Fields That Require Slice-Config Inputs

| Adapter output | Status | Why |
|---|---|---|
| `product_id = basil` | `slice-config required` | Runtime emits `plant_basil`, but the first slice chooses the product interpretation explicitly. |
| `channel_id = channel_wholesale` | `slice-config required` | Channel is a business slice choice, not a runtime observation. |
| `scenario_name` | `slice-config required` | Runtime emits IDs and paths, not a human-readable scenario label. |
| `time_basis = scenario_rollup` | `slice-config required` | Current cumulative scenario file names behave like rollup snapshots even though `time.timestep` is `daily`. |

## Fields Still Missing

| Adapter output | Status | Notes |
|---|---|---|
| `saleable_harvest_mass_kg` | `missing` | Main blocker for `basil bulk kg wholesale`. |
| `growing_area_m2` | `missing` | Useful later for area-normalized reporting, labor, and CAPEX views. |
| `water_use_l` | `missing` | Only `operations_policy.water_top_up_l_per_day` exists, which is `proxy_only_do_not_promote`. |
| `supplement_input_records` | `missing` | Only boolean dosing-policy flags exist. |
| `harvest_event_count` | `missing` | `harvest_policy = manual` is policy only. |
| `first_harvest_utc` / `last_harvest_utc` | `missing` | No harvest timing records found. |
| `period_start_utc` / `period_end_utc` | `missing` | No explicit simulated UTC period framing exists. |

## Explicit Blocker List

- `saleable_harvest_mass_kg` is missing from all current runtime-facing output families.
- Runtime outputs are state snapshots and daily assessments, not harvest rollups.
- `time_basis` needs a translation decision because the chosen file family mixes daily timestep metadata with cumulative rollup naming.
- `run_id` is not emitted as a stable runtime field and must be derived outside canonical simulation files.

## Smallest Viable Adapter Behavior

The smallest first adapter should do only this:

1. take one cumulative basil `scenario_snapshot` file as input
2. flatten the required chemistry, crop, and energy fields into business-layer names
3. inject explicit slice-config values for:
   - `product_id = basil`
   - `channel_id = channel_wholesale`
   - `time_basis = scenario_rollup`
4. derive a deterministic `run_id` from adapter context or from the chosen file basename rule
5. leave missing harvest/event/water/supplement fields null or deferred
6. stop before any pricing, labor, or cost-rate population

This keeps the adapter thin and reviewable.

## What Must Remain Null/Deferred

| Field | Status | Why |
|---|---|---|
| `saleable_harvest_mass_kg` | `missing` | Do not infer from standing biomass or daily gain. |
| `cull_or_unsaleable_mass_kg` | `deferred` | No current runtime source. |
| `harvest_event_count` | `deferred` | No event rollup exists. |
| `first_harvest_utc` / `last_harvest_utc` | `deferred` | No event timing exists. |
| `water_use_l` | `deferred` | Top-up policy is not the same as observed use. |
| `supplement_input_records` | `deferred` | Control flags are not dose records. |
| `adjustment_event_count` | `deferred` | No adjustment event stream exists. |
| `quality_risk_event_records` / `out_of_range_event_records` / `downtime_event_count` / `disease_or_pathogen_event_records` | `deferred` | Current overlap scores and warnings are proxies, not event records. |

## What Should NOT Be Invented Inside Canonical Files

- Do not backfill `saleable_harvest_mass_kg` into canonical biology or simulation files.
- Do not convert `operations_policy.water_top_up_l_per_day` into canonical observed `water_use_l`.
- Do not treat runtime `economics.*` or `derived.daily_operating_cost` as canonical business inputs.
- Do not promote overlap-assessment scores into business risk event records without an explicit translation rule.
- Do not rewrite business-layer contract or business JSON just to match current runtime field gaps.

## Notes and Cautions

- The current runtime audit already shows that chemistry, identity, and energy are mostly adapter-ready; harvest rollup is the real blocker.
- Absolute Windows paths in `scenario_file` and `saved_scenario_file` should be normalized to basename or repo-relative references inside adapter logic.
- `plant_crop.plant_count` is only a first-pass proxy for both `planting_count` and `live_plant_count_end`; it should not be treated as a proven lifetime count field once harvesting starts.
- This note is adapter prep only. It does not activate deferred business rules or populate any business rates.
