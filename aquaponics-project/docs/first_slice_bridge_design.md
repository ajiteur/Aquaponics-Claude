# First Slice Bridge Design

Status: `draft`

## Purpose

- Define one concrete minimal bridge design for the current first slice.
- Make the next implementation step explicit without changing canon, runtime files, or schemas in this pass.
- Keep the bridge centered on `crop_system_type` first and the harvest-output bridge second.

## Scope

- Slice remains fixed as `basil bulk kg wholesale`.
- `architecture_dwc_raft` remains the current first biological baseline only, not a canonical winner.
- This note is design-only. It does not modify runtime files, simulation files, or `data/knowledge/**`.
- This note keeps the current first-slice economics view locked and unchanged.
- This note avoids a broad architecture-key redesign and focuses on one minimum bridge field first.

## Current First Slice

- `basil bulk kg wholesale`

## Current First Biological Baseline

- `architecture_dwc_raft`
- Current status: `directionally_supported`
- Current role: first working biological baseline for the slice, not permanent canon

## Minimum Bridge to Add First

- Add one field first:
  - `crop_system_type`

Minimum meaning:

- a single scenario-to-runtime-to-adapter architecture label
- used first to make the DWC or raft baseline explicit
- later reused unchanged for fair NFT comparison scenarios

## Why `crop_system_type` Is the First Bridge Field

- It is already the most natural minimum bridge in current repo docs:
  - `docs/runtime_to_business_field_audit.md` marks `crop_system_type` as missing but useful for later architecture-aware business rules.
  - `docs/first_slice_adapter_spec.md` lists it as missing but not required for the narrow direct-mass proof.
  - `docs/first_slice_architecture_runtime_plan.md` already identifies it as the smallest architecture-aware bridge if only one identifier is introduced first.
- It is lighter than adding multiple simultaneous identifiers such as:
  - `architecture_variant_id`
  - a second scenario-only tag
  - an additional adapter-only normalization field
- One field is enough to:
  - tag the baseline scenario explicitly
  - propagate architecture meaning into runtime-facing outputs
  - let later business interpretation read the same value without a second naming scheme

Why this pass does not choose multiple simultaneous identifiers:

- the current blocker is absence of any architecture-aware bridge, not absence of a rich architecture taxonomy
- adding more than one identifier now would widen the pass into schema design rather than bridge design
- the smallest useful next step is one stable field with one stable value pattern

## Exact Recommended Bridge Value Pattern for the First Baseline Scenario

Recommended field and value:

```json
"crop_system_type": "architecture_dwc_raft"
```

Recommended usage:

- use this exact value pattern in scenario framing first
- propagate the same field name and same value unchanged into runtime-facing output
- let the adapter or business interpretation consume the same field without renaming it again

## One Compatible Value Pattern for Later NFT Comparison Scenarios

Recommended later compatible pattern:

```json
"crop_system_type": "architecture_nft"
```

Compatibility rule:

- same field name
- same value style
- no second bridge identifier required just to distinguish the later NFT path

## First Insertion Point for the Bridge

First insertion point:

- scenario framing

Reason:

- architecture should become explicit at the source scenario level before it is expected downstream
- this keeps the runtime-facing output from inventing architecture meaning later
- it also avoids creating an adapter-only architecture guess

## Where the Bridge Should Conceptually Enter

### Scenario framing

- add `crop_system_type` to the chosen basil baseline scenario frame
- first baseline value:
  - `architecture_dwc_raft`

### Runtime-facing output

- propagate the same `crop_system_type` field into runtime-facing scenario output
- do not rename it
- do not create a second parallel architecture tag if the first bridge can simply pass through

### Adapter/business interpretation

- treat `crop_system_type` as a context field for later architecture-aware interpretation
- keep current direct-mass basil pricing logic unchanged for now
- do not activate architecture-conditioned revenue rules just because the field exists

## What Should Not Be Added Yet

- a second architecture identifier alongside `crop_system_type`
- a broad architecture-key hierarchy
- architecture-conditioned pricing or revenue selection logic
- numeric architecture penalties or multipliers
- architecture-specific canonical defaults for shrink, labor, or profitability
- a full runtime event redesign

## Next Harvest-Output Bridge After `crop_system_type`

Next major bridge:

- `saleable_harvest_mass_kg`

Reason:

- it is still the main first-slice blocker
- the first basil bulk-kg path cannot become a real architecture-aware first-slice test without harvest-ready output

What this pass recommends:

- do not invent `saleable_harvest_mass_kg`
- next implementation work should choose one of these only:
  - direct runtime output of `saleable_harvest_mass_kg`, or
  - harvest-event output that rolls up cleanly to `saleable_harvest_mass_kg`

## What a Later Implementation Pass May Change

- scenario framing can become architecture-explicit
- runtime-facing outputs can propagate `crop_system_type`
- the thin adapter can start carrying `crop_system_type` through to interpretation outputs
- a harvest-output bridge can later add:
  - `saleable_harvest_mass_kg`
  - or harvest-event output sufficient to derive it

## What Must Remain Unchanged in That Pass

- current slice remains `basil bulk kg wholesale`
- `architecture_dwc_raft` remains a first working baseline only, not canonized as permanent winner
- current working economics values remain locked
- canonical biology, model, and business files remain unchanged unless a later explicit canon pass is requested
- no invented harvest mass from standing biomass or daily gain

## Smallest Sequence of Future Steps

1. Add `crop_system_type = architecture_dwc_raft` to the chosen basil baseline scenario framing.
2. Propagate that same field unchanged into runtime-facing output.
3. Allow the thin adapter to carry `crop_system_type` through as a context field.
4. Add the next harvest-output bridge:
   - direct `saleable_harvest_mass_kg`, or
   - compatible harvest-event output
5. Only after that, prepare one fair later NFT comparison scenario using:
   - `crop_system_type = architecture_nft`
   with the same field pattern.

## Recommended Next Action

- Use `crop_system_type` as the first and only bridge field added next.
- For the first baseline scenario, use:
  - `crop_system_type = architecture_dwc_raft`
- Make that field appear in scenario framing first, then propagate it unchanged into runtime-facing output.
- Keep `saleable_harvest_mass_kg` as the next major bridge after that.
