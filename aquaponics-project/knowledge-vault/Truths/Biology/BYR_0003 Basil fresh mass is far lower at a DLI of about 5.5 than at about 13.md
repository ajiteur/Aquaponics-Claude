---
fact_id: "BYR_0003"
domain: "biology"
type: "parameter"
confidence: "low"
status: "provisional"
source_id: "walters_tarr_lopez_2023"
source_tier: "tier_2"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/basil_yield_response_facts.json"
tags:
  - truth
  - biology
  - candidate
---

# BYR_0003

> Basil fresh mass is far lower at a DLI of about 5.5 than at about 13 mol/m2/d (fitted model about 6 g vs 31 g per plant at 23 C), and higher temperature helps more at higher light.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- species: basil 'Nufar'
- system: greenhouse flood tables, shade cloth

## Source

- Source ID: `walters_tarr_lopez_2023`
- Section: `Table 2 model`
- Source type: `peer_reviewed_journal`

## Reliability

- Source tier: tier_2
- Source gate: trusted (Peer-reviewed (PLoS ONE).)
- Confidence: low. Reason: Values are our evaluation of a fitted regression (R2 0.63), not measured means.
- Corroboration: single_source; `walters_tarr_lopez_2023`

## Related Notes

- [[Truths/Biology/Biology|Biology]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
