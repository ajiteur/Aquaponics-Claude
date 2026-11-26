---
fact_id: "HEAT_0010"
domain: "environment"
type: "parameter"
confidence: "low"
status: "provisional"
source_id: "iima_2009_11_04_sharan"
source_tier: "tier_3"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/heating_climate_facts.json"
tags:
  - truth
  - environment
  - candidate
---

# HEAT_0010

> A fan-pad cooled 120 m2 polyhouse in semi-arid North-West India would use about 15 to 18 kWh per day.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- region: North-West India (not Karnataka)
- structure: fan-pad polyhouse, 120 m2

## Source

- Source ID: `iima_2009_11_04_sharan`
- Section: `working paper`
- Source type: `business_school_working_paper`

## Reliability

- Source tier: tier_3
- Source gate: conditional (Working paper, not peer reviewed; wrong region.)
- Confidence: low. Reason: Single source; text near the figure appears garbled.
- Corroboration: single_source; `iima_2009_11_04_sharan`

## Related Notes

- [[Truths/Environment/Environment|Environment]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
