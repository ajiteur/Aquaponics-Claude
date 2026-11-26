---
fact_id: "PHB_0010"
domain: "environment"
type: "parameter"
confidence: "high"
status: "provisional"
source_id: "bis_is_10500_2012"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/ph_buffer_facts.json"
tags:
  - truth
  - environment
  - candidate
---

# PHB_0010

> India's drinking-water standard IS 10500:2012 sets total alkalinity at 200 mg/L as CaCO3 acceptable and 600 permissible, total hardness 200 and 600, and [[Reference/Explainers/pH|pH]] 6.5 to 8.5.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- location: India
- water: drinking water standard

## Source

- Source ID: `bis_is_10500_2012`
- Section: `Tables 1 and 2`
- Source type: `official_standard`

## Reliability

- Source tier: tier_1
- Source gate: trusted (National standard.)
- Confidence: high. Reason: Official text, Tables 1 and 2.
- Corroboration: single_source; `bis_is_10500_2012`

## Related Notes

- [[Truths/Environment/Environment|Environment]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
