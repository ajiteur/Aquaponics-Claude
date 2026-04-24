# First Slice Saleable Harvest Mass Plan

Status: `draft`

## Purpose

- Define the smallest safe next bridge for `saleable_harvest_mass_kg` for the current first slice.
- Keep the plan narrow to `basil bulk kg wholesale`.
- Separate what is acceptable now from what should wait for stronger runtime output.

## What Is Already Solved

The first slice already has:

- a locked slice choice:
  - `basil bulk kg wholesale`
- a proven `crop_system_type` bridge from tracked config through runtime-facing basil `scenario_snapshot` output
- a thin adapter path that can now carry `crop_system_type` through as context
- a working-input-pack position that keeps `saleable_harvest_mass_kg` explicit, nullable, and outside canon unless reviewed

That means the first bridge after architecture context is no longer `crop_system_type`.
It is `saleable_harvest_mass_kg`.

## Why `saleable_harvest_mass_kg` Is Now the Main Blocker

- `saleable_harvest_mass_kg` is still required for the current first slice.
- The runtime audit still marks it as `missing` and as the main blocker for `basil bulk kg wholesale`.
- The current adapter spec still treats it as missing from all runtime-facing output families.
- Current simulation files expose standing plant biomass and daily biomass gain, not saleable harvested mass.

Why that matters:

- the first slice is priced on saleable kg
- contribution-margin and break-even interpretation cannot become a true runtime-to-business output without an explicit saleable harvest bridge

## Current Acceptable Bridge Options

### 1. Reviewed manual bridge input

What it is:

- one explicit reviewed override value supplied to the adapter for `saleable_harvest_mass_kg`

Current acceptability:

- `yes`

Why it is acceptable now:

- it is the most conservative near-term bridge
- it keeps the missing field explicit
- it does not pretend current runtime state equals harvest output
- it matches the current working-input-pack and bridge-decision posture

### 2. Adapter-side rollup possibility

What it is:

- a later adapter calculation over explicit upstream harvest observations

Current acceptability:

- `not yet`

Why not yet:

- the required upstream harvest observations do not exist in the current first-slice runtime path
- forcing this now would invite hidden inference from standing biomass or daily gain

### 3. Runtime-native future output

What it is:

- a later runtime-facing output that emits saleable harvest directly or emits explicit harvest observations cleanly enough for a rollup

Current acceptability:

- `future target only`

Why:

- it is the strongest long-term bridge
- it is not available now without broadening into runtime-output work

## Best Current Near-Term Option

Best current near-term option:

- `reviewed manual bridge input`

Recommended meaning:

- pass `saleable_harvest_mass_kg` into the first-slice adapter as an explicit reviewed override
- use it only for the current first-slice run or reviewed example run
- keep provenance and review basis explicit outside canonical files

If no reviewed value exists:

- keep `saleable_harvest_mass_kg = null`
- do not invent it from runtime proxies

## What a Later Stronger Runtime-Native Option Would Look Like

The later stronger option should look like one of these:

### Direct runtime-native output

- runtime-facing basil output emits:
  - `saleable_harvest_mass_kg`

Why this is strongest:

- simplest adapter consumption path
- least ambiguity about what was harvested and what was saleable

### Explicit upstream harvest observations that support adapter-side rollup

- runtime-facing basil output emits explicit harvest records or harvest totals with enough clarity to roll up:
  - harvested mass
  - saleable mass
  - optional cull or unsaleable mass later

Why this is still acceptable later:

- keeps rollup logic outside canonical business files
- can support later event counts and timing without redesigning the business layer first

## What Should Not Be Done

- do not infer `saleable_harvest_mass_kg` from standing biomass
- do not infer it from `daily_plant_biomass_gain_g_per_plant`
- do not derive it from `plant_count`
- do not mix this pass with a broad harvest-event redesign unless a later bounded pass explicitly calls for it
- do not backfill `saleable_harvest_mass_kg` into canonical biology, model, or business files
- do not hide a manual value as if it were runtime-native truth

## Smallest Safe Next Implementation Direction

The smallest safe next direction is:

1. keep the runtime bridge unchanged for now
2. keep the adapter thin
3. add one explicit reviewed-manual override path for `saleable_harvest_mass_kg` in the first-slice adapter flow if it is not already present in the chosen run path
4. document the review basis for that manual value with the working calculation inputs
5. continue to emit `null` when no reviewed manual value is available

Why this is the smallest safe move:

- it unblocks the first real reviewable runtime-to-business slice without pretending runtime harvest output already exists
- it does not require runtime redesign
- it preserves a clean later upgrade path to runtime-native harvest output

## Recommended Next Action

- use `reviewed manual bridge input` as the next first-slice bridge for `saleable_harvest_mass_kg`
- keep that input explicit, non-canonical, and review-scoped
- only after that, plan one later bounded pass for either:
  - direct runtime-native `saleable_harvest_mass_kg`, or
  - explicit harvest observations that support adapter-side rollup

Until one of those stronger upstream outputs exists, `saleable_harvest_mass_kg` should remain reviewed-manual input or `null`, never inferred from standing biomass or daily gain.
