---
fact_id: "CD_0009"
domain: "business"
type: "parameter"
confidence: "low"
status: "provisional"
source_id: "nfdb_ras_recent_trends"
source_tier: "tier_1"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/component_design_facts.json"
tags:
  - truth
  - business
  - candidate
---

# CD_0009

> India's NFDB GIFT tilapia RAS model costs one 90 m3 tank at Rs 1.5 lakh and its pumps, filters, aerators, pipes and valves at Rs 4.5 lakh, with fingerlings at Rs 4 each and floating feed at Rs 30/kg.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- system: RAS, one 90 m3 tank, GIFT tilapia
- location: India
- year basis: undated (file name suggests 2017)

## Source

- Source ID: `nfdb_ras_recent_trends`
- Section: `gift_tilapia_ras_model`
- Source type: `government_scheme_document`

## Reliability

- Source tier: tier_1
- Source gate: conditional (official_but_undated_with_arithmetic_errors)
- Confidence: low. Reason: The model's own numbers disagree (6,000 vs 4,500 fingerlings; feed total vs cost); 2026 listings price feed at Rs 45-47/kg.
- Corroboration: conflicting; `retail_in_indiamart`

## Related Notes

- [[Truths/Business/Business|Business]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
