---
fact_id: "NITR_0013"
domain: "system_design"
type: "parameter"
confidence: "medium"
status: "provisional"
source_id: "fao_589_somerville_2014"
source_tier: "tier_1"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/nitrogen_cycle_facts.json"
tags:
  - truth
  - system_design
  - candidate
---

# NITR_0013

> FAO small-scale aquaponics guidance sizes a media-bed biofilter at 1 L of volcanic gravel (about 300 m2/m3) per g of daily feed, or 0.5 L of bioballs (about 600 m2/m3), as a minimum; limestone gravel has about 150 to 200 m2/m3, and larger gravel gives less surface.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- system: small-scale media-bed and DWC/NFT units
- scale: 1 to 12 m2 grow area

## Source

- Source ID: `fao_589_somerville_2014`
- Section: `s.4.3 and s.8 component ratios`
- Source type: `fao_technical_paper`

## Reliability

- Source tier: tier_1
- Source gate: conditional (FAO Fisheries and Aquaculture Technical Paper 589, read via a third-party reproduction (FarmHub).)
- Confidence: medium. Reason: Stated design minimum, not a measured capacity; read through a reproduction.
- Corroboration: single_source; `fao_589_somerville_2014`

## Related Notes

- [[Truths/System Design/System Design|System Design]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
