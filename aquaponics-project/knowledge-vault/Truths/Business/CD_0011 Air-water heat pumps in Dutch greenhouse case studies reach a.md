---
fact_id: "CD_0011"
domain: "business"
type: "parameter"
confidence: "medium"
status: "accepted"
source_id: "fennis_2024_heat_pumps"
source_tier: "tier_2"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/component_design_facts.json"
tags:
  - truth
  - business
  - accepted
---

# CD_0011

> Air-water heat pumps in Dutch greenhouse case studies reach a modelled seasonal COP of 3.7 (2 ha boiler holding, 45 C supply) to 4.4-4.6 (5 ha CHP holdings, 45/40 C supply). A 2012 KEMA study gives an air-source average of 3.94 and a sector presentation uses COP 4.

## Context

- system: greenhouse heating, low-temperature (35-45 C) distribution
- location: Netherlands
- scale: 2-5 ha commercial greenhouses
- year basis: 2012 and 2024

## Source

- Source ID: `fennis_2024_heat_pumps`
- Section: `slide: Doorrekening van de Lucht-Water warmtepomp`
- Source type: `sector_presentation`

## Reliability

- Source tier: tier_2
- Source gate: conditional (modelled_scop_hectare_scale)
- Confidence: medium. Reason: Three Tier 2 sources agree within about 3.7-4.6; values are modelled for large greenhouses, not measured in a small one.
- Corroboration: corroborated; `glastuinbouw_nl_bax_heat_pump`, `kema_2012_kas_energiebron_heat_pumps`

## Related Notes

- [[Truths/Business/Business|Business]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
