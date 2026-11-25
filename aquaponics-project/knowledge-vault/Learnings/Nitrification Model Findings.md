# Nitrification Model Findings

What changed in the nitrification model on 2026-11-25, what it shows, and how much each value can be trusted. Simulation results here are **scenario estimates, not validated**. Values marked candidate wait for Ajit's review before they count as truths.

## Simulation findings (2026-11-25)

Run: `src/simulate_crop_cycle.py`, 28 days, on the two `basil_raft_crop_cycle` scenarios, with the raft (11.25 m²) as the only nitrifying surface.

- **Fish scaled to the UVI feed ratio: TAN settles near 2.1 to 2.3 mg/L and NH3 near 0.015 mg/L.** The old placeholder let TAN climb to about 14 mg/L and NH3 to about 1.1 mg/L. The raft runs at about 58 percent of its modelled capacity. Basil still reaches the 2.0 kg/m² anchor.
- **TAN of about 2 mg/L is above the NMSU guidance of TAN < 1 ppm**, but NH3 stays low because pH is 6.9. Guidance, not a toxicity rule.
- **Starter fixture (8 kg fish): TAN about 0.2 mg/L.** With the pH fix alone, basil fell to 0.77 kg/m² because the placeholder nitrate uptake scaled with the plant score. After replacing that placeholder with growth-based uptake, basil reaches 1.91 kg/m² and nitrate stays near 38 to 42 mg/L.
- **Nitrate builds up to about 161 mg/L in the UVI case** (UVI measured about 42), because the model has no nitrogen sinks besides plant shoots. *Fixed later the same day: water exchange and a calibrated residual loss now hold it near 42 (see the Simulation Findings Log).*
- **Basil pH score is now 1.0 across pH 6.9 to 7.6 in coupled loops** (was 0 everywhere in that range).

## Candidate values and their reliability

Source levels follow the Source Trust Policy (E5 official manual, E4 university/extension, E3 peer-reviewed, E2 textbook, E1 industry association). Confidence follows its rule: high needs E4+, direct, complete context and no contradiction.

| Value | Source | Level | Confidence | Why |
|---|---|---|---|---|
| Raft treats the waste of 180 g feed/m²/day | SRAC 454 (Rakocy, Masser, Losordo) | E4, Tier 1 | Medium | Direct number from UVI's lead researcher. Doesn't say at what TAN level, or whether plant ammonium uptake is included. |
| Nitrification rate is linear in TAN below ~2 mg/L, flat above 3 to 4 mg/L | Losordo, DeLong, Guerdat 2015, Global Aquaculture Advocate | E1 host, from an E2 textbook chapter | Low | Industry magazine; generic RAS biofilters, not raft. |
| Nitrification optimal from pH 7.0; practically stops below 6.0 | SRAC 454; UVI page | E4, Tier 1 | Medium | Two university sources agree on the endpoints. Shape between them is assumed. |
| Biofilters optimal at 25 to 30 °C | SRAC 454 | E4, Tier 1 | Medium | Direct, but generic. |
| Rate falls ~4.3 % per °C below optimum (TAN-limited) | Zhu and Chen 2002, Aquacultural Engineering | E3 | Medium | Peer-reviewed, abstract only. Measured at 20 °C; linear use is assumed. |
| Nitrifiers inefficient below 2 mg/L DO | Biofilters corroboration report | E4 | Medium | Threshold sourced; shape assumed. |
| Basil shoot dry matter about 11 percent of fresh mass | Solis-Toapanta et al. 2020, HortScience | E3, Tier 2 | Medium | Our arithmetic on printed fresh and dry mass, warm greenhouse. |
| Basil tissue N 4 percent of dry mass (sufficiency range 4 to 6) | Solis-Toapanta et al. 2020 | E3, Tier 2 | Medium | Printed; measured values vary 2.2 to 6.2 percent with conditions. |
| Basil aquaponic pH scoring: preferred 5.8 to 7.6 | CEA Herbs factsheet, hydroponic study, Rakocy et al. 2004 | E3 to E4 | Medium at the edges, **low for 6.2 to 6.9** | The 6.2 to 6.9 band sits between two evidenced bands but was not observed. |

## Cross-check that disagrees

Per m² of biofilm, trickling filters and RBCs remove about 0.24 to 0.53 g TAN/m²/day (Godoy-Olmos et al. 2019; Sandu and Hallerman 2013). The raft figure works out to about 5.4 g TAN per m² of grow area per day, about ten times higher. They aren't directly comparable (the raft counts all tank surfaces and plant uptake per m² of grow area), but this is the biggest open uncertainty in the model.

## Gaps

- No half-saturation constant for raft biofilm.
- Organic carbon effect not modelled (C:N of 1:1 can cut nitrification by over 70 percent).
- Nitrite step not modelled; startup ramp still uses scenario `biofilter_maturity`.
- No evidence for basil above pH 7.6, so its score drops to 0 there.

## Decisions waiting on Ajit

- Accept or reject the candidate nitrification model, the basil aquaponic pH ranges and the basil N uptake values (truths NITR_0001 to NITR_0008).

## Related Notes

- [[Learnings/Simulation Learnings|Simulation Learnings]]
- [[Sources/Source Register|Source Register]]
