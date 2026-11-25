---
fact_id: "CD_0001"
domain: "system_design"
type: "parameter"
confidence: "medium"
status: "provisional"
source_id: "uvi_aquaponic_system_design"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/component_design_facts.json"
tags:
  - truth
  - system_design
  - candidate
---

# CD_0001

> The UVI commercial aquaponic system produced about 5 t of tilapia a year from four 7.8 m3 rearing tanks, about 160 kg of fish per m3 of rearing tank per year.

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
- Source gate: trusted (university_research_station_design_summary)
- Confidence: medium. Reason: Direct figures, arithmetic checks (5,000 / 31.2 = 160); one site, tropical water.
- Corroboration: corroborated; `ista9_rakocy_commercial_scale_aquaponic_system`

## Related Notes

- [[Truths/System Design/System Design|System Design]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
