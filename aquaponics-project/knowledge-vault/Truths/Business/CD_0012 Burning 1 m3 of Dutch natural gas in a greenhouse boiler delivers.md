---
fact_id: "CD_0012"
domain: "business"
type: "parameter"
confidence: "medium"
status: "accepted"
source_id: "kema_2012_kas_energiebron_heat_pumps"
source_tier: "tier_2"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/component_design_facts.json"
tags:
  - truth
  - business
  - accepted
---

# CD_0012

> Burning 1 m3 of Dutch natural gas in a greenhouse boiler delivers about 8.6 to 8.8 kWh of heat: 31.7 MJ/Nm3 at 98% boiler efficiency (KEMA 2012) gives 8.63 kWh, and a sector presentation states about 8.79 kWh.

## Context

- system: condensing gas boiler, lower heating value
- location: Netherlands
- year basis: 2012 and about 2023

## Source

- Source ID: `kema_2012_kas_energiebron_heat_pumps`
- Section: `p.33`
- Source type: `institute_report`

## Reliability

- Source tier: tier_2
- Source gate: conditional (kema_value_read_through_summary)
- Confidence: medium. Reason: Two Tier 2 sources within 2%; the KEMA figure was not read verbatim.
- Corroboration: corroborated; `glastuinbouw_nl_bax_heat_pump`

## Related Notes

- [[Truths/Business/Business|Business]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
