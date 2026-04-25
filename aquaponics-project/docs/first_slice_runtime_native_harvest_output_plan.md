# First Slice Runtime-Native Harvest Output Plan

Status: `draft`

## Purpose

- Define the smallest future runtime-native harvest-output path that could replace the reviewed-manual `saleable_harvest_mass_kg` bridge for the current first slice.
- Keep the analysis narrow to `basil bulk kg wholesale`.
- Separate the smallest acceptable runtime-native implementation from broader harvest-event redesign.

## What Is Already Solved

The current first slice already has:

- a fixed slice:
  - `basil bulk kg wholesale`
- a proven `crop_system_type` bridge from tracked config through regenerated basil `scenario_snapshot` output
- a thin adapter path that can carry `crop_system_type` as context
- a reviewed-manual override path for:
  - `saleable_harvest_mass_kg`

What is not solved:

- no runtime-native harvest output currently provides `saleable_harvest_mass_kg`
- the reviewed-manual path remains paused because approval of a non-null example value is currently withheld

## Why the Reviewed-Manual Path Is Paused

- No approved non-null reviewed-manual example value currently exists in the repo for the first reviewed run.
- The current approval packet explicitly records:
  - `approval withheld, continue using null`
- That means the repo still lacks a usable non-null first-slice harvest value, even though the run path for manual override exists.

Practical result:

- `saleable_harvest_mass_kg` remains the main blocker for a true runtime-to-business first-slice example output

## What Future Runtime-Native Harvest Output Must Provide

For the first slice, future runtime-native harvest output must provide harvest information that is:

- explicit
- expressed in kilograms
- specific to harvested saleable mass
- clearly distinguishable from standing crop state

Minimum semantic requirement:

- the runtime-facing output must make it clear that the field refers to harvested saleable basil mass for the run, not current standing biomass, growth rate, or plant count

## Smallest Acceptable Runtime-Native Options

### Option 1. Direct runtime-native `saleable_harvest_mass_kg`

Minimum output field:

- `saleable_harvest_mass_kg`

Minimum location:

- the runtime-facing basil `scenario_snapshot` family, or another equally direct runtime-facing output consumed by the first-slice adapter

Why this is acceptable:

- one field is enough to satisfy the first slice
- it is the smallest runtime-native shape that can retire the reviewed-manual bridge
- the adapter can consume it directly without broader redesign

### Option 2. Explicit harvest observations supporting rollup

Minimum explicit upstream fields:

- `harvested_mass_kg`
- `saleable_harvest_mass_kg`
- `cull_or_unsaleable_mass_kg`

Minimum requirement:

- these must be explicit harvest observations or explicit harvest totals
- they must not be derived implicitly from standing biomass, daily gain, or plant count

Why this is acceptable later:

- it gives enough distinction to support a safe adapter-side rollup
- it separates harvested mass, saleable mass, and non-saleable mass clearly

### Option 3. Broader harvest-event framework

Current status:

- deferred

Why:

- it is larger than the first slice needs
- it is not the smallest acceptable path for replacing the reviewed-manual bridge

## Best Current Future Direction

Best current future direction:

- direct runtime-native `saleable_harvest_mass_kg`

Why this is the best future fit:

- it is the smallest field contract that satisfies the first slice directly
- it avoids introducing a broad event framework just to retire one manual bridge
- it lets the adapter remain thin
- it matches the current first-slice need more closely than a generalized harvest-event system

Exact minimum output field that would satisfy the first slice:

- `saleable_harvest_mass_kg`

Exact minimum conditions to retire the reviewed-manual bridge:

1. the runtime-facing output emits non-manual `saleable_harvest_mass_kg`
2. the field is clearly defined as harvested saleable mass in kilograms for the run
3. the field is not inferred from standing biomass, daily gain, or plant count
4. the adapter can read it directly from runtime-facing output for the same basil run path

## What Should Not Be Done

- do not infer `saleable_harvest_mass_kg` from standing biomass
- do not infer it from `daily_plant_biomass_gain_g_per_plant`
- do not infer it from `plant_count`
- do not add a broad harvest-event framework if one bounded field can satisfy the first slice
- do not recommend adapter-side rollup unless upstream observation fields explicitly distinguish:
  - harvested mass
  - saleable mass
  - non-saleable mass
- do not mix this pass with broader simulation redesign

## What Remains Deferred

- first/last harvest timestamps
- harvest event counts
- broader harvest-event vocabularies
- timing-rich or multi-channel harvest interpretation
- wider adapter redesign
- canon changes

These remain useful later, but they are not the minimum requirement for replacing the reviewed-manual bridge for the first slice.

## Smallest Future Implementation Order

1. Choose one bounded runtime-facing output target for the basil first-slice path.
2. Add the smallest direct harvest field if feasible:
   - `saleable_harvest_mass_kg`
3. If direct output is not feasible, add explicit upstream harvest observations with at least:
   - `harvested_mass_kg`
   - `saleable_harvest_mass_kg`
   - `cull_or_unsaleable_mass_kg`
4. Keep the adapter thin:
   - direct consume the field if Option 1 is used
   - use rollup only if Option 2 fields are explicit enough
5. Retire the reviewed-manual bridge for the first slice only after one of those upstream paths is real and reviewable.

## Recommended Next Action

- Plan one future bounded runtime pass aimed first at direct runtime-native `saleable_harvest_mass_kg`.
- Treat that single field as the preferred minimum harvest-output contract for `basil bulk kg wholesale`.
- If a direct field cannot be added cleanly, use the next-smallest acceptable shape:
  - explicit harvest observations with `harvested_mass_kg`, `saleable_harvest_mass_kg`, and `cull_or_unsaleable_mass_kg`
- Keep broader harvest-event redesign deferred until the first slice actually needs it.
