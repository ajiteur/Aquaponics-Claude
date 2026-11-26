---
fact_id: "VR3_0005"
domain: "biology"
type: "parameter"
confidence: "low"
status: "provisional"
source_id: "knaus_appelbaum_palm_2018_aacl"
source_tier: "tier_2"
source_gate: "conditional"
source_file: "data/knowledge/atomic_facts/validation_round3_facts.json"
tags:
  - truth
  - biology
  - candidate
---

# VR3_0005

> In a backyard tilapia unit with gravel ebb-and-flow beds in a northern German glasshouse in autumn, basil grown from three-week-old rockwool seedlings averaged 16.1 +/- 13.8 g fresh biomass after 70 days at [[Reference/Explainers/pH|pH]] 8.0; the authors attribute below-expectation plant growth mainly to the high alkaline pH.

**Candidate truth.** Not yet approved (`candidate_pending_user_review`).

## Context

- species: basil (Kiepenkerl seed, cultivar not named), mixed with mint and parsley at 18 plants/m2
- system: coupled, gravel ebb-and-flow beds
- location: Rostock, Germany, 8 Aug to 16 Oct 2014

## Source

- Source ID: `knaus_appelbaum_palm_2018_aacl`
- Section: `Table 2 and Discussion`
- Source type: `peer_reviewed_journal`

## Reliability

- Source tier: tier_2
- Source gate: conditional (Open-access peer-reviewed, low-impact journal.)
- Confidence: low. Reason: Large spread (SD 86 percent of the mean); the pH attribution is the authors' view, not a controlled test.
- Corroboration: single_source; `knaus_appelbaum_palm_2018_aacl`

## Related Notes

- [[Truths/Biology/Biology|Biology]]
- [[Truths/Truths|Truths]]
- [[Sources/Source Register|Source Register]]
