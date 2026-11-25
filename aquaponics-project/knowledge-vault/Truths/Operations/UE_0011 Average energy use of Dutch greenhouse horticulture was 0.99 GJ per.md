---
fact_id: "UE_0011"
domain: "operations"
type: "parameter"
confidence: "medium"
status: "provisional"
source_id: "wur_energiemonitor_2024"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/unit_economics_facts.json"
tags:
  - truth
  - operations
  - candidate
---

# UE_0011

> Average energy use of Dutch greenhouse horticulture was 0.99 GJ per m2 in 2024 (temperature-corrected, provisional), across about 10,000 ha and all crop types.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- scope: all Dutch greenhouse horticulture, incl. lit crops
- year basis: 2024, provisional

## Source

- Source ID: `wur_energiemonitor_2024`
- Section: `summary_s1`
- Source type: `official_statistics`

## Reliability

- Source tier: tier_1
- Source gate: trusted (government_funded_wur_statistics_series)
- Confidence: medium. Reason: Government-funded WUR time series; a sector average, not specific to basil or unheated production.
- Corroboration: single_source

## Related Notes

- [[Truths/Operations/Operations|Operations]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
