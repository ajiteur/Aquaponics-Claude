# Model pH as alkalinity over CO2

In a freshwater tilapia aquaponics system, pH can be modelled as the result of two quantities: carbonate alkalinity, which changes slowly, and dissolved CO2, which changes quickly. At 22–30 °C and pH 6–8.3, the two are linked by **pH ≈ pK1(T) + log10([HCO3-]/[CO2*])**, with **pK1 ≈ 6.35 at 25 °C** ([aqion][aqion]). The well-sourced terms are:

- **Nitrification consumes 7.05 g CaCO3 per g TAN-N.** This figure includes biomass synthesis; 7.14 is the no-growth value ([Ebeling et al. 2006][eb]; [CWEA][cwea]).
- **Heterotrophic assimilation consumes 3.57 g/g N.** ([Ebeling et al. 2006][eb])
- **Fish produce about 1 mol CO2 per mol O2**, which is roughly **0.34–0.69 kg CO2 per kg feed**. ([Watten et al. course notes][co2ctl])
- **CO2 strips at about 0.67–0.86 times the O2 transfer coefficient.** ([Aitchison et al. 2007][aitch])

Plant nitrate uptake raises alkalinity in direction, and that direction is well supported ([Dickson & Fisher 2019][dickson]). Its size per mole of N in aquaponics has never been measured. Base dosing in practice is much smaller than simple stoichiometry predicts:

- **UVI's commercial system used about 79.5 kg/yr of Ca(OH)2 + KOH** in a 111 m3 system ([Rakocy et al., ISTA6][ista6]).
- That works out to about 13–14 g CaCO3-eq per kg feed. This is my own arithmetic from the paper's figures.
- Simple stoichiometry predicts about 0.21 kg/kg feed, roughly **15 times more**.

My reconciliation is that the gap is mostly bookkeeping, not missing chemistry. I made three computed cross-checks:

- If fish excrete NH3 that protonates in the water, the excretion step adds back half of what nitrification later removes.
- Plant NO3- uptake and denitrification can return most of the rest.
- UVI's rainwater make-up alone removes roughly as much alkalinity as the base it records.

The guidance on target pH splits by context:

- **About 7.0 (tolerable 6.4–7.4)** is the extension consensus ([NMSU CR-680][nmsu]).
- **pH 8.0** gave the fastest TAN removal ([Tyson et al. 2008][tyson08]).
- **pH 6.0–6.3** was preferred for N-use efficiency and nutrient uptake ([Zou et al. 2016][zou]; [Savidov 2005][savidov]).

Source water also splits:

- **Dutch tap water supplies about 95–155 mg/L as CaCO3** ([Waternet][waternet22]; [Dunea][dunea]; [Vitens][vitens]).
- **South Indian hard-rock borewells often supply 150–400+ mg/L** ([Subba Rao 2018][subba]; [Gulgundi & Shetty 2018][gulgundi]).

The model therefore has to handle both a base-demand regime (the Netherlands) and an acid-demand regime (India). In this report, every dosing or per-kg-feed figure is a **scenario estimate, not validated**. Nothing here is a fish-safety, aeration-adequacy or cost claim.

**Value labels used in the tables:**

- **Read**: taken from a fetched source page.
- **Computed**: my arithmetic from sourced inputs.
- **Recalled**: from memory, not verified against a fetched page.
- **Inference**: reasoning without a direct source.

Tiers are suggested per the project's source-trust convention: tier_1 = peer-reviewed or official, tier_2 = extension or reputable grey literature, tier_3 = commercial or anecdotal.

## Carbonate chemistry: three constants and one equation set the pH

The 25 °C constants come from Stumm & Morgan and WATEQ4F and agree to within ±0.005 log units ([aqion][aqion]). Henry's-law solubility of CO2 is consistent across six independent compilations ([Sander 2023 / henrys-law.org][henry]). Air-equilibrium CO2 at 420 ppm is therefore only about **0.6 mg/L**.

Any measured CO2 above that level is CO2 that the system is producing and failing to strip, and each tenfold rise in CO2 costs a full pH unit at constant alkalinity. The model needs the temperature functions of Plummer & Busenberg (1982), the source used by PHREEQC and WATEQ4F ([USGS record][pb82]). The full text was not fetched. The coefficients below were **recalled**; they reproduce the WATEQ4F 25 °C values to three decimals, but they must be checked against `phreeqc.dat` or the paper before they become canon.

**Henderson–Hasselbalch check against the course data.** I used concentration-based pK1 at 100 mg/L alkalinity. It gave pH 6.69 at 40 mg/L CO2, where the Vinci/Timmons/Summerfelt/Watten course table gives 6.8, and pH 7.16 at 13.6 mg/L, where the table gives 7.2 ([Watten et al. course notes][co2ctl]). So the uncorrected form reads about 0.05–0.1 units low, and an activity correction (Davies) is warranted.

The approximation breaks down below about 20 mg/L alkalinity, below pH 6, and above pH 8.3, where CO3^2- and OH- matter. That last regime matters for Indian borewell water at air equilibrium.

