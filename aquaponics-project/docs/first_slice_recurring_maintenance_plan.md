# First Slice Recurring Maintenance Plan

Status: `draft`

## Purpose

- Define the smallest recurring maintenance plan for first-slice repo health checks.
- Keep the recurring checks read-only by default.
- Preserve the current first-slice state:
  - `crop_system_type` is context only
  - `saleable_harvest_mass_kg` remains unresolved unless a future approved value exists

## Scope

- Slice remains fixed as `basil bulk kg wholesale`.
- Scope is limited to first-slice tracked scripts, tracked config, example inputs, and first-slice documentation consistency.
- This plan does not modify canonical biology/model/business files, runtime files, or ignored derived outputs.

## Checks Already Available

Current repeatable checks already in the repo:

- `scripts/validate_first_slice_inputs.py`
  - validates tracked first-slice config and example JSON inputs
  - confirms:
    - `starter_tilapia_basil_system.crop_system_type = architecture_dwc_raft`
- `scripts/generate_first_slice_repo_audit.py`
  - scans repo text files for first-slice reference usage in four groups:
    - `crop_system_type`
    - `saleable_harvest_mass_kg`
    - basil scenario paths
    - reviewed-manual override flow
- `docs/first_slice_syntax_and_smoke_check.md`
  - records the current syntax-and-smoke-check pattern
- `docs/first_slice_repo_audit.md`
  - records the current interpretation of the repo-audit output
- `docs/first_slice_doc_consistency_sweep.md`
  - records the current consistency cleanup rules and stale-wording targets

## Recommended Weekly Syntax/Smoke Check

Run one narrow syntax-and-smoke pass weekly against the current first-slice tracked helpers and inputs.

Minimum weekly intent:

1. compile the first-slice helper scripts
2. validate tracked first-slice config and example inputs
3. confirm the bridge config still contains:
   - `starter_tilapia_basil_system.crop_system_type = architecture_dwc_raft`
4. keep the run read-only

Why this weekly check matters:

- it catches broken helper syntax quickly
- it catches drift in tracked first-slice example inputs
- it protects the current narrow bridge contract without touching runtime output

## Recommended Weekly Consistency/Blocker Audit

Run one narrow consistency/blocker audit weekly after the syntax/smoke pass.

Minimum weekly intent:

1. regenerate the first-slice repo audit output
2. review whether `crop_system_type` is still described as:
   - present
   - carried through as context
   - not activating architecture-conditioned business logic
3. review whether `saleable_harvest_mass_kg` is still described as:
   - unresolved
   - main blocker
   - not inferable from standing biomass, daily gain, or plant count
4. review whether the basil scenario-path split still stays clean between:
   - baseline scenario source
   - cumulative 7-day example-run scenario
5. review whether the reviewed-manual override flow still remains:
   - non-canonical
   - review-scoped
   - `null` unless a future approved value exists

## Exact Commands To Run

Weekly syntax/smoke commands:

```powershell
python -m py_compile scripts/materialize_first_slice_bridge.py scripts/build_first_slice_adapter_payload.py scripts/calculate_first_slice_unit_economics.py scripts/validate_first_slice_inputs.py scripts/generate_first_slice_repo_audit.py
python scripts/validate_first_slice_inputs.py
```

Weekly consistency/blocker audit commands:

```powershell
python scripts/generate_first_slice_repo_audit.py
rg -n "crop_system_type.*missing|crop_system_type.*absent|Use `crop_system_type` as the first and only bridge field added next|architecture-aware interpretation is still blocked by missing `crop_system_type`" docs
rg -n "saleable_harvest_mass_kg|main blocker|Do not infer from standing biomass|daily gain|plant count" docs scripts
```

## Expected Healthy Output

Healthy weekly syntax/smoke results:

- `python -m py_compile` exits successfully with no syntax errors
- `python scripts/validate_first_slice_inputs.py` reports `OK` for:
  - `configs/first_slice_bridge_baselines.yaml`
  - `scripts/example_first_slice_overrides.json`
  - `scripts/example_first_slice_reviewed_manual_overrides.json`
  - `scripts/example_first_slice_working_inputs.json`
- validator confirms:
  - `starter_tilapia_basil_system.crop_system_type=architecture_dwc_raft`

Healthy weekly consistency/blocker results:

- repo audit still shows live `crop_system_type` implementation references in the tracked bridge/config/helper/adapter path
- repo audit still shows `saleable_harvest_mass_kg` as unresolved rather than runtime-native
- reviewed-manual override flow still exists but remains paused at `null` unless a future approved value exists
- targeted `rg` checks do not find stale wording in active first-slice docs that says:
  - `crop_system_type` is missing as a current field
  - `crop_system_type` is still the next field to implement
- targeted `rg` checks still confirm that `saleable_harvest_mass_kg` is described as unresolved/main blocker

## What Should Trigger Human Review

Trigger human review if any of the following happen:

- `python -m py_compile` fails for any first-slice helper
- `python scripts/validate_first_slice_inputs.py` fails
- bridge config no longer validates as:
  - `starter_tilapia_basil_system.crop_system_type = architecture_dwc_raft`
- repo audit suggests `crop_system_type` is being described as missing, absent, or next-to-implement in active first-slice docs
- repo audit or targeted searches suggest `crop_system_type` is being used to justify pricing, revenue rules, or output-form logic
- repo audit or targeted searches suggest `saleable_harvest_mass_kg` is no longer being treated as unresolved without a corresponding approved upstream change
- `scripts/example_first_slice_reviewed_manual_overrides.json` changes from `null` to a non-null value without matching human review documentation
- basil scenario-path references drift so the baseline source path and cumulative 7-day example-run path are being mixed carelessly

## What Should Not Be Auto-Fixed

- canonical biology/model/business files
- runtime files under `data/simulation/**`
- non-null `saleable_harvest_mass_kg` values
- reviewed-manual override values without explicit human approval
- architecture-conditioned pricing, revenue, or output-form behavior
- historical planning notes whose wording needs judgment rather than mechanical replacement

## Recommended Automation Schedule

Recommended default schedule:

- run the syntax/smoke commands once per week
- run the consistency/blocker audit once per week immediately after the syntax/smoke commands
- keep both runs read-only by default
- require human review before any follow-up edits are applied

Recommended practical cadence:

- weekly scheduled local or CI read-only run
- additional manual run before merging first-slice script or doc changes that touch:
  - bridge config
  - adapter payload fields
  - reviewed-manual override files
  - first-slice docs
