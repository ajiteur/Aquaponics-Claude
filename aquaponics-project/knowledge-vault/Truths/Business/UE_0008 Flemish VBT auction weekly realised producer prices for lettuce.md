---
fact_id: "UE_0008"
domain: "business"
type: "parameter"
confidence: "low"
status: "provisional"
source_id: "vbt_landbouwcijfers_vlaanderen_weekly_prices"
source_file: "data/knowledge/atomic_facts/unit_economics_facts.json"
tags:
  - truth
  - business
  - candidate
---

# UE_0008

> Flemish VBT auction weekly realised producer prices for lettuce ('Sla') ranged from about EUR 0.19 (week 24, 2025) to EUR 0.72 (week 24, 2024) per unit, probably per head.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- market: Belgium (Flanders), VBT auctions, producer price
- product: lettuce, type not stated
- year basis: 2024-2025, EUR

## Reliability

- Source tier: T1_official_statistics
- Confidence: low
- Confidence reason: Official realised prices, but the text extraction was column-scrambled and the unit per product is not printed.
- Cross check: Far below US farm-gate lettuce prices used in Tokunaga et al. and Zappernick et al., as expected for an auction channel.

## Source

- Source ID: `vbt_landbouwcijfers_vlaanderen_weekly_prices`
- Section: `weekly_price_pdfs_w24_2024_w50_2024_w24_2025`
- Source type: `official_statistics`

## Related Notes

- [[Truths/Business/Business|Business]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
