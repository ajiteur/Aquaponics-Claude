---
fact_id: "PHB_0005"
domain: "operations"
type: "parameter"
confidence: "medium"
status: "provisional"
source_id: "srac_454"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/ph_buffer_facts.json"
tags:
  - truth
  - operations
  - candidate
---

# PHB_0005

> Aquaponics guidance keeps alkalinity at or above about 100 mg/L as CaCO3 (SRAC 454, NMSU; Texas A&M gives 50 to 150, preferably above 100) and never uses sodium bicarbonate, to keep sodium below about 50 mg/L.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- system: coupled aquaponics, general extension guidance

## Source

- Source ID: `srac_454`
- Section: `water quality, pH`
- Source type: `extension_fact_sheet`

## Reliability

- Source tier: tier_1
- Source gate: trusted (USDA-SRAC extension, corroborated by university extension and FAO 589.)
- Confidence: medium. Reason: Stated targets, not tested in trials.
- Corroboration: corroborated; `srac_454`, `nmsu_cr_680`, `texas_am_masabni_sink`, `fao_tp_589`

## Related Notes

- [[Truths/Operations/Operations|Operations]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
