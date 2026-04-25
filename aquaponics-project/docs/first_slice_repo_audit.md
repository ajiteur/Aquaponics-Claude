# First Slice Repo Audit

Status: `draft`

## Purpose

- Record a repeatable repo audit for current first-slice reference usage.
- Focus on four reference groups only:
  - `crop_system_type`
  - `saleable_harvest_mass_kg`
  - first-slice basil scenario paths
  - reviewed-manual override flow
- Distinguish live first-slice implementation references from historical planning references and lower-signal repo artifacts.

## Scope

- Slice remains fixed as `basil bulk kg wholesale`.
- This audit is repo-local and review-only.
- It does not change canonical biology/model/business files, runtime files, or scripts beyond the optional audit helper used to regenerate this note.

## Regeneration

Repeatable helper:

- `scripts/generate_first_slice_repo_audit.py`

Command:

```powershell
python scripts/generate_first_slice_repo_audit.py
```

Helper scan behavior:

- scans working-tree text files under `aquaponics-project/`
- excludes:
  - `.git/**`
  - `knowledge-vault/.obsidian/**`
  - `data/simulation/**`
  - `__pycache__/**`

Interpretation note:

- the helper reports broad working-tree references, not canonical-only references
- some hits are expected to come from historical planning notes, consistency-sweep notes, or low-signal log artifacts that mention the same field names or scenario paths

## Current Audit Summary

- `crop_system_type` is now present in the active first-slice bridge/config/helper/adapter path.
- `saleable_harvest_mass_kg` remains unresolved and is still referenced primarily as:
  - a canonical business-layer requirement
  - a missing runtime-facing output
  - an explicit reviewed-manual override path
- The first-slice basil scenario path references are split cleanly between:
  - the baseline scenario source
  - the cumulative 7-day scenario used for adapter/example-run work
- The reviewed-manual override flow is present and wired, but still paused because approval for a non-null example value is currently withheld.

## `crop_system_type` References

### Live first-slice implementation path

Current live references are aligned across:

- `configs/first_slice_bridge_baselines.yaml`
  - durable tracked bridge source
- `scripts/materialize_first_slice_bridge.py`
  - narrow config-to-baseline-scenario materialization helper
- `scripts/build_first_slice_adapter_payload.py`
  - runtime-facing adapter carry-through
- `scripts/validate_first_slice_inputs.py`
  - tracked-config validation
- `docs/runtime_to_business_field_audit.md`
  - now treats `crop_system_type` as `present_directly`
- `docs/first_slice_adapter_spec.md`
  - now treats `crop_system_type` as a direct carry-through context field
- `docs/first_slice_bridge_regeneration_validation.md`
  - shows end-to-end materialization and propagation

Current meaning is consistent in those files:

- present upstream
- carried through as context
- not yet activating architecture-conditioned pricing, revenue rules, or output-form logic

### Historical or pre-implementation references still present

Some files still describe earlier bridge state or next-step planning:

- `docs/first_slice_architecture_runtime_plan.md`
- `docs/first_slice_bridge_implementation_surface.md`
- `docs/first_slice_adapter_crop_system_type_plan.md`
- `docs/runtime_field_inventory.md`
- `docs/first_slice_method_comparison.md`

Current interpretation:

- these are not part of the live first-slice implementation chain
- several still preserve pre-implementation wording such as missing/next-step framing
- they are valid audit findings for future cleanup, but not blockers for the current bridge state

### Intentional quoted stale wording

Some `crop_system_type` hits are expected because they preserve historical wording inside review artifacts:

- `docs/first_slice_doc_consistency_sweep.md`

Those references are audit artifacts, not live contract wording.

## `saleable_harvest_mass_kg` References

### Canonical/business requirement references

The field is clearly present as a business-layer requirement in:

- `data/knowledge/business/yield_to_revenue_rules.json`
- `data/knowledge/business/cost_models.json`
- `data/knowledge/business/labor_models.json`
- `docs/business_layer_contract.md`

### Current first-slice implementation references

The current non-canonical first-slice flow references the field in:

- `scripts/build_first_slice_adapter_payload.py`
  - explicit adapter output field
  - still populated only from overrides
- `scripts/example_first_slice_overrides.json`
  - current example value remains `null`
- `scripts/example_first_slice_reviewed_manual_overrides.json`
  - current reviewed-manual example value remains `null`
- `scripts/example_first_slice_working_inputs.json`
  - all current example cases keep `saleable_harvest_mass_kg = null`
