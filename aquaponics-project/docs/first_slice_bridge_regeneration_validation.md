# First Slice Bridge Regeneration Validation

Status: `draft`

## Purpose

- Validate the first architecture-aware bridge end to end.
- Confirm the bridge stays limited to `crop_system_type`.
- Confirm the tracked config, narrow helper, native basil regeneration path, and regenerated basil `scenario_snapshot` chain all agree on the same bridge value.

## Scope

- Slice remains fixed as `basil bulk kg wholesale`.
- Bridge remains limited to `crop_system_type`.
- First baseline value remains exactly `architecture_dwc_raft`.
- This validation does not reopen economics, add `saleable_harvest_mass_kg`, or redesign scenario management.
- Regenerated runtime artifacts are treated as local validation outputs only.

## Current Tracked Bridge Source

- `configs/first_slice_bridge_baselines.yaml`

Exact current contents used in this validation:

```yaml
starter_tilapia_basil_system:
  crop_system_type: architecture_dwc_raft
```

## Current Helper Used

- `scripts/materialize_first_slice_bridge.py`

Role in this pass:

- read only `configs/first_slice_bridge_baselines.yaml`
- look up only `starter_tilapia_basil_system`
- materialize only `crop_system_type` into the basil baseline scenario

## Exact Target Baseline Scenario

- `data/simulation/scenarios/starter_tilapia_basil_system.json`

Expected bridge field at top level:

```json
"crop_system_type": "architecture_dwc_raft"
```

## Exact Native Regeneration Path Used

Native regeneration path used in this validation:

- `src/simulate_day.py`

Reason:

- it is the existing repo-native day-step regeneration path
- it regenerates the basil `scenario_snapshot` chain without touching `multi_day_summary.json`

Exact command sequence used:

```powershell
python scripts/materialize_first_slice_bridge.py
python src/simulate_day.py data/simulation/scenarios/starter_tilapia_basil_system.json
python src/simulate_day.py data/simulation/scenarios/starter_tilapia_basil_system_day_1.json
python src/simulate_day.py data/simulation/scenarios/starter_tilapia_basil_system_day_1_day_2.json
python src/simulate_day.py data/simulation/scenarios/starter_tilapia_basil_system_day_1_day_2_day_3.json
python src/simulate_day.py data/simulation/scenarios/starter_tilapia_basil_system_day_1_day_2_day_3_day_4.json
python src/simulate_day.py data/simulation/scenarios/starter_tilapia_basil_system_day_1_day_2_day_3_day_4_day_5.json
python src/simulate_day.py data/simulation/scenarios/starter_tilapia_basil_system_day_1_day_2_day_3_day_4_day_5_day_6.json
```

## Validation Commands Run

Commands run for this pass:

```powershell
Get-Content configs/first_slice_bridge_baselines.yaml
Get-FileHash data/simulation/multi_day_summary.json | Select-Object -ExpandProperty Hash
python scripts/materialize_first_slice_bridge.py
python src/simulate_day.py data/simulation/scenarios/starter_tilapia_basil_system.json
python src/simulate_day.py data/simulation/scenarios/starter_tilapia_basil_system_day_1.json
python src/simulate_day.py data/simulation/scenarios/starter_tilapia_basil_system_day_1_day_2.json
python src/simulate_day.py data/simulation/scenarios/starter_tilapia_basil_system_day_1_day_2_day_3.json
python src/simulate_day.py data/simulation/scenarios/starter_tilapia_basil_system_day_1_day_2_day_3_day_4.json
python src/simulate_day.py data/simulation/scenarios/starter_tilapia_basil_system_day_1_day_2_day_3_day_4_day_5.json
python src/simulate_day.py data/simulation/scenarios/starter_tilapia_basil_system_day_1_day_2_day_3_day_4_day_5_day_6.json
@'
import json
from pathlib import Path
paths = sorted(Path("data/simulation/scenarios").glob("starter_tilapia_basil_system*.json"))
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    print(f"{path.name}\t{data.get('crop_system_type')}")
'@ | python -
@'
import json
from pathlib import Path
logs = sorted(Path("data/simulation/day_logs").glob("day_log_*.json"), key=lambda p: p.stat().st_mtime, reverse=True)[:7]
for path in sorted(logs, key=lambda p: p.name):
    data = json.loads(path.read_text(encoding="utf-8"))
    print(f"{path.name}\t{Path(data['scenario_file']).name}\t{Path(data['saved_scenario_file']).name}")
'@ | python -
Get-FileHash data/simulation/multi_day_summary.json | Select-Object -ExpandProperty Hash
```

