# First Vertical Slice Choice

Status: `draft`

## Purpose

- Make the first vertical slice decision explicit and reviewable.
- Keep the first business-layer proof narrow enough to inspect end to end.

## Current Objective

- Build one narrow, reviewable first vertical slice from runtime outputs to business interpretation.

## Candidate Slices Considered

- `basil bulk kg wholesale`
- `tilapia kg wholesale`
- count-based or bunch-based plant slices such as lettuce heads or basil bunches

## Chosen Slice

- `basil bulk kg wholesale`

## Why This Slice Wins Now

- It already aligns with an active direct-mass path in the current business-layer scaffolding.
- It avoids head-count, bunch-count, delivery-timing, and architecture-advisory complexity.
- It keeps the first adapter focused on runtime identity, chemistry, energy, and one explicit saleable-mass bridge.
- It avoids the extra fish price-basis ambiguity still present in the first tilapia path.

## What This Slice Intentionally Avoids

- lettuce head-count or bunch-count translation
- fish harvest and fish product-form decisions
- architecture-conditioned output-form guidance
- risk-penalty activation
- cash timing, delivery timing, and order timing logic
- broader multi-channel expansion

## Required Inputs for the Slice

### Required now

- `scenario_id`
- adapter-stable `run_id`
- `time_basis`
- `crop_id`
- `product_id = basil`
- `channel_id = channel_wholesale`
- `saleable_harvest_mass_kg`
- `observed_pH`
- `observed_tan_mg_l`
- `observed_unionized_nh3_mg_l`
- `observed_nitrate_mg_l`
- `energy_kwh`
- `operating_day_count`

### Slice-config required

- `product_id`
- `channel_id`
- `scenario_name`
- `time_basis`

### Missing or bridge-required

- `saleable_harvest_mass_kg`

## What Remains Deferred

- `cull_or_unsaleable_mass_kg`
- `harvest_event_count`
- `first_harvest_utc`
- `last_harvest_utc`
- `water_use_l`
- `supplement_input_records`
- `adjustment_event_count`
- `quality_risk_event_records`
- `out_of_range_event_records`
- `downtime_event_count`
- `disease_or_pathogen_event_records`
- area- and architecture-aware extensions such as `growing_area_m2` and `crop_system_type`

## Definition of Done for First-Slice Proof

- The chosen slice is explicitly fixed as `basil bulk kg wholesale`.
- One thin adapter can emit a reviewable first-slice payload from a basil runtime scenario snapshot.
- Adapter-ready runtime fields are flattened into business-layer names without changing canonical runtime or business files.
- `saleable_harvest_mass_kg` is handled by an explicit temporary bridge or remains explicit `null`.
- Missing and deferred fields remain explicit rather than invented.
- The output is reviewable enough to support the next pass that populates one narrow pricing, cost, and labor path.
