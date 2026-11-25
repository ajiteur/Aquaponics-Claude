---
fact_id: "NITR_0003"
domain: "water_chemistry"
type: "parameter"
confidence: "low"
status: "provisional"
source_id: "losordo_delong_guerdat_2015_gaa_advocate"
source_tier: "tier_2"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/nitrogen_cycle_facts.json"
tags:
  - truth
  - water_chemistry
  - candidate
---

# NITR_0003

> Biofilter [[Reference/Explainers/Nitrification|nitrification]] rate rises roughly in step with [[Reference/Explainers/TAN|TAN]] below about 2 mg/L and stops rising above about 3 to 4 mg/L.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- system: RAS fixed-film biofilters (generic, not raft-specific)

## Source

- Source ID: `losordo_delong_guerdat_2015_gaa_advocate`
- Section: `tan_concentration`
- Source type: `industry_magazine_summary_of_textbook_chapter`

## Reliability

- Source tier: tier_2
- Source gate: conditional (source level E1 host summarising E2 textbook; direct_quote; context partial)
- Confidence: low. Reason: Industry magazine article by recognised RAS engineers, drawn from a Woodhead textbook chapter. Generic RAS, not aquaponics.
- Corroboration: single_source

## Related Notes

- [[Truths/Water Chemistry/Water Chemistry|Water Chemistry]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
