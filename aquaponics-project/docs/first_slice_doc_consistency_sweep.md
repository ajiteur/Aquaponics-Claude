# First Slice Doc Consistency Sweep

Status: `draft`

## Purpose

- Record a narrow consistency sweep across current first-slice materials.
- Focus only on field names, value names, scenario paths, status wording, and first-slice scope wording.
- Separate real cross-doc drift from notes that already remain aligned enough.

## Scope

Reviewed at minimum:

- `docs/first_vertical_slice_choice.md`
- `docs/runtime_to_business_field_audit.md`
- `docs/first_slice_adapter_spec.md`
- `docs/first_slice_bridge_design.md`
- `docs/first_slice_bridge_materialization_contract.md`
- `docs/first_slice_bridge_regeneration_validation.md`
- `docs/first_slice_saleable_harvest_mass_plan.md`
- `docs/first_slice_reviewed_manual_run_note.md`

Current repo state used as comparison context:

- `crop_system_type = architecture_dwc_raft` is now carried through the basil baseline runtime path and through the thin first-slice adapter as a context field.
- `saleable_harvest_mass_kg` remains unresolved and still requires reviewed-manual input or a later runtime-native harvest-output bridge.

## Summary Judgment

- `basil bulk kg wholesale` scope wording is mostly consistent across the checked notes.
- The 7-day basil scenario path is used consistently where an exact example run is intended.
- The main drift is around `crop_system_type`:
  - some older first-slice notes still describe it as missing, deferred, or next-to-implement
  - current bridge and adapter notes now document it as present and carried through as context
- `saleable_harvest_mass_kg` wording is consistent:
  - still the main blocker
  - still not to be inferred from standing biomass, daily gain, or plant count

## Inconsistencies Found

### 1. `crop_system_type` status drift in slice-scope wording

File:

- `docs/first_vertical_slice_choice.md`

Issue:

- The deferred list still describes `crop_system_type` as part of future area- and architecture-aware extensions.
- Current repo-first-slice docs now treat `crop_system_type` as an available context field, even though architecture-conditioned business logic remains deferred.

Recommended cleanup:

- keep `crop_system_type` out of the deferred-extension example wording
- defer only broader architecture-conditioned business behavior, not the field itself

### 2. `crop_system_type` and runtime source-path drift in the audit note

File:

- `docs/runtime_to_business_field_audit.md`

Issues:

- `crop_system_type` is still marked as `missing`, which is no longer true for the current basil scenario path
- several scenario-facing source paths still use `plant_crop_after.*` and `water_state_after.*`, while the current primary scenario-snapshot path uses:
  - `plant_crop.*`
  - `water_state.*`

Recommended cleanup:

- update `crop_system_type` to `present_directly`
- normalize primary scenario-snapshot source references to `plant_crop.*` and `water_state.*`
- keep `*_after` wording only where day-log paths are explicitly being discussed

### 3. `crop_system_type` status drift in the adapter spec

File:

- `docs/first_slice_adapter_spec.md`

Issue:

- `crop_system_type` is still listed under `Fields Still Missing`.
- The current adapter now carries `crop_system_type` through directly from the top-level runtime scenario snapshot.

Recommended cleanup:

- move `crop_system_type` out of the missing list
- describe it as a direct rename/flattening context field

### 4. Stale next-action wording in the bridge design note

File:

- `docs/first_slice_bridge_design.md`

Issue:

- The note still reads as though adding and propagating `crop_system_type` is the next action.
- That bridge is already implemented and validated in later notes.

Recommended cleanup:

- keep the design content
- update the next-action wording so it no longer points to already-completed bridge work

### 5. Stale deferred/next-action wording in the materialization contract

File:

- `docs/first_slice_bridge_materialization_contract.md`

Issues:

- `adapter consumption of crop_system_type` is still listed as deferred
- the recommended next action still says to add the config and helper, which now already exist

Recommended cleanup:

- remove `crop_system_type` adapter consumption from the deferred list
- update the next-action wording to reflect that the contract is already in place

## No Change Needed

These checked notes are already aligned enough for the current repo state:

- `docs/first_slice_bridge_regeneration_validation.md`
- `docs/first_slice_saleable_harvest_mass_plan.md`
- `docs/first_slice_reviewed_manual_run_note.md`

Why:

- they correctly reflect that `crop_system_type` is solved for the first bridge
- they correctly keep `saleable_harvest_mass_kg` as the remaining main blocker
- they keep the slice fixed as `basil bulk kg wholesale`

## Exact Proposed Diffs

