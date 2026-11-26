---
fact_id: "HEAT_0003"
domain: "environment"
type: "parameter"
confidence: "low"
status: "provisional"
source_id: "wikipedia_bengaluru_weather_box_mirror"
source_tier: "tier_3"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/heating_climate_facts.json"
tags:
  - truth
  - environment
  - candidate
---

# HEAT_0003

> Bengaluru record lows since 1901 fall below 10 C in January (7.8), February (9.4), November (9.6) and December (8.9).

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- location: Bengaluru, Karnataka, India
- period: 1901-present

## Source

- Source ID: `wikipedia_bengaluru_weather_box_mirror`
- Section: `weather box`
- Source type: `encyclopedia_mirror`

## Reliability

- Source tier: tier_3
- Source gate: conditional (Tertiary mirror citing IMD; not checked against an IMD extremes document.)
- Confidence: low. Reason: Single tertiary source.
- Corroboration: single_source; `wikipedia_bengaluru_weather_box_mirror`

## Related Notes

- [[Truths/Environment/Environment|Environment]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
