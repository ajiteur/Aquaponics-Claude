---
fact_id: "FISH_0002"
domain: "biology"
type: "parameter"
confidence: "high"
status: "accepted"
source_id: "srac_282"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/fish_growth_facts.json"
tags:
  - truth
  - biology
  - accepted
---

# FISH_0002

> Suggested tank-culture feeding rates for tilapia fall from 15-20 percent of body weight a day for fry under 0.5 g to 3-5 percent at 18-75 g and 1.5-3 percent from 75 g to market size.

## Context

- species: tilapia
- system: tank culture

## Source

- Source ID: `srac_282`
- Section: `Table 1`
- Source type: `extension_fact_sheet`

## Reliability

- Source tier: tier_1
- Source gate: trusted (SRAC 282.)
- Confidence: high. Reason: NCRAC 114 (NRC 1993, 28 C) and FAO AFFRIS Table 26b agree above 100 g.
- Corroboration: corroborated; `srac_282`, `ncrac_114`, `fao_affris_table_26`

## Related Notes

- [[Truths/Biology/Biology|Biology]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
