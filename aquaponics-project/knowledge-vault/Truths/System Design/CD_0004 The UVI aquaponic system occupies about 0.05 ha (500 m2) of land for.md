---
fact_id: "CD_0004"
domain: "system_design"
type: "parameter"
confidence: "low"
status: "provisional"
source_id: "uvi_aquaponic_system_design"
source_tier: "tier_1"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/component_design_facts.json"
tags:
  - truth
  - system_design
  - candidate
---

# CD_0004

> The UVI aquaponic system occupies about 0.05 ha (500 m2) of land for 214 m2 of plant growing area, about 2.3 m2 of land per m2 of grow area.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- system: UVI commercial-scale coupled DWC raft, 214 m2 grow area, 4 rearing tanks
- location: St. Croix, US Virgin Islands, tropical
- species: tilapia with lettuce or basil

## Source

- Source ID: `uvi_aquaponic_system_design`
- Section: `system_summary`
- Source type: `institutional_report`

## Reliability

- Source tier: tier_1
- Source gate: conditional (land_area_may_include_space_beyond_the_system)
- Confidence: low. Reason: One site; the land figure is rounded and its boundary is not described.
- Corroboration: single_source

## Related Notes

- [[Truths/System Design/System Design|System Design]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
