---
fact_id: "HEAT_0005"
domain: "environment"
type: "definition"
confidence: "high"
status: "provisional"
source_id: "iplo_aardgasequivalenten"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/heating_climate_facts.json"
tags:
  - truth
  - environment
  - candidate
---

# HEAT_0005

> One Dutch natural-gas equivalent (m3 a.e.) is defined as 31.65 MJ on a lower heating value basis.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- region: Netherlands

## Source

- Source ID: `iplo_aardgasequivalenten`
- Section: `Tabel aardgasequivalenten`
- Source type: `government_reference_table`

## Reliability

- Source tier: tier_1
- Source gate: trusted (Dutch government definition.)
- Confidence: high. Reason: Definition; KEMA 2012 figures (381.5 MJ = 12.0 m3 a.e.) match.
- Corroboration: corroborated; `iplo_aardgasequivalenten`, `kema_2012_edepot_289335`

## Related Notes

- [[Truths/Environment/Environment|Environment]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
