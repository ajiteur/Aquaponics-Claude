# Source-water alkalinity, hardness and pH: Netherlands and South India (make-up water for aquaponics)

Conventions used below (my arithmetic, not from the sources):
- Alkalinity as CaCO3 (mg/L) = HCO3- (mg/L) x 0.820 (50.04/61.02), valid near pH 7-8.5 where carbonate is negligible.
- Hardness: 1 mmol/L = 100.1 mg/L as CaCO3 = 5.61 °dH; 1 °dH = 17.85 mg/L as CaCO3.
- Suggested tiers follow the brief: tier_1 = official statistics / peer-reviewed, tier_2 = extension / reputable grey literature, tier_3 = commercial / anecdotal.
- About 28 web fetches were used. The CGWB (cgwb.gov.in) and faolex hosts could not be fetched (robots/proxy errors), so the CGWB Ground Water Year Books are **not** summarised here.

## Q1. Netherlands: drinking-water bicarbonate, hardness, pH by supplier, and the Drinkwaterbesluit limits

### Takeaway
Dutch tap water is moderately buffered. Bicarbonate is typically about 115-190 mg/L HCO3- (about 95-155 mg/L as CaCO3), hardness about 1.1-1.75 mmol/L (6-10 °dH) and pH about 7.8-8.7 at the suppliers sampled. Some soft-water sources sit near the legal minimum of 60 mg/L HCO3- (about 49 mg/L as CaCO3). The Drinkwaterbesluit sets HCO3- > 60 mg/L, pH 7.0-9.5, SI > -0.2, and hardness > 1.0 mmol/L where softening is used.

