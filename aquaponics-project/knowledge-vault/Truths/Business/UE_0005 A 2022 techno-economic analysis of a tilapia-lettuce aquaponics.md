---
fact_id: "UE_0005"
domain: "business"
type: "finding"
confidence: "medium"
status: "provisional"
source_id: "zappernick_2022_techno_economic"
source_file: "data/knowledge/atomic_facts/unit_economics_facts.json"
tags:
  - truth
  - business
  - candidate
---

# UE_0005

> A 2022 techno-economic analysis of a tilapia-lettuce aquaponics system found labour and greenhouse costs to be the prime factors controlling profitability; it assumed lettuce harvest at about 30 plants per hour.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- system: modelled RAS aquaponics, about 62 m2 grow bed in a greenhouse
- crop: lettuce plus tilapia
- location: US Midwest
- year basis: 2019, USD

## Reliability

- Source tier: T2_peer_reviewed
- Confidence: medium
- Confidence reason: Peer-reviewed; the abstract and methods were read verbatim, later results only through a summary.
- Cross check: Labour as a top driver agrees with Tokunaga et al.; the harvest rate is much slower than the Hawaii task table implies.

## Source

- Source ID: `zappernick_2022_techno_economic`
- Section: `abstract_and_sec_2_2_2`
- Source type: `peer_reviewed_journal`

## Related Notes

- [[Truths/Business/Business|Business]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
