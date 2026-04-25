# First Slice Bridge Materialization Contract

Status: `draft`

## Purpose

- Define the smallest durable config-to-runtime materialization contract for the first `crop_system_type` bridge.
- Keep the bridge limited to the current basil baseline path only.
- Make the next implementation step concrete without redesigning broader scenario management.

## What the Tracked Source Will Be

The tracked source should be:

- `configs/first_slice_bridge_baselines.yaml`

Role:

- tracked non-canonical configuration
- durable source-of-truth for the first bridge input
- separate from canonical knowledge and separate from derived runtime output

## Minimum Config Shape

Minimum shape:

```yaml
starter_tilapia_basil_system:
  crop_system_type: architecture_dwc_raft
```

Why this shape is enough:

- one lookup key
- one bridge field
- one baseline value

No additional fields are required for the first bridge contract.

## Exact Lookup Key for the First Basil Baseline

Exact lookup key:

- `starter_tilapia_basil_system`

Reason:

- it matches the existing baseline scenario identity used in the basil baseline path
- it is specific enough for the first bridge without introducing a second identifier

## Exact First Materialization Target File

Exact first target file:

- `data/simulation/scenarios/starter_tilapia_basil_system.json`

Reason:

- this is the earliest clean scenario-framing point already identified in the bridge-design and implementation-surface notes

## Exact Intended Materialization Target

The materialization target is the top-level scenario field:

```json
"crop_system_type": "architecture_dwc_raft"
```

Contract rule:

- preserve the exact field name `crop_system_type`
- preserve the exact value `architecture_dwc_raft`
- write it at top level on the baseline scenario object

## Smallest Point Where the Config Should Be Read

Smallest read point:

- before native runtime regeneration begins

More specifically:

- read the tracked config before the basil baseline scenario is used as input to the existing simulation path

## Whether the Smallest Consumer Is a Narrow Pre-Regeneration Helper Step or a Minimal Existing Runtime Hook

Best current choice:

- a narrow pre-regeneration helper step

Why:

- the bridge only needs one field inserted into the baseline scenario before native regeneration
- the existing runtime path already passes the top-level field through unchanged once it is present
- this avoids modifying the existing runtime scripts just to read one tracked config value

Current conclusion:

- a minimal existing runtime hook is not required for the first bridge contract

## What the Materialization Step Should Do

The materialization step should do only this:

1. read `configs/first_slice_bridge_baselines.yaml`
2. look up `starter_tilapia_basil_system`
3. extract:
   - `crop_system_type = architecture_dwc_raft`
4. write that exact field/value into:
   - `data/simulation/scenarios/starter_tilapia_basil_system.json`
5. stop

After that, the existing native runtime regeneration path can be run separately to produce the basil `scenario_snapshot` chain.

## What It Must Not Do

- do not modify canonical biology/model/business files
- do not write `saleable_harvest_mass_kg`
- do not introduce `architecture_variant_id` or any second bridge identifier
- do not activate architecture-conditioned pricing or revenue rules
- do not redesign broader scenario management
- do not update `multi_day_summary.json`
- do not retrofit unrelated scenario families
- do not read or write more bridge fields than `crop_system_type`

## What Remains Deferred

- NFT comparison configuration
- broader scenario/config schema
- harvest-output bridging such as `saleable_harvest_mass_kg`
- any architecture-aware business-rule activation

## Recommended Next Action

- Keep `configs/first_slice_bridge_baselines.yaml` as the durable tracked bridge source.
- Keep the narrow pre-regeneration helper as the only materialization step for this bridge.
- Treat `saleable_harvest_mass_kg` as the next distinct bridge rather than extending this contract.
