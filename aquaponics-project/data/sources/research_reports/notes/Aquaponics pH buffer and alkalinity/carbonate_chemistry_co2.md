# Carbonate chemistry, alkalinity stoichiometry and CO2 balance for a daily pH/alkalinity buffer model (freshwater tilapia + basil/lettuce aquaponics, DWC + gravel media, 22-30 C)

Fetch note: about 22 page fetches used. Several primary sources (Timmons & Ebeling textbook, Stumm & Morgan, Plummer & Busenberg 1982 full text, Zou et al. 2016 full text, Loyless & Malone 1997 full text, US EPA 1975/1993 manuals) could not be read in full. Values that rest on abstracts or secondary pages are flagged as such. Tier labels follow the brief: tier_1 = peer-reviewed / official / textbook of record; tier_2 = extension / reputable grey literature; tier_3 = commercial / anecdotal.

## Q1. Alkalinity consumed by nitrification, heterotrophic and algal assimilation; fish NH3 excretion

### Takeaway
Use 7.05 g CaCO3 per g TAN-N nitrified (Ebeling et al. 2006 Eq. 14, which includes nitrifier biomass synthesis). The textbook "no-growth" value is 7.14 (US EPA, cited second-hand). Heterotrophic assimilation consumes 3.57 g CaCO3/g N. Algal uptake of NH4+ consumes 3.13 g/g N. Algal uptake of NO3- produces 4.02 g/g N.

