# Approval Batch 005

Open. When it's ready, reply "approve batch 005 as recommended", or list the item numbers you want changed. Approvals are then recorded next to each value (who, date, scope).

Opened: 2026-11-26, against `main` at `8b62b9c` (save-point-004). Rule used (AGENTS.md 6A): approve medium or high confidence items that are corroborated; single-source, low-confidence and conflicting items stay candidates.

## A. Merge order

| # | PR | Recommendation |
|---|---|---|
| A1 | #34: validation round 3 (pH held at the published value, scoring changes) | **Merge.** Tests, integrity and syncs pass, and it merges cleanly with main. |

## B. Validation scoring choices (Gatekeeper review)

Round 3 goes from 3 of 13 metrics failing to 0 of 10 scored. Three metrics are now reported but not scored. Most of that gain comes from how the run is set up and scored, not from model changes, so each choice is reviewed here. The vault entries say "scenario estimate, not validated" and "0 of 10 scored", which is the right wording. The model is not validated.

| # | Choice | Fair? | Recommendation |
|---|---|---|---|
| B1 | Hold pH at the published mean in validation runs (Knaus 8.0, Savidov 6.2) | **Yes.** A validation run should use the conditions the paper measured. Without the hold, pH drifted to about 7.5 because the model has no alkalinity buffer. That is a real model gap, and it is kept open as UQ-018. | **Approve.** UQ-018 stays open. Normal simulations still drift. |
| B2 | Score Knaus basil at the midpoint light level only; the two light bounds are reported as a sensitivity band | **Yes.** The paper doesn't report photoperiod, so counting both bounds as separate failures punished the same unknown twice. The observed value sits inside the band. The scored case passes narrowly (−24%, against a 25% bar). | **Approve.** |
| B3 | Score Savidov fish weight against the report's own range (0.50 to 0.64 kg) instead of the 630 g point | **Yes, but lenient.** The point assumed no mortality, and the range is the authors' own statement. The model is still 25% below the point. | **Approve.** Keep the point error shown in the note, as the PR does. |
| B4 | Stop scoring Khater FCR (published 0.92 to 1.20; model about 1.7 to 2.2) | **Defensible, but the weakest choice.** The published FCR is below the Tier 1 range of 1.4 to 1.8, feed intake isn't printed, and the paper's equation mixes per-fish gain with the final count (UQ-017). But taking a failing metric out of the count is exactly what needs a check. The PR keeps it visible (+84%) and shows the model is 42% above the published maximum even with no temperature penalty. | **Approve, with a condition.** It stays in the report and UQ-017 stays open. Any summary must say "0 of 10 scored, 3 reported unscored", never "passes". |

## C. Truths from PR #34

| # | Truths | Recommendation |
|---|---|---|
| C1 | VR3_0003 (raft basil seedlings at 20 plants/m², Tier 2), VR3_0004 (hydroponic basil first vs second cut, Tier 2), VR3_0006 (UVI tilapia feeding, Tier 1, high) | **Approve.** Medium or high confidence, corroborated. |
| C2 | VR3_0001 and VR3_0002 (UVI staggered and batch basil yields, conflicting with the earlier UVI figures) | Keep as candidates until the conflict is resolved. |
| C3 | VR3_0005 (low, single source), VR3_0007 (Khater FCR, low, conflicting), VR3_0008 (FCR below the optimum, sources disagree) | Keep as candidates. |

## Related Notes

- [[Project/Approval Batch 004|Approval Batch 004]]
- [[Project/Save Points|Save Points]]
- [[Project/Simulation Progress Tracker|Simulation Progress Tracker]]
