---
fact_id: "PHB_0011"
domain: "environment"
type: "parameter"
confidence: "low"
status: "provisional"
source_id: "gulgundi_shetty_2018_applied_water_science"
source_tier: "tier_1"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/ph_buffer_facts.json"
tags:
  - truth
  - environment
  - candidate
---

# PHB_0011

> South Indian borewell water is often highly alkaline and hard: Bengaluru wells 88 to 530 mg/L alkalinity (2014, 67 wells), Chennai Anna Nagar 18 to 360 mg/L bicarbonate, and Prakasam district (Andhra Pradesh) 480 to 1,025 mg/L bicarbonate, so an Indian farm on borewell water may need acid rather than base.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- location: Karnataka, Tamil Nadu, Andhra Pradesh
- water: groundwater, borewells
- note: city piped supply (Cauvery, Krishna) is likely softer; no utility values found

## Source

- Source ID: `gulgundi_shetty_2018_applied_water_science`
- Section: `results tables`
- Source type: `peer_reviewed_journal`

## Reliability

- Source tier: tier_1
- Source gate: conditional (Peer-reviewed, but each city is one study and well water varies widely.)
- Confidence: low. Reason: Wide ranges, one study per place, and Bengaluru's basis (HCO3 or CaCO3) is unclear; test on site.
- Corroboration: single_source; `gulgundi_shetty_2018_applied_water_science`, `krishnakumar_2015_applied_water_science`, `subba_rao_2018_applied_water_science`

## Related Notes

- [[Truths/Environment/Environment|Environment]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
