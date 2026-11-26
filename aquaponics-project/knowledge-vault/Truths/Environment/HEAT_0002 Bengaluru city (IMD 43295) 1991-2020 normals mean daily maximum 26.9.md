---
fact_id: "HEAT_0002"
domain: "environment"
type: "parameter"
confidence: "high"
status: "accepted"
source_id: "imd_bengaluru_climatological_table_1991_2020"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/heating_climate_facts.json"
tags:
  - truth
  - environment
  - accepted
---

# HEAT_0002

> Bengaluru city (IMD 43295) 1991-2020 normals: mean daily maximum 26.9 C (December) to 34.1 C (April); mean daily minimum 16.1 C (January) to 22.1 C (April).

## Context

- location: Bengaluru, Karnataka, India
- period: 1991-2020

## Source

- Source ID: `imd_bengaluru_climatological_table_1991_2020`
- Section: `climatological table`
- Source type: `national_meteorological_service_normals`

## Reliability

- Source tier: tier_1
- Source gate: trusted (Official IMD table.)
- Confidence: high. Reason: Direct read; reproduced exactly by a Wikipedia template citing IMD.
- Corroboration: corroborated; `imd_bengaluru_climatological_table_1991_2020`, `wikipedia_bengaluru_weather_box_mirror`

## Related Notes

- [[Truths/Environment/Environment|Environment]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
