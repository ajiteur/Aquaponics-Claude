---
fact_id: "HEAT_0004"
domain: "environment"
type: "parameter"
confidence: "medium"
status: "accepted"
source_id: "asabe_ep406_4"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/heating_climate_facts.json"
tags:
  - truth
  - environment
  - accepted
---

# HEAT_0004

> Greenhouse cover heat-loss coefficients (W/m2 K): single glass about 6.2 (ASABE) to 7-8 (NSW DPI); single plastic film 6.2 to 8.5; double polyethylene about 4.0 (4.0 to 5.0); single glass with a closed, well-sealed thermal blanket 4.0.

## Context

- structure: greenhouse covers, generic

## Source

- Source ID: `asabe_ep406_4`
- Section: `Table 1`
- Source type: `engineering_standard`

## Reliability

- Source tier: tier_1
- Source gate: trusted (ASABE engineering practice, with government and extension corroboration.)
- Confidence: medium. Reason: Double PE agrees across three sources; single glass and film differ (6.2 vs 7 to 8.5), kept as ranges. Read through fetch summaries.
- Corroboration: corroborated; `asabe_ep406_4`, `nsw_dpi_heating_greenhouses`, `vt_spes_821`

## Related Notes

- [[Truths/Environment/Environment|Environment]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