Key outputs:

- helper result:
  - `No change needed: ...starter_tilapia_basil_system.json already has crop_system_type=architecture_dwc_raft`
- scenario verification result:
  - all `starter_tilapia_basil_system*.json` files reported `architecture_dwc_raft`
- latest basil day-log verification result:
  - `day_log_1_20260422T022332Z.json` through `day_log_7_20260422T022334Z.json` pointed to the expected basil scenario chain
- `multi_day_summary.json` hash before and after:
  - `C46A398144783453178232255CC8EED3D21C4AE0B922B1C53381DD7E2CA246BD`

## What Changed Locally During Validation

Local validation changed only derived runtime artifacts:

- regenerated basil `scenario_snapshot` chain:
  - `starter_tilapia_basil_system_day_1.json`
  - `starter_tilapia_basil_system_day_1_day_2.json`
  - `starter_tilapia_basil_system_day_1_day_2_day_3.json`
  - `starter_tilapia_basil_system_day_1_day_2_day_3_day_4.json`
  - `starter_tilapia_basil_system_day_1_day_2_day_3_day_4_day_5.json`
  - `starter_tilapia_basil_system_day_1_day_2_day_3_day_4_day_5_day_6.json`
  - `starter_tilapia_basil_system_day_1_day_2_day_3_day_4_day_5_day_6_day_7.json`
- corresponding regenerated basil day logs:
  - `day_log_1_20260422T022332Z.json`
  - `day_log_2_20260422T022333Z.json`
  - `day_log_3_20260422T022333Z.json`
  - `day_log_4_20260422T022333Z.json`
  - `day_log_5_20260422T022333Z.json`
  - `day_log_6_20260422T022334Z.json`
  - `day_log_7_20260422T022334Z.json`

Observed effect:

- the regenerated scenario snapshots received fresh runtime content such as updated `updated_at_utc`, `derived`, and day-state values
- the bridge field remained unchanged during that regeneration

## What Was Verified Successfully

- the tracked config contains:
  - `starter_tilapia_basil_system -> crop_system_type = architecture_dwc_raft`
- the helper reads that tracked config and completes successfully
- the helper did not need to modify the baseline scenario in this run because the bridge field was already present
- the native basil regeneration path preserved `crop_system_type = architecture_dwc_raft` in:
  - `data/simulation/scenarios/starter_tilapia_basil_system.json`
  - all regenerated `starter_tilapia_basil_system*.json` scenario files in the basil chain
- the corresponding regenerated basil day logs point to the expected basil scenario chain in order
- `multi_day_summary.json` did not change
- no second architecture identifier was introduced

## What Remained Unchanged

- canonical biology/model/business files
- existing runtime scripts
- helper scope
- bridge field name:
  - `crop_system_type`
- first baseline bridge value:
  - `architecture_dwc_raft`
- `multi_day_summary.json`

## Whether the Bridge Is Now Proven End to End

- yes, for the current first bridge scope

What is proven:

- tracked config can hold the durable bridge source
- the narrow helper can materialize that bridge into the basil baseline scenario
- the native basil regeneration path can carry the field unchanged through the regenerated basil `scenario_snapshot` chain

## What Still Remains Outside Durable Tracked State

- `data/simulation/scenarios/*.json`
- regenerated basil `scenario_snapshot` files
- corresponding basil day logs

These remain derived runtime artifacts and local validation outputs only.

## Recommended Next Action

- keep the durable tracked bridge source in:
  - `configs/first_slice_bridge_baselines.yaml`
- keep the narrow helper as the first materialization step
- if a later pass needs runtime/business consumption, read `crop_system_type` from the regenerated basil scenario path without introducing a second bridge identifier
- keep `saleable_harvest_mass_kg` as a separate later bridge
