---
fact_id: "FISH_0003"
domain: "biology"
type: "threshold"
confidence: "high"
status: "provisional"
source_id: "srac_283"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/fish_growth_facts.json"
tags:
  - truth
  - biology
  - candidate
---

# FISH_0003

> Tilapia stop feeding below about 17 C (63 F).

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- species: tilapia

## Source

- Source ID: `srac_283`
- Section: `text`
- Source type: `extension_fact_sheet`

## Reliability

- Source tier: tier_1
- Source gate: trusted (SRAC 283 and FAO TP 589.)
- Confidence: high. Reason: Two Tier 1 sources agree (17.2 and 17 C); a pond bioenergetic model uses 18.7 C.
- Corroboration: corroborated; `srac_283`, `fao_tp_589`, `fao_w5268e`

## Related Notes

- [[Truths/Biology/Biology|Biology]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
