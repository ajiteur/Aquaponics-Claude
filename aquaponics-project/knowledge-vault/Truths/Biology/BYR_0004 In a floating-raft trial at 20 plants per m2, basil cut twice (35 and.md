---
fact_id: "BYR_0004"
domain: "biology"
type: "parameter"
confidence: "low"
status: "provisional"
source_id: "modarelli_2023_plants"
source_tier: "tier_2"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/basil_yield_response_facts.json"
tags:
  - truth
  - biology
  - candidate
---

# BYR_0004

> In a floating-raft trial at 20 plants/m2, basil cut twice (35 and 79 days after planting) gave about 32 to 44 g fresh mass per plant per cut in aquaponics and about 38 g in hydroponics, i.e. roughly 0.65 to 0.89 kg/m2 per cut (our arithmetic).

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- species: basil (Genovese)
- system: floating raft, aquaponic and hydroponic, under 75 percent shade net
- location: Portici (Naples), Italy, 24 Jun to 10 Sep 2021

## Source

- Source ID: `modarelli_2023_plants`
- Section: `Table 1`
- Source type: `peer_reviewed_journal`

## Reliability

- Source tier: tier_2
- Source gate: trusted (Peer-reviewed (Plants 12:1355).)
- Confidence: low. Reason: Per-plant values read from Table 1; the 20 plants/m2 density came from a page summary, not verbatim; table means and abstract disagree slightly (41.7 vs 38.4 g); heavy shade, so light-limited.
- Corroboration: single_source; `modarelli_2023_plants`

## Related Notes

- [[Truths/Biology/Biology|Biology]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
