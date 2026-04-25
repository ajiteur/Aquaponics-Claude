# First Slice Adapter Crop System Type Plan

Status: `draft`

## Purpose

- Record the smallest safe adapter change that was needed once the first `crop_system_type` bridge was proven end to end.
- Keep the change limited to context carry-through for the current first slice.
- Avoid widening the adapter into architecture rules, harvest logic, or broader schema work.

## What Has Already Been Proven

The current bridge path has already shown that:

- `configs/first_slice_bridge_baselines.yaml` is the durable tracked bridge source
- `scripts/materialize_first_slice_bridge.py` can materialize the bridge into the basil baseline scenario
- the native basil regeneration path preserves:
  - `crop_system_type = architecture_dwc_raft`
  unchanged through the regenerated basil `scenario_snapshot` chain

That missing piece has now been closed on the active first-slice path.

## Current Adapter Behavior for `crop_system_type`

Current thin-adapter behavior in `scripts/build_first_slice_adapter_payload.py` is:

- the payload schema already includes a top-level `crop_system_type` output field
- `metadata.field_statuses.crop_system_type` reports direct carry-through when the source field is present
- the emitted payload carries the runtime value unchanged when present
- the script reads the top-level runtime `crop_system_type` field from the incoming `scenario_snapshot`

Current implication:

- the bridge is present upstream in the runtime-facing basil scenario chain
- the adapter path no longer drops it

## Why Adapter Consumption Was the Right Next Step

- The bridge is already proven end to end from tracked config through regenerated basil runtime output.
- The adapter already has a natural output slot for `crop_system_type`, so this is a narrow carry-through change rather than a new schema addition.
- Carrying the field through now improves first-slice traceability without activating any architecture-conditioned pricing or revenue behavior.
- This keeps the current first-slice biological baseline visible in the adapter output while the economics view remains locked.

## Smallest Safe Adapter Change

The smallest safe change was:

1. read top-level `crop_system_type` from the runtime `scenario_snapshot` input
2. copy that exact value into the adapter payload top-level `crop_system_type`
3. update the adapter metadata status for `crop_system_type` so it no longer reports `missing` when the source field is present
4. leave all other payload fields and adapter behavior unchanged

What this change should not do:

- it should not reread `configs/first_slice_bridge_baselines.yaml`
- it should not inject a fallback bridge value inside the adapter
- it should not translate `architecture_dwc_raft` into any second identifier
- it should not add any new business logic

## Exact Source Field Expected by the Adapter

Expected adapter source field:

- top-level `scenario_snapshot.crop_system_type`

Expected first-slice value for the current baseline path:

```json
"crop_system_type": "architecture_dwc_raft"
```

Why this is the right source:

- the bridge is already materialized and regenerated into the runtime-facing basil scenario chain
- the adapter should consume the runtime-facing field directly rather than reaching backward into tracked config

## Exact Output Field to Preserve

Exact adapter output field:

- top-level `crop_system_type`

Carry-through rule:

- preserve the exact field name `crop_system_type`
- preserve the exact runtime value unchanged
- if the input field is absent, keep the output null and treat that as a missing upstream bridge condition rather than inventing a value

## What Should Remain Unchanged

- current slice remains `basil bulk kg wholesale`
- current first biological baseline remains a working baseline only, not canon
- existing adapter source family remains the cumulative basil `scenario_snapshot`
- `saleable_harvest_mass_kg` remains unresolved and separate
- `product_id = basil` and `channel_id = channel_wholesale` remain slice-config inputs
- no second architecture identifier is introduced
- no new overrides or config files are needed for the adapter change itself

## What This Still Does Not Activate

- architecture-conditioned pricing
- architecture-conditioned revenue rules
- architecture-specific penalties or multipliers
- NFT comparison behavior
- harvest rollup logic
- `saleable_harvest_mass_kg`
- any canon promotion into `data/knowledge/**`

This remains a context-carry-through change only.

## Recommended Next Action

- Keep the implemented `crop_system_type` carry-through unchanged.
- Keep using `crop_system_type` as a context field only.
- Leave all pricing, labor, cost, and harvest-mass behavior untouched.
