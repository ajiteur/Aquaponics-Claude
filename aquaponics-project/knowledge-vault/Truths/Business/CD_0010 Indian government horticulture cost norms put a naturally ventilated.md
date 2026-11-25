---
fact_id: "CD_0010"
domain: "business"
type: "parameter"
confidence: "low"
status: "provisional"
source_id: "midh_hmneh_cost_norms_2018_19"
source_tier: "tier_1"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/component_design_facts.json"
tags:
  - truth
  - business
  - candidate
---

# CD_0010

> Indian government horticulture cost norms put a naturally ventilated tubular polyhouse at Rs 935 per m2 (MIDH HMNEH 2018-19) and, earlier, Rs 400 to 650 per m2 excluding micro-irrigation (NHB, 2008).

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- system: naturally ventilated polyhouse
- location: India (HMNEH norm is for North-East and Himalayan states)
- year basis: 2008 and 2018-19

## Source

- Source ID: `midh_hmneh_cost_norms_2018_19`
- Section: `c_1_i`
- Source type: `government_scheme_document`

## Reliability

- Source tier: tier_1
- Source gate: conditional (official_norms_but_old_and_regional)
- Confidence: low. Reason: Norms are subsidy ceilings, not quotes; the plains norm for 2026 was not read.
- Corroboration: corroborated; `nhb_cost_norms_2008`

## Related Notes

- [[Truths/Business/Business|Business]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
