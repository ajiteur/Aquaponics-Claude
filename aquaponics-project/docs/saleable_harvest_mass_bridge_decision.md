# Saleable Harvest Mass Bridge Decision

Status: `draft`

## Purpose

- Decide how the first slice will temporarily handle `saleable_harvest_mass_kg`.
- Keep the bridge conservative until runtime harvest outputs become explicit.

## Current Constraint

- `saleable_harvest_mass_kg` is required for the `basil bulk kg wholesale` slice.
- Current runtime outputs do not emit harvest-event rollups.
- Standing biomass and daily biomass gain are not the same thing as saleable harvest mass and must not be promoted as a substitute.

## Options Considered

### 1. Manual reviewed first-slice input

What it is:

- A reviewed, non-canonical input supplied to the adapter as an override for one first-slice payload.

Pros:

- Most conservative option available now.
- Keeps the temporary bridge explicit and reviewable.
- Avoids pretending that current runtime files already contain harvest outputs.
- Does not require canonical biology, simulation, or business-file changes.

Risks:

- Adds a manual step.
- Can drift if the review basis is not documented outside the payload run.
- Not suitable as the long-term runtime-to-business bridge.

What it assumes:

- A reviewer can supply a case-specific saleable harvest mass from outside canonical files.
- The value is treated as temporary bridge input, not as runtime truth.

Acceptable for the first slice now:

- `yes`

### 2. Adapter-side derived harvest rollup

What it is:

- The adapter computes `saleable_harvest_mass_kg` from upstream harvest observations or harvest-event records.

Pros:

- Eventually becomes more reusable than manual one-off input.
- Keeps bridge logic outside canonical files.
- Can later absorb explicit harvest events without redesigning the business layer.

Risks:

- Not defensible now because the required upstream harvest observations do not exist yet.
- Would encourage hidden inference if forced too early.
- Risks collapsing standing biomass into harvested mass, which this pass should avoid.

What it assumes:

- Future upstream runtime outputs will expose harvest-event or saleable-harvest data that can be rolled up explicitly.

Acceptable for the first slice now:

- `no`

### 3. Future runtime harvest-event output

What it is:

- A later runtime-side improvement where simulation outputs include explicit harvest events and saleable harvest rollups.

Pros:

- Best eventual source of truth for adapter-side harvest translation.
- Removes the need for manual override once upstream outputs become explicit.
- Supports later timing, cull, and event-count extensions cleanly.

Risks:

- Not available now.
- Would broaden this pass into runtime-output redesign if attempted immediately.

What it assumes:

- Future runtime work will add explicit harvest observations with stable shape and units.

Acceptable for the first slice now:

- `no`

## Recommended Temporary Bridge for the First Slice

- Use `manual reviewed first-slice input` as the temporary bridge.
- Pass it to the thin adapter as an explicit override value for `saleable_harvest_mass_kg`.
- If no reviewed override is available, emit `saleable_harvest_mass_kg = null` and keep the first payload reviewable rather than invented.

## What To Do Later When Runtime Harvest Outputs Improve

- Replace the manual override path with an adapter-side harvest rollup over explicit runtime harvest observations.
- Keep the rollup outside canonical business and biology files.
- Continue to treat standing biomass, growth score, and daily biomass gain as non-harvest proxies unless runtime outputs explicitly say otherwise.
