---
fact_id: "PHB_0006"
domain: "water_chemistry"
type: "parameter"
confidence: "medium"
status: "provisional"
source_id: "tyson_2008_hortscience_43_719"
source_tier: "tier_1"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/ph_buffer_facts.json"
tags:
  - truth
  - water_chemistry
  - candidate
---

# PHB_0006

> In perlite biofilters with cucumber, [[Reference/Explainers/TAN|TAN]] removal was 19, 31 and 80 g/m3/day at [[Reference/Explainers/pH|pH]] 6, 7 and 8, so [[Reference/Explainers/Nitrification|nitrification]] ran about four times faster at pH 8 than at pH 6.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- system: perlite biofilter, cucumber aquaponics
- note: context_split with PHB_0007: different outcome measured

## Source

- Source ID: `tyson_2008_hortscience_43_719`
- Section: `abstract`
- Source type: `peer_reviewed_journal`

## Reliability

- Source tier: tier_1
- Source gate: conditional (Peer-reviewed, read via abstract record.)
- Confidence: medium. Reason: Abstract-level read; one system.
- Corroboration: single_source; `tyson_2008_hortscience_43_719`

## Related Notes

- [[Truths/Water Chemistry/Water Chemistry|Water Chemistry]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
