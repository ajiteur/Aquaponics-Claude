---
fact_id: "PHB_0012"
domain: "biology"
type: "parameter"
confidence: "medium"
status: "provisional"
source_id: "hamad_2024_aquaculture_590_741038"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/ph_buffer_facts.json"
tags:
  - truth
  - biology
  - candidate
---

# PHB_0012

> Short CO2 exposure depresses Nile tilapia resting metabolism (about 11, 22 and 29 percent at 10, 30 and 60 mg/L CO2 after one hour at 26 C), while extension guidance keeps dissolved CO2 below 20 mg/L.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- species: Nile tilapia
- system: lab respirometry, 26 C
- note: no growth endpoint; context_split with the SRAC 452 guideline

## Source

- Source ID: `hamad_2024_aquaculture_590_741038`
- Section: `results`
- Source type: `peer_reviewed_journal`

## Reliability

- Source tier: tier_1
- Source gate: trusted (Peer-reviewed physiology study.)
- Confidence: medium. Reason: Lab respirometry only; growth effects not measured.
- Corroboration: single_source; `hamad_2024_aquaculture_590_741038`, `srac_452`

## Related Notes

- [[Truths/Biology/Biology|Biology]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
