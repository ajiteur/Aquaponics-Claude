# First Slice Reviewed Manual Run Note

Status: `draft`

## Purpose

- Define the smallest safe repo-local structure for one reviewed-manual `saleable_harvest_mass_kg` example run.
- Keep the example explicit, non-canonical, and review-scoped.
- Prevent a manual bridge value from being mistaken for runtime-native harvest output.

## Scope

- Slice is fixed as `basil bulk kg wholesale`.
- This note applies only to the reviewed-manual bridge path for the first slice.
- This note does not approve a harvest value by itself.

## Current Example Run Target

This reviewed-manual override is prepared for the current first-slice example run path using:

- runtime scenario family:
  - `data/simulation/scenarios/starter_tilapia_basil_system_day_1_day_2_day_3_day_4_day_5_day_6_day_7.json`
- adapter:
  - `scripts/build_first_slice_adapter_payload.py`
- reviewed-manual override file:
  - `scripts/example_first_slice_reviewed_manual_overrides.json`

## Current Override Status

- `saleable_harvest_mass_kg` in `scripts/example_first_slice_reviewed_manual_overrides.json` is currently:
  - `null`

Reason:

- no explicitly approved non-null example value was found in the current repo
- this file is therefore prepared as a non-final reviewed-manual run scaffold, not as a completed reviewed run

## What `saleable_harvest_mass_kg` Means Here

- `saleable_harvest_mass_kg` is reviewed manual bridge input
- it is not runtime-native output
- it must not be treated as if the simulation already emitted harvest mass

## What Must Be Reviewed Before Replacing the Placeholder

Before replacing `null` with a real example value, review all of the following:

- the exact scenario or run the value applies to
- the basis for the reviewed manual harvest estimate
- whether the value refers to:
  - saleable harvested mass
  - not standing biomass
  - not unsaleable or culled mass
- whether the value matches the intended product interpretation:
  - `basil bulk kg wholesale`
- the date and reviewer responsible for the manual bridge value

## What Must Not Be Used as Harvest Substitutes

Do not replace `saleable_harvest_mass_kg` with values inferred from:

- standing biomass
- daily biomass gain
- plant count

Those are not acceptable harvest substitutes for the current first slice.

## What Must Remain Unchanged

- the value remains non-canonical
- the value remains reviewed-manual input or `null` only
- runtime files remain unchanged
- canonical biology/model/business files remain unchanged
- pricing, labor, cost, and harvest logic remain unchanged

## Recommended Use

- Keep `scripts/example_first_slice_reviewed_manual_overrides.json` as the run-scoped example override file for the first reviewed-manual harvest-mass run.
- Replace `saleable_harvest_mass_kg: null` only after human review supplies an explicit approved example value.
- Keep a short companion review record that states the value is reviewed manual bridge input, not runtime-native output.
