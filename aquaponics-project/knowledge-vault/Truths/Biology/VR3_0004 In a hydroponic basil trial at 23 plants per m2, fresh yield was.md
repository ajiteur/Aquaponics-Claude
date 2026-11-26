---
fact_id: "VR3_0004"
domain: "biology"
type: "parameter"
confidence: "medium"
status: "accepted"
source_id: "corrado_2020_agronomy"
source_tier: "tier_2"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/validation_round3_facts.json"
tags:
  - truth
  - biology
  - accepted
---

# VR3_0004

> In a hydroponic basil trial at 23 plants/m2, fresh yield was higher at the first cut (47 days after transplant) than at the second (75 days); the abstract gives a yield reduction of about 20 percent.

## Context

- species: basil, Genovese type
- system: hydroponic, pots on benches in a glasshouse, mean air 26 C
- location: Bellizzi (Salerno), Italy, from April

## Source

- Source ID: `corrado_2020_agronomy`
- Section: `Results 3.1 and abstract`
- Source type: `peer_reviewed_journal`

## Reliability

- Source tier: tier_2
- Source gate: trusted (Peer-reviewed (MDPI Agronomy).)
- Confidence: medium. Reason: Per-cut values are only in a figure; the -20 percent is the abstract's figure. Direction agrees with VR3_0002 and VR3_0003.
- Corroboration: corroborated; `corrado_2020_agronomy`, `modarelli_2023_plants`, `rakocy_2004_tilapia_basil`

## Related Notes

- [[Truths/Biology/Biology|Biology]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