### Cited Findings
**Legal limits (Drinkwaterbesluit 2011, Bijlage A, Tabel IIIa, as quoted by suppliers and KWR)**
- HCO3- > 60 mg/L (minimum); pH 7.0 < pH < 9.5; saturation index (SI, CaCO3) > -0.2 as an annual average; total hardness > 1 mmol/L (> 5.6 °dH). Waternet's Leiduin 2022 report lists these as the legal norms. — [Waternet / Het Waterlaboratorium, 2023, "Jaaroverzicht 2022, Productielocatie Leiduin"](https://www.waternet.nl/siteassets/ons-water/drinkwater/drinkwater-leiduin-2022.pdf). Tier_1 (statutory report by a utility), confidence high, corroborated by Dunea and Vitens reports and KWR (below).
- The hardness norm applies only where softening (ontharding) or desalination is used, and is tested on the 90th percentile. — [Slaats, Meerkerk, Palmen (KWR) & Brink (WMD), 2015, "Conditionering van drinkwater: de aanbevelingen voor optimale samenstelling in 2014", H2O-Online, 9 Jan 2015, Table 1](https://api.kwrwater.nl//uploads/2017/02/Slaats-Meerkerk-Palmen-Brink-Conditionering-van-drinkwater-de-aanbevelingen-voor-optimale-samenstelling-in-2014-H2O-Online-(2015)-9-januari.pdf). Tier_2 (sector research institute, trade journal), confidence medium: the fetched table was partly garbled. Corroborated by the Vitens footnote.
- The water sector's own recommendations (not law): pH > 7.4, TAC > 2 mmol/L, SI > -0.2, total hardness < 1.8 mmol/L (Table 2). After softening, hardness should not drop below 1.0 mmol/L. — [Slaats et al. 2015, Table 2](https://api.kwrwater.nl//uploads/2017/02/Slaats-Meerkerk-Palmen-Brink-Conditionering-van-drinkwater-de-aanbevelingen-voor-optimale-samenstelling-in-2014-H2O-Online-(2015)-9-januari.pdf). Tier_2, confidence medium, single source.

**Supplier data**

| Supplier / site | Period | pH min-avg-max | HCO3- mg/L min-avg-max (≈ as CaCO3) | Total hardness mmol/L (°dH) | Ca mg/L | Mg mg/L | Source |
|---|---|---|---|---|---|---|---|
| Waternet, Leiduin (Amsterdam, dune-infiltrated Rhine water) | 2022 | 7.76-8.08-8.40 | 160-175-188 (131-143-154) | 1.20-1.37-1.55 (6.7-7.7-8.7) | 34.2-39.6-45.5 | 8.2-9.3-10.2 | [Waternet 2023, Jaaroverzicht 2022 Leiduin](https://www.waternet.nl/siteassets/ons-water/drinkwater/drinkwater-leiduin-2022.pdf) |
| Waternet (all customers) | current web page | n/a | n/a | 1.40 (7.8 °dH), down from 8.4 °dH before 2015 | n/a | n/a | [Waternet, "Tap water hardness"](https://www.waternet.nl/en/service-and-contact/tap-water/tap-water-hardness/) |
| Dunea, Scheveningen (The Hague region) | 2025 | 8.29-8.48-8.66 | 167-176-190 (137-144-156) | 1.29-1.42-1.74 (7.2-8.0-9.7) | 38.1-42.9-51.3 | 7.6-8.5-11.2 | [Dunea, 2026, "Scheveningen year 2025" (English)](https://www.dunea.nl/english/-/media/bestanden/home/drinkwater/waterkwaliteitsrapportages/2025-rapportages/scheveningen-year-2025-english.pdf) |
| Vitens, report file "WZ_MPb-Hoenderloo" (Veluwe; the site name is not printed in the document) | Jan-Jun 2025, n=27 | 7.83-7.92-8.02 | 116-126-132 (95-103-108) | 1.14-1.22-1.32 (6.4-6.8-7.4) | 39.4-41.7-45.3 | 3.8-4.3-4.8 | [Vitens Waterexpertisecentrum, 2025, Waterkwaliteitsoverzicht WZ_MPb-Hoenderloo](https://www.vitens.nl/-/media/Project/Vitens/VitensNl/Service/Waterkwaliteitsoverzicht/WZ_MPb-Hoenderloo.PDF) |
| Vitens, Pinkenberg pumping station | 2017 | n/a | 59-66-77 (48-54-63); 2 results below the norm | n/a | n/a | n/a | [ILT, 2018, "Kwaliteit drinkwater van Nederlandse drinkwaterbedrijven 2017", Bijlage A p. 22](https://www.ilent.nl/binaries/ilt/documenten/leefomgeving-en-wonen/drinkwater/drinkwater/rapporten/kwaliteit-drinkwater-van-nederlandse-drinkwaterbedrijven-2017/Kwaliteit+drinkwater+van+Nederlandse+drinkwaterbedrijven+2017.pdf) |
| Vitens, Leersum distribution | 2017 | n/a | 59-67-80 (48-55-66); 1 result below the norm | n/a | n/a | n/a | [ILT 2018, p. 23](https://www.ilent.nl/binaries/ilt/documenten/leefomgeving-en-wonen/drinkwater/drinkwater/rapporten/kwaliteit-drinkwater-van-nederlandse-drinkwaterbedrijven-2017/Kwaliteit+drinkwater+van+Nederlandse+drinkwaterbedrijven+2017.pdf) |
| WML, purchased water "Inkoop Enwor (WdKA)" | 2017 | n/a | 40-47-60 (33-39-49); all 5 below the norm | n/a | n/a | n/a | [ILT 2018, p. 24](https://www.ilent.nl/binaries/ilt/documenten/leefomgeving-en-wonen/drinkwater/drinkwater/rapporten/kwaliteit-drinkwater-van-nederlandse-drinkwaterbedrijven-2017/Kwaliteit+drinkwater+van+Nederlandse+drinkwaterbedrijven+2017.pdf) |
| PWN, Heemskerk distribution | 2017 | 6.74-8.12-8.96 (n=466, 1 result outside the norm) | n/a | n/a | n/a | n/a | [ILT 2018, p. 21](https://www.ilent.nl/binaries/ilt/documenten/leefomgeving-en-wonen/drinkwater/drinkwater/rapporten/kwaliteit-drinkwater-van-nederlandse-drinkwaterbedrijven-2017/Kwaliteit+drinkwater+van+Nederlandse+drinkwaterbedrijven+2017.pdf) |
| WML, regular vs back-up supply | 2013 | n/a | 160 regular, 335 back-up (131 / 275) | 2.1 regular, 2.8 back-up | n/a | n/a | [Palmen (KWR), 2015, "De hardheid van drinkwater: hoe hard zijn de aanbevelingen?", seminar slides, slide 18](https://edepot.wur.nl/397017) |
| Untreated hard groundwater (model example) | n/a | 7.3 raw | 345 raw (283) | 3.7 raw | n/a | n/a | [Palmen 2015, slide 19](https://edepot.wur.nl/397017). Computed AquaCalc example, not measured |

Reliability per row:
- Waternet, Dunea and Vitens rows: tier_1 (utility statutory monitoring), confidence high (directly reported min/avg/max). Each is single-site, but the ranges for HCO3-, hardness and pH agree with each other.
- ILT rows: tier_1 (national regulator, the Human Environment and Transport Inspectorate), confidence high for the values. The data are old (2017) and only exceedance rows are listed.
- National totals for 2017: 8 HCO3- results below the norm out of 9,985 measurements, and 1 pH result outside the norm out of 31,991. — [ILT 2018, Tabel 4, p. 15](https://www.ilent.nl/binaries/ilt/documenten/leefomgeving-en-wonen/drinkwater/drinkwater/rapporten/kwaliteit-drinkwater-van-nederlandse-drinkwaterbedrijven-2017/Kwaliteit+drinkwater+van+Nederlandse+drinkwaterbedrijven+2017.pdf). Tier_1, high.
- Palmen 2015 rows: tier_2 (slides), confidence medium.
- National average hardness is about 8 °dH (≈1.4 mmol/L). — [Waternet, "Tap water hardness"](https://www.waternet.nl/en/service-and-contact/tap-water/tap-water-hardness/). Tier_2 (utility web page, not a statistic), confidence medium, single source.
- The Vewin "Drinkwaterstatistieken 2022" extract that was fetched had no per-company hardness, HCO3- or pH table. Section 4.1 (p. 80) and Bijlage 2 (p. 158) were not reached. — [Vewin 2022](https://vewin.nl/wp-content/uploads/2024/06/vewin-drinkwaterstatistieken-2022-nl-web.pdf).

### Inferences
- For make-up water, Dutch tap water typically supplies about 95-155 mg/L alkalinity as CaCO3. This is near or above common aquaponics alkalinity targets, so routine base dosing could be lower than with soft water, depending on nitrification acid production. This needs checking against the project's canonical targets.
- Soft-water areas (parts of the Vitens Veluwe/Utrecht area, some WML purchased water) can deliver only about 40-65 mg/L as CaCO3.
- Supplier water varies by production site. A farm should use the specific pumping-station report for its postcode rather than a national number.
- Ca is roughly 35-50 mg/L and Mg 4-11 mg/L across the sampled sites. The Ca:Mg ratio differs between Vitens groundwater (Mg ~4 mg/L) and the dune/river sources (Mg ~8-11 mg/L).
- Rainwater would add near-zero alkalinity and hardness. **No source fetched for this; gap.** This is general chemistry knowledge, not a cited value.

### Gaps
- The exact Drinkwaterbesluit Tabel IIIa wording, including whether a **maximum** hardness of 2.5 mmol/L exists, was not verified: the faolex copy was truncated before Tabel IIIa. Suppliers' reports show only "> 1 mmol/L". Treat "1.0-2.5 mmol/L" as unverified.
- Not fetched: Evides, PWN (full parameters), Brabant Water, Oasen, WML current reports, and Vitens sites by name. No single national per-company table was found.
- No source on Dutch private groundwater or borewell (eigen winning) alkalinity was fetched.
- No measured data on Dutch rainwater alkalinity or pH.

## Q2. India: BIS IS 10500:2012 limits

### Takeaway
IS 10500:2012 sets acceptable/permissible limits (the permissible value applies in the absence of an alternate source) of 200/600 mg/L as CaCO3 for total alkalinity and total hardness, 75/200 mg/L for Ca and 30/100 mg/L for Mg. pH must be 6.5-8.5, with no relaxation.

### Cited Findings
- pH 6.5-8.5, no relaxation (Table 1, Sl iii). Total alkalinity as CaCO3: 200 acceptable, 600 permissible (Table 2, Sl xxii). Total hardness as CaCO3: 200 / 600 (Table 2, Sl xxiii). Calcium: 75 / 200 (Table 2, Sl vi). Magnesium: 30 / 100 (Table 2, Sl xiii). Second Revision, May 2012. Amendment No. 2 (Sept 2018) does not change these parameters. — [Bureau of Indian Standards, 2012, IS 10500:2012 Drinking Water – Specification (Second Revision)](https://consumerhelpline.gov.in/public/assets/docs/bis/IS10500-2012.pdf). Tier_1 (national standard), confidence high, corroborated by many state copies (for example [BIS copy](https://www.bis.gov.in/other/DrinWatIS10500.pdf)), which were not fetched.

### Inferences
- The BIS acceptable limit for alkalinity (200 mg/L as CaCO3) is above typical aquaponics targets. Water that is fit to drink in India can therefore still be strongly alkaline for aquaponics.
- Note that Gulgundi & Shetty (below) cite a hardness "desirable" limit of 300 mg/L. That is the older IS 10500:1991 value, so check which edition a paper uses.

### Gaps
- None for the standard itself.

## Q3. India: measured groundwater/borewell and municipal values (Bengaluru, Chennai, Hyderabad, AP/Telangana, Karnataka, Tamil Nadu)

### Takeaway
Hard-rock (granite-gneiss) groundwater in South India is typically hard and well buffered. Bengaluru borewells show HCO3- of about 88-530 mg/L and hardness of 48 to more than 1,800 mg/L. Chennai (Anna Nagar) borewells show HCO3- of 18-360 mg/L and hardness of 90-815 mg/L. Hyderabad-fringe and Telangana wells show hardness of about 200-820 mg/L. Coastal AP (Prakasam) shows HCO3- of 480-1,025 mg/L. Spread between wells is very large, so site testing is essential. Municipal surface-water supplies (Cauvery, Krishna) are likely much softer. No published utility values were found, only BIS pass/fail tests.

### Cited Findings
**Groundwater (peer-reviewed)**

| Area | Samples / date | pH | HCO3- or TA mg/L (≈ as CaCO3) | TH mg/L | Ca mg/L | Mg mg/L | Source |
|---|---|---|---|---|---|---|---|
| Western half of Bengaluru city (241 km²) | 67 wells x 2 seasons, Mar & Nov 2014 | 6.07-8.13 pre; 5.8-7.7 post | "HCO3 (alkalinity)": 88-505 pre, 92-530 post (if HCO3-: ≈72-434) | 48-1784 pre; 50-1873 post | 6-312 / 6-316 | 8-3244 (likely typo) / 8-268 | [Gulgundi & Shetty, 2018, "Groundwater quality assessment of urban Bengaluru using multivariate statistical techniques", Applied Water Science 8:43](https://link.springer.com/10.1007/s13201-018-0684-z) |
| Anna Nagar, Chennai | 24 borewells, 80-150 m deep; date not stated | 6.0-8.2 | HCO3- 18.3-359.9 (≈15-295) | 89.5-814.6 (mean 211.6) as CaCO3 | 26-130 | 1.2-141.6 | [Krishna kumar, Logeshkumaran, Magesh, Godson & Chandrasekar, 2015 (online 2014), "Hydro-geochemistry and application of water quality index (WQI) for groundwater quality assessment, Anna Nagar, part of Chennai City", Applied Water Science 5:335-343](https://link.springer.com/article/10.1007/s13201-014-0196-4) |
| Jawaharnagar dumpsite, Ranga Reddy district (Hyderabad fringe), Telangana | 10 borewells, monthly May 2015-May 2016 | 7.2-7.8 | Total alkalinity 222-427 (unit basis not stated in the extract) | 420-584 | 115-140 | 55-115 | [Unnisa & Zainab Bi, 2017, "Groundwater quality characterization around Jawaharnagar open dumpsite, Telangana State", Applied Water Science 7:3911-3918](https://link.springer.com/10.1007/s13201-017-0544-2) |
| Subledu Basin, Khammam district, Telangana | 22 hand pumps, May 2019 | 7.53-8.35 (mean 8.09) | not in extract | 200-820 (mean 439) | 16-112 (mean 45.8) | 15-165 (mean 78.9) | [Narasaiah & Venkateswara Rao, 2021, "Groundwater quality of an hard rock aquifer in the Subledu Basin of Khammam district, India", Applied Water Science 11:89](https://link.springer.com/article/10.1007/s13201-021-01424-2) |
| Part of Prakasam district, Andhra Pradesh (325 km²) | 30 wells, summer 2012 | 7.2-8.3 (mean 7.81) | HCO3- 480-1025, mean 731 (≈394-841, mean 600) | not in extract | 55-90 (mean 65.7) | 42-105 (mean 76.9) | [Subba Rao, 2018, "Groundwater quality from a part of Prakasam District, Andhra Pradesh, India", Applied Water Science 8:30, Table 1](https://link.springer.com/article/10.1007/s13201-018-0665-2) |

Reliability:
- All five are tier_1 (peer-reviewed, Springer Applied Water Science, open access).
- Confidence is medium for each: values come from the article text, not the Table 1 bodies (which were not visible), and each study is local and small.
- Bengaluru: the Mg maximum of 3,244 mg/L looks like a typo. The alkalinity basis (HCO3- vs CaCO3) is ambiguous.
- Chennai: sampling date unknown.
- Jawaharnagar: the site is near a landfill and probably not representative.
- Prakasam: the paper reports inconsistent pH and Mg ranges between its own sections.
- Corroboration: the studies are qualitatively consistent (hard, high-alkalinity hard-rock groundwater), but no two cover the same area, so each figure is **single_source**.

**Municipal piped water (official, pass/fail only)**
- In BIS tests of 10 piped drinking-water samples per city, against 44 parameters (late 2019):
  - **Bengaluru**: all 10 non-conforming, mainly for aluminium, turbidity and coliform. Calcium failed only at Jalahalli West. No hardness, alkalinity or pH failures.
  - **Chennai**: all 10 non-conforming. Total hardness failed at Perambur and Kolathur, TDS at most sites. No alkalinity or pH failures.
  - **Hyderabad**: 9 of 10 conformed. The only failure was phenolics.
  - **Amaravati (AP)**: total alkalinity and total hardness failed at Penamaluru, Gudavalli (Gannavaram) and Ballemvari Veedi. Total alkalinity also failed at Uyyuru.
  - No numeric values are given.
  - — [Bureau of Indian Standards / Ministry of Consumer Affairs, c. Nov 2019, "Report of Testing of Piped Drinking Water Samples from 20 Capital Cities and Delhi"](https://www.bis.gov.in/wp-content/uploads/2019/11/Drinking_Water_20112019.pdf). Tier_1 (official), confidence medium (10 grab samples per city, pass/fail only), single source.

**Surface-water source context (CWC)**
- For Cauvery basin river water, the only station summary reached was Gopurajapuram on the Puravidaiyanar, a Cauvery delta distributary near Karaikal (Puducherry UT, not Tamil Nadu), with n=3, June 2017-May 2018:
  - pH 6.9-8.5 (mean 7.5)
  - total alkalinity 21-51 (mean 38) mg/L as CaCO3
  - total hardness 28-60 (mean 44) mg/L as CaCO3
  - Ca 5-11 mg/L, Mg 3.9-7.8 mg/L
  - — [Central Water Commission, 2019, "Water Year Book Vol. II: Water Quality Data, June 2017-May 2018, Cauvery Basin", Station 3.1 p. 22](https://cwc.gov.in/sites/default/files/admin/6ACBWQYB17-18.pdf). Tier_1, confidence low as a proxy for city supply: a delta distributary with 3 samples, not the Bengaluru intake (T.K. Halli). The T.K. Halli and Kollegal tables were not reached in the fetched text.

### Inferences
- Borewell make-up water in these markets will often carry alkalinity of 150-400+ mg/L as CaCO3 and hardness of 200-800+ mg/L. Some coastal AP wells exceed 400 mg/L as CaCO3.
  - For aquaponics this usually means no base dosing is needed, but there is a risk of pH creeping high and of Ca/Mg carbonate scaling. Blending with rainwater or RO water may be needed.
  - This is an inference. Treatment needs must come from project canon and site tests.
- Cauvery-sourced BWSSB water and Krishna/Godavari-sourced HMWSSB water are probably soft and low in alkalinity, based on river chemistry. That is an inference from one CWC delta station plus the absence of hardness failures in the BIS Bengaluru and Hyderabad tests, not a measured utility value.
- Chennai piped water appears harder and higher in TDS than Bengaluru or Hyderabad water (BIS hardness failures at 2 sites). Chennai supply mixes reservoir, desalinated and groundwater sources, but that mix is not documented in the sources fetched.

### Gaps
- **CGWB Ground Water Year Books** (Karnataka 2021-22, Bangalore North NAQUIM aquifer report, Hyderabad district brochure, Telangana/AP/Tamil Nadu year books) could not be fetched (cgwb.gov.in robots unreachable). These are the main official sources for state-wide ranges and % of samples above BIS limits.
  - URLs for follow-up: [Karnataka GWYB 2021-22](https://cgwb.gov.in/old_website/Regions/SWR/Reports/GWY%20Book%20KARNATAKA%202021-2022.pdf), [Bangalore North AMP](https://cgwb.gov.in/old_website/AQM/NAQUIM_REPORT/karnataka/2022/Bangalore%20Urban%20District/Bangalore%20North%20AMP_Bangalore%20final%20with%20cov%20pg.pdf), [CGWB Hyderabad district](https://cgwb.gov.in/sites/default/files/2022-10/hyderabad.pdf).
- No numeric published utility data were found for BWSSB, CMWSSB or HMWSSB treated-water alkalinity or hardness.
- No dedicated Hyderabad-city (core urban) groundwater paper was fetched. The Telangana values are from the Hyderabad fringe (Jawaharnagar) and Khammam.
- No Tamil Nadu state-wide or Karnataka rural groundwater dataset. State pollution control board data were not found.
- Bengaluru Rural groundwater: no data.

## Q4. Rostock (Germany) and Alberta (Canada) municipal water (lower priority)

### Takeaway
No citable values were found for either.

### Cited Findings
- A search for Nordwasser (Rostock) Trinkwasser hardness and bicarbonate returned other German utilities only. No Rostock analysis page was identified. — no source.

### Inferences
- None.

### Gaps
- Rostock (Nordwasser/Eurawasser) drinking-water hardness, HCO3- and pH: not found.
- Alberta: the municipal water at Brooks (Crop Diversification Centre South, the Savidov 2005 site): not searched, because of the fetch budget.
