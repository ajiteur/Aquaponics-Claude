---
fact_id: "PHB_0004"
domain: "water_chemistry"
type: "parameter"
confidence: "medium"
status: "provisional"
source_id: "rakocy_ista6_uvi_update"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/ph_buffer_facts.json"
tags:
  - truth
  - water_chemistry
  - candidate
---

# PHB_0004

> Under routine base dosing, UVI water alkalinity averaged 113.2 mg/L as CaCO3 (range 65.6 to 206.7) in batch basil and 88.6 (65.6 to 115.6) in staggered basil, with [[Reference/Explainers/pH|pH]] 7.4 and 7.1.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- system: UVI commercial-scale coupled DWC raft
- location: St. Croix

## Source

- Source ID: `rakocy_ista6_uvi_update`
- Section: `water quality table`
- Source type: `conference_proceedings_system_operator`

## Reliability

- Source tier: tier_1
- Source gate: trusted (Measured means and ranges from the operator.)
- Confidence: medium. Reason: Measured, but from one system.
- Corroboration: single_source; `rakocy_ista6_uvi_update`

## Related Notes

- [[Truths/Water Chemistry/Water Chemistry|Water Chemistry]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
