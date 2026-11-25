---
fact_id: "UE_0006"
domain: "business"
type: "parameter"
confidence: "low"
status: "provisional"
source_id: "cbi_2024_fresh_culinary_herbs"
source_tier: "tier_1"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/unit_economics_facts.json"
tags:
  - truth
  - business
  - candidate
---

# UE_0006

> CBI's 2024 herbs study lists Dutch importing-wholesaler basil prices of EUR 7.50 (Kenya), 8.00 (Ethiopia) and 9.25 (Israel) per kg box, dated March 2020.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- market: Netherlands, importing wholesaler price lists
- product: fresh cut basil, kg boxes
- year basis: March 2020, EUR

## Source

- Source ID: `cbi_2024_fresh_culinary_herbs`
- Section: `table_1`
- Source type: `institutional_report`

## Reliability

- Source tier: tier_1
- Source gate: conditional (government_backed_study_but_price_list_examples_from_march_2020)
- Confidence: low. Reason: Government-backed market study, but price-list examples (not transactions) and more than 5 years old.
- Corroboration: single_source

## Related Notes

- [[Truths/Business/Business|Business]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
