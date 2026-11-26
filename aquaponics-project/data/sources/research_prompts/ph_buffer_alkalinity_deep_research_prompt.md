# Deep research prompt: pH buffering and alkalinity for an aquaponics simulation

Written 2026-11-26 for ticket UQ-018 (the model has no alkalinity buffer). Claude ran this
research itself on 2026-11-26; the report is in the repo at
`aquaponics-project/data/sources/research_reports/markdown/Aquaponics pH buffer and alkalinity.md`.
Paste the prompt below into a deep research tool to re-run or extend it.

---

I am building a daily simulation of a freshwater coupled aquaponics system (Nile tilapia
with basil or lettuce; deep-water raft, NFT and gravel media beds; water 22 to 30 C;
farms in the Netherlands and South India). I need sourced values and equations to model
pH as the result of an alkalinity and CO2 balance, instead of a fixed pH drift.

Use peer-reviewed papers, textbooks of record (Timmons and Ebeling, Recirculating
Aquaculture; Stumm and Morgan, Aquatic Chemistry), official standards and statistics,
and university extension (SRAC, FAO Fisheries Technical Paper 589) first. Label grey
literature and commercial sources. Never invent a number: if you cannot find a value,
say it is a gap. For every value give the full citation (authors, year, title, journal
or publisher, DOI or URL, page, table or equation), units, context (RAS or aquaponics,
species, temperature, scale), a reliability tier (tier 1 peer-reviewed or official,
tier 2 extension or reputable grey literature, tier 3 commercial or anecdotal), a
confidence (high, medium, low) with a one-line reason, and whether a second source
corroborates it.

1. Alkalinity stoichiometry: alkalinity consumed by nitrification (about 7.07 g CaCO3 per
   g N), by heterotrophic bacterial assimilation of TAN (about 3.57 g per g N) and by
   algae; alkalinity released when plants take up nitrate versus ammonium (equivalents
   per mole N), with measured evidence from hydroponics or aquaponics.
2. Carbonate equilibrium: pK1 and pK2 of carbonic acid and Henry's constant for CO2 as
   functions of temperature; the pH = pK1 + log10(HCO3 / CO2) relation and its valid
   range; dissolved CO2 at equilibrium with the atmosphere at about 420 ppm.
3. CO2 sources and sinks: fish CO2 per g O2 consumed (respiratory quotient) and O2 per kg
   feed for tilapia; CO2 from nitrification and from solids decay; CO2 stripping by
   diffused aeration, waterfalls, trickling and media beds (KLa values, CO2 to O2 KLa
   ratio); typical dissolved CO2 in aerated tilapia RAS and aquaponics; tilapia CO2
   limits.
4. Bases: alkalinity added per gram of KOH, Ca(OH)2, CaCO3, K2CO3, KHCO3 and NaHCO3; how
   much base operating systems add per kg of feed or per day (UVI system and others);
   why NaHCO3 is avoided in aquaponics.
5. Observed data: aquaponics and RAS papers that report alkalinity or pH over time, with
   and without base dosing (Zou et al. 2016, Tyson et al. 2004 and 2008, Wongkiew et al.
   2017, Knaus and Palm 2017 and 2018, Savidov 2005, Rakocy et al.), and published dynamic
   pH, alkalinity or CO2 models of RAS or aquaponics.
6. Target pH trade-offs: tilapia optimum and tolerance; nitrification rate versus pH;
   basil and lettuce yield and nutrient availability (Fe, Mn, P, Ca) versus pH; the
   recommended compromise range and alkalinity target (for example 100 mg/L or more as
   CaCO3).
7. Source water: alkalinity, hardness and pH of tap water and groundwater in the
   Netherlands (by water company; Drinkwaterbesluit limits) and in Karnataka (Bengaluru),
   Tamil Nadu (Chennai), Andhra Pradesh and Telangana (Hyderabad) (CGWB reports, BIS IS
   10500, peer-reviewed groundwater studies); rainwater as an option.

Output: a report with one section per topic, a table of every value with its
citation, tier, confidence, reason and corroboration, a list of gaps, and a short
recommended model structure (state variables, daily balance terms, parameters).
