---
fact_id: "HEAT_0001"
domain: "environment"
type: "parameter"
confidence: "high"
status: "provisional"
source_id: "knmi_klimtab_9120_260"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/heating_climate_facts.json"
tags:
  - truth
  - environment
  - candidate
---

# HEAT_0001

> De Bilt (KNMI station 260) 1991-2020 normals: mean temperature 10.5 C for the year, 3.6 C in January and 18.3 C in July; global radiation about 3,648 MJ/m2 per year (364.8 kJ/cm2), from 54 MJ/m2 in December to 553 in July.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- location: De Bilt, Netherlands
- period: 1991-2020

## Source

- Source ID: `knmi_klimtab_9120_260`
- Section: `monthly table`
- Source type: `national_meteorological_service_normals`

## Reliability

- Source tier: tier_1
- Source gate: trusted (Official KNMI normals.)
- Confidence: high. Reason: Direct read; radiation column matched by position because PDF headers were garbled, totals fit.
- Corroboration: single_source; `knmi_klimtab_9120_260`

## Related Notes

- [[Truths/Environment/Environment|Environment]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
