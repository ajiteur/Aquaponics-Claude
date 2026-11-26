---
fact_id: "FISH_0006"
domain: "biology"
type: "parameter"
confidence: "high"
status: "provisional"
source_id: "uvi_ista6_rakocy_2004"
source_tier: "tier_2"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/fish_growth_facts.json"
tags:
  - truth
  - biology
  - candidate
---

# FISH_0006

> In the UVI aquaponic system, all-male Nile tilapia grew from 79 g to 814 g in 24 weeks (4.4 g/day, FCR 1.7, 98 percent survival) at 77 fish per m3, harvesting 61.5 kg/m3 per tank, about 4.16 t a year from four 7.8 m3 tanks.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- species: Nile tilapia, all-male
- system: UVI aquaponics, 24 to 29 C

## Source

- Source ID: `uvi_ista6_rakocy_2004`
- Section: `Table 1`
- Source type: `conference_proceedings`

## Reliability

- Source tier: tier_2
- Source gate: trusted (UVI developers' measured data.)
- Confidence: high. Reason: Mean of 20 harvests; reproduced in SRAC 454 Table 1. The 5 t/yr design target is a different figure.
- Corroboration: corroborated; `uvi_ista6_rakocy_2004`, `srac_454`

## Related Notes

- [[Truths/Biology/Biology|Biology]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
