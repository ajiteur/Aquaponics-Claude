---
fact_id: "VR3_0003"
domain: "biology"
type: "parameter"
confidence: "medium"
status: "provisional"
source_id: "modarelli_2023_plants"
source_tier: "tier_2"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/validation_round3_facts.json"
tags:
  - truth
  - biology
  - candidate
---

# VR3_0003

> In an aquaponic floating raft at 20 plants/m2, two-week-old basil seedlings gave 32.4 g fresh weight per plant at the first cut (35 days after planting) and 44.4 g at the second cut (79 days); the cut had no significant effect on fresh yield.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- species: basil cv. Sanremo
- system: coupled aquaponic floating raft, cold greenhouse under 75 percent shade net
- location: Portici (Naples), Italy, June to September 2021

## Source

- Source ID: `modarelli_2023_plants`
- Section: `Table 1`
- Source type: `peer_reviewed_journal`

## Reliability

- Source tier: tier_2
- Source gate: trusted (Peer-reviewed (MDPI Plants).)
- Confidence: medium. Reason: Direct table values, n = 3; per day the first cut is close to the second (0.92 vs 1.01 g/d, our arithmetic), but light fell between the cuts.
- Corroboration: corroborated; `modarelli_2023_plants`, `corrado_2020_agronomy`, `rakocy_2004_tilapia_basil`

## Related Notes

- [[Truths/Biology/Biology|Biology]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
