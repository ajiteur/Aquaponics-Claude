---
fact_id: "NITR_0015"
domain: "water_chemistry"
type: "parameter"
confidence: "medium"
status: "accepted"
source_id: "greiner_timmons_1998"
source_tier: "tier_2"
source_gate: "trusted"
source_file: "data/knowledge/atomic_facts/nitrogen_cycle_facts.json"
tags:
  - truth
  - water_chemistry
  - accepted
---

# NITR_0015

> Trickling-filter media of 164 m2/m3 removed 0.94 to 3.92 g [[Reference/Explainers/TAN|TAN]] per m2 per day at 0.81 to 4.63 mg TAN/L, with removal linear in TAN up to about 2.5 mg/L.

## Context

- system: RAS trickling filter (Norpak media) vs microbead filter
- species: tilapia RAS

## Source

- Source ID: `greiner_timmons_1998`
- Section: `Results`
- Source type: `peer_reviewed_journal`

## Reliability

- Source tier: tier_2
- Source gate: trusted (Peer-reviewed (Aquacultural Engineering 18:189-200).)
- Confidence: medium. Reason: Measured rates; the paper's table and text swap the two filter volumes; heavily loaded RAS, not aquaponics.
- Corroboration: corroborated; `greiner_timmons_1998`, `srac_453_1999`

## Related Notes

- [[Truths/Water Chemistry/Water Chemistry|Water Chemistry]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