- `scripts/calculate_first_slice_unit_economics.py`
  - consumes the field if present
  - explicitly states it is not derived from standing biomass or runtime proxies

### Current repo judgment

Current repo-wide wording is directionally consistent:

- `saleable_harvest_mass_kg` remains the main blocker for a true runtime-to-business first-slice output
- it must not be inferred from:
  - standing biomass
  - daily biomass gain
  - plant count
- current acceptable paths remain:
  - reviewed-manual override input
  - later runtime-native direct output
  - later explicit harvest observations strong enough to support rollup

### What is not present yet

No current live script or runtime-facing output path emits runtime-native:

- `saleable_harvest_mass_kg`

That absence is still consistent with the current first-slice docs.

## First-Slice Basil Scenario Path References

### Baseline scenario source path

The baseline source path is:

- `data/simulation/scenarios/starter_tilapia_basil_system.json`

Current role:

- bridge materialization target
- earliest scenario-framing source for `crop_system_type`

Primary references:

- `scripts/materialize_first_slice_bridge.py`
- `docs/first_slice_bridge_materialization_contract.md`
- `docs/first_slice_bridge_regeneration_validation.md`
- `docs/first_slice_bridge_implementation_surface.md`

### Cumulative 7-day scenario path

The cumulative first-slice example scenario path is:

- `data/simulation/scenarios/starter_tilapia_basil_system_day_1_day_2_day_3_day_4_day_5_day_6_day_7.json`

Current role:

- primary adapter/example-run input
- reviewed-manual run target

Primary references:

- `docs/first_slice_adapter_spec.md`
- `docs/runtime_to_business_field_audit.md`
- `docs/first_slice_saleable_harvest_mass_run_path.md`
- `docs/first_slice_reviewed_manual_run_note.md`
- `docs/first_slice_reviewed_manual_harvest_value_approval_packet.md`

### Current judgment on path usage

This split is consistent, not conflicting:

- baseline scenario path is used for bridge materialization and regeneration start
- cumulative 7-day path is used for adapter/example-run interpretation

### Lower-signal historical path references

The audit helper may also surface historical scenario-path mentions in files such as:

- `data/logs/update_logs/**`

Those are useful for diagnostics but not current first-slice contract sources.

## Reviewed-Manual Override Flow References

### Current flow is present

The reviewed-manual flow is clearly present across:

- `scripts/build_first_slice_adapter_payload.py`
  - `--overrides` input path
- `scripts/example_first_slice_reviewed_manual_overrides.json`
  - run-scoped reviewed-manual override file
- `docs/first_slice_saleable_harvest_mass_run_path.md`
  - documents override entry point
- `docs/first_slice_reviewed_manual_run_note.md`
  - documents run-scoped use and current null status
- `docs/first_slice_reviewed_manual_harvest_value_approval_packet.md`
  - documents approval path and withheld outcome

### Current flow status

The flow exists, but the reviewed run remains paused:

- approval is withheld
- the reviewed-manual override file still keeps:
  - `saleable_harvest_mass_kg = null`
- no approved non-null example value is currently present in the repo

### Current judgment

This flow is internally consistent:

- the adapter can accept reviewed-manual overrides now
- the reviewed-manual example file exists
- the approval packet and run note both keep the value non-canonical and review-scoped
- the repo does not currently pretend that a reviewed-manual value is runtime-native

## Audit Judgment

### Aligned now

- live `crop_system_type` bridge references
- `saleable_harvest_mass_kg` as unresolved/main blocker
- baseline-vs-cumulative scenario path split
- reviewed-manual override flow structure

### Still mixed or historical

- some planning and inventory docs still preserve older `crop_system_type` missing/next-step wording
- a few lower-signal artifacts still mention the first-slice scenario paths outside the main contract chain

### Most important current repo truth

For the current first slice:

- `crop_system_type` is implemented and carried through as context
- `saleable_harvest_mass_kg` is not solved yet
- the reviewed-manual override flow exists but remains paused at `null`

## Recommended Next Action

- Keep using `scripts/generate_first_slice_repo_audit.py` as the repeatable audit helper.
- Treat the live first-slice implementation chain as:
  - bridge config
  - bridge materialization helper
  - adapter carry-through
  - reviewed-manual override scaffolding
- If a future cleanup pass is requested, target only the remaining historical `crop_system_type` planning references rather than reopening the implemented bridge itself.