### `docs/first_vertical_slice_choice.md`

```diff
--- a/docs/first_vertical_slice_choice.md
+++ b/docs/first_vertical_slice_choice.md
@@
- `cull_or_unsaleable_mass_kg`
- `harvest_event_count`
- `first_harvest_utc`
- `last_harvest_utc`
- `water_use_l`
- `supplement_input_records`
- `adjustment_event_count`
- `quality_risk_event_records`
- `out_of_range_event_records`
- `downtime_event_count`
- `disease_or_pathogen_event_records`
- area- and architecture-aware extensions such as `growing_area_m2` and `crop_system_type`
+ `cull_or_unsaleable_mass_kg`
+ `harvest_event_count`
+ `first_harvest_utc`
+ `last_harvest_utc`
+ `water_use_l`
+ `supplement_input_records`
+ `adjustment_event_count`
+ `quality_risk_event_records`
+ `out_of_range_event_records`
+ `downtime_event_count`
+ `disease_or_pathogen_event_records`
+ area-aware extensions such as `growing_area_m2`
+ architecture-conditioned pricing or output-form extensions beyond the current context field `crop_system_type`
```

### `docs/runtime_to_business_field_audit.md`

```diff
--- a/docs/runtime_to_business_field_audit.md
+++ b/docs/runtime_to_business_field_audit.md
@@
-| `crop_id` | required_now | `plant_crop_after.species_id = plant_basil` | `derivable_by_simple_mapping` | Flatten the nested plant record. | no | Current runtime species ID already matches the canonical plant identifier pattern. |
+| `crop_id` | required_now | `plant_crop.species_id = plant_basil` | `derivable_by_simple_mapping` | Flatten the nested plant record from the primary scenario snapshot. | no | Current runtime species ID already matches the canonical plant identifier pattern. |
@@
-| `crop_system_type` | useful_now | no runtime source found | `missing` | Needed later for architecture-aware business rules. | no | Not required for the current basil kg direct-mass path. |
+| `crop_system_type` | useful_now | scenario file `crop_system_type` | `present_directly` | Already emitted directly on the current basil scenario path. | no | Context field only; architecture-conditioned business rules remain deferred. |
@@
-| `planting_count` | useful_now | `plant_crop_after.plant_count` | `derivable_by_simple_mapping` | Works only as a first-pass proxy because current runtime does not separate transplanted vs surviving plants. | no | Relevant later if `cost_plant_inputs_basil` is populated. |
-| `live_plant_count_end` | useful_now | `plant_crop_after.plant_count` | `derivable_by_simple_mapping` | Current plant count behaves like end-of-period live count. | no | This meaning is cleaner than using the same value as guaranteed planting count. |
+| `planting_count` | useful_now | `plant_crop.plant_count` | `derivable_by_simple_mapping` | Works only as a first-pass proxy because current runtime does not separate transplanted vs surviving plants. | no | Relevant later if `cost_plant_inputs_basil` is populated. |
+| `live_plant_count_end` | useful_now | `plant_crop.plant_count` | `derivable_by_simple_mapping` | Current plant count behaves like end-of-period live count. | no | This meaning is cleaner than using the same value as guaranteed planting count. |
@@
-| `observed_pH` | required_now | `water_state_after.pH` | `derivable_by_simple_mapping` | Flatten the nested water-state object. | no | Naming change only. |
-| `observed_tan_mg_l` | required_now | `water_state_after.tan_mg_L` | `derivable_by_simple_mapping` | Rename and normalize `mg_L` vs `mg_l`. | no | Same physical unit, naming mismatch only. |
-| `observed_unionized_nh3_mg_l` | required_now | `water_state_after.unionized_nh3_mg_L` | `derivable_by_simple_mapping` | Rename and normalize case. | no | Same physical unit, naming mismatch only. |
-| `observed_nitrate_mg_l` | required_now | `water_state_after.nitrate_mg_L` | `derivable_by_simple_mapping` | Rename and normalize case. | no | Same physical unit, naming mismatch only. |
+| `observed_pH` | required_now | `water_state.pH` | `derivable_by_simple_mapping` | Flatten the nested water-state object from the primary scenario snapshot. | no | Naming change only. |
+| `observed_tan_mg_l` | required_now | `water_state.tan_mg_L` | `derivable_by_simple_mapping` | Rename and normalize `mg_L` vs `mg_l`. | no | Same physical unit, naming mismatch only. |
+| `observed_unionized_nh3_mg_l` | required_now | `water_state.unionized_nh3_mg_L` | `derivable_by_simple_mapping` | Rename and normalize case. | no | Same physical unit, naming mismatch only. |
+| `observed_nitrate_mg_l` | required_now | `water_state.nitrate_mg_L` | `derivable_by_simple_mapping` | Rename and normalize case. | no | Same physical unit, naming mismatch only. |
@@
- `crop_system_type` and `growing_area_m2` are absent, although they do not block the narrow basil wholesale proof.
+ `growing_area_m2` is absent, although it does not block the narrow basil wholesale proof.
+ `crop_system_type` is now present as a context field, although it still does not block the narrow basil wholesale proof.
@@
- The current runtime files use nested objects such as `water_state_after`, `plant_crop_after`, and `fish_batch_after`, so a flattening and renaming layer is expected.
+ The current runtime-facing files use nested objects such as scenario-snapshot `water_state`, `plant_crop`, and `fish_batch`, plus day-log variants like `water_state_after` and `plant_crop_after`, so a flattening and renaming layer is expected.
```

