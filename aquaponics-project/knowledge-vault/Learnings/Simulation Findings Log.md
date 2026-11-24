# Simulation Findings Log

What the simulation shows, newest first. These are **scenario estimates, not validated**: they describe the model, not the real world, and they are never truths.

## 2026-11-25: Basil grown to a full 28-day harvest

Run: `src/simulate_crop_cycle.py` on the `basil_raft_crop_cycle` scenarios (PR #1). Basil cut-mass growth is calibrated to the UVI anchor: 8 plants/m², 28 days, 2.0 kg/m² per harvest.

- **Starter fixture (8 kg tilapia, 90 basil plants, 11.25 m²): about 1.2 kg/m² per harvest.** The basil runs short of nitrate, which falls from 42 to about 15 mg/L by day 27. Feed per m² is about a tenth of what UVI used.
- **Fish scaled to the UVI feed ratio: 2.0 kg/m².** Water quality collapses, though: TAN about 14 mg/L, NH3 about 1.1 mg/L. The placeholder nitrification model can't remove that load, so this isn't a valid operating point.
- **Bug found:** before this run, basil was never nitrate-limited because of a mismatched field name. Earlier basil runs were too optimistic.
- **Model gap:** the basil pH score is 0 at any pH from 6.9 to 7.6, the normal aquaponic range, because it uses hydroponic ranges. UVI grew basil well at pH 7.4.

Related truths: [[Truths/Biology/Biology|Biology]] (CROP_0002 to CROP_0004), [[Truths/Operations/Operations|Operations]] (CROP_0006, CROP_0007).

## Related Notes

- [[Learnings/Simulation Learnings|Simulation Learnings]] (older generated summary)
- [[Project/Project|Project]]
