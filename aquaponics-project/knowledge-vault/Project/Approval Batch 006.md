# Approval Batch 006

**Status: approved as recommended by Ajit on 2026-11-26 (23:13 Europe/Amsterdam).** Each approval is recorded next to its value. Two points for later, not part of this approval: the carbonate constants (Plummer and Busenberg 1982) should be checked against phreeqc.dat before the buffer model is accepted, and UQ-019 (which alkalinity returns to credit by default) is Ajit's call.

Opened: 2026-11-26, against `main` at `ee43d55`. Rule used (AGENTS.md 6A): approve medium or high confidence items that are corroborated; single-source, low-confidence and conflicting items stay candidates.

## A. Merge order

| # | PR | Recommendation |
|---|---|---|
| A1 | #36: the Batch 005 approval record (and this note) | **Merge first.** PR #35 was merged at its first commit only, so the Batch 005 record is not on `main` yet. Tests, integrity and syncs pass. |
| A2 | #37: pH and alkalinity buffer (opt-in), UQ-019, and project files moved into the repo | **Merge second.** Tests, integrity and syncs pass, and it merges cleanly with main. After #36 it conflicts only in two generated truth notes, so its thread re-runs the truths export. |
| A3 | Tag `save-point-006` on the merge of #37 | `save-point-005` was pushed on `ee43d55`, before #36. That commit is green but has no Batch 005 record. The tag can stay; save-point-006 is the first tag with both. |

## B. Model

| # | Item | Recommendation |
|---|---|---|
| B1 | Carbonate alkalinity buffer model (alkalinity balance and carbonate pH, opt-in) | Keep as candidate. It is a new model. Validation runs still hold pH at the published value; the pH-free run is reported, not scored. |

## C. Truths from PR #37

| # | Truths | Recommendation |
|---|---|---|
| C1 | PHB_0001 (7.05 g alkalinity per g TAN-N nitrified, high), PHB_0002 (UVI base use and make-up water, medium), PHB_0005 (keep alkalinity at or above about 100 mg/L, medium), PHB_0009 (Dutch tap water bicarbonate 116 to 190 mg/L, high) | **Approve.** Tier 1, corroborated. |
| C2 | PHB_0004, PHB_0006, PHB_0007, PHB_0008, PHB_0010, PHB_0012 (medium or high, single source) | Keep as candidates until a second source agrees. |
| C3 | PHB_0003 (UVI base per kg feed, our own arithmetic, low) and PHB_0011 (South Indian borewell alkalinity, low) | Keep as candidates. |

## D. Inputs filed from project files

| # | Item | Recommendation |
|---|---|---|
| D1 | `farm_viability_inputs_v0.json`: 9 inputs marked "awaiting Ajit" (location, scale, budget and the like) | Nothing to approve. They are yours to supply, and only needed if the farm go/no-go comes back. |
| D2 | `india_state_location_inputs_v0.json`: the study price band, marked candidate and not used as the default | Keep as candidate (as in Batch 002 B1). |

## Related Notes

- [[Project/Approval Batch 005|Approval Batch 005]]
- [[Project/Save Points|Save Points]]
- [[Project/Simulation Progress Tracker|Simulation Progress Tracker]]
