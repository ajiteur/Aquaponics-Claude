---
fact_id: "PHB_0001"
domain: "water_chemistry"
type: "parameter"
confidence: "high"
status: "accepted"
source_id: "ebeling_timmons_bisogni_2006_aquaculture_257_346"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/ph_buffer_facts.json"
tags:
  - truth
  - water_chemistry
  - accepted
---

# PHB_0001

> Nitrifying 1 g of [[Reference/Explainers/TAN|TAN]]-N consumes about 7.05 g of alkalinity as CaCO3 when bacterial growth is included (7.14 g without it); the same reaction uses 4.18 g O2 and gives off 5.85 g CO2 per g N.

## Context

- system: freshwater RAS and biofilters
- scope: autotrophic nitrification stoichiometry (Eq. 14)

## Source

- Source ID: `ebeling_timmons_bisogni_2006_aquaculture_257_346`
- Section: `Eq. 14`
- Source type: `peer_reviewed_journal`

## Reliability

- Source tier: tier_1
- Source gate: trusted (Peer-reviewed RAS engineering paper, widely used.)
- Confidence: high. Reason: Standard stoichiometry; the no-growth value from the US EPA manual agrees within 1 percent.
- Corroboration: corroborated; `ebeling_timmons_bisogni_2006_aquaculture_257_346`, `us_epa_625_4_73_004a_via_cwea`

## Related Notes

- [[Truths/Water Chemistry/Water Chemistry|Water Chemistry]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
