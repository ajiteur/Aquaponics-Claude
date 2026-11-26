---
fact_id: "VR3_0007"
domain: "biology"
type: "parameter"
confidence: "low"
status: "provisional"
source_id: "khater_2023_sci_rep"
source_tier: "tier_2"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/validation_round3_facts.json"
tags:
  - truth
  - biology
  - candidate
---

# VR3_0007

> Khater et al. 2023 report tilapia FCR of 0.92 to 1.20 (40 g fingerlings, 60 days, 23.4 to 23.6 C) but do not print feed intake, and their FCR equation divides feed intake by per-fish gain times the final fish count, so the values cannot be recomputed.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- species: Nile tilapia
- system: coupled troughs with foam rafts, hydraulic loading 1.2 to 3.0 m/day
- location: Benha, Egypt, January to March 2023

## Source

- Source ID: `khater_2023_sci_rep`
- Section: `Methods Eq. 5 and fish results table`
- Source type: `peer_reviewed_journal`

## Reliability

- Source tier: tier_2
- Source gate: conditional (Peer-reviewed, but the fish results table was read through a fetch summary and feed intake is missing.)
- Confidence: low. Reason: Below the Tier 1 range (1.4 to 1.8) and UVI's 1.71 to 1.92 with no stated reason.
- Corroboration: conflicting; `khater_2023_sci_rep`, `srac_282`, `fao_tp_589`, `rakocy_2004_tilapia_basil`

## Related Notes

- [[Truths/Biology/Biology|Biology]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
