---
fact_id: "PHB_0003"
domain: "water_chemistry"
type: "parameter"
confidence: "low"
status: "provisional"
source_id: "rakocy_ista6_uvi_update"
source_tier: "tier_1"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/ph_buffer_facts.json"
tags:
  - truth
  - water_chemistry
  - candidate
---

# PHB_0003

> UVI's recorded base use works out to about 11 to 13 g of base per kg of feed (our arithmetic), roughly one-fifteenth of what [[Reference/Explainers/Nitrification|nitrification]] stoichiometry alone (about 0.2 kg CaCO3 per kg of 32 percent protein feed) would need; denitrification in the filter tanks, plant nitrate uptake and how fish ammonia excretion is counted are the likely reasons.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- system: UVI commercial-scale coupled DWC raft
- basis: derived from PHB_0002 doses and the ISTA6 feed rate

## Source

- Source ID: `rakocy_ista6_uvi_update`
- Section: `derived`
- Source type: `derived_from_conference_proceedings`

## Reliability

- Source tier: tier_1
- Source gate: conditional (Derived arithmetic, not a printed value; the explanation is an inference.)
- Confidence: low. Reason: Our arithmetic; the cause of the gap is not measured.
- Corroboration: single_source; `rakocy_ista6_uvi_update`

## Related Notes

- [[Truths/Water Chemistry/Water Chemistry|Water Chemistry]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
