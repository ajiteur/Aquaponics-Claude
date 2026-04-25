# First Slice Reviewed Manual Harvest Value Approval Packet

Status: `draft`

## Purpose

- Prepare the smallest safe review packet for a human to approve one non-null `saleable_harvest_mass_kg` for the current first reviewed-manual example run.
- Keep the packet narrow to one example run for `basil bulk kg wholesale`.
- Keep the approval explicit, non-canonical, and separate from runtime-native output.

## Exact Scenario/Run This Applies To

This approval packet applies only to:

- slice:
  - `basil bulk kg wholesale`
- runtime scenario path:
  - `data/simulation/scenarios/starter_tilapia_basil_system_day_1_day_2_day_3_day_4_day_5_day_6_day_7.json`
- adapter:
  - `scripts/build_first_slice_adapter_payload.py`
- reviewed-manual override target:
  - `scripts/example_first_slice_reviewed_manual_overrides.json`

Scope limit:

- one reviewed-manual value for one example run only

## Exact Field Needing Approval

Field:

- `saleable_harvest_mass_kg`

Unit:

- kilograms

Scope:

- one reviewed-manual value for one example run only

Current status:

- no approved non-null example value is currently present in the repo

Current recorded outcome:

- `approval withheld, continue using null`

## What the Approved Value Must Mean

If approved, the value must mean:

- saleable harvested mass
- in kilograms
- for the exact example run named above
- for `basil bulk kg wholesale`
- not standing biomass
- not daily biomass gain
- not plant count
- not unsaleable or culled mass

## What Evidence/Review Basis Is Acceptable

Acceptable review basis can include:

- a reviewed manual calculation or estimate tied to the exact example run
- reviewed notes that clearly distinguish harvested saleable mass from standing crop state
- reviewed run-specific reasoning documented in plain language

Required placeholders:

- evidence source/reference:
  - `____________________________`
- short approval rationale:
  - `____________________________`

## What Must Not Be Used as a Substitute

Do not approve a value based on:

- standing biomass
- daily biomass gain
- plant count
- generic basil yield assumptions with no run-specific review basis
- a value copied from canonical business, biology, or runtime files as if it were already observed harvest output

## Approval Checklist

- [ ] The slice is confirmed as `basil bulk kg wholesale`.
- [ ] The exact run is confirmed as the 7-day `starter_tilapia_basil_system` example scenario chain.
- [ ] The approved field is exactly `saleable_harvest_mass_kg`.
- [ ] The unit is kilograms.
- [ ] The value refers to saleable harvested mass only.
- [ ] The value is not inferred from standing biomass, daily gain, or plant count.
- [ ] The evidence source/reference is recorded.
- [ ] A short approval rationale is recorded.
- [ ] The reviewer understands the value is reviewed-manual input, not runtime-native output.
- [ ] If approved, the value will be copied only into `scripts/example_first_slice_reviewed_manual_overrides.json`.
- [ ] If approval is withheld, the override remains `null`.

## Placeholder for Approved Value

Approved value for `saleable_harvest_mass_kg`:

- `________________ kg`

Outcome path:

- `approved with value`
- or `approval withheld, continue using null`

## Placeholder for Reviewer/Date

- reviewer:
  - `pending named human reviewer`
- date:
  - `2026-04-24`
- evidence source/reference:
  - `________________`
- short approval rationale:
  - `No explicit human-approved non-null example value exists yet for this exact reviewed-manual example run.`

## Why This Approved Value Is Still Non-Canonical

Even if approved, this value remains:

- reviewed-manual bridge input
- run-scoped
- non-canonical

It must not be copied into:

- runtime files
- canonical biology files
- canonical model files
- canonical business files

## What This Approval Unlocks

This approval unlocks only:

- replacing `saleable_harvest_mass_kg: null` in `scripts/example_first_slice_reviewed_manual_overrides.json` for this one example run
- running the current adapter override flow with one explicit reviewed-manual harvest value

It does not unlock:

- runtime-native harvest output
- harvest-event redesign
- canon promotion
- broader economics changes

## Recommended Next Action After Approval

- If approved, copy the approved value only into `scripts/example_first_slice_reviewed_manual_overrides.json`.
- Keep the companion review note with the approved value, reviewer, date, evidence source/reference, and short rationale.
- If approval is withheld, continue using `saleable_harvest_mass_kg: null`.
