# First Slice Bridge Persistence Decision

Status: `draft`

## Purpose

- Decide where the first architecture-aware bridge should live durably in the repo.
- Keep the decision narrow to the first `crop_system_type` bridge for the basil baseline path.
- Preserve the current repo boundary between tracked source material and derived runtime output.

## What the Local Bridge Proof Successfully Demonstrated

The local bridge proof showed that the minimum bridge is technically viable within the current simulation flow:

- adding `crop_system_type = architecture_dwc_raft` at the earliest basil baseline scenario framing point is sufficient for the first bridge
- the existing native regeneration path can carry that field unchanged through the basil `scenario_snapshot` chain
- no second architecture identifier was required
- no adapter change was required for the bridge proof itself
- `multi_day_summary.json` did not need to change for the proof

This confirms the bridge design itself is sound.

## Why the Current Apply Location Is Not Durable

The local proof was applied under `data/simulation/**`.

That location is not durable because:

- `AGENTS.md` defines `data/simulation/**` as derived runtime output
- the current repo ignore rules treat `data/*` as ignored by default and only unignore `data/knowledge/**`
- as a result, the changed basil scenario chain under `data/simulation/scenarios/**` and the corresponding generated basil day logs under `data/simulation/day_logs/**` are local runtime artifacts, not durable tracked repo source

That makes the proof useful as a validation exercise, but not as a stable committed bridge location.

## Repo Boundary Implications of `data/simulation/**` Being Ignored

The current ignore behavior reinforces the repo contract:

- `data/simulation/**` is derived
- `data/knowledge/**` is canonical
- tracked bridge inputs should not depend on force-adding ignored runtime artifacts

Implications for this first bridge:

- the basil baseline scenario under `data/simulation/scenarios/**` should not be treated as the durable source of truth for `crop_system_type`
- the regenerated basil `scenario_snapshot` files are proof artifacts, not the correct long-term persistence layer
- keeping the current ignore boundary is preferable to weakening the repo contract just to preserve the first bridge

## Candidate Durable Options

### 1. Keep as local proof only

What it means:

- leave the successful bridge proof as a local runtime demonstration only
- do not try to commit the ignored runtime files

Pros:

- preserves the current canonical-vs-derived boundary completely
- avoids premature schema or repo-structure changes
- confirms the bridge design before choosing a tracked persistence layer

Cons:

- the bridge is not durably represented in tracked repo state
- the result must be reproduced later from a tracked source before it becomes part of normal workflow

Current fit:

- acceptable as a proof
- not sufficient as the durable next state

### 2. Move earliest scenario source to a tracked location

What it means:

- relocate the earliest basil baseline scenario source from ignored runtime storage into a tracked repo location
- later generate the runtime scenario chain from that tracked source

Pros:

- gives the bridge a durable tracked home
- keeps the earliest scenario framing explicit
- fits the current bridge design emphasis on scenario-level insertion first

Cons:

- requires choosing a new tracked source location and ownership boundary
- if done carelessly, can blur the line between source scenario inputs and derived runtime outputs

Current fit:

- directionally good
- needs one explicit tracked source location decision first

### 3. Introduce a tracked scenario/config source that later generates runtime scenarios

What it means:

- keep `data/simulation/**` derived and ignored
- add one tracked scenario/config source for the basil baseline path in a tracked non-runtime location
- generate runtime scenarios from that tracked source in a later bounded pass

Pros:

- best preserves the current repo contract
- gives the bridge a durable tracked home without force-tracking derived outputs
- fits the current bridge design, which only needs one field and one baseline value pattern
- scales better if later NFT comparison scenarios are added using the same bridge field

Cons:

- requires one more decision about the tracked source location and generation path
- does not make the current local proof itself durable

Current fit:

- strongest current option

## Best Current Recommendation

Best current recommendation:

- introduce a tracked scenario/config source that later generates runtime scenarios

Why this is the best current fit:

- it preserves `data/simulation/**` as derived output
- it does not force-add ignored runtime files
- it keeps the first bridge narrow:
  - one field
  - one baseline value
  - one basil baseline path
- it leaves canonical biology/model/business files untouched
- it keeps the later harvest bridge separate from the current persistence decision

In practical terms, the next durable version of the bridge should live in a tracked source location outside `data/simulation/**`, and the basil runtime scenario chain should be regenerated from there.

## What Should Not Happen

- do not force-add ignored runtime files from `data/simulation/**`
- do not weaken the canonical-vs-derived repo boundary just to preserve the first bridge
- do not promote derived scenario snapshots into canonical knowledge
- do not turn this into a broad scenario-schema redesign
- do not introduce `architecture_variant_id` or any second bridge identifier just to solve persistence
- do not mix this persistence decision with the later `saleable_harvest_mass_kg` bridge

## Smallest Safe Next Implementation Direction

The smallest safe next direction is:

1. keep the local basil bridge proof as a validated runtime demonstration only
2. choose one tracked non-runtime source location for the earliest basil baseline scenario/config
3. carry only the minimum bridge field into that tracked source:
   - `crop_system_type = architecture_dwc_raft`
4. use a later bounded implementation pass to regenerate the basil runtime scenario chain from that tracked source
5. leave adapter behavior unchanged until the tracked source and regeneration path are settled

This keeps the bridge durable without changing the repo contract.

## Recommended Next Action

- do not try to commit the current ignored runtime bridge proof
- choose one tracked source location for the basil baseline scenario/config outside `data/simulation/**`
- in the next bounded pass, add only:
  - `crop_system_type = architecture_dwc_raft`
  to that tracked source
- then regenerate the basil runtime scenario chain from that tracked source using a repo-native path or an explicitly approved narrow generator step

Backlog:

- no backlog change needed
