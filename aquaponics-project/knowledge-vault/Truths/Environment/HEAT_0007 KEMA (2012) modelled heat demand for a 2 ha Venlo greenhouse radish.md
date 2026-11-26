---
fact_id: "HEAT_0007"
domain: "environment"
type: "parameter"
confidence: "medium"
status: "provisional"
source_id: "kema_2012_edepot_289335"
source_tier: "tier_2"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/heating_climate_facts.json"
tags:
  - truth
  - environment
  - candidate
---

# HEAT_0007

> KEMA (2012) modelled heat demand for a 2 ha Venlo greenhouse: radish at 12 C day / 8 C night 381.5 MJ/m2/yr (12.0 m3 a.e.); cold pot plant at 15/13 C with screen 682.4 MJ/m2/yr (21.5 m3 a.e.).

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- region: Netherlands
- structure: Venlo glasshouse, 2 ha
- crop: radish; cold pot plant

## Source

- Source ID: `kema_2012_edepot_289335`
- Section: `results`
- Source type: `research_consultancy_report_for_sector_programme`

## Reliability

- Source tier: tier_2
- Source gate: conditional (Modelled, not measured; consultancy report hosted by WUR.)
- Confidence: medium. Reason: Stated setpoints and house; not herbs; conflicts with KEMA 2009 (contradiction ticket UQ-012).
- Corroboration: conflicting; `kema_2012_edepot_289335`, `kema_2009_edepot_289333`

## Related Notes

- [[Truths/Environment/Environment|Environment]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
