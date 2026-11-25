# Approval Batch 001

Everything waiting on Ajit, in one list, with the Gatekeeper's recommendation for each. Reply "approve batch 001 as recommended", or list the item numbers you want changed. Approvals are then recorded next to each value (who, date, scope).

Prepared: 2026-11-25, against `main` at `7f57d3f`, PR #10 at `4cf2758` and PR #11 at `a539274`.

Rule used for the recommendations (AGENTS.md 6A): approve items with medium or high confidence that Tier 1 or Tier 2 sources corroborate. Single-source, Tier 3 and low-confidence items stay candidates. The simulation uses candidates anyway, so keeping one as a candidate doesn't stop any work.

## A. Pull requests to merge

| # | Item | Recommendation |
|---|---|---|
| A1 | PR #11: basil nitrate uptake based on growth, plus NITR truths | **Merge first.** Tests, the full integrity check, and the canon and vault syncs pass. Known gap: with no nitrogen sinks besides basil shoots, nitrate climbs to about 161 mg/L at the UVI feed ratio, where UVI measured about 42. |
| A2 | PR #10: unit design comparison (Netherlands and India) | **Merge second, after one rerun.** Checks pass, but it conflicts with #11 in the revenue range, the vault logs and the truths hub. After #11 merges, it needs main merged in, the comparison rerun (the simulated high yield moves from 25.87 to about 26.0 kg/m²/yr) and the truths re-exported. |
| A3 | This note (PR #12) | Merge. Vault only. |

## B. Scenario inputs (scenario estimates only, never canon)

| # | Item | Recommendation |
|---|---|---|
| B1 | Netherlands basil wholesale price €7 / €8 / €9 per kg (CBI 2024, citing March 2020 importer examples) | **Approve for scenario use.** Sourced, but old, with tax treatment not normalized. |
| B2 | Netherlands basil saleability 85 / 90 / 95% | **Approve for scenario use.** Research-pack operator assumption, not measured. |
| B3 | India basil price ₹65 to ₹180 per kg (about ₹110 typical) as the base case | **Approve.** Ten Bengaluru IndiaMART listings ask ₹65 to ₹180, and Ajit confirmed on 2026-11-25 that basil does cost that much in Bangalore. That makes it a user-supplied input from local knowledge. It's still an asking-price level, not first-wholesale. The old ₹600 to ₹1,000 band (one 2025 Andhra Pradesh study) stays only as a sensitivity case. |
| B4 | India basil saleability 80 to 92% | Approve for scenario use. Operator assumption, low confidence. |
| B5 | Karnataka wage (₹533/day minimum + 15% burden, 8 h/day) and electricity (₹3.45 to ₹7.10/kWh) | Approve for scenario use. Low confidence: the wage period has expired, and the tariff category for aquaponics is unknown. |

## C. Candidate model values in canon

| # | Item | Recommendation |
|---|---|---|
| C1 | Basil pH scoring for coupled aquaponic loops: preferred 5.8 to 7.6 (PR #6) | **Approve the evidenced edges, keep 6.2 to 6.9 as an assumption.** UVI grew basil well at pH 7.4. The middle band wasn't observed. |
| C2 | Biofilm nitrification capacity, 180 g feed per m² per day (PR #6) | **Keep as candidate.** Single source, and about ten times typical biofilter rates. It's the model's largest open question. |
| C3 | Basil shoot N uptake, 11.2% dry matter × 4% N (PR #11) | **Keep as candidate.** Single study, and the nitrate balance is still missing its other sinks. |

## D. Candidate truths

| # | Truths | Recommendation |
|---|---|---|
| D1 | NITR_0002, NITR_0004, NITR_0006 (medium, corroborated) | **Approve.** |
| D2 | NITR_0001, NITR_0005, NITR_0007, NITR_0008 (medium, single source) | Keep as candidates until a second source agrees. |
| D3 | NITR_0003 (low, single Tier 2 source) | Keep as candidate. |
| D4 | UE_0002, UE_0005, UE_0007, UE_0009, UE_0010 (medium, corroborated) | **Approve.** |
| D5 | UE_0001, UE_0003, UE_0011 (medium, single source) | Keep as candidates. |
| D6 | UE_0004 (low, corroborated); UE_0006, UE_0008 (low, single source) | Keep as candidates. |
| D7 | 13 older candidates: PROV_CORE_0001 to 0005, PROV_GUIDE_0001 to 0002, PROV_PARAM_0001 to 0005, PROV_WARN_0001 | Keep as candidates. They have no reliability record yet, and several are conditional sources. They need the backfill pass first. |
| — | CROP_0001 to CROP_0007 | Already accepted on 2026-11-25. Nothing to do. |

## After approval

1. The thread that owns each file records the approvals: basil price and saleability inputs, India inputs, basil pH, and the accepted truths.
2. The Gatekeeper rechecks `main`, and Ajit tags `save-point-001` from his PC (this session can't push tags).

## Related Notes

- [[Project/Save Points|Save Points]]
- [[Project/Feasibility Register|Feasibility Register]]
- [[Project/Decisions Log|Decisions Log]]
