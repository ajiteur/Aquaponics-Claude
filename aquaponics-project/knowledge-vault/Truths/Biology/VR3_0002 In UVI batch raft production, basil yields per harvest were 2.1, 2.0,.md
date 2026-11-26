---
fact_id: "VR3_0002"
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

# VR3_0002

> In UVI batch raft production, basil yields per harvest were 2.1, 2.0, 1.7 and 2.0 kg/m2 (first harvest after transplant, then three regrowth harvests; production period about 28.3 days), so the first harvest was not lower than later ones.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- species: basil (Genovese)
- system: UVI coupled DWC raft, batch planting of the whole 214 m2, 8 plants/m2
- location: St. Croix, tropical, outdoor

## Source

- Source ID: `rakocy_2004_tilapia_basil`
- Section: `Table 3`
- Source type: `institutional_report`

## Reliability

- Source tier: tier_1
- Source gate: trusted (UVI research report.)
- Confidence: medium. Reason: Direct table values; conflicts with the same paper's staggered result (VR3_0001), so the context (batch vs staggered planting) matters and the cause is not stated.
- Corroboration: conflicting; `rakocy_2004_tilapia_basil`

## Related Notes

- [[Truths/Biology/Biology|Biology]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
