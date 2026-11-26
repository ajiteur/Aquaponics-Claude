---
fact_id: "FISH_0005"
domain: "biology"
type: "parameter"
confidence: "medium"
status: "provisional"
source_id: "srac_282"
source_tier: "tier_1"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/fish_growth_facts.json"
tags:
  - truth
  - biology
  - candidate
---

# FISH_0005

> Optimum tilapia growth temperature is reported as 27 to 29 C (SRAC 282), 27 to 30 C (FAO TP 589) and 29 to 31 C (SRAC 283); acceptable growth 25 to 32 C.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- species: tilapia

## Source

- Source ID: `srac_282`
- Section: `text`
- Source type: `extension_fact_sheet`

## Reliability

- Source tier: tier_1
- Source gate: trusted (SRAC and FAO.)
- Confidence: medium. Reason: Sources overlap at 27 to 30 but differ at the top; kept as a context split.
- Corroboration: conflicting; `srac_282`, `fao_tp_589`, `srac_283`

## Related Notes

- [[Truths/Biology/Biology|Biology]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
