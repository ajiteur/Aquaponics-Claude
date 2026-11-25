---
fact_id: "NITR_0001"
domain: "system_design"
type: "parameter"
confidence: "medium"
status: "provisional"
source_id: "srac_454_rakocy_masser_losordo_aquaponics"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/nitrogen_cycle_facts.json"
tags:
  - truth
  - system_design
  - candidate
---

# NITR_0001

> In UVI-style raft aquaponics, the raft can treat the waste of about 180 g of fish feed per m2 of grow area per day, if solids are removed before the raft.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- system: coupled DWC raft (UVI-style)
- condition: solids removed upstream of the raft

## Source

- Source ID: `srac_454_rakocy_masser_losordo_aquaponics`
- Section: `waste_treatment_capacity`
- Source type: `university_extension`

## Reliability

- Source tier: tier_1
- Source gate: trusted (source level E4; direct_quote; context partial)
- Confidence: medium. Reason: Extension fact sheet by UVI's lead researcher. It does not say at what TAN level this applies, or whether plant ammonium uptake is included. Cross-check: Consistent with UVI's statement that the raft gives adequate biofiltration at the design feed ratio; about 10x higher per m2 than trickling-filter and RBC biofilm rates, which are not directly comparable.
- Corroboration: single_source

## Related Notes

- [[Truths/System Design/System Design|System Design]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
