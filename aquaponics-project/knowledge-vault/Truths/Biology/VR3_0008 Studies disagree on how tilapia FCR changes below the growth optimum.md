---
fact_id: "VR3_0008"
domain: "biology"
type: "parameter"
confidence: "low"
status: "provisional"
source_id: "abd_el_hack_2022_ijb"
source_tier: "tier_2"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/validation_round3_facts.json"
tags:
  - truth
  - biology
  - candidate
---

# VR3_0008

> Studies disagree on how tilapia FCR changes below the growth optimum: Azaza et al. 2008 found FCR best at 26 and 30 C (vs 22 and 34 C), Mirea 2013 found FCR rising with temperature from 20 to 30 C, and Workagegn 2014 found feed use worst at 24 C (of 24 to 34 C).

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- species: Nile tilapia juveniles
- system: aquaria and tanks
- location: various

## Source

- Source ID: `abd_el_hack_2022_ijb`
- Section: `review text; Workagegn via The Fish Site`
- Source type: `peer_reviewed_journal`

## Reliability

- Source tier: tier_2
- Source gate: conditional (Read through a peer-reviewed review and a Tier 3 trade summary; primary tables not read.)
- Confidence: low. Reason: No numbers read from the primary papers; the directions conflict.
- Corroboration: conflicting; `abd_el_hack_2022_ijb`, `azaza_2008`, `mirea_2013`, `workagegn_2014`

## Related Notes

- [[Truths/Biology/Biology|Biology]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
