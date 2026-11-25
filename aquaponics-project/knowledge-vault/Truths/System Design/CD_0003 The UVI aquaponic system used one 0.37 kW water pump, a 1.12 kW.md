---
fact_id: "CD_0003"
domain: "system_design"
type: "parameter"
confidence: "medium"
status: "accepted"
source_id: "uvi_aquaponic_system_design"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/component_design_facts.json"
tags:
  - truth
  - system_design
  - accepted
---

# CD_0003

> The UVI aquaponic system used one 0.37 kW water pump, a 1.12 kW blower for fish and degassing and a 0.75 kW blower for the hydroponic tanks, 2.24 kW in total for 214 m2 of plant area.

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
- Confidence: medium. Reason: Rated power, not metered use; metered use (Heidemann and Bailey) was 23,360 kWh/yr, about 2.7 kW average.
- Corroboration: corroborated; `heidemann_bailey_2015_uvi_economics`

## Related Notes

- [[Truths/System Design/System Design|System Design]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
