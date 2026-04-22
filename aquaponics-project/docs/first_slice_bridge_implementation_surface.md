# First Slice Bridge Implementation Surface

Status: `draft`

## Purpose

- Identify the exact smallest file-level implementation surface for the first architecture-aware bridge.
- Keep the bridge limited to `crop_system_type = architecture_dwc_raft` for the current first baseline path.
- Make the next apply pass concrete without changing code or runtime files in this review pass.

## Scope

- Slice remains fixed as `basil bulk kg wholesale`.
- `architecture_dwc_raft` remains the current first working baseline only, not a canonized winner.
- The bridge field name remains exactly `crop_system_type`.
- The baseline bridge value remains exactly `architecture_dwc_raft`.
- This note covers only the minimum surface needed to introduce the bridge and let it pass through into the runtime-facing `scenario_snapshot` family.
- This note does not reopen the current working economics view.

## Current Bridge Design Being Implemented

The current design is:

- add one bridge field first:
  - `crop_system_type`
- use one baseline value pattern first:
  - `architecture_dwc_raft`
- insert it at the earliest clean scenario-framing point
- let it propagate unchanged into runtime-facing output
- keep `saleable_harvest_mass_kg` as the next major bridge, not something to invent now

This follows:

- [docs/first_slice_bridge_design.md](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/docs/first_slice_bridge_design.md)
- [docs/first_slice_architecture_runtime_plan.md](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/docs/first_slice_architecture_runtime_plan.md)
- [docs/runtime_to_business_field_audit.md](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/docs/runtime_to_business_field_audit.md)
- [docs/runtime_field_inventory.md](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/docs/runtime_field_inventory.md)
- [docs/first_slice_adapter_spec.md](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/docs/first_slice_adapter_spec.md)

## Exact File-Level Touch Candidates

Only one file has a concrete reason to change in the smallest apply pass:

| File | Why it is in scope | Required in the smallest apply pass |
|---|---|---|
| [data/simulation/scenarios/starter_tilapia_basil_system.json](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/data/simulation/scenarios/starter_tilapia_basil_system.json) | Earliest clean basil baseline scenario-framing source. Adding `crop_system_type` here makes the bridge explicit at the source scenario level. | `yes` |

No other file needs to change for the minimum bridge insertion if the only required runtime-facing target is the `scenario_snapshot` family.

## First Baseline Scenario Insertion Point

First insertion point:

- top-level field on the baseline basil scenario object in [data/simulation/scenarios/starter_tilapia_basil_system.json](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/data/simulation/scenarios/starter_tilapia_basil_system.json)

Recommended field and value:

```json
"crop_system_type": "architecture_dwc_raft"
```

Why top-level is the smallest clean insertion:

- it matches the current bridge-design framing as a scenario-level architecture bridge
- it keeps the field easy to propagate unchanged through scenario snapshots
- it avoids adding a second architecture tag or nesting rule before there is a proven need
- it keeps later adapter consumption simple if the field is needed downstream

## Runtime-Facing Propagation Point

Existing propagation point:

- [src/simulate_day.py](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/src/simulate_day.py)

Why this is the relevant propagation point:

- it loads the full scenario object
- it mutates known sub-objects in place
- it saves the full updated scenario object to the next scenario snapshot file

Current minimal conclusion:

- no code change is required in [src/simulate_day.py](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/src/simulate_day.py) for the first bridge pass if `crop_system_type` is added as a top-level field in the baseline scenario file
- the field should pass through unchanged into the derived basil `scenario_snapshot` files because the updated scenario is written back as the full scenario object

Minimum runtime-facing target for this bridge:

- the basil `scenario_snapshot` family only

Why the target stays that narrow:

- [docs/runtime_field_inventory.md](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/docs/runtime_field_inventory.md) already identifies the `scenario_snapshot` family as the strongest adapter source for the first slice
- [docs/first_slice_adapter_spec.md](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/docs/first_slice_adapter_spec.md) already uses the cumulative basil `scenario_snapshot` file as the primary adapter input

## Adapter-Consumption Point, If Needed

Current conclusion:

- adapter touch is not required for the minimum bridge insertion pass

Reason:

- [docs/runtime_to_business_field_audit.md](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/docs/runtime_to_business_field_audit.md) and [docs/first_slice_adapter_spec.md](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/docs/first_slice_adapter_spec.md) both treat `crop_system_type` as useful but not required for the current narrow basil kg proof
- the minimum immediate goal is to introduce the bridge and preserve it in runtime-facing scenario snapshots

Low-risk later consumption point:

- [scripts/build_first_slice_adapter_payload.py](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/scripts/build_first_slice_adapter_payload.py)

Why this is only later and optional:

- the script already has a `crop_system_type` output slot and currently emits `null`
- that makes it a natural later read-through point once the runtime-facing field exists
- it does not need to change in the first apply pass

## What Does Not Need to Change Yet

- [src/simulate_day.py](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/src/simulate_day.py)
  - no first-pass code edit needed if top-level passthrough behaves as inspected
- [src/simulate_n_days.py](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/src/simulate_n_days.py)
  - summary outputs do not need `crop_system_type` for the minimum bridge
- [scripts/build_first_slice_adapter_payload.py](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/scripts/build_first_slice_adapter_payload.py)
  - later optional consumption point only
- existing day logs
  - they do not need to be retrofitted in the first bridge pass
- broader architecture identifiers such as `architecture_variant_id`
  - not needed yet
- harvest-output fields such as `saleable_harvest_mass_kg`
  - remain the next bridge, not part of this minimum bridge insertion

## Smallest Safe Implementation Order

1. Add `"crop_system_type": "architecture_dwc_raft"` to [data/simulation/scenarios/starter_tilapia_basil_system.json](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/data/simulation/scenarios/starter_tilapia_basil_system.json).
2. Regenerate the basil `scenario_snapshot` chain from that baseline scenario rather than manually backfilling derived runtime files.
3. Verify that the resulting basil scenario snapshots retain `crop_system_type` unchanged.
4. Stop there for the minimum bridge pass.
5. Only after that, decide whether a later adapter read-through is needed.

## Stop Conditions for the Later Apply Pass

Stop the later apply pass if any of these are true:

- adding `crop_system_type` to the baseline scenario does not survive into regenerated scenario snapshots
- the intended bridge target expands beyond `scenario_snapshot` files and now requires day-log or summary redesign
- implementation would require introducing a second architecture identifier at the same time
- implementation would require editing canonical biology, model, or business files
- implementation pressure shifts from bridge insertion to harvest-output redesign

If any of those occur, the later pass is no longer a minimal bridge apply pass and should stop for re-scoping.

## Recommended Next Action

- In the later apply pass, touch only [data/simulation/scenarios/starter_tilapia_basil_system.json](/C:/Users/ajith/Documents/Aquaponics/Aquaponics-project/data/simulation/scenarios/starter_tilapia_basil_system.json) first.
- Add the exact baseline bridge field:
  - `crop_system_type = architecture_dwc_raft`
- Regenerate basil scenario snapshots and confirm unchanged passthrough before considering any adapter touch.
- Keep `saleable_harvest_mass_kg` as the next major bridge after this one.