| Parameter | Value | Citation | Tier | Confidence (reason) | Corroboration | Origin |
|---|---|---|---|---|---|---|
| pK1 (25 °C) | 6.35 (S&M); 6.3447 (LLNL) | [aqion][aqion] | tier_2 compiling tier_1 | high (standard constants, agree to ±0.005) | corroborated | read |
| pK2 (25 °C) | 10.33 (S&M); 10.329 (WATEQ4F) | [aqion][aqion] | tier_2 compiling tier_1 | high | corroborated | read |
| log KH (25 °C, mol L⁻¹ atm⁻¹) | −1.47 / −1.468 | [aqion][aqion] | tier_2 compiling tier_1 | high | corroborated | read |
| KH(cp) 298 K; d ln H/d(1/T) | 0.033–0.034 mol L⁻¹ atm⁻¹; 2300–2400 K | [henrys-law.org (Sander 2023)][henry] | tier_1 | high (six sources agree) | corroborated | read |
| T-functions for K1, K2, KH (Plummer & Busenberg 1982) | log K1 = −356.3094 − 0.06091964T + 21834.37/T + 126.8339 log T − 1684915/T²; log K2 = −107.8871 − 0.03252849T + 5151.79/T + 38.92561 log T − 563713.9/T²; log KH = 108.3865 + 0.01985076T − 6919.53/T − 40.45154 log T + 669365/T² | [USGS record][pb82] (full text not read) | tier_1 (if verified) | medium (reproduces the 25 °C values, but not read) | single_source | **recalled** |
| pK1 at 22/25/28/30 °C | 6.369 / 6.352 / 6.337 / 6.328 | from the recalled equations | n/a | medium | n/a | **computed** |
| pK2 at 22/25/28/30 °C | 10.356 / 10.329 / 10.304 / 10.288 | from the recalled equations | n/a | medium | n/a | **computed** |
| Air-equilibrium CO2* at 420 ppm, 22/25/28/30 °C | 0.68 / 0.63 / 0.58 / 0.55 mg/L | from the KH equation; 25 °C cross-checked with the Sander KH | n/a | medium-high (two routes agree) | corroborated (internal) | **computed** |
| Course worked examples | 100 mg/L alkalinity: ~70 mg/L CO2 at pH 6.5, ~20 at 7.0, ~3 at 8.0; tank 40 mg/L CO2 / pH 6.8 | [Watten et al. course notes][co2ctl] | tier_2 | high (textbook authors' course material) | corroborated by H-H to within 0.1 pH | read |
| Ionic-strength shift in apparent pK1 at EC 0.5–1.5 mS/cm | −0.05 to −0.1 | none | n/a | low | none | **inference** |

**How strongly CO2 drives pH.** The table below shows the size of the effect at 25 °C. It is **computed** with uncorrected Henderson–Hasselbalch, so its values will read about 0.05–0.1 units low.

| Alkalinity (mg/L CaCO3) | CO2 0.63 (air eq.) | 5 mg/L | 10 mg/L | 20 mg/L | 40 mg/L |
|---|---|---|---|---|---|
| 40 (Cornell tubs) | 8.10 | 7.20 | 6.90 | 6.60 | 6.29 |
| 100 (extension target) | 8.49 | 7.60 | 7.29 | 6.99 | 6.69 |
| 150 (Dutch tap, upper) | 8.67* | 7.77 | 7.47 | 7.17 | 6.87 |
| 300 (South Indian borewell) | 8.97* | 8.07 | 7.77 | 7.47 | 7.17 |

*Above pH 8.3 the approximation overstates pH. Use the full charge balance there.

The table shows the main design point. **A well-degassed raft system with Dutch tap water at 100–150 mg/L alkalinity will settle near pH 7.6–8.5 unless nitrification consumes alkalinity.** A borewell-fed Indian system will sit above pH 7.5 even at 20 mg/L CO2. Degassing raises pH without changing alkalinity, because it removes C_T but not charge. This matches the course tables, where alkalinity holds at 100 mg/L while pH rises from 6.8 to 7.2 across a stripper ([Watten et al. course notes][co2ctl]).

## Nitrogen pathways set the alkalinity budget

The cleanest stoichiometry is Ebeling, Timmons & Bisogni (2006). For autotrophic nitrification, their Eq. 14 consumes **7.05 g CaCO3 alkalinity, 4.18 g O2** and produces **5.85 g CO2 per g NH4+-N** ([Ebeling et al. 2006][eb]). The EPA no-growth value of 7.14, reported second-hand by CWEA, is the same chemistry without cell synthesis ([CWEA][cwea]).

Heterotrophic assimilation (Eq. 16) consumes only 3.57 g/g N, but requires 15.17 g carbohydrate per g N. It produces **9.65 g CO2/g N**, so it shifts the pH burden from alkalinity to CO2. Gravel media beds host heterotrophs, so their share of TAN removal is an unknown parameter, not zero.

**Plant uptake.** Nitrate uptake produces "almost one OH- per NO3-", but part of it is neutralised inside the plant by organic-acid synthesis ([Raven & Smith 1976][raven]). Dickson & Fisher measured that every species they tested, including basil and lettuce, raised hydroponic pH on 100% nitrate. They give results only per gram of dry-weight gain, up to 1.31 mEq/g, not per mole of N ([Dickson & Fisher 2019][dickson]). That leaves the model parameter, eq of alkalinity returned per mol NO3--N taken up, at **0.5–1.0**, and that range is an inference.

**Denitrification** in anoxic gravel zones and solids tanks returns about 3.5 g per g of NO3--N reduced ([Univ. of Hawaii, Khanal lab][hawaii]). Zou et al. attribute 75–79% of N2O in media-based aquaponics to denitrification, which confirms the pathway is active ([Zou et al. 2016][zou]).

| Term | Value (g CaCO3 per g N unless stated) | Citation | Tier | Confidence (reason) | Corroboration | Origin |
|---|---|---|---|---|---|---|
| Autotrophic nitrification, with biomass | −7.05; also −4.18 g O2, +5.85 g CO2, +0.20 g VSS, 0.976 g NO3-N | [Ebeling et al. 2006, Eq. 14][eb] | tier_1 | high (explicit equation, standard RAS reference) | corroborated by the EPA value | read |
| Nitrification, no growth | −7.14 | [CWEA citing EPA-625/4-73-004a][cwea] | tier_2 | high for the value (EPA original not fetched) | corroborated (2 mol HCO3- per mol N) | read |
| Heterotrophic assimilation (carbohydrate) | −3.57; +9.65 g CO2; 15.17 g carbohydrate; 8.07 g VSS | [Ebeling et al. 2006, Eq. 16][eb] | tier_1 | high | single_source (widely re-cited) | read |
| Algal NH4+ uptake | −3.13; −18.07 g CO2 | [Ebeling et al. 2006, Eq. 3][eb] | tier_1 | high | single_source | read |
| Algal NO3- uptake | +4.02; −24.4 g CO2 | [Ebeling et al. 2006, Eq. 4][eb] | tier_1 | medium (the extracted equation's sign conflicts with the text; check the original) | single_source | read |
| Denitrification | +~3.5 per g NO3-N reduced | [Hawaii Khanal page][hawaii]; qualitative support from [Masabni & Sink][tamu] | tier_2 | medium (standard stoichiometry, web page) | corroborated (qualitative) | read |
| Plant NO3- uptake (basil, lettuce) | raises pH; up to 1.31 mEq per g DW gain (arugula); lettuce neutral at ~6.6% NH4+ in hydroponics | [Dickson & Fisher 2019][dickson] | tier_1 | high for direction, medium for magnitude | corroborated in direction ([Raven & Smith 1976][raven]) | read |
| Plant NO3- uptake, per mol N | +0.5 to +1.0 eq/mol (+1.79 to +3.57 g/g N), central 0.75 | upper bound from [Raven & Smith 1976][raven] (abstract) | n/a | low (the lower bound is an assumption) | none | **inference** |
| Fish NH3 excretion, protonated in water | +1 eq/mol N (+3.57 g/g N) while N stays as NH4+ | none | n/a | low-medium (charge balance; fish acid-base physiology not checked) | none | **inference** |
| Net, NH3 excreted through to NO3- | −3.57 g/g N | none | n/a | low-medium | none | **inference** |

**Accounting choice.** The model needs one recorded decision here. Ebeling's equations start from NH4+. If fish excrete N mainly as NH3 that then protonates, crediting −7.05 per g nitrated overstates alkalinity loss by a factor of two. Crediting the excretion step as well as using 7.05 is correct only if both steps are modelled explicitly.

This choice explains more of the UVI discrepancy than any missing process does. It is an inference, because no fetched source measures how fish N excretion changes alkalinity. It needs a contradiction-style review before canon promotion.

## CO2 production and stripping set the fast variable

Fish respire at a **respiratory quotient of about 1 mol CO2/mol O2 (1.375–1.38 g/g)** and use **0.25–0.5 kg O2 per kg feed**. The course example is 0.4 kg O2/kg feed, giving 0.55 kg CO2/kg feed ([Watten et al. course notes][co2ctl]). Nitrification adds 5.85 g CO2/g N. Part of that is HCO3- converted to CO2 rather than new carbon ([Ebeling et al. 2006][eb]).

**Removal.** Theory gives KLa(CO2)/KLa(O2) = 0.90. Measured transfer was 74–96% of theory at about 130 mg/L alkalinity, and fell sharply at about 1,000 mg/L ([Aitchison et al. 2007][aitch]). A 1.7 m cascade column removed 67–89% per pass ([Moran 2010][moran]). In warm alkaline water, HCO3- → CO2 conversion during passage makes the "non-reactive CO2" assumption fail ([Colt, Watten et al., part II][colt2]). That matters for Indian borewell water.

**Tilapia CO2 guidance depends on which endpoint is used, so it is a context split rather than a contradiction:**

- SRAC 452 gives a stress guideline of below 20 mg/L ([SRAC 452][srac452]).
- The NRAES course gives about 60 mg/L as an "operational limit" ([Watten et al. course notes][co2ctl]).
- Respirometry shows standard metabolic rate depressed by 11/22/29% after one hour at 10/30/60 mg/L CO2 at 26 °C ([Hamad et al. 2024][hamad]).

| Parameter | Value | Citation | Tier | Confidence (reason) | Corroboration | Origin |
|---|---|---|---|---|---|---|
| Fish RQ | 1 mol CO2 per mol O2 = 1.38 g/g | [Watten et al. course notes][co2ctl] | tier_2 | medium-high (standard assumption) | single_source here | read |
| Fish O2 demand | 0.25–0.5 kg O2/kg feed (example 0.4) | [Watten et al. course notes][co2ctl] | tier_2 | medium (generic RAS, not tilapia-specific) | single_source | read |
| Fish CO2 production | 0.34–0.69 kg/kg feed; 0.55 central | from the two rows above | n/a | medium | n/a | **computed** (0.55 is read) |
| Tilapia MO2, 26 °C, lab | 87.02 mg O2/kg/h | [Hamad et al. 2024][hamad] | tier_1 | high for lab respirometry (not production RAS) | single_source | read |
| Nitrification CO2 | 5.85 g/g N | [Ebeling et al. 2006][eb] | tier_1 | high | single_source | read |
| TAN yield | ~0.03 kg TAN/kg feed at 32–35% protein (0.092 × protein fraction) | Timmons & Ebeling rule, not fetched | n/a | low (unverified) | none | **recalled** |
| KLa(CO2)/KLa(O2), theory | 0.90 | [Aitchison et al. 2007][aitch] | tier_1 | medium-high (single study, temperature not reported) | single_source | read |
| Measured / theory | 96% (high exposure), 74% (moderate) at ~130 mg/L alkalinity; 0.84 / 0.51 at ~1,000 mg/L | [Aitchison et al. 2007][aitch] | tier_1 | medium-high | single_source | read |
| Effective φ for model | 0.67–0.86 | 0.90 × (0.74–0.96) | n/a | medium | n/a | **computed** |
| Cascade column removal | 67–89% per pass (15 °C, 10–60 mg/L in) | [Moran 2010][moran] | tier_1 | high (abstract) | corroborated in order by [course notes][co2ctl] (~66% at G:L 10) | read |
| CO2 guideline (stress) | < 20 mg/L | [SRAC 452][srac452]; [Masabni & Sink][tamu] | tier_2 | medium (generic) | corroborated | read |
| Operational limit, tilapia | ~60 mg/L | [Watten et al. course notes][co2ctl] | tier_2 | medium | conflicting endpoint → context_split | read |
| Metabolic depression, tilapia | −10% MO2 at 5 mg/L; SMR −11/22/29% at 10/30/60 mg/L (1 h) and −10/16/28% (24 h) | [Hamad et al. 2024][hamad] | tier_1 | high for physiology; no growth endpoint | single_source | read |

**Biggest CO2 gap.** No fetched source reports measured dissolved CO2 in any coupled aquaponics system. No source gives KLa for DWC air-stone channels or for flood-and-drain media beds. UVI runs a continuous 0.7 m3 degassing tank but publishes no CO2 values ([Rakocy et al., ISTA9][ista9]). The CO2 term will need calibration from site pH and alkalinity pairs, using the Loyless & Malone back-calculation ([Loyless & Malone 1997][loyless]).

## UVI's measured base is about one-fifteenth of stoichiometric theory

The University of the Virgin Islands (UVI) system is the only operating aquaponics system with published base masses:

- **22.5 kg Ca(OH)2 in 23 doses and 21.5 kg KOH in 22 doses**, projected to **40.65 and 38.85 kg/yr**.
- Dosed through a 189 L base tank, holding pH at 7.0–7.5 with daily checks.
- System: 111,196 L, 214 m2 of plants, rainwater make-up averaging **2.61 m3/day**.
- Measured alkalinity: **113.2 (65.6–206.7) mg/L** under batch basil and **88.6 (65.6–115.6)** under staggered basil.
- Source: [Rakocy et al., ISTA6][ista6].

SRAC 454 describes the same practice as "500 to 1,000 g" doses of each base, alternated several times a week ([SRAC 454][srac454]). The practice set elsewhere is:

- Savidov held pH 6.1–6.3 with Ca(OH)2/KHCO3 and used H3PO4 to lower it ([Savidov 2005][savidov]).
- Cornell held pH 7.0 with daily 1 M K2CO3 at only about 40 mg/L alkalinity ([Vandam et al. 2017][vandam]).
- SRAC 454 and FAO 589 both forbid NaHCO3 in aquaponics, keeping Na below 50 mg/L ([SRAC 454][srac454]; [FAO 589][fao]).
- SRAC 452's RAS rule of 0.17–0.20 kg NaHCO3 per kg feed therefore does not carry over to the plant loop as a chemical choice ([SRAC 452][srac452]).

| Parameter | Value | Citation | Tier | Confidence (reason) | Corroboration | Origin |
|---|---|---|---|---|---|---|
| UVI Ca(OH)2 / KOH | 22.5 kg (23 doses) / 21.5 kg (22 doses); projected 40.65 / 38.85 kg/yr | [Rakocy et al. ISTA6][ista6] | tier_1/2 (operator's symposium paper) | medium (measured totals; annual figure is a projection, duration not restated) | corroborated in order by [SRAC 454][srac454] | read |
| UVI pH | 7.4 (7.0–7.6) batch basil; 7.1 (6.9–7.3) staggered | [ISTA6][ista6] | tier_1/2 | medium-high (measured means) | single_source | read |
| UVI alkalinity | 113.2 (65.6–206.7); 88.6 (65.6–115.6); okra 115.9 mg/L | [ISTA6][ista6] | tier_1/2 | medium-high | single_source | read |
| UVI volume, make-up | 111.2 m3; rainwater 2.61 m3/d (2.4%/d) | [ISTA6][ista6] | tier_1/2 | medium-high | conflicting: 1.5%/d in [ISTA9][ista9] (different period) | read |
| UVI feeding ratio, FCR | 81.4–99.6 g/m2/d basil; FCR 1.7–1.8; 32% protein | [ISTA6][ista6] | tier_1/2 | medium-high | corroborated by [ISTA9][ista9] (60–100 g/m2/d) | read |
| SRAC dose description | 500–1,000 g each base, several times a week | [SRAC 454][srac454] | tier_1 | medium (vague frequency) | corroborates ISTA6 (≈78–156 vs 79.5 kg/yr) | read; comparison computed |
| Base equivalents | g CaCO3-eq per g: KOH 0.892, NaOH 1.251, Ca(OH)2 1.351, CaO 1.785, CaCO3 1.000, K2CO3 0.724, KHCO3 0.500, NaHCO3 0.596 | molar masses | n/a | high (standard chemistry) | n/a | **computed** |
| UVI base, CaCO3-eq | ≈ 89.6 kg/yr ≈ 0.245 kg/d ≈ 13–14 g/kg feed ≈ 2.0 g base/m3/d | from ISTA6 masses and feed basis | n/a | medium (feed total not reported directly) | n/a | **computed** |
| Cornell alkalinity at pH 7.0 | ~40 mg/L (K2CO3 daily) | [Vandam et al. 2017][vandam] | tier_1 | medium (koi, 1,000 L) | single_source | read |
| Do not use NaHCO3 | Na < 50 mg/L | [SRAC 454][srac454]; [FAO 589][fao] | tier_1 | medium-high | corroborated | read |
| Alkalinity target | ≥100 mg/L ([SRAC 454][srac454], [NMSU][nmsu]); 50–150, preferably >100 ([Masabni & Sink][tamu]); 60–140 ([KSU][ksu]) | as cited | tier_1/tier_2 | medium (stated, not tested in aquaponics) | corroborated near 100 | read |

### Three bookkeeping cases bracket UVI's base demand

All values in this subsection are **scenario estimates, not validated**. Each case uses the unverified 0.0294 kg TAN-N per kg of 32%-protein feed. All values are **computed**.

**Case A, naive.** All TAN is counted as NH4+ and fully nitrified, giving **0.21 kg CaCO3-eq/kg feed**. That is about 15 times UVI's implied 13–14 g/kg.

**Case B, NH3 excretion credited.** Fish excrete NH3, which protonates and is then nitrified. This gives **about 0.105 kg/kg**. Separately, SRAC 452's RAS rule (0.17–0.20 kg NaHCO3/kg feed) converts to 0.10–0.12 kg CaCO3-eq/kg feed. **The two figures are almost identical.** This suggests the RAS rule of thumb already reflects the NH3-to-NO3- net rather than the NH4+ figure.

**Case C, Case B plus plant uptake.** Plants take up the nitrate at 0.5–1.0 eq/mol. This gives **0 to 0.05 kg/kg**. Any denitrification pushes it lower still.

**Dilution cross-check.** UVI discards and replaces water with rainwater at up to 2.61 m3/d at its measured 89–113 mg/L. That loses up to **0.23–0.29 kg CaCO3/d** through dilution alone, which is about equal to the **0.245 kg/d** of base recorded.

This is an upper bound, because part of the make-up only replaces evapotranspiration, which removes no alkalinity. It still implies that UVI's net biological alkalinity consumption was small. That fits Case C plus the filter-tank denitrification UVI uses on purpose to control nitrate ([ISTA9][ista9]).

**Consequence for the engine.** It should not hard-code stoichiometric base demand. It should carry the excretion-accounting toggle, a plant-uptake coefficient and a denitrified fraction as explicit, reviewable parameters.

## Target pH depends on the regime, so keep three contexts

The extension consensus is **about 7.0, with a tolerable band of 6.4–7.4** ([NMSU CR-680][nmsu]; [Masabni & Sink][tamu]). That band is a compromise between three things:

- Nitrification is faster at higher pH.
- Fe, Mn, Cu, Zn and B lose availability above 7.0, and P, Ca and Mg lose it below 6.0 ([SRAC 454][srac454]).
- Tilapia tolerate pH 5–10 ([NMSU CR-680][nmsu]).

The peer-reviewed evidence does not converge on one optimum:

- **Nitrification rate.** Tyson et al. measured TAN removal of **19, 31 and 80 g/m3/day at pH 6, 7 and 8** in perlite biofilters with cucumber ([Tyson et al. 2008][tyson08]). In plant-free vessels at 28–30 °C, they found no nitrification at pH 5.5 ([Tyson et al. 2004][tyson04]).
- **N-use efficiency.** Zou et al. found **50.9 / 47.3 / 44.7% at pH 6.0 / 7.5 / 9.0** in media beds, and recommended pH 6.0 ([Zou et al. 2016][zou]).
- **Low-pH nitrification.** Derikvand et al. found lab systems at pH 5.8–6.0 nitrified, with comammox *Nitrospira* dominant. Lettuce biomass trended higher there, though not significantly ([Derikvand et al. 2024][derik]).
- **Leafy crops at pH 7.** Lettuce in aquaponic water at pH 7.0 reached **95% of the pH 5.8 hydroponic control**, while hydroponic lettuce at pH 7.0 fell to **77%**. Tissue Mn was lower in the aquaponic lettuce ([Anderson et al. 2017][anderson]).

The extension claim that nitrification "stops" at pH 6.0 ([Rakocy, Ten Guidelines][rakocy10]; [Hawaii][hawaii]) therefore applies to start-up or unacclimated biofilms, not necessarily to mature ones.

| Parameter | Value | Citation | Tier | Confidence (reason) | Corroboration | Origin |
|---|---|---|---|---|---|---|
| TAN removal vs pH (perlite, cucumber) | 19 / 31 / 80 g/m3/d at pH 6 / 7 / 8 | [Tyson et al. 2008][tyson08] | tier_1 | medium-high (fruiting crop, not leafy) | corroborated in direction by extension optima | read |
| Days to TAN = 0 from 5 mg/L, 28–30 °C | 12 (pH 8.5), 20 (7.5), 20–24 (6.5), none (5.5) | [Tyson et al. 2004][tyson04] | tier_1 (proceedings) | medium (vessel test; text inconsistency) | corroborated in direction | read |
| N-use efficiency vs pH (media bed) | 50.9 / 47.3 / 44.7% at 6.0 / 7.5 / 9.0; N2O ratio 2.0 → 0.6% | [Zou et al. 2016][zou] | tier_1 | medium (abstract only) | conflicting optimum with Tyson 2008 → context_split | read |
| Low-pH nitrification | functional at 5.8–6.0, comammox dominant (23 °C, lettuce) | [Derikvand et al. 2024][derik] | tier_1 | medium (lab scale) | conflicts with "stops at 6.0" extension claims | read |
| Lettuce fresh weight vs pH and system | 178 g (H5.8), 137 g (H7.0), 169 g (A7.0) | [Anderson et al. 2017][anderson] | tier_1 | medium (single trial, koi) | corroborated by spinach in [Vandam et al. 2017][vandam] | read |
| Lettuce / tilapia pH optima | lettuce 5.5–6.5; Nile tilapia 7–9 | [Goddek et al. 2019, ch. 8][goddek] | tier_1 | high (edited book) | corroborated by extension | read |
| Micronutrient lock-up | Fe/Mn/Cu/Zn/B ↓ above 7.0; P/Ca/Mg/Mo ↓ below 6.0; Fe-DTPA to 2 mg/L | [SRAC 454][srac454]; [KSU][ksu]; [Yildiz et al. 2017][yildiz] | tier_1 | high | corroborated | read |
| Compromise pH | 6.8–7.0; tolerable 6.4–7.4 | [NMSU CR-680][nmsu]; [Masabni & Sink][tamu] (7.0) | tier_2 | medium | corroborated | read |
| Operating pH, commercial | UVI 7.0–7.5 ([ISTA6][ista6]); Savidov 6.1–6.3 ([Savidov 2005][savidov]) | as cited | tier_1/2; tier_2 | medium | context_split | read |
| NH3 share of TAN | < 10% below pH 8, rising sharply above | [Hawaii][hawaii] | tier_2 | medium | corroborated (dose slowly: [Masabni & Sink][tamu], [NMSU][nmsu]) | read |

**How the regimes map to the farms (inference):**

- **Netherlands.** Tap water plus strong raft aeration sits near the alkaline edge, so the 7.0 ± 0.3 compromise is reachable with modest Ca/K base dosing once nitrification draws alkalinity down.
- **South India on borewell water.** The farm will drift above 7.5 at 22–30 °C. Micronutrient lock-up and NH3-fraction context then dominate, and the relevant dosing is H3PO4 into the top-up reservoir ([FAO 589][fao]), or blending with rainwater or RO water.

NH3 fraction here is chemistry context, not a fish-safety statement.

## Source water flips the dosing sign between the two farm sites

**Netherlands.** Dutch tap water is regulated to **HCO3- > 60 mg/L, 7.0 < pH < 9.5 and SI > −0.2**, with hardness above 1.0 mmol/L where water is softened ([Waternet Leiduin 2022][waternet22]; [KWR, Slaats et al. 2015][kwr]). Measured supplies cluster at 95–155 mg/L as CaCO3, but soft sources go lower:

- Vitens Pinkenberg/Leersum measured 48–66 mg/L in 2017.
- WML's purchased Enwor water measured 33–49 mg/L, below the legal minimum ([ILT 2018][ilt]).

**South India.** IS 10500:2012 allows **alkalinity and hardness up to 200 mg/L acceptable and 600 mg/L permissible**, with pH 6.5–8.5 ([BIS IS 10500:2012][bis]). Water that is legal to drink can therefore be far above aquaponics targets. Peer-reviewed hard-rock groundwater studies show very wide ranges between wells. The one surface-water proxy found, a Cauvery delta distributary, is soft at about 38 mg/L ([CWC Cauvery 2019][cwc]). It is not the Bengaluru intake.

All alkalinity values "as CaCO3" below are **computed** from HCO3- × 0.820 unless the source reports them as total alkalinity.

| Source | pH | Alkalinity, mg/L as CaCO3 | Hardness | Citation | Tier | Confidence (reason) | Corroboration |
|---|---|---|---|---|---|---|---|
| Drinkwaterbesluit limits | 7.0–9.5 | HCO3- > 60 (≈49) | > 1.0 mmol/L if softened | [Waternet 2023][waternet22]; [KWR 2015][kwr] | tier_1 | high (max 2.5 mmol/L unverified) | corroborated |
| Water-sector recommendations | > 7.4 | TAC > 2 mmol/L (≈100) | < 1.8 mmol/L | [KWR 2015][kwr] | tier_2 | medium (garbled table) | single_source |
| Waternet Leiduin 2022 | 7.76–8.08–8.40 | 131–143–154 | 1.20–1.37–1.55 mmol/L | [Waternet 2023][waternet22] | tier_1 | high (statutory min/avg/max) | corroborated range |
| Dunea Scheveningen 2025 | 8.29–8.48–8.66 | 137–144–156 | 1.29–1.42–1.74 mmol/L | [Dunea 2026][dunea] | tier_1 | high | corroborated range |
| Vitens WZ_MPb-Hoenderloo 2025 | 7.83–7.92–8.02 | 95–103–108 | 1.14–1.22–1.32 mmol/L | [Vitens 2025][vitens] | tier_1 | high (site name not printed) | corroborated range |
| Vitens Pinkenberg / Leersum 2017 | n/a | 48–54–63 / 48–55–66 | n/a | [ILT 2018][ilt] | tier_1 | high (old, exceedance rows only) | single_source |
| WML Enwor purchased water 2017 | n/a | 33–39–49 | n/a | [ILT 2018][ilt] | tier_1 | high | single_source |
| Dutch national average hardness | n/a | n/a | ~8 °dH (1.4 mmol/L) | [Waternet web page][waternetH] | tier_2 | medium | single_source |
| BIS IS 10500:2012 | 6.5–8.5 | 200 acceptable / 600 permissible | 200 / 600 mg/L | [BIS][bis] | tier_1 | high | corroborated by state copies (not fetched) |
| Bengaluru west, 67 wells, 2014 | 5.8–8.13 | "HCO3 (alkalinity)" 88–530 (basis ambiguous; ≈72–434 if HCO3-) | 48–1,873 mg/L | [Gulgundi & Shetty 2018][gulgundi] | tier_1 | medium (Mg typo, basis unclear) | single_source |
| Chennai Anna Nagar, 24 borewells | 6.0–8.2 | ≈15–295 | 90–815 (mean 212) | [Krishna kumar et al. 2015][krishna] | tier_1 | medium (date unknown) | single_source |
| Hyderabad fringe (Jawaharnagar dumpsite) | 7.2–7.8 | TA 222–427 (basis not stated) | 420–584 | [Unnisa & Zainab Bi 2017][unnisa] | tier_1 | low-medium (landfill site) | single_source |
| Khammam, Telangana | 7.53–8.35 | n/a | 200–820 (mean 439) | [Narasaiah & Venkateswara Rao 2021][narasaiah] | tier_1 | medium | single_source |
| Prakasam, coastal AP | 7.2–8.3 | ≈394–841 (mean 600) | n/a | [Subba Rao 2018][subba] | tier_1 | medium (internal inconsistencies) | single_source |
| Cauvery delta distributary (Gopurajapuram), n=3 | 6.9–8.5 | 21–51 (mean 38) | 28–60 | [CWC 2019][cwc] | tier_1 | low as a city-supply proxy | single_source |
| Piped water, BIS tests 2019 | pass/fail | Amaravati alkalinity failures; none in Bengaluru, Hyderabad or Chennai | Chennai hardness failures at 2 sites | [BIS piped-water report][bispiped] | tier_1 | medium (10 grab samples per city) | single_source |
| Rainwater alkalinity | n/a | ~0 | ~0 | none | n/a | low | **inference** (no source fetched) |

**What this means for the model, as scenario estimates, not validated:**

- **Netherlands.** Make-up water supplies about 95–155 mg/L of alkalinity. Each cubic metre exchanged adds about 95–155 g CaCO3-eq, offsetting part of the nitrification draw. Rainwater make-up, as at UVI, adds nothing.
- **South India.** At 150–400+ mg/L, borewell make-up adds alkalinity faster than a well-planted system consumes it. The base-dose term goes to zero and an acid or dilution term appears.
- Because measured wells range over a factor of ten, the engine must take the site's own laboratory analysis as a required input. A regional default will not do.

## Conclusion: a minimal daily model for the engine

The finding that changes the modelling approach is about structure. The hard part of a pH model is not the carbonate equilibrium. That is solved chemistry. The hard part is the nitrogen-accounting convention and the outflow volume, which together decide whether base demand is 0 or 0.2 kg CaCO3-eq per kg feed. UVI's data are consistent with near-zero net biological consumption, and RAS rules of thumb match the NH3-credited case. So the engine should expose excretion accounting, the plant-uptake coefficient and the denitrified fraction as labelled parameters, calibrated per site, not as constants. The second structural point is timing: CO2 equilibrates in hours, so a daily model can treat CO2 as quasi-steady and carry only alkalinity as a state. The short-term pH jump from hydroxide versus bicarbonate dosing then matters only for dosing practice, not for the daily balance.

The minimal daily structure below fits the existing MVP layers. TAN-N comes from P1. KLa, or the measured CO2 used in its place, comes from the P1.5 aeration context, and that context is not an aeration-adequacy claim. Base-dose and acid-dose outputs are **scenario estimates, not validated**, and must carry `estimate_status: "scenario_estimate"`.

```text
State (daily):  Alk  [g CaCO3-eq in system volume V]   (optional: Ca, K, Na tallies from dosing)
Inputs:         feed_g, T, V, Q_discharge (m3/d, removes Alk), Q_makeup (= discharge + evapotranspiration),
                Alk_makeup (site lab value), N_TAN (from P1), f_nit, f_het, f_denit, f_plant_NO3,
                KLa_O2 (or measured CO2 for calibration), base/acid doses

dAlk = + s_ex  * 3.57 * N_TAN                      # NH3-excretion credit; s_ex in {0,1}, decision required
       - 7.05 * N_TAN * f_nit                      # Ebeling Eq.14 (sensitivity 7.14)
       - 3.57 * N_TAN * f_het                      # Ebeling Eq.16
       + 3.57 * N_NO3 * f_denit                    # denitrification return (~3.5)
       + k_pl * N_NO3 * f_plant_NO3                # k_pl 1.79-3.57 g/g N (inference, calibrate)
       + sum(dose_i * e_i)                         # e: KOH 0.892, Ca(OH)2 1.351, K2CO3 0.724, KHCO3 0.500
       - Q_discharge * Alk/V  +  Q_makeup * Alk_makeup
P_CO2  = 1.375 * (0.25-0.5) * feed_g  + 5.85 * N_TAN*f_nit + 9.65 * N_TAN*f_het (+ solids decay: gap)
CO2*   = CO2_eq(T) + P_CO2 / (phi * KLa_O2 * V),   phi = 0.67-0.86
pH     = solve charge balance (Alk, CO2*, K1(T), K2(T), Kw; Davies activity); H-H check in 6-8.3
Inverse (target pH):  Alk_req = 50.04 * [CO2* mmol/L] * 10^(pH_target - pK1)   -> base or acid demand
Context flags (not safety claims): pH < 6.0 nitrification-rate context; pH > 7.5 Fe/Mn/P availability
                                   context; NH3 fraction context; CO2 vs 20 / 60 mg/L context_split
Calibration set: UVI ISTA6 (V 111.2 m3, rain 2.61 m3/d, Alk 89-113, pH 7.1-7.4, base 79.5 kg/yr)
```

**Open gaps that block canon promotion:**

- **Missing measurements:**
  - No measured dissolved CO2 in any coupled aquaponics system.
  - No KLa for raft air-stones or bell-siphon media beds.
  - No measured eq/mol alkalinity return from plant nitrate uptake.
  - No pH- or alkalinity-decline rate from an undosed aquaponics system.
  - No basil yield comparison across pH.
  - No tilapia growth comparison across pH or CO2 in aquaponics.
- **Unverified constants and stoichiometry:**
  - The Plummer & Busenberg coefficients were recalled, not read.
  - The TAN rule (0.092 × protein) is unverified.
  - The sign of Ebeling Eq. 4 needs checking.
  - The EPA originals were not fetched.
  - No source covers how fish NH3 excretion changes alkalinity.
- **Incomplete UVI records:** the split of UVI's make-up between discharge and evapotranspiration is not published.
- **Source-water data:**
  - The CGWB Ground Water Year Books for Karnataka, Telangana, AP and Tamil Nadu could not be fetched.
  - No numeric BWSSB, CMWSSB or HMWSSB treated-water values were found.
  - Dutch private-well and rainwater chemistry were not found.
  - The Drinkwaterbesluit maximum hardness is unverified.

**Handling of new values.** Each value entering `data/knowledge/atomic_facts/` should be saved as `provisional` with `candidate_pending_user_review`, carrying the tier, confidence and corroboration status shown in the tables above. Recalled and computed values should be tagged as such until a fetched source confirms them.

[aqion]: https://www.aqion.de/sd/175?page=7
[henry]: https://henrys-law.org/henry/casrn/124-38-9
[pb82]: https://pubs.usgs.gov/publication/70011789
[co2ctl]: https://ag.arizona.edu/azaqua/ista/ISTA7/RecircWorkshop/Workshop%20PP%20%20&%20Misc%20Papers%20Adobe%202006/8%20Gas%20Transfer/Degassing/CO2%20Control.pdf
[eb]: https://ag.arizona.edu/azaqua/ista/ISTA7/RecircWorkshop/Workshop%20PP%20%20%26%20Misc%20Papers%20Adobe%202006/7%20Biofiltration/Microbial%20Floc%20Systems/2006%20Aquaculture%20Stoichiometry%20of%20photo-auto-hetero%20-%20Ebeling.pdf
[cwea]: https://www.cwea.org/news/how-alkalinity-affects-nitrification/
[srac452]: https://www.srac.msstate.edu/pdfs/Fact%20Sheets/452%20Recirculating%20Aquaculture%20Tank%20Production%20Systems-%20Management%20of%20Recirculating%20Systems.pdf
[srac454]: https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf
[raven]: https://www.scilit.com/publications/2a63e7dcd8bfafd3a961aed2db7131c3
[dickson]: https://journals.ashs.org/downloadpdf/view/journals/hortsci/54/6/article-p1093.pdf
[goddek]: https://link.springer.com/content/pdf/10.1007/978-3-030-15943-6_8.pdf
[colt2]: https://pubs.usgs.gov/publication/70043555
[hamad]: https://pure.au.dk/ws/files/451434507/1-s2.0-S004484862400499X-main.pdf
[aitch]: https://vtechworks.lib.vt.edu/items/eccf9efa-1aa4-4141-b27c-c5128563d910/full
[moran]: https://lup.lub.lu.se/record/1981410
[loyless]: https://informahealthcare.com/doi/abs/10.1577/1548-8640%281997%29059%3C0198%3AASBDMF%3E2.3.CO%3B2
[ista6]: https://ag.arizona.edu:443/azaqua/ista/ista6/ista6web/pdf/676.pdf
[ista9]: https://cales.arizona.edu/azaqua/ista/ISTA9/PDF's/RakocyAquaponicSystem.pdf
[savidov]: https://issuu.com/ponics/docs/110504140652-36fd13b4bc2849e4895c5eeeb258c678
[vandam]: https://www.mdpi.com/2311-7524/3/2/32
[anderson]: https://bpb-us-e1.wpmucdn.com/blogs.cornell.edu/dist/1/3676/files/2019/09/Growth-and-Tissue-Elemental-Composition-Response-of-Butterhead-Lettuce.pdf
[ksu]: https://www.kysu.edu/documents/school-of-agriculture-communities-and-the-environment/aquaponics_handbook_2021_final_022421.pdf
[nmsu]: https://pubs.nmsu.edu/_circulars/CR680/
[fao]: https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/3-water-quality-in-aquaponics/manipulating-ph/
[hawaii]: https://www2.hawaii.edu/~khanal/aquaponics/nitrogen.html
[tamu]: https://extension.rwfm.tamu.edu/wp-content/uploads/sites/8/2020/10/Water-Quality-In-Aquaponics-Sink-Masabni.pdf
[tyson04]: https://journals.flvc.org/fshs/article/download/85855/82771/107719
[tyson08]: https://agris.fao.org/search/en/records/65dfb69e63b8185d9cae3f3a
[zou]: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.biortech.2015.12.079&resultType=core&format=json
[derik]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10867649/
[yildiz]: https://mdpi.com/2073-4441/9/1/13
[rakocy10]: https://cdn.aquaponicsassociation.org/uploads/2019/10/Aquaponics-Journal-10-Guidelines.pdf
[waternet22]: https://www.waternet.nl/siteassets/ons-water/drinkwater/drinkwater-leiduin-2022.pdf
[waternetH]: https://www.waternet.nl/en/service-and-contact/tap-water/tap-water-hardness/
[dunea]: https://www.dunea.nl/english/-/media/bestanden/home/drinkwater/waterkwaliteitsrapportages/2025-rapportages/scheveningen-year-2025-english.pdf
[vitens]: https://www.vitens.nl/-/media/Project/Vitens/VitensNl/Service/Waterkwaliteitsoverzicht/WZ_MPb-Hoenderloo.PDF
[ilt]: https://www.ilent.nl/binaries/ilt/documenten/leefomgeving-en-wonen/drinkwater/drinkwater/rapporten/kwaliteit-drinkwater-van-nederlandse-drinkwaterbedrijven-2017/Kwaliteit+drinkwater+van+Nederlandse+drinkwaterbedrijven+2017.pdf
[kwr]: https://api.kwrwater.nl//uploads/2017/02/Slaats-Meerkerk-Palmen-Brink-Conditionering-van-drinkwater-de-aanbevelingen-voor-optimale-samenstelling-in-2014-H2O-Online-%282015%29-9-januari.pdf
[bis]: https://consumerhelpline.gov.in/public/assets/docs/bis/IS10500-2012.pdf
[gulgundi]: https://link.springer.com/10.1007/s13201-018-0684-z
[krishna]: https://link.springer.com/article/10.1007/s13201-014-0196-4
[unnisa]: https://link.springer.com/10.1007/s13201-017-0544-2
[narasaiah]: https://link.springer.com/article/10.1007/s13201-021-01424-2
[subba]: https://link.springer.com/article/10.1007/s13201-018-0665-2
[bispiped]: https://www.bis.gov.in/wp-content/uploads/2019/11/Drinking_Water_20112019.pdf
[cwc]: https://cwc.gov.in/sites/default/files/admin/6ACBWQYB17-18.pdf
