---
fact_id: "PHB_0002"
domain: "operations"
type: "parameter"
confidence: "medium"
status: "accepted"
source_id: "rakocy_ista6_uvi_update"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/ph_buffer_facts.json"
tags:
  - truth
  - operations
  - accepted
---

# PHB_0002

> At the UVI aquaponic system (111.2 m3, 214 m2 of rafts, rainwater make-up about 2.61 m3/day), [[Reference/Explainers/pH|pH]] was held at 7.0 to 7.5 by adding 22.5 kg Ca(OH)2 in 23 doses and 21.5 kg KOH in 22 doses during the basil trials, projected to 40.65 and 38.85 kg a year.

## Context

- system: UVI commercial-scale coupled DWC raft, tilapia with basil
- location: St. Croix, US Virgin Islands, tropical

## Source

- Source ID: `rakocy_ista6_uvi_update`
- Section: `base addition, water quality section`
- Source type: `conference_proceedings_system_operator`

## Reliability

- Source tier: tier_1
- Source gate: trusted (Operator's own measured records in symposium proceedings.)
- Confidence: medium. Reason: Measured dose totals, but the annual figure is a projection and the trial length is not restated.
- Corroboration: corroborated; `rakocy_ista6_uvi_update`, `srac_454`

## Related Notes

- [[Truths/Operations/Operations|Operations]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
