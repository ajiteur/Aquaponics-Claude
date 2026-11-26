---
fact_id: "NITR_0014"
domain: "system_design"
type: "parameter"
confidence: "medium"
status: "provisional"
source_id: "srac_453_1999"
source_tier: "tier_1"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/nitrogen_cycle_facts.json"
tags:
  - truth
  - system_design
  - candidate
---

# NITR_0014

> SRAC 453 (1999) gives trickling filters a design loading of 3.6 kg feed per m3 of media per day for media generally below 330 m2/m3, with [[Reference/Explainers/Nitrification|nitrification]] of about 90 g [[Reference/Explainers/TAN|TAN]]/m3/day.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- system: RAS trickling filter
- note: used as the analogue for intermittently wetted gravel beds

## Source

- Source ID: `srac_453_1999`
- Section: `Biofiltration table`
- Source type: `extension_fact_sheet`

## Reliability

- Source tier: tier_1
- Source gate: conditional (University extension fact sheet; the TAN rate rests on unpublished data (Losordo).)
- Confidence: medium. Reason: Design criterion, not a measurement; one edition; the 2013 edition does not restate it.
- Corroboration: single_source; `srac_453_1999`

## Related Notes

- [[Truths/System Design/System Design|System Design]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
