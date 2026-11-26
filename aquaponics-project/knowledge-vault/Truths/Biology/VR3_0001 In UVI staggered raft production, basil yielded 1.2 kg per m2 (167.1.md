---
fact_id: "VR3_0001"
domain: "biology"
type: "parameter"
confidence: "medium"
status: "provisional"
source_id: "rakocy_2004_tilapia_basil"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/validation_round3_facts.json"
tags:
  - truth
  - biology
  - candidate
---

# VR3_0001

> In UVI staggered raft production, basil yielded 1.2 kg/m2 (167.1 g per plant) at the first harvest 28 days after transplant and 2.4 kg/m2 (327.1 g per plant) at the regrowth harvest; the authors note slow growth after transplanting while plants became established.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- species: basil (Genovese)
- system: UVI commercial-scale coupled DWC raft, staggered weekly planting, 8 plants/m2, cut at 15 cm
- location: St. Croix, tropical, outdoor

## Source

- Source ID: `rakocy_2004_tilapia_basil`
- Section: `Table 4 and text`
- Source type: `institutional_report`

## Reliability

- Source tier: tier_1
- Source gate: trusted (UVI research report (published as Acta Horticulturae 648).)
- Confidence: medium. Reason: Measured at the anchor site and density, but the same paper's batch system shows no first-cut penalty, and two raft trials elsewhere show none either.
- Corroboration: conflicting; `rakocy_2004_tilapia_basil`, `modarelli_2023_plants`, `corrado_2020_agronomy`

## Related Notes

- [[Truths/Biology/Biology|Biology]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
