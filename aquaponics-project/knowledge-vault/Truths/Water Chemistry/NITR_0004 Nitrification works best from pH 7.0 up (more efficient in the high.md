---
fact_id: "NITR_0004"
domain: "water_chemistry"
type: "parameter"
confidence: "medium"
status: "provisional"
source_id: "srac_454_rakocy_masser_losordo_aquaponics"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/nitrogen_cycle_facts.json"
tags:
  - truth
  - water_chemistry
  - candidate
---

# NITR_0004

> Nitrification works best from [[Reference/Explainers/pH|pH]] 7.0 up (more efficient in the high 8s) and practically stops below pH 6.0.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- system: aquaponics and RAS biofilters

## Source

- Source ID: `srac_454_rakocy_masser_losordo_aquaponics`
- Section: `ph_effects`
- Source type: `university_extension`

## Reliability

- Source tier: tier_1
- Source gate: trusted (source level E4; direct_quote and paraphrase; context partial)
- Confidence: medium. Reason: SRAC 454 and the UVI system page agree on the endpoints; matches existing canon (inhibited at or below pH 6.0).
- Corroboration: corroborated; `uvi_aquaponic_systems_page`

## Related Notes

- [[Truths/Water Chemistry/Water Chemistry|Water Chemistry]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
