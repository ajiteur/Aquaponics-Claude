---
fact_id: "NITR_0016"
domain: "water_chemistry"
type: "parameter"
confidence: "medium"
status: "provisional"
source_id: "anderson_goldstein_timmons_2019"
source_tier: "tier_2"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/nitrogen_cycle_facts.json"
tags:
  - truth
  - water_chemistry
  - candidate
---

# NITR_0016

> In a lettuce raft study, surface [[Reference/Explainers/Nitrification|nitrification]] was 0.83 g [[Reference/Explainers/TAN|TAN]]/m2/day on inert surfaces and about 0.20 g/m2/day on root surfaces; direct plant uptake was under 2 percent of the TAN removed.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- system: lettuce raft, aquaponic application
- species: lettuce

## Source

- Source ID: `anderson_goldstein_timmons_2019`
- Section: `abstract`
- Source type: `peer_reviewed_journal`

## Reliability

- Source tier: tier_2
- Source gate: trusted (Peer-reviewed (Aquacultural Engineering 86:101997).)
- Confidence: medium. Reason: Abstract only; the root value is printed without the 'g' unit; TAN level of the measurement not read.
- Corroboration: single_source; `anderson_goldstein_timmons_2019`

## Related Notes

- [[Truths/Water Chemistry/Water Chemistry|Water Chemistry]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
