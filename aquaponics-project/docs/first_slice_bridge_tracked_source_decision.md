# First Slice Bridge Tracked Source Decision

Status: `draft`

## Purpose

- Choose the best tracked repo location for the durable source-of-truth of the first `crop_system_type` bridge.
- Keep the decision narrow to the first basil baseline path only.
- Preserve `data/simulation/**` as derived and ignored runtime output.

## What Has Already Been Proven Locally

The local bridge proof already established that:

- `crop_system_type = architecture_dwc_raft` is the correct minimum first bridge value pattern for the basil baseline path
- adding that field at the earliest scenario-framing point is enough for the first bridge
- the existing native runtime regeneration path can carry the field unchanged through the basil `scenario_snapshot` chain
- no second architecture identifier is required
- no adapter change is required for the bridge proof itself

That means the open question is no longer bridge viability.
The open question is tracked persistence.

## What Must Remain Derived

These must remain derived runtime artifacts rather than the durable tracked bridge source:

- `data/simulation/scenarios/*.json`
- regenerated basil `scenario_snapshot` files
- corresponding basil day logs

Why:

- `AGENTS.md` defines `data/simulation/**` as derived runtime output
- the current ignore rules treat `data/*` as ignored by default, with only `data/knowledge/**` unignored
- the bridge should not be preserved by force-adding ignored runtime files

## Concrete Candidate Tracked Source Locations

The concrete candidate locations for the durable first bridge source are:

1. `data/knowledge/models/plant_system_models.json`
2. `data/sources/run_configs/`
3. `configs/first_slice_bridge_baselines.yaml`
4. `docs/first_slice_bridge_design.md`

These were chosen because they are either:

- already existing tracked structure, or
- a natural adjacent extension of existing tracked structure

## Evaluation of Each Candidate

### 1. `data/knowledge/models/plant_system_models.json`

Fit:

- weak

Why:

- this is canonical knowledge, not first-slice scenario/config state
- the first bridge value is not a universal biological truth; it is a baseline scenario selection for the current slice
- storing the bridge here would blur the line between canonical architecture knowledge and tracked scenario/config choice

### 2. `data/sources/run_configs/`

Fit:

- mixed

Why:

- conceptually, this is tracked non-canonical configuration
- however, the current repo uses `data/sources/run_configs/` for source/extraction run configs, not simulation baseline scenario configuration
- more importantly, a new file under `data/sources/**` is still ignored today because `.gitignore` ignores `data/*` and only re-allows `data/knowledge/**`

Implication:

- using this location would require ignore-rule changes before the new bridge source could be tracked
- that is avoidable, so it is not the smallest current choice

### 3. `configs/first_slice_bridge_baselines.yaml`

Fit:

- strong

Why:

- `configs/` is already a tracked machine-readable configuration area
- it is already used for repo-level policy/config inputs such as:
  - `configs/model_policy.yaml`
  - `configs/source_registry.yaml`
- a new file here would not require weakening the ignore boundary
- it keeps the bridge outside canonical knowledge and outside derived runtime output
- it is small and specific enough for the first bridge only

### 4. `docs/first_slice_bridge_design.md`

Fit:

- weak

Why:

- docs are the right place for design decisions and human-readable guidance
- docs are not the right durable machine-consumable source-of-truth for a generator or regeneration step
- leaving the bridge only in docs would preserve clarity for humans, but not create a clean tracked source for future runtime generation

## Ownership Implications of Each Candidate

| Candidate | Ownership category | Implication |
|---|---|---|
| `data/knowledge/models/plant_system_models.json` | `canonical knowledge` | Too strong. Would incorrectly promote a first-slice baseline choice into canon. |
| `data/sources/run_configs/` | `tracked non-canonical configuration` | Closer in spirit, but currently tied to extraction runs and blocked by ignore behavior for new files. |
| `configs/first_slice_bridge_baselines.yaml` | `tracked non-canonical configuration` | Best match for a small machine-readable bridge source that should persist and drive later regeneration. |
| `docs/first_slice_bridge_design.md` | `implementation support input` | Fine for design reference, but not ideal as the durable operational source-of-truth. |

## Best Current Tracked-Source Recommendation

Best current recommendation:

- `configs/first_slice_bridge_baselines.yaml`

Recommended first content shape, conceptually:

- one explicit basil baseline entry
- one explicit bridge field
- one explicit bridge value

Minimum intent only:

```yaml
starter_tilapia_basil_system:
  crop_system_type: architecture_dwc_raft
```

This is not a broader schema proposal.
It is the smallest tracked configuration shape that can preserve the first bridge durably.

## Why This Choice Best Preserves the Repo Boundary

This choice is best because:

- it keeps `data/simulation/**` derived and ignored
- it avoids force-adding ignored runtime files
- it does not promote first-slice bridge state into canonical knowledge
- it does not require an immediate `.gitignore` policy change just to track one bridge input
- it keeps the bridge in a machine-readable tracked location that is already aligned with repo configuration semantics

## Smallest Future Generator/Regeneration Implication

The smallest future implication is:

- one later bounded implementation pass reads `configs/first_slice_bridge_baselines.yaml`
- that pass applies `crop_system_type = architecture_dwc_raft` to the basil baseline scenario before native runtime regeneration
- the existing runtime path can then propagate the field unchanged through the basil `scenario_snapshot` chain

That is enough for the first bridge.
It does not require a broader generator redesign in this decision pass.

## What Should Not Happen

- do not force-add ignored files under `data/simulation/**`
- do not put the first bridge into `data/knowledge/**`
- do not use docs alone as the operational source-of-truth
- do not broaden this into a generic scenario-management redesign
- do not introduce `architecture_variant_id` or any second bridge identifier just to pick a tracked source location
- do not mix this decision with the later `saleable_harvest_mass_kg` bridge

## Recommended Next Action

- in the next bounded pass, introduce one tracked non-canonical bridge source at:
  - `configs/first_slice_bridge_baselines.yaml`
- add only the first basil baseline mapping:
  - `starter_tilapia_basil_system -> crop_system_type = architecture_dwc_raft`
- then plan one narrow follow-up pass that reads that tracked config and materializes the basil runtime baseline path without changing the broader repo boundary
