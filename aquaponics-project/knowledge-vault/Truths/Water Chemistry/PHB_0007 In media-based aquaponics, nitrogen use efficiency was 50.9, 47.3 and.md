---
fact_id: "PHB_0007"
domain: "water_chemistry"
type: "parameter"
confidence: "medium"
status: "provisional"
source_id: "zou_2016_bioresource_technology_210_81"
source_tier: "tier_1"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/ph_buffer_facts.json"
tags:
  - truth
  - water_chemistry
  - candidate
---

# PHB_0007

> In media-based aquaponics, nitrogen use efficiency was 50.9, 47.3 and 44.7 percent at [[Reference/Explainers/pH|pH]] 6.0, 7.5 and 9.0, and the share of N lost as N2O fell from 2.0 to 0.6 percent as pH rose; the authors recommend pH 6.0.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- system: media-based aquaponics, lab scale
- note: context_split with PHB_0006: NUE vs nitrification rate

## Source

- Source ID: `zou_2016_bioresource_technology_210_81`
- Section: `abstract`
- Source type: `peer_reviewed_journal`

## Reliability

- Source tier: tier_1
- Source gate: conditional (Peer-reviewed; full text not read.)
- Confidence: medium. Reason: Abstract-level read; one system.
- Corroboration: single_source; `zou_2016_bioresource_technology_210_81`

## Related Notes

- [[Truths/Water Chemistry/Water Chemistry|Water Chemistry]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
