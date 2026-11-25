---
fact_id: "CD_0007"
domain: "business"
type: "parameter"
confidence: "low"
status: "provisional"
source_id: "wecr_2017_070_greenhouse_quickscan"
source_tier: "tier_2"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/component_design_facts.json"
tags:
  - truth
  - business
  - candidate
---

# CD_0007

> Dutch Venlo glasshouse investment for structure, glass, screens and fans was about EUR 50 to 63 per m2 in 2017 builder quotes, with a 16-year structure life; heating installation not included.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- system: commercial Venlo glasshouse (hectare scale)
- location: Netherlands
- year basis: 2017 quotes (AAB Nederland)

## Source

- Source ID: `wecr_2017_070_greenhouse_quickscan`
- Section: `bijlage_1_3_tabel_3`
- Source type: `research_note`

## Reliability

- Source tier: tier_2
- Source gate: conditional (research_note_using_builder_quotes)
- Confidence: low. Reason: 2017 prices for large greenhouses; a small farm greenhouse costs more per m2. KWIN 2026 (paid) has current figures.
- Corroboration: single_source

## Related Notes

- [[Truths/Business/Business|Business]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