### Cited Findings
- **Nitrification (autotrophic), Ebeling, Timmons & Bisogni (2006), "Engineering analysis of the stoichiometry of photoautotrophic, autotrophic, and heterotrophic removal of ammonia-nitrogen in aquaculture systems", *Aquaculture* 257:346-358, DOI 10.1016/j.aquaculture.2006.03.019, Eq. (14):** NH4+ + 1.83 O2 + 1.97 HCO3- -> 0.0244 C5H7O2N + 0.976 NO3- + 2.90 H2O + 1.86 CO2. Per g NH4+-N this gives 7.05 g alkalinity as CaCO3 consumed, 4.18 g O2 consumed, 5.85 g CO2 produced, 0.20 g VSS nitrifier biomass and 0.976 g NO3--N produced. No carbohydrate is needed. — [Ebeling et al. 2006 (PDF, ISTA7 workshop copy)](https://ag.arizona.edu/azaqua/ista/ISTA7/RecircWorkshop/Workshop%20PP%20%20%26%20Misc%20Papers%20Adobe%202006/7%20Biofiltration/Microbial%20Floc%20Systems/2006%20Aquaculture%20Stoichiometry%20of%20photo-auto-hetero%20-%20Ebeling.pdf). Suggested tier_1, confidence high: peer-reviewed, the equation is given explicitly, and it is the standard RAS reference. Corroborated (see the next bullet).
- **Theoretical 7.14 mg CaCO3 per mg NH4-N oxidized.** CWEA (California Water Environment Association) is a trade-association article that cites US EPA *EPA-625/4-73-004a, Revised Nitrification and Denitrification Facilities* (1970s). CWEA also gives residual-alkalinity guidance: about 70-80 mg/L as CaCO3 after full nitrification to keep pH near neutral, and "most experts" recommend 75-150 mg/L in effluent. — [CWEA, How Alkalinity Affects Nitrification](https://www.cwea.org/news/how-alkalinity-affects-nitrification/). Suggested tier_2, confidence high for the 7.14 value: grey literature reporting an EPA value. The EPA 1993 manual itself was not fetched. Agrees with Ebeling: 7.14 is the stoichiometry without cell synthesis (2 mol HCO3- per mol N = 2 x 50/14). 7.05 is lower because some N goes into biomass.
- **Heterotrophic (carbohydrate-supplemented) TAN assimilation, Ebeling et al. 2006, Eq. (16):** NH4+ + 1.18 C6H12O6 + HCO3- + 2.06 O2 -> C5H7O2N + 6.06 H2O + 3.07 CO2. Per g N this consumes 3.57 g alkalinity as CaCO3, 4.71 g O2 and 15.17 g carbohydrate, and produces 9.65 g CO2 and 8.07 g VSS. No NO2-/NO3- is produced. — [Ebeling et al. 2006](https://ag.arizona.edu/azaqua/ista/ISTA7/RecircWorkshop/Workshop%20PP%20%20%26%20Misc%20Papers%20Adobe%202006/7%20Biofiltration/Microbial%20Floc%20Systems/2006%20Aquaculture%20Stoichiometry%20of%20photo-auto-hetero%20-%20Ebeling.pdf). Suggested tier_1, confidence high for stoichiometry. Single source here, although it is widely re-cited.
- **Photoautotrophic (algal) uptake, Ebeling et al. 2006, Eq. (3), NH4+ as N source:** 16 NH4+ + 92 CO2 + 92 H2O + 14 HCO3- + HPO4^2- -> C106H263O110N16P + 106 O2. Per g N this consumes 3.13 g CaCO3 alkalinity and 18.07 g CO2, and produces 15.14 g O2 and 15.85 g algal biomass. — [Ebeling et al. 2006](https://ag.arizona.edu/azaqua/ista/ISTA7/RecircWorkshop/Workshop%20PP%20%20%26%20Misc%20Papers%20Adobe%202006/7%20Biofiltration/Microbial%20Floc%20Systems/2006%20Aquaculture%20Stoichiometry%20of%20photo-auto-hetero%20-%20Ebeling.pdf). Tier_1, confidence high.
- **Algal uptake, Eq. (4), NO3- as N source:** 16 NO3- + 124 CO2 + 140 H2O + 18 HCO3- + HPO4^2- -> biomass + 138 O2. The paper text gives this as alkalinity *produced* of 4.02 g CaCO3 per g NO3--N, 24.4 g CO2 consumed and 19.71 g O2 produced. — [Ebeling et al. 2006](https://ag.arizona.edu/azaqua/ista/ISTA7/RecircWorkshop/Workshop%20PP%20%20%26%20Misc%20Papers%20Adobe%202006/7%20Biofiltration/Microbial%20Floc%20Systems/2006%20Aquaculture%20Stoichiometry%20of%20photo-auto-hetero%20-%20Ebeling.pdf). Tier_1, confidence medium. The sign is clear, but the equation as extracted lists HCO3- on the reactant side while the text says alkalinity is produced. Check the exact form of Eq. 4 in the original before coding.
- **SRAC 452** (Masser, Rakocy & Losordo, 1999 rev.) states only qualitatively that "bacterial nitrification produces acids and consumes alkalinity". It recommends alkalinity of 50-100 mg/L as CaCO3 or higher. — [SRAC 452](https://www.srac.msstate.edu/pdfs/Fact%20Sheets/452%20Recirculating%20Aquaculture%20Tank%20Production%20Systems-%20Management%20of%20Recirculating%20Systems.pdf). Tier_2, confidence high for the target range.

### Inferences
- **Model default:** dAlk_nitrif [g CaCO3/d] = -7.05 x (TAN-N nitrified, g/d). Sensitivity range 7.05-7.14.
- **Fish ammonia excretion (NH3).** No fetched source answers this. By charge-balance reasoning: when NH3 is excreted and protonates in water (NH3 + H+ -> NH4+, or equivalently NH3 + H2CO3 -> NH4+ + HCO3-), alkalinity rises by 1 eq per mol N (about 3.57 g CaCO3/g N) as long as N stays as NH4+. When that NH4+ is then nitrified, 2 eq/mol is consumed (7.14 g/g N). The net from NH3 excretion through to nitrate is about -1 eq/mol N, or about -3.57 g CaCO3/g N.
- **Accounting convention.** Ebeling's equations start from NH4+. If the model uses 7.05/7.14 per g TAN nitrified, it should **not** also credit alkalinity for NH3 excretion, unless both steps are modelled explicitly. Doing both would double count, or would undercount if only one step is included. This is a modelling choice that needs a documented decision, and it is an inference rather than a cited fact.
- **Gravel media beds** also host heterotrophs, so a share of TAN may be assimilated heterotrophically (3.57 instead of 7.05). That share is unknown for this system.

### Gaps
- The original US EPA (1975) *Process Design Manual for Nitrogen Control* and the EPA (1993) *Manual: Nitrogen Control* (EPA/625/R-93/010) were not fetched. The page and equation numbers for 7.14 are unverified.
- No fetched peer-reviewed source states quantitatively how fish NH3 excretion changes alkalinity. The figure above is derived.
- Timmons & Ebeling, *Recirculating Aquaculture* (textbook), was not accessed. Its alkalinity chapter page numbers are not recorded.

## Q2. Alkalinity change from plant uptake of NO3- vs NH4+

### Takeaway
Plant-physiology literature (Raven & Smith 1976) says NO3- assimilation generates "almost one OH- per NO3-". Only part of that OH- leaves the root, because the rest is neutralised internally by organic-acid synthesis. NH4+ uptake acidifies. A usable model parameter is +0.5 to +1.0 eq alkalinity per mol NO3--N taken up (midpoint about 0.75). That range is an inference from the qualitative literature, so confidence is low to medium.

### Cited Findings
- Raven, J.A. & Smith, F.A. (1976), "Nitrogen assimilation and transport in vascular land plants in relation to intracellular pH regulation", *New Phytologist* 76(3):415-431, DOI 10.1111/j.1469-8137.1976.tb01477.x. The abstract states that NO3- assimilation "produces almost one OH- per NO3-". In roots the excess OH- is partly excreted and partly neutralised by the "biochemical pH stat" (organic acid synthesis). When NO3- is reduced in shoots, the OH- can be stored as organate or Ca-oxalate, or moved back to the roots and released. — [Raven & Smith 1976 (Scilit abstract)](https://www.scilit.com/publications/2a63e7dcd8bfafd3a961aed2db7131c3). Suggested tier_1, confidence medium: a classic peer-reviewed paper, but only the abstract was read and the excreted fraction is not quantified there.
- Dickson, R.W. & Fisher, P.R. (2019), "Quantifying the acidic and basic effects of vegetable and herb species in peat-based substrate and hydroponics", *HortScience* 54(6):1093-1100, DOI 10.21273/HORTSCI13959-19, p. 1093. NH4+-N supply causes root-zone acidity from greater net cation uptake. NO3--N causes basicity from OH-/HCO3- efflux. In hydroponics with 100% NO3- (0:100 NH4:NO3), every species tested (basil and lettuce included) raised pH. Basicity reached up to 1.31 mEq per g dry-weight gain (arugula). Lettuce extrapolated to 100% NH4+ gave up to 4.52 mEq/g acidity. Literature comparison: castor gave 3.70 mEq/g acidity on NH4+ and 1.03 mEq/g basicity on NO3- (van Beusichem et al. 1988). Table 1 gives the NH4+ share needed for pH neutrality: basil and lettuce about 6.6-26.5% depending on system, lettuce about 6.6% in hydroponics. Sonneveld & Voogt (2009) recommend 5-10% NH4+-N in hydroponics. Results are per g dry weight, not per mol N. — [Dickson & Fisher 2019](https://journals.ashs.org/downloadpdf/view/journals/hortsci/54/6/article-p1093.pdf). Tier_1, confidence high for direction, medium for magnitude. Corroborates Raven & Smith in direction.
- Ebeling et al. (2006) Eq. 4 makes the same point for algae: nitrate uptake produces about 4.02 g CaCO3 per g N, which is about 1.1 eq per mol N. — [Ebeling et al. 2006](https://ag.arizona.edu/azaqua/ista/ISTA7/RecircWorkshop/Workshop%20PP%20%20%26%20Misc%20Papers%20Adobe%202006/7%20Biofiltration/Microbial%20Floc%20Systems/2006%20Aquaculture%20Stoichiometry%20of%20photo-auto-hetero%20-%20Ebeling.pdf). Tier_1, corroborates the direction and an upper bound near 1 eq/mol.
- Goddek et al. (2019), "Decoupled Aquaponics Systems", ch. 8 in *Aquaponics Food Production Systems* (Springer), pp. 201-229, DOI 10.1007/978-3-030-15943-6_8. Table 8.1 (p. 207) gives pH optima: Nile tilapia 7-9, lettuce 5.5-6.5, tomato 6.3-6.5. The chapter does not quantify alkalinity release from nitrate uptake. — [Goddek et al. 2019 ch. 8](https://link.springer.com/content/pdf/10.1007/978-3-030-15943-6_8.pdf). Tier_1 (edited academic book), confidence high for the pH optima listed.
- Wongkiew et al. (2017), "Nitrogen transformations in aquaponic systems: A review", *Aquacultural Engineering* 76:9-19, DOI 10.1016/j.aquaeng.2017.01.004. Only the metadata page was accessible, so its content on pH and alkalinity was not read. — [Wongkiew et al. 2017 (SciSpace record)](https://scispace.com/papers/nitrogen-transformations-in-aquaponic-systems-a-review-152bkhn7tx). Not used for values.

### Inferences
- **Suggested parameter:** alk_plant_NO3 = +0.5 to +1.0 eq per mol NO3--N taken up (= +1.79 to +3.57 g CaCO3 per g N), central value 0.75. The upper bound of 1.0 follows from Raven & Smith's "almost one OH- per NO3-" if all of it were excreted. The lower bound reflects the partial internal neutralisation they describe. The 0.5 figure is a modelling assumption, not a cited value. Tier: inference, confidence low.
- **Net per g TAN-N in a well-balanced aquaponics loop:** -7.05 (nitrification) + 1.8 to 3.6 (plant NO3- uptake) = about -3.5 to -5.3 g CaCO3 per g N that is both nitrified and taken up by plants. N lost by denitrification in anoxic gravel zones would return about 3.57 g CaCO3/g N (classic denitrification stoichiometry, not fetched here). This is not modelled in the sources found.
- Dickson & Fisher's dry-weight-based values could be converted to per-mol N using plant N content, but plant N % was not fetched.

### Gaps
- No fetched aquaponics paper (Zou et al. 2016, Wongkiew et al. 2017) gave a measured eq/mol value for nitrate-uptake alkalinisation in a coupled system.
- Marschner, *Mineral Nutrition of Higher Plants* (textbook), was not accessed. It would give the cation-anion balance discussion with page numbers.
- **Zou, Y., Hu, Z., Zhang, J., et al. (2016), "Effects of pH on nitrogen transformations in media-based aquaponics", *Bioresource Technology* 210:81-87.** The HAL record was blocked, so the reported NUE at pH 6.0/7.5/9.0 could not be verified here. This citation is from memory: confirm the volume and pages.

## Q3. Carbonate equilibrium constants vs temperature; Henderson-Hasselbalch form; atmospheric-equilibrium CO2

### Takeaway
At 25 C, pK1 = 6.35, pK2 = 10.33 and log KH = -1.47 (mol/L/atm), per Stumm & Morgan and the WATEQ4F database. The temperature function below is the Plummer & Busenberg (1982) form (coefficients recalled, not fetched; see the caveat). It reproduces the WATEQ4F 25 C values to three decimals. Air-equilibrium dissolved CO2 at 420 ppm is about 0.63 mg/L at 25 C, and 0.55-0.72 mg/L over 20-30 C.

### Cited Findings
- **Constants at 25 C** (aqion compilation): log KH(CO2(g)->H2CO3*) = -1.47 (Stumm & Morgan) and -1.468 (WATEQ4F). log K1 = -6.35 (Stumm & Morgan) and -6.3447 (LLNL). log K2 = -10.33 (Stumm & Morgan) and -10.329 (WATEQ4F). — [aqion, Carbonate Equilibria and log K Values](https://www.aqion.de/sd/175?page=7). Tier_2 compilation of tier_1 values, confidence high. Corroborated: the sources agree to ±0.005.
- **Henry's-law solubility of CO2 at 298.15 K:** Hscp = 3.3-3.4 x 10^-4 mol m^-3 Pa^-1 (= 0.033-0.034 mol L^-1 atm^-1). Temperature dependence d ln H / d(1/T) = 2300-2400 K. The sources (Weiss 1974; Carroll et al. 1991; Crovetto 1991; Sander et al. 2006, 2011; Burkholder et al. 2019) all agree. Cite as Sander, R. (2023), *Atmos. Chem. Phys.* 23:10901-12440, DOI 10.5194/acp-23-10901-2023. — [henrys-law.org CO2 entry](https://henrys-law.org/henry/casrn/124-38-9). Tier_1, confidence high, corroborated by multiple sources.
- Plummer, L.N. & Busenberg, E. (1982), "The solubilities of calcite, aragonite and vaterite in CO2-H2O solutions between 0 and 90 C...", *Geochimica et Cosmochimica Acta* 46:1011-1040, DOI 10.1016/0016-7037(82)90056-4. This is the standard source of the T-functions used in PHREEQC/WATEQ4F. Only the USGS record was found; the full text was not fetched. — [USGS record](https://pubs.usgs.gov/publication/70011789).
- **Henderson-Hasselbalch form, worked check against Vinci/Timmons/Summerfelt/Watten course data.** At 100 mg/L alkalinity, dissolved CO2 is about 70 mg/L at pH 6.5, about 20 mg/L at pH 7.0 and about 3 mg/L at pH 8.0. Their example waters are: culture tank 40 mg/L CO2, alkalinity 100, pH 6.8, CT 0.002909 mol/L; stripper effluent 13.6 mg/L, pH 7.2; makeup water 5 mg/L, pH 7.7. — [Watten, Timmons, Vinci, Summerfelt, Piedrahita, "Carbon Dioxide Stripping: Fundamentals and Computer Design Model", RAS short course; model = Vinci et al. 1998, *Carbon Dioxide Control in Intensive Aquaculture* v2.1, NRAES/Cornell](https://ag.arizona.edu/azaqua/ista/ISTA7/RecircWorkshop/Workshop%20PP%20%20&%20Misc%20Papers%20Adobe%202006/8%20Gas%20Transfer/Degassing/CO2%20Control.pdf). Suggested tier_2 (course material from textbook authors), confidence high.
- **Air-equilibrium CO2:** about 0.69 mg/L at 15 C for x_CO2 = 0.00035 (350 ppm). — [Watten et al. course notes](https://ag.arizona.edu/azaqua/ista/ISTA7/RecircWorkshop/Workshop%20PP%20%20&%20Misc%20Papers%20Adobe%202006/8%20Gas%20Transfer/Degassing/CO2%20Control.pdf). The proposed standard condition for CO2 transfer testing is 20 C, 1 atm, 20 mg/kg CO2, mole fraction 0.000285 (Colt, Watten et al., "Carbon dioxide stripping in aquaculture - part II", *Aquacultural Engineering*, USGS record). — [USGS record, CO2 stripping part II](https://pubs.usgs.gov/publication/70043555). Tier_1, confidence medium (abstract only).

### Inferences
- **Equations for the model** (T in K, log = log10). This is the Plummer & Busenberg (1982) Table form as implemented in WATEQ4F/PHREEQC. **The coefficients were recalled, not read from a fetched page.** The check: they reproduce the WATEQ4F 25 C values exactly (pK1 6.352 vs 6.35, pK2 10.329 vs 10.329, log KH -1.468 vs -1.468). Verify against the original paper or phreeqc.dat before adopting them as canon.
  - log K1 = -356.3094 - 0.06091964 T + 21834.37/T + 126.8339 log T - 1684915/T^2
  - log K2 = -107.8871 - 0.03252849 T + 5151.79/T + 38.92561 log T - 563713.9/T^2
  - log KH = 108.3865 + 0.01985076 T - 6919.53/T - 40.45154 log T + 669365/T^2   (KH in mol L^-1 atm^-1)
- **Computed values** (local calculation from the equations above; air-equilibrium CO2 at 420 ppm, 1 atm, ignoring water-vapour correction of about -3%):

| T (C) | pK1 | pK2 | -log KH | CO2* at air eq. (mg/L) |
|---|---|---|---|---|
| 20 | 6.382 | 10.376 | 1.407 | 0.72 |
| 22 | 6.369 | 10.356 | 1.432 | 0.68 |
| 25 | 6.352 | 10.329 | 1.468 | 0.63 |
| 28 | 6.337 | 10.304 | 1.502 | 0.58 |
| 30 | 6.328 | 10.288 | 1.524 | 0.55 |

- The Sander KH (0.034 mol/L/atm at 25 C) gives 0.034 x 420e-6 x 44010 mg/mol = 0.63 mg/L. This agrees with the table above.
- **pH = pK1 + log10([HCO3-]/[CO2*])** is valid when carbonate alkalinity is about equal to [HCO3-]. That holds at roughly pH 6-8.3, below which H+ matters and above which CO3^2- and OH- matter. In low-alkalinity water (<20 mg/L) or at pH <6, the full charge balance is needed. With carbonate alkalinity in eq/L, [HCO3-] ≈ Alk(mg/L CaCO3)/50040.
  - **Check, culture tank:** 40 mg/L CO2 (0.909 mM) and 100 mg/L alkalinity (2.0 mM HCO3-) give pH = 6.35 + log(2.0/0.909) = 6.69. The course table gives 6.8. The ~0.1 difference is plausibly from activity coefficients, temperature or an unstated basis.
  - **Check, stripper effluent:** 13.6 mg/L CO2 gives 7.16 vs 7.2.
  - So H-H with concentration-based pK1 can be about 0.05-0.1 pH units low. An activity correction (Davies equation) is worth including.
- Ionic strength in aquaponics (EC ~0.5-1.5 mS/cm) shifts the apparent pK1 down by about 0.05-0.1. This is a general-chemistry inference; no fetched value supports it.

### Gaps
- The full text of Plummer & Busenberg (1982) Table 2 and the Stumm & Morgan (1996) page numbers were not retrieved.
- No fetched source gives the conditional pK1 at aquaponic ionic strength.

## Q4. Fish CO2 production: RQ, O2 per kg feed, CO2 per kg feed; CO2 from nitrification and solids decay

### Takeaway
Fish produce about 1 mol CO2 per mol O2, which is 1.375-1.38 g CO2 per g O2. Fish consume 0.25-0.5 kg O2 per kg feed, so they produce about 0.34-0.69 kg CO2 per kg feed (0.55 at 0.4 kg O2/kg feed). Nitrification adds 5.85 g CO2 per g N. Heterotrophic assimilation with carbohydrate adds 9.65 g CO2 per g N.

### Cited Findings
- "1 mol CO2 per mol O2 consumed", i.e. 1.38 g CO2/g O2. O2 consumption is 0.25-0.5 kg O2/kg feed (worked example 0.4). CO2 production is about 0.55 kg CO2/kg feed, from the example of 100 kg feed/d giving 55.2 kg CO2/d. — [Watten et al. course notes / Vinci et al. 1998 NRAES](https://ag.arizona.edu/azaqua/ista/ISTA7/RecircWorkshop/Workshop%20PP%20%20&%20Misc%20Papers%20Adobe%202006/8%20Gas%20Transfer/Degassing/CO2%20Control.pdf). Suggested tier_2 (course material reflecting the Timmons & Ebeling textbook), confidence medium-high. The RQ = 1 assumption is standard, but the 0.25-0.5 range is generic RAS, not tilapia-specific.
- Nitrification produces 5.85 g CO2 per g N. Heterotrophic glucose-driven assimilation produces 9.65 g CO2 per g N. — [Ebeling et al. 2006](https://ag.arizona.edu/azaqua/ista/ISTA7/RecircWorkshop/Workshop%20PP%20%20%26%20Misc%20Papers%20Adobe%202006/7%20Biofiltration/Microbial%20Floc%20Systems/2006%20Aquaculture%20Stoichiometry%20of%20photo-auto-hetero%20-%20Ebeling.pdf). Tier_1, confidence high.
- Measured tilapia MO2 at 26 C was 87.02 mg O2/kg/h under control conditions. — [Hamad et al. 2024, *Aquaculture* 590:741038, DOI 10.1016/j.aquaculture.2024.741038](https://pure.au.dk/ws/files/451434507/1-s2.0-S004484862400499X-main.pdf). Tier_1, confidence high for those test conditions (lab respirometry, not production RAS).

### Inferences
- **Model:** CO2_fish [g/d] = 1.375 x O2_fish [g/d], with O2_fish = (0.25-0.5) x feed [g/d]. Central value: about 0.55 kg CO2/kg feed.
- **CO2 from nitrifying TAN:** per kg of 35% protein feed with about 0.03 kg TAN/kg feed, 0.03 x 5.85 ≈ 0.18 kg CO2/kg feed. The 0.092 x protein fraction TAN rule is from Timmons & Ebeling and was not fetched here, so the TAN yield is an unverified assumption.
- Note that bicarbonate consumed in nitrification is converted to CO2 (1.86 mol CO2 per mol N in Eq. 14). Part of this is the HCO3- -> CO2 shift that lowers pH, not new carbon.
- CO2 from heterotrophic decay of solids or uneaten feed is not quantified in any fetched source. A COD-based approach (about 1.375 g CO2 per g O2 of BOD) is a reasonable analogue but is an inference.

### Gaps
- No tilapia-specific kg O2/kg feed figure was found from a primary source. Timmons & Ebeling give feed-based O2 values but were not accessed.
- No source was found for CO2 from solids mineralisation in media beds.

## Q5. CO2 removal: degassing, KLa ratio, steady-state CO2, tilapia CO2 tolerance

### Takeaway
KLa(CO2) ≈ 0.90 x KLa(O2) in theory. Measured ratios are 74-96% of that at about 130 mg/L alkalinity, and lower at very high alkalinity. Packed or cascade strippers remove about 60-89% per pass. Tilapia CO2 guidance varies: SRAC gives <20 mg/L, the Cornell/NRAES course gives an operational limit of about 60 mg/L, and metabolic depression is measurable from about 5-10 mg/L.

### Cited Findings
- Aitchison, T.F., Timmons, M.B., Bisogni, J.J. Jr., Piedrahita, R.H. & Vinci, B.J. (2007), "Using oxygen gas transfer coefficients to predict carbon dioxide removal", *International Journal of Recirculating Aquaculture* 8(1), DOI 10.21061/ijra.v8i1.1416. The theoretical φT = KLa(CO2)/KLa(O2) = 0.90. The measured φE/φT was 96% (high-exposure surface aerator) and 74% (moderate) at about 130 mg/L alkalinity. It fell to 0.84 and 0.51 at about 1,000 mg/L alkalinity. The test used a 10,000 L tank. — [Aitchison et al. 2007 (VTechWorks)](https://vtechworks.lib.vt.edu/items/eccf9efa-1aa4-4141-b27c-c5128563d910/full). Tier_1, confidence medium-high: peer-reviewed, single study, test temperature not reported.
- Moran, D. (2010), "Carbon dioxide degassing in fresh and saline water I: degassing performance of a cascade column", *Aquacultural Engineering* 43(1):29-36, DOI 10.1016/j.aquaeng.2010.05.001. A 1.7 m cascade column at 15 C with influent CO2 of 10-60 mg/L gave 67-89% removal per pass. Efficiency rose with influent CO2, and countercurrent air did not improve it. — [Moran 2010 (LUP record)](https://lup.lub.lu.se/record/1981410). Tier_1, confidence high (abstract).
- Stripping towers work at G:L ratios of 1-20. Example: 1 m packing, G:L 10, 40 mg/L influent gave about 66% removal. Removal gains flatten beyond about 1 m of packing. Higher CO2 in the stripping gas cuts removal: about 60% at 1,000 ppm vs 20% at 5,000 ppm. The example culture tank runs at 40 mg/L. The operational limit is about 60 mg/L for tilapia and striped bass and 9-30 mg/L for trout. — [Watten et al. course notes](https://ag.arizona.edu/azaqua/ista/ISTA7/RecircWorkshop/Workshop%20PP%20%20&%20Misc%20Papers%20Adobe%202006/8%20Gas%20Transfer/Degassing/CO2%20Control.pdf). Tier_2, confidence medium.
- Treating CO2 as non-reactive in packed columns is reasonable for cold acidic water but not for warm alkaline water, because HCO3- -> CO2 conversion during passage matters. — [Colt/Watten et al., CO2 stripping part II (USGS record)](https://pubs.usgs.gov/publication/70043555). Tier_1, abstract only.
- SRAC 452: fish begin to stress above 20 ppm CO2, and the recommendation is <20 ppm. pH target 7.0-8.0, with action at pH <6.8. Nitrifiers are inhibited below pH 6. — [SRAC 452](https://www.srac.msstate.edu/pdfs/Fact%20Sheets/452%20Recirculating%20Aquaculture%20Tank%20Production%20Systems-%20Management%20of%20Recirculating%20Systems.pdf). Tier_2, confidence medium (generic, not tilapia-specific).
- Hamad, Damsgaard, Munubi & Skov (2024), *Aquaculture* 590:741038, Nile tilapia at 26 C:
  - Progressive CO2 ramp: MO2 fell about 10% at 5 mg/L and about 30% at 60 mg/L.
  - 1 h exposure: SMR fell 11/22/29% at 10/30/60 mg/L.
  - 24 h exposure: SMR stayed depressed by 10/16/28%.
  - Blood pH fell by up to 0.52 at 60 mg/L, and only the 10 mg/L group fully recovered intracellular pH.
  - Growth was not measured. The paper cites a CO2 field range of 10-15 mg/L in early-morning ponds (Hargreaves & Brunson 1996).
  — [Hamad et al. 2024](https://pure.au.dk/ws/files/451434507/1-s2.0-S004484862400499X-main.pdf). Tier_1, confidence high for physiology. It does not establish a growth threshold.
- **Disagreement:** SRAC gives <20 mg/L and the NRAES course gives ~60 mg/L as the "operational limit" for tilapia. Hamad et al. show metabolic effects at ≥10 mg/L. These are different endpoints (stress guideline vs operational tolerance vs physiology), so treat them as context_split rather than a contradiction.

### Inferences
- **Model:** dCO2/dt (stripping) = KLa_CO2 x (CO2* - CO2_eq). Set KLa_CO2 = φ x KLa_O2 with φ = 0.90 x (0.74-0.96), i.e. about 0.67-0.86 at aquaponic alkalinities of about 100-150 mg/L.
- Steady state: CO2_ss = CO2_eq + P_CO2 / (KLa_CO2 x V).
- Aquaponic DWC raft channels with diffused air, and media beds that flood and drain, both act as degassers. No KLa values for these specific components were found.

### Gaps
- No fetched source reports measured steady-state dissolved CO2 in coupled tilapia aquaponics (for example UVI). This is a key gap.
- No KLa for DWC air-stone channels or for bell-siphon media beds.

## Q6. Base stoichiometry (alkalinity as CaCO3 per g of chemical)

### Takeaway
The figures below come from molar masses and equivalents (1 eq alkalinity = 50.04 g CaCO3). They are standard chemistry, not quoted from a fetched page. Hydroxides consume dissolved CO2 (OH- + CO2 -> HCO3-), carbonates consume half as much per equivalent, and bicarbonates leave CO2 unchanged.

### Cited Findings
- SRAC 452: dose sodium bicarbonate at 17-20% of daily feed mass, about 0.17-0.20 kg NaHCO3 per kg feed per day. Example: about 2 lb NaHCO3 for 10 lb feed per day. — [SRAC 452](https://www.srac.msstate.edu/pdfs/Fact%20Sheets/452%20Recirculating%20Aquaculture%20Tank%20Production%20Systems-%20Management%20of%20Recirculating%20Systems.pdf). Tier_2, confidence medium.
- SRAC 454 (Rakocy, Losordo & Masser 1992): in integrated systems, potassium hydroxide and calcium oxide or hydroxide "must be added daily to maintain the pH of the system near 7". No amounts are given. Lettuce:tilapia feeding ratio is 2.4 g feed/plant/day (stated as "3.2 g/m3/m2", unit as printed). — [SRAC 454](https://cales.arizona.edu/azaqua/extension/Classroom/SRAC/454fs.pdf). Tier_2, confidence high for practice, no dose numbers.
- Loyless, J.C. & Malone, R.F. (1997), "A sodium bicarbonate dosing methodology for pH management in freshwater-recirculating aquaculture systems", *Progressive Fish-Culturist* 59(3):198-205, DOI 10.1577/1548-8640(1997)059<0198:ASBDMF>2.3.CO;2 (volume, issue and DOI from the URL; pages from the DOI string). Per the abstract, sodium bicarbonate is preferred for cost, solubility and safety. Measured pH and alkalinity are used to back-calculate CO2, then the alkalinity needed to reach the target pH. Dosage tables are given by system size, and charts show when extra CO2 stripping is needed. — [Loyless & Malone 1997 abstract](https://informahealthcare.com/doi/abs/10.1577/1548-8640%281997%29059%3C0198%3AASBDMF%3E2.3.CO%3B2). Tier_1, confidence medium (abstract only).

### Inferences
- Alkalinity added per g of chemical, as g CaCO3 equivalent (computed):

| Chemical | M (g/mol) | eq/mol | g CaCO3 per g | CO2 consumed per eq |
|---|---|---|---|---|
| KOH | 56.11 | 1 | 0.892 | 1 mol CO2 (OH- + CO2 -> HCO3-) |
| NaOH | 40.00 | 1 | 1.251 | 1 |
| Ca(OH)2 | 74.09 | 2 | 1.351 | 1 |
| CaO | 56.08 | 2 | 1.785 | 1 |
| CaCO3 | 100.09 | 2 | 1.000 | 0.5 (CO3^2- + CO2 + H2O -> 2 HCO3-) |
| K2CO3 | 138.21 | 2 | 0.724 | 0.5 |
| KHCO3 | 100.12 | 1 | 0.500 | 0 |
| NaHCO3 | 84.01 | 1 | 0.596 | 0 |

- **Consequence for the pH model.** Hydroxide dosing raises pH both by adding alkalinity and by lowering CO2*. In a CO2-limited system, KOH or Ca(OH)2 therefore gives a larger instantaneous pH jump than an equal-equivalent NaHCO3 dose.
- **Cross-check of SRAC's NaHCO3 dose against nitrification stoichiometry.** 0.17-0.20 kg NaHCO3/kg feed is about 0.10-0.12 kg CaCO3-eq/kg feed. That would replace nitrification losses for about 0.014-0.017 kg TAN-N/kg feed at 7.05 g/g. This is about half the TAN yield of a 35%-protein feed under the unverified 0.092 x PC rule. So either effective TAN per kg feed is lower, or the SRAC dose is a floor. Flag this for review.

### Gaps
- No fetched source gives measured daily KOH or Ca(OH)2 doses per kg feed in tilapia aquaponics (for example UVI records).

## Q7. Published dynamic pH/alkalinity/CO2 models of RAS or aquaponics

### Takeaway
The fetched literature contains no full open dynamic pH/alkalinity model for coupled aquaponics. Loyless & Malone (1997) is a steady-state dosing method built on carbonate equilibria. The Vinci et al. (1998) NRAES "CO2 Control" model is the RAS CO2 stripping design tool. Körner et al. (2017) models greenhouse-aquaponics energy, not water chemistry.

### Cited Findings
- **Loyless & Malone (1997):** a pH-and-alkalinity -> CO2 -> required alkalinity dosing method for RAS with hydraulic retention time over about 5 days. — [abstract](https://informahealthcare.com/doi/abs/10.1577/1548-8640%281997%29059%3C0198%3AASBDMF%3E2.3.CO%3B2). Tier_1, medium.
- **Vinci, Timmons, Summerfelt & Watten (1998), *Carbon Dioxide Control in Intensive Aquaculture* (v2.1), NRAES, Cornell:** a spreadsheet design model that combines CO2 production from feed (RQ), tank and makeup water carbonate equilibrium (CT, alkalinity, pH), and packed-tower stripping (G:L, packing depth, stripping-gas CO2). — [course notes](https://ag.arizona.edu/azaqua/ista/ISTA7/RecircWorkshop/Workshop%20PP%20%20&%20Misc%20Papers%20Adobe%202006/8%20Gas%20Transfer/Degassing/CO2%20Control.pdf). Tier_2, medium.
- **Colt, Watten et al., "Carbon dioxide stripping in aquaculture" parts I-III** (terminology, gas-transfer models, verification), *Aquacultural Engineering*, USGS records. Abstract only. — [Part II](https://pubs.usgs.gov/publication/70043555); [Part III](https://pubs.usgs.gov/publication/70043572). Tier_1, low-medium (not read in full).
- **Körner, O., Gutzmann, E. & Kledal, P.R. (2017), "A dynamic model simulating the symbiotic effects in aquaponic systems", *Acta Horticulturae* 1170:309-316, DOI 10.17660/ActaHortic.2017.1170.37:** greenhouse climate plus RAS tilapia model (700-3,000 kg peak biomass). The abstract mentions no pH, alkalinity or water-CO2 chemistry. Energy saving is about 41 MJ m^-2 K^-1 yr^-1 of pond temperature. — [AGRIS record](https://agris.fao.org/search/en/records/65deacef63b8185d9ca90298). Tier_1, high for what it covers.
- **Goddek et al. (2019) ch. 8:** decoupled-system modelling at nutrient and water-balance level, with pH treated only qualitatively. — [Springer](https://link.springer.com/content/pdf/10.1007/978-3-030-15943-6_8.pdf). Tier_1.

### Inferences
- **Suggested minimal daily model structure**, built from the cited stoichiometry. State variables are Alk (eq) and C_T (mol); pH is solved each step from Alk, C_T and K1(T), K2(T).
  - **dAlk/dt** = -2·N_nitrif(1 - 0.0244·…) [use 7.05 g CaCO3/g N] - 1·N_het + f_NO3·N_plantNO3 + base dose eq - exchange·(Alk - Alk_makeup)
  - **dC_T/dt** = CO2_fish + CO2_nitrif(net 1.86 - 1.97 + C fixed) + CO2_het + base carbonate C - KLa_CO2·V·(CO2* - CO2_eq) - exchange·(C_T - C_T,makeup)
  - with CO2* = C_T·α0(pH, T).
- Alkalinity enters as eq and is conserved through the CO2 exchange, because degassing changes C_T but not Alk. This is why CO2 stripping raises pH without changing alkalinity, a standard result consistent with the Vinci et al. tables (alkalinity 100 mg/L constant while pH rises 6.8 -> 7.2 across the stripper).

### Gaps
- No open-source aquaponics model with an explicit carbonate-system module was found within the fetch budget.
- Summerfelt's and Colt's full-text CO2 mass-balance papers were not read.
- No calibration data (daily base dose, pH, alkalinity time series) from a coupled tilapia-basil/lettuce system was found.
