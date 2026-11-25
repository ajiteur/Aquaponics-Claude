---
fact_id: "CD_0008"
domain: "operations"
type: "parameter"
confidence: "low"
status: "provisional"
source_id: "wecr_2017_070_greenhouse_quickscan"
source_tier: "tier_2"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/component_design_facts.json"
tags:
  - truth
  - operations
  - candidate
---

# CD_0008

> An unlit Dutch sweet-pepper greenhouse used about 21 to 30 m3 of natural gas per m2 per year for heating (2015 Energiemonitor data and 2018 modern-greenhouse estimates).

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- crop: sweet pepper, unlit
- location: Netherlands

## Source

- Source ID: `wecr_2017_070_greenhouse_quickscan`
- Section: `verwarming`
- Source type: `research_note`

## Reliability

- Source tier: tier_2
- Source gate: conditional (modelled_values_for_another_crop)
- Confidence: low. Reason: Not basil: used in the configurator only as a transferred heating range.
- Corroboration: single_source

## Related Notes

- [[Truths/Operations/Operations|Operations]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