### `docs/first_slice_adapter_spec.md`

```diff
--- a/docs/first_slice_adapter_spec.md
+++ b/docs/first_slice_adapter_spec.md
@@
 | `observed_unionized_nh3_mg_l` | `scenario_snapshot.water_state.unionized_nh3_mg_L` | Normalize case only. |
 | `observed_nitrate_mg_l` | `scenario_snapshot.water_state.nitrate_mg_L` | Normalize case only. |
 | `energy_kwh` | `scenario_snapshot.derived.daily_energy_kwh` | Direct flattening from the chosen rollup snapshot. |
 | `operating_day_count` | `scenario_snapshot.time.day` | Convenience adapter output, not a contract field. |
+| `crop_system_type` | `scenario_snapshot.crop_system_type` | Direct carry-through context field only. |
@@
-| `crop_system_type` | `missing` | Not required for the narrow direct-mass proof, but absent. |
```

### `docs/first_slice_bridge_design.md`

```diff
--- a/docs/first_slice_bridge_design.md
+++ b/docs/first_slice_bridge_design.md
@@
-## Recommended Next Action
-
- Use `crop_system_type` as the first and only bridge field added next.
- For the first baseline scenario, use:
-   - `crop_system_type = architecture_dwc_raft`
- Make that field appear in scenario framing first, then propagate it unchanged into runtime-facing output.
- Keep `saleable_harvest_mass_kg` as the next major bridge after that.
+## Recommended Next Action
+
+- Keep the implemented `crop_system_type` bridge stable and unchanged.
+- Treat `saleable_harvest_mass_kg` as the next major bridge for the first slice.
+- Keep broader architecture-conditioned business behavior deferred.
```

### `docs/first_slice_bridge_materialization_contract.md`

```diff
--- a/docs/first_slice_bridge_materialization_contract.md
+++ b/docs/first_slice_bridge_materialization_contract.md
@@
-## What Remains Deferred
-
- adapter consumption of `crop_system_type`
- NFT comparison configuration
- broader scenario/config schema
- harvest-output bridging such as `saleable_harvest_mass_kg`
- any architecture-aware business-rule activation
+## What Remains Deferred
+
+- NFT comparison configuration
+- broader scenario/config schema
+- harvest-output bridging such as `saleable_harvest_mass_kg`
+- any architecture-aware business-rule activation
@@
-## Recommended Next Action
-
- in the next bounded implementation pass, add:
-   - `configs/first_slice_bridge_baselines.yaml`
- use the exact first mapping:
-   - `starter_tilapia_basil_system -> crop_system_type = architecture_dwc_raft`
- implement a narrow pre-regeneration helper that materializes only that field into:
-   - `data/simulation/scenarios/starter_tilapia_basil_system.json`
- then run the existing native basil regeneration path separately
+## Recommended Next Action
+
+- Keep `configs/first_slice_bridge_baselines.yaml` as the durable tracked bridge source.
+- Keep the narrow pre-regeneration helper as the only materialization step for this bridge.
+- Treat `saleable_harvest_mass_kg` as the next distinct bridge rather than extending this contract.
```

## Recommended Sweep Outcome

- `crop_system_type` should now be described consistently as:
  - present upstream
  - carried through as context
  - not yet activating architecture-conditioned business logic
- `saleable_harvest_mass_kg` should continue to be described consistently as:
  - unresolved
  - main blocker
  - not inferable from standing biomass, daily gain, or plant count
- no changes are needed to the reviewed-manual pause wording until a future approved non-null harvest value exists
