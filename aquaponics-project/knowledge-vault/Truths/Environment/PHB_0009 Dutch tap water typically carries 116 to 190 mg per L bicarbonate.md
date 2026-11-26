---
fact_id: "PHB_0009"
domain: "environment"
type: "parameter"
confidence: "high"
status: "provisional"
source_id: "waternet_leiduin_2022"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/ph_buffer_facts.json"
tags:
  - truth
  - environment
  - candidate
---

# PHB_0009

> Dutch tap water typically carries 116 to 190 mg/L bicarbonate (about 95 to 155 mg/L alkalinity as CaCO3; Waternet Leiduin 2022, Dunea Scheveningen 2025, Vitens 2025) at [[Reference/Explainers/pH|pH]] 7.8 to 8.7; the Drinking Water Decree requires at least 60 mg/L bicarbonate.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- location: Netherlands
- water: municipal tap water

## Source

- Source ID: `waternet_leiduin_2022`
- Section: `annual quality tables`
- Source type: `official_utility_report`

## Reliability

- Source tier: tier_1
- Source gate: trusted (Official water company quality reports.)
- Confidence: high. Reason: Three utilities agree; soft supplies near the legal minimum exist (ILT 2017).
- Corroboration: corroborated; `waternet_leiduin_2022`, `dunea_scheveningen_2025`, `vitens_hoenderloo_2025`, `ilt_drinkwater_2017`

## Related Notes

- [[Truths/Environment/Environment|Environment]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
