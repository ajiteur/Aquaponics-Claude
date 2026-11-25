---
fact_id: "UE_0004"
domain: "business"
type: "finding"
confidence: "low"
status: "provisional"
source_id: "quagrainie_purdue_indiana_aquaponics"
source_tier: "tier_1"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/unit_economics_facts.json"
tags:
  - truth
  - business
  - candidate
---

# UE_0004

> In Purdue's representative Indiana basil-and-tilapia aquaponics farms, labour was 62-67% of operating cost, and blended cost per lb of output fell from USD 4.44 (small) to USD 3.60 (large).

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- system: hypothetical representative greenhouse aquaponics farms (small, medium, large)
- crop: basil plus tilapia
- location: Indiana, USA
- year basis: USD, year not stated

## Source

- Source ID: `quagrainie_purdue_indiana_aquaponics`
- Section: `tables_6_to_9`
- Source type: `institutional_report`

## Reliability

- Source tier: tier_1
- Source gate: conditional (university_report_with_internal_inconsistencies_and_hypothetical_farms)
- Confidence: low. Reason: Hypothetical farms, no grow area, no price year, and several internal inconsistencies in the paper.
- Corroboration: corroborated; `tokunaga_2015_hawaii_aquaponics_economics`, `engle_2015_srac_5006`

## Related Notes

- [[Truths/Business/Business|Business]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
