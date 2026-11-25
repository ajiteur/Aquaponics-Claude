---
fact_id: "UE_0005"
domain: "business"
type: "finding"
confidence: "medium"
status: "accepted"
source_id: "zappernick_2022_techno_economic"
source_tier: "tier_2"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/unit_economics_facts.json"
tags:
  - truth
  - business
  - accepted
---

# UE_0005

> A 2022 techno-economic analysis of a tilapia-lettuce aquaponics system found labour and greenhouse costs to be the prime factors controlling profitability; it assumed lettuce harvest at about 30 plants per hour.

## Context

- system: modelled RAS aquaponics, about 62 m2 grow bed in a greenhouse
- crop: lettuce plus tilapia
- location: US Midwest
- year basis: 2019, USD

## Source

- Source ID: `zappernick_2022_techno_economic`
- Section: `abstract_and_sec_2_2_2`
- Source type: `peer_reviewed_journal`

## Reliability

- Source tier: tier_2
- Source gate: trusted (peer_reviewed_journal)
- Confidence: medium. Reason: Peer-reviewed; the abstract and methods were read verbatim, later results only through a summary.
- Corroboration: corroborated; `tokunaga_2015_hawaii_aquaponics_economics`

## Related Notes

- [[Truths/Business/Business|Business]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
