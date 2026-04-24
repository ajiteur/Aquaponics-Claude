# First Slice Saleable Harvest Mass Run Path

Status: `draft`

## Purpose

- Define the smallest safe way to use a reviewed manual `saleable_harvest_mass_kg` in the current first-slice run path.
- Keep the path explicit about what is manual review input versus what is runtime-native output.
- Avoid widening the current first-slice flow beyond what is needed for one reviewable basil wholesale run.

## What Is Already Solved

The current first-slice path already has:

- a fixed slice:
  - `basil bulk kg wholesale`
- a proven runtime-to-adapter path for the basil `scenario_snapshot` family
- a completed `crop_system_type` bridge carried through as context
- an adapter script that already accepts an overrides file
- an override slot for:
  - `saleable_harvest_mass_kg`

That means the next question is not whether the run path can accept a manual harvest value in principle.
The question is how to use that value safely without pretending it came from runtime output.

## Current Run-Path Components

The current narrow run path is:

1. one cumulative basil `scenario_snapshot` file
   - example:
     - `data/simulation/scenarios/starter_tilapia_basil_system_day_1_day_2_day_3_day_4_day_5_day_6_day_7.json`
2. one thin adapter script
   - `scripts/build_first_slice_adapter_payload.py`
3. one optional overrides file
   - `scripts/example_first_slice_overrides.json`
4. one reviewable adapter payload emitted to stdout
5. later business interpretation or working-input use outside canonical files

Current relevant detail:

- `scripts/example_first_slice_overrides.json` already includes:
  - `saleable_harvest_mass_kg`
- current example value is:
  - `null`

## Where Reviewed Manual `saleable_harvest_mass_kg` Should Enter

Reviewed manual `saleable_harvest_mass_kg` should enter at:

- the adapter override layer

More specifically:

- pass it through the overrides object consumed by `scripts/build_first_slice_adapter_payload.py`
- keep the source runtime `scenario_snapshot` unchanged
- keep the value explicit as a reviewed manual bridge input, not a runtime observation

Why this is the right insertion point:

- it matches the current bridge decision
- it keeps the manual bridge outside canonical files
- it avoids implying that current runtime state already contains harvest output

## Whether the Current Adapter/Override Path Already Supports It Cleanly

Current status:

- `already supported`

Why:

- `scripts/build_first_slice_adapter_payload.py` already reads an optional `--overrides` JSON file
- the script already emits:
  - `saleable_harvest_mass_kg: overrides.get("saleable_harvest_mass_kg")`
- `scripts/example_first_slice_overrides.json` already contains the field

Current implication:

- no adapter redesign is needed to accept a reviewed manual `saleable_harvest_mass_kg`
- the current example override file simply leaves that field as `null`

## If Not, What the Smallest Safe Adjustment Would Be

Current status:

- `no adjustment needed` for the adapter/override mechanism itself

Smallest safe practical adjustment for a real reviewed run:

- provide one reviewed manual value in a run-specific override file or reviewed copy of the example override file
- keep the field name unchanged:
  - `saleable_harvest_mass_kg`
- keep all other adapter behavior unchanged

What is still deferred:

- any runtime-native harvest output
- any adapter-side harvest rollup
- any broader event redesign

## What Provenance or Review Note Must Accompany the Value

The reviewed manual value must carry a review note outside canonical files that states:

- the value is:
  - `reviewed_manual_input`
- the slice is:
  - `basil bulk kg wholesale`
- the value is not runtime-native
- the review basis used to choose the value
- the scenario or run it applies to
- the date of review

Minimum provenance expectation:

- one explicit note in the run artifact, override file companion note, or review doc that distinguishes:
  - reviewed manual bridge input
  - current runtime output

Why this matters:

- it prevents manual bridge input from being mistaken for harvested mass observed by the simulation
- it limits drift and keeps the bridge reviewable

## What Must Remain Unchanged

- current slice remains `basil bulk kg wholesale`
- `saleable_harvest_mass_kg` remains reviewed manual input or `null` only
- standing biomass, daily gain, and plant count must not be used as harvest substitutes
- runtime files must remain unchanged
- canonical biology/model/business files must remain unchanged
- the adapter must not inject fallback harvest values
- no broader first-slice flow redesign is needed

## Recommended Next Action

- Use the existing adapter override path for the first reviewed manual `saleable_harvest_mass_kg` run.
- Keep `scripts/build_first_slice_adapter_payload.py` unchanged for this purpose.
- For the actual reviewed run, replace `null` with one reviewed manual `saleable_harvest_mass_kg` value in a run-scoped overrides file.
- Attach a short provenance/review note that explicitly says the value is reviewed manual bridge input, not runtime-native harvest output.
- Leave runtime-native harvest output and any later adapter-side rollup as separate deferred work.
