# Aquaponics equipment inventory: climate and structure, heating and cooling

Scope note: this is an evidence inventory for a component database. It is not a farm design and does not size any farm. Date read for all sources: 2026-11-25. No prices were converted between currencies (no exchange rate was looked up). The notes make no claim about profitability, viability, fish safety or aeration adequacy.

Research limit: the shared WebFetch budget (100 calls per hour across all agents) ran out partway through this task. Many items below are therefore marked "not found" because the source pages could not be opened, not because the data does not exist. The Gaps sections name the documents a follow-up pass should open first.

Tag format used on every value: `[tier | confidence: level, reason | corroboration]`.

## Key question 0 (objective): per-item inventory records

### Takeaway
Indian structure cost norms (NHB/MIDH) and US extension sizing rules for fan-and-pad cooling were found and are sourced to Tier 1 and Tier 2 documents. Dutch glasshouse costs, retail and contractor prices (bol.com, Praxis, Gamma, IndiaMART), and almost all heating and cooling equipment data were not retrieved because the fetch budget ran out. Those fields are "not found" below.

### Cited Findings

#### A. Climate and structure

**A1. Fan-and-pad polyhouse / "hi-tech greenhouse" (India)**
- function: closed polyhouse cooled by evaporative pads plus exhaust fans. The tubular steel frame has a plastic film cover.
- system_types: all three (coupled and decoupled aquaponics, recirculating hydroponics). The cost norm is crop-agnostic. Inference: suitability for fish is not addressed by the source.
- scale: commercial. NHB assistance applies only to "projects having area over 2500 sq meter" (non-NE) and "over 1000 sq meter" in the NE region — [NHB Scheme-1 guideline](https://nhb.gov.in/guideline/112.pdf) `[tier_1 | confidence: high, national cost-norm document | single_source (same publisher as next item)]`
- price (India, national norm): Rs 1,400/m² (hilly states Rs 1,610/m²). Pattern of assistance: credit-linked back-ended subsidy at 50% of cost, limited to Rs 56.00 lakh per project, with a maximum project cost of Rs 112.00 lakh for areas above 2,500 m². VAT/GST status is not stated. — [NHB Scheme-1 guideline](https://nhb.gov.in/guideline/112.pdf); same figures in [NHB Cost Norms, Appendix-1 (XII Plan)](https://nhb.gov.in/hindi/pdf/Cost%20Norms.pdf) `[tier_1 | confidence: medium, government norm but no year printed; "XII Plan" implies 2012-17, so likely dated | corroborated by Haryana state scheme listing HTGH Rs 1,400–1,650/m²]`
- price (state scheme listing, Haryana, for context only, not a target state): Hi-Tech Green House (HTGH) total cost Rs 1,400–1,650/m², with a 50% subsidy of Rs 700–825/m² under the state plan. Scheduled Caste families get 85% (Rs 1,190–1,402.5/m²). — [Haryana Kisan Kalyan Pradhikaran, horticulture scheme details](https://hkkp.org.in/Other_Files/Details%20of%20scheme%20of%20Horticulture%20Dept%20eng.pdf) `[tier_1 | confidence: medium, state government document, no year visible | corroborated with NHB for the Rs 1,400 lower bound]`
- area slabs for fan-and-pad: not found. Rs 1,400–1,650 is the range given, but the slab boundaries for this structure were not retrieved.
- dimensions (span, gutter height, bay): not found.
- power, duty hours: not found.
- lifetime: not found in any cost norm retrieved. The NHB Appendix-1 does not mention film replacement ([NHB Cost Norms](https://nhb.gov.in/hindi/pdf/Cost%20Norms.pdf)).
- failure modes: see the pad-and-fan cooling item (A5).

**A2. Naturally ventilated polyhouse (NVPH) (India)**
- function: film-covered structure ventilated by roof and side vents, with no forced cooling.
- system_types: all three (crop-agnostic norm).
- scale: small commercial to commercial. MIDH area slabs run from ≤500 m² to 4,000 m².
- price by frame type (national norm, Rs/m², hilly rate in brackets) — [NHB Scheme-1 guideline](https://nhb.gov.in/guideline/112.pdf); [NHB Cost Norms Appendix-1](https://nhb.gov.in/hindi/pdf/Cost%20Norms.pdf) `[tier_1 | confidence: medium, government norm, undated (XII Plan) | tubular 844 corroborated by Haryana doc; wooden and bamboo single_source]`
  - tubular (GI steel): Rs 844 (Rs 970)
  - wooden: Rs 540 (Rs 621)
  - bamboo: Rs 450 (Rs 518)
- MIDH area slabs, tubular NVPH: Rs 1,060/m² up to 500 m²; Rs 935/m² for >500 up to 1,008 m²; Rs 890/m² for >1,008 up to 2,080 m²; Rs 844/m² for >2,080 up to 4,000 m². Hilly areas are 15% higher. — [Haryana HKKP scheme details, Scheme-III (MIDH) B.5](https://hkkp.org.in/Other_Files/Details%20of%20scheme%20of%20Horticulture%20Dept%20eng.pdf) `[tier_1 | confidence: medium, state document quoting the MIDH norm | corroborated: the 844 bottom slab matches NHB]`
- Hilly uplift: "In hilly area cost of poly house will be 15% more" — [NHB Cost Norms](https://nhb.gov.in/hindi/pdf/Cost%20Norms.pdf) `[tier_1 | high | corroborated by the Haryana doc's "15% higher for hilly areas"]`
- Conflict inside the Haryana document: its SC scheme lists NVPH total cost as Rs 717.4–901/m², against Rs 844–1,060/m² in its general scheme. Both values are recorded and not averaged. Its listed NVPH subsidy (Rs 422–530) does not equal 85% of Rs 717.4–901. — [Haryana HKKP](https://hkkp.org.in/Other_Files/Details%20of%20scheme%20of%20Horticulture%20Dept%20eng.pdf) `[tier_1 | confidence: low, internal inconsistency | conflicting]`
- Tamil Nadu (Coimbatore district Horticulture Department page): "Poly house Rs. 467.50 per sq m, 50%, 4,000 sq m per beneficiary, MIDH-NHM" — [Coimbatore district, Dept of Horticulture & Plantation Crops](https://coimbatore.nic.in/department-of-horticulture-plantation-crops/) `[tier_1 | confidence: medium, district government page, undated, ventilation type not stated | single_source]`
- Karnataka, Andhra Pradesh, Telangana state rates: not found (see Gaps).
- dimensions: not found. Power: none, since it is naturally ventilated (no forced fans in this structure class per its definition). Lifetime: not found.

**A3. Shade net house (India)**
- function: frame covered with knitted shade net, giving partial shade and some insect and bird exclusion.
- price (national norm, Rs/m², hilly in brackets) — [NHB Scheme-1](https://nhb.gov.in/guideline/112.pdf); [NHB Cost Norms](https://nhb.gov.in/hindi/pdf/Cost%20Norms.pdf) `[tier_1 | medium, undated XII Plan norm | tubular 710 corroborated by Haryana doc; wooden and bamboo single_source]`
  - tubular: Rs 710 (Rs 816)
  - wooden: Rs 492 (Rs 566)
  - bamboo: Rs 360 (Rs 414)
- Haryana state listing: Anti-Insect/Shade Net House Rs 630–710/m²; Poly Net House Rs 710/m²; Cable Purlin Net House Rs 500–525/m²; hi-tech triple-layer flat-roof net house Rs 1,625/m² (up to 4,000 m²) — [Haryana HKKP](https://hkkp.org.in/Other_Files/Details%20of%20scheme%20of%20Horticulture%20Dept%20eng.pdf) `[tier_1 | medium | single_source for the sub-types]`
- Tamil Nadu (Coimbatore): "Shade net house Rs. 355 per sq m, 50%, 4,000 sq m per beneficiary" — [Coimbatore district Horticulture](https://coimbatore.nic.in/department-of-horticulture-plantation-crops/) `[tier_1 | medium, undated | single_source]`
- shade %: not found in the norms retrieved.

**A4. Plastic tunnel / walk-in tunnel / anti-bird and hail net (India)**
- Plastic tunnel Rs 60/m² (hilly Rs 75); walk-in tunnel Rs 600/m²; anti-bird/anti-hail nets Rs 35/m²; plastic mulching Rs 32,000/ha (hilly Rs 36,800/ha) — [NHB Scheme-1](https://nhb.gov.in/guideline/112.pdf); [NHB Cost Norms](https://nhb.gov.in/hindi/pdf/Cost%20Norms.pdf) `[tier_1 | medium, undated | walk-in tunnel Rs 600 corroborated by Haryana doc; others single_source]`
- scale: inference only: the low-cost tunnel suits hobby and small commercial use. The source does not state scale.

**A5. Pad-and-fan evaporative cooling (equipment)**
- function: exhaust fans pull outside air through wetted pads. Evaporation cools the air.
- cooling effect: "as much as 10 to 20ºF below the outside temperature" — [UMass Extension fan and pad fact sheet](https://www.umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/fan-pad-evaporative-cooling-systems) `[tier_2 | medium, extension guide, climate-dependent | single_source]`. Pad efficiency is up to 85%. Entering air can come within 3–4°F of outside wet bulb, exhaust air is typically 7–8°F warmer than entering air, and heat gain is up to about 1°F per 10 ft on sunny days — [UF/IFAS AE069](https://ask.ifas.ufl.edu/publication/AE069) `[tier_2 | medium, extension, Florida climate | single_source]`
- sizing rules: see Key question 3.
- pad life: corrugated cellulose pads "about ten years with proper maintenance"; aspen pads usually short-lived in Florida — [UF/IFAS AE069](https://ask.ifas.ufl.edu/publication/AE069) `[tier_2 | medium, extension statement, basis not given | single_source]`
- power: the worked example uses two 42-inch, ½ hp fans for a 30 ft × 100 ft house — [UMass](https://www.umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/fan-pad-evaporative-cooling-systems) `[tier_2 | medium | single_source]`. Duty hours/day: not found.
- maintenance: screen returned water at 50 mesh; use continuous bleed-off or periodic flushing against salt; use a black sump and piping and run fans 30 min after cooling stops against algae; control the pump with a humidistat — [UMass](https://www.umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/fan-pad-evaporative-cooling-systems). Check humidistats at least weekly against a psychrometer and thermostats each spring and fall — [UF/IFAS AE069](https://ask.ifas.ufl.edu/publication/AE069) `[tier_2 | medium | single_source each]`
- failure modes (equipment level): algae and decay clog pads; holes and thin spots let air bypass and create hot spots; excess water flow raises resistance and carries water into the house; open doors short-circuit air (a gap creates a hot spot 6–8× its width); sensors drift — [UF/IFAS AE069](https://ask.ifas.ufl.edu/publication/AE069) `[tier_2 | medium | partly corroborated by UMass (doors closed, algae)]`. The effect on fish or plants is not stated by the sources.
- price (any market): not found.

**A6–A16, not retrieved.** The following were in scope but no source was opened before the fetch budget ran out. Every field is "not found":
- Venlo glass greenhouse (NL): cost per m², depreciation life, span, gutter height and bay size. KWIN-Glastuinbouw is sold as a paid book ([KWIN product page](https://digitaal.kwin.nl/producten/kwin-glastuinbouw-boek)). The last openly downloadable edition found is KWIN 2008 ([core.ac.uk PDF](https://core.ac.uk/download/pdf/29260561.pdf)), which was not opened.
- Plastic tunnel/polytunnel for the EU hobby market (bol.com, Praxis, Gamma): not found.
- Insulated indoor building / container farm: not found.
- Circulation (HAF) fans: sizing source located but not opened ([UMass HAF fact sheet](https://www.umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/horizontal-air-flow-is-best-for-greenhouse-air-circulation); [UConn HAF](https://ipm.cahnr.uconn.edu/horizontal-air-flow-systems/)).
- Exhaust fans, separate from fan-and-pad: only the extension rules in Key question 3.
- Misting/fogging: not found. Per the fetch summary, NHB Appendix I-B includes a "drip and fogger system" in a polyhouse model at Rs 33.76 lakh per acre, but the summary did not make clear whether that figure covers the whole polyhouse or only the irrigation and fogger part — [NHB Cost Norms](https://nhb.gov.in/hindi/pdf/Cost%20Norms.pdf) `[tier_1 | confidence: low, ambiguous extraction | single_source]`
- Thermal/shade screens: not found.
- Insect nets (mesh 40/50): not found.
- Cladding film UV-stabilised 200 micron, replacement life: not found as a life figure. The only replacement figure found is a Haryana state scheme for "replacement of plastic cladding" at 70% subsidy up to 4,000 m²: polyhouse Rs 153/m² total (subsidy Rs 107.10); net house Rs 97–114/m² (subsidy Rs 67.9–79.8); walk-in tunnel Rs 122.75–156/m² (subsidy Rs 85.92–109.20) — [Haryana HKKP](https://hkkp.org.in/Other_Files/Details%20of%20scheme%20of%20Horticulture%20Dept%20eng.pdf) `[tier_1 | medium, state document, undated, not a target state | single_source]`
- Frame types (GI steel, bamboo, wood): cost differences are captured in A2 and A3 via the NHB norms. Frame life by type: not found.

#### B. Heating and cooling

None of the heating or cooling items were retrieved. All fields (function, sizing, power, lifetime, price, failure modes) are "not found" for:
- aquarium/immersion water heaters. Sizing pages located, all Tier 3 retail or hobby ([Aquarium Co-Op heater wattage](https://www.aquariumcoop.com/blogs/aquarium/heater-wattage); [aquariumscience.org heaters](https://aquariumscience.org/index.php/14-8-aquarium-heaters)), none opened.
- heat pumps, air-to-water. A Dutch report on heat pumps in glasshouse horticulture was located but not opened ([Blueterra, Warmtepompen in de glastuinbouw, 2025](https://www.blueterra.nl/content/uploads/2025/09/Eindrapportage_warmtepompen_voor_de_glastuinbouw_v12.pdf)).
- gas boilers/CHP (Dutch glasshouse). A government tariff study likely to contain reference costs was located but not opened ([Rijksoverheid / Berenschot, Tariefstudie CO2-heffing glastuinbouw, 2024](https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/rapporten/2024/09/17/eindrapportage-tariefstudie-co2-heffing-glastuinbouw/eindrapportage-tariefstudie-co2-heffing-glastuinbouw.pdf)).
- electric space heaters, chillers, tank and pipe insulation, solar water heating: no source located.
- NHB cost norms: "No heating norms" for protected cultivation. Solar PV and solar thermal appear only as cold-storage alternate technology (max Rs 35 lakh per project, 100% of invoice cost) — [NHB Cost Norms](https://nhb.gov.in/hindi/pdf/Cost%20Norms.pdf) `[tier_1 | high, absence confirmed in the document read | single_source]`

### Inferences
- The Coimbatore figures (Rs 467.50/m² polyhouse, Rs 355/m² shade net, Rs 16,000 mulching) are exactly 50% of the MIDH norms Rs 935/m² (NVPH, 500–1,008 m² slab), Rs 710/m² (tubular shade net) and Rs 32,000/ha (mulch). They are probably the subsidy amount per m², not the structure cost. This is an arithmetic inference and the page does not say so.
- The NHB norms are defined per frame type (tubular, wooden, bamboo), so frame material is the main cost split that Indian norms recognise for NVPH and shade nets.

### Gaps
- Every heating and cooling item (B) and most EU/NL structure items: not found (fetch budget ran out).
- IndiaMART contractor quotes by city (Bengaluru, Chennai, Coimbatore, Hyderabad, Vijayawada): not found. Search found the listing hubs ([IndiaMART polyhouse construction services](https://m.indiamart.com/impcat/polyhouse-construction-services.html)) but they were not opened, so no price is recorded.
- Dimensions (span, gutter height, bay size) for any structure: not found.

## Key question 1: cost per m² ranges per structure per market

### Takeaway
For India, the national NHB/MIDH norms give Rs 1,400–1,650/m² for fan-and-pad, Rs 844–1,060/m² for tubular NVPH (falling with size slab), Rs 450–540/m² for bamboo and wooden NVPH, and Rs 360–710/m² for shade net houses. Hilly areas are about 15% higher. The documents retrieved are undated or XII-Plan era, so current 2025-26 rates may differ. No Netherlands/EU or retail price was retrieved.

### Cited Findings
- India, national norms (Rs/m², VAT/GST basis not stated): fan & pad 1,400 (hilly 1,610); NVPH tubular 844 (970), wooden 540 (621), bamboo 450 (518); shade net tubular 710 (816), wooden 492 (566), bamboo 360 (414); plastic tunnel 60 (75); walk-in tunnel 600; anti-bird/hail net 35 — [NHB Scheme-1 guideline](https://nhb.gov.in/guideline/112.pdf); [NHB Cost Norms Appendix-1, XII Plan](https://nhb.gov.in/hindi/pdf/Cost%20Norms.pdf) `[tier_1 | medium, authoritative but undated | tubular NVPH, shade net and walk-in tunnel corroborated by Haryana; others single_source]`
- India, MIDH NVPH tubular slabs: Rs 1,060 (≤500 m²), 935 (>500–1,008), 890 (>1,008–2,080), 844 (>2,080–4,000) — [Haryana HKKP doc, MIDH section B.5](https://hkkp.org.in/Other_Files/Details%20of%20scheme%20of%20Horticulture%20Dept%20eng.pdf) `[tier_1 | medium | corroborated at the 844 slab by NHB]`
- India, fan-and-pad / hi-tech greenhouse range Rs 1,400–1,650/m² — [Haryana HKKP](https://hkkp.org.in/Other_Files/Details%20of%20scheme%20of%20Horticulture%20Dept%20eng.pdf) `[tier_1 | medium | lower bound corroborated by NHB]`
- India subsidy pattern (NHB commercial scheme): credit-linked back-ended 50% of cost, max Rs 56 lakh per project, project area >2,500 m² (>1,000 m² in the NE) — [NHB Scheme-1](https://nhb.gov.in/guideline/112.pdf) `[tier_1 | high | corroborated by NHB Cost Norms (same publisher)]`
- India MIDH 2025 Operational Guidelines: components "inclusive of irrigation systems"; materials must conform to BIS standards for subsidy eligibility; SLSC can approve protected-cultivation projects up to Rs 70 lakh — [MIDH Operational Guidelines 2025 (NHB)](https://nhb.gov.in/writereaddata/082825102800MIDH%20Guideline%202025.pdf) `[tier_1 | high | single_source]`. Its Annexure V protected-cultivation cost table could not be extracted (the PDF text cut off at 98,298 characters before that table).
- Tamil Nadu (Coimbatore district): polyhouse Rs 467.50/m², shade net Rs 355/m², both 50%, max 4,000 m² per beneficiary, MIDH-NHM — [Coimbatore district Horticulture](https://coimbatore.nic.in/department-of-horticulture-plantation-crops/) `[tier_1 | medium, undated | single_source]`
- Telangana: the state MIDH Implementation Guidelines 2025-26 say the norms follow MIDH Operational Guidelines 2025 and are "indicative". Protected cultivation is Component 7 (pp. 121–147), but the figures could not be extracted — [Telangana SHM, MIDH Implementation Guidelines 2025-26](https://shm.tg.nic.in/Download/MIDH%20-%20Implementation%20Guidelines%20-%202025-26.pdf) `[tier_1 | high for the policy statement | single_source]`
- Netherlands/EU (Venlo glass, hobby greenhouses), US/Alibaba: not found.

### Inferences
- In the national norms, bamboo NVPH (Rs 450) costs about 53% of tubular NVPH (Rs 844) at the largest slab (arithmetic on cited norms). The small-area slab (≤500 m²) carries a 26% premium over the 2,080–4,000 m² slab (1,060 vs 844).

### Gaps
- Fan-and-pad slab structure under MIDH 2025, and current 2025-26 national norms: not found (the PDF table was unreadable through the fetch tool).
- Karnataka and Andhra Pradesh state rates and top-ups: not found. The AP protected cultivation guidelines PDF ([horticulture.ap.nic.in](https://horticulture.ap.nic.in/assets/pdfs/P_C_GUIDELINES.pdf)) failed with a robots.txt error. The Karnataka department page was not located.
- KWIN-AGV / WUR glasshouse cost per m²: not found (KWIN is a paywalled book). The CBS energy price for growers was not retrieved.
- Hobby greenhouse prices on bol.com, Praxis and Gamma: not found.

## Key question 2: depreciation lives in cost norms (frame vs film)

### Takeaway
None of the Indian cost norms retrieved states a depreciation life for structures or film. The only replacement-related norm found is a state (Haryana) subsidy for replacing plastic cladding (Rs 153/m² for a polyhouse). Dutch depreciation norms (KWIN, Belastingdienst Landbouwnormen) were located but could not be opened.

### Cited Findings
- NHB Cost Norms Appendix-1: film replacement is not mentioned — [NHB Cost Norms](https://nhb.gov.in/hindi/pdf/Cost%20Norms.pdf) `[tier_1 | high, absence in document read | single_source]`
- Plastic cladding replacement scheme (Haryana, 70% subsidy, up to 4,000 m²): polyhouse Rs 153/m²; net house Rs 97–114/m²; walk-in tunnel Rs 122.75–156/m² — [Haryana HKKP](https://hkkp.org.in/Other_Files/Details%20of%20scheme%20of%20Horticulture%20Dept%20eng.pdf) `[tier_1 | medium | single_source]`
- Cellulose evaporative pad life about 10 years with proper maintenance (equipment, not structure) — [UF/IFAS AE069](https://ask.ifas.ufl.edu/publication/AE069) `[tier_2 | medium | single_source]`
- Netherlands: the Belastingdienst publishes national farm norms annually ([Landelijke Landbouwnormen 2024](https://download.belastingdienst.nl/belastingdienst/docs/landelijke_landbouwnormen_2024_aa9601z41pl.pdf)). The document was located, but its contents were not read, so no depreciation value is recorded.

### Inferences
- That a state "replacement of plastic cladding" scheme exists shows that film replacement is a recurring cost recognised by at least one Indian state. The replacement interval is not given.

### Gaps
- Film life in years (200 micron UV-stabilised) by any source: not found.
- Frame life (GI steel, bamboo, wood): not found.
- KWIN/WUR depreciation percentages for glasshouse, screens, boilers and CHP: not found.

## Key question 3: sizing rules (ventilation, pad cooling area, HAF, heating)

### Takeaway
Two US extension guides give fan-and-pad sizing. They agree on structure but differ slightly on pad ratings. UMass gives 8 cfm per ft² of floor; UF gives a minimum of one air change per minute. Pad face ratings are 140–150 cfm/ft² for aspen and 230–350 cfm/ft² for cellulose depending on source and thickness. No NHB/ASABE ventilation rule and no heating rule (kW per m²) was retrieved.

### Cited Findings
- Ventilation rate: "eight cubic feet per minute (cfm) per square foot of floor area" at 0.1 in water static pressure. Increase it if summer light is unshaded above 5,000 foot-candles, if the site is above 1,000 ft elevation, or if pad-to-fan distance is under 100 ft (no multiplier given) — [UMass](https://www.umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/fan-pad-evaporative-cooling-systems) `[tier_2 | medium | single_source as stated]`
  - Unit normalisation (conversion only): 8 cfm/ft² is a face velocity of 8 ft/min = 2.44 m/min, which equals about 146 m³/h per m² of floor (1 ft = 0.3048 m).
- Ventilation rate (alternative form): "a minimum of one air change per minute" (= 60 air changes per hour); rate fans at 1/8 in static pressure — [UF/IFAS AE069](https://ask.ifas.ufl.edu/publication/AE069) `[tier_2 | medium | single_source]`
- Pad area (aspen): 1 ft² of pad per 140 cfm — [UF/IFAS AE069](https://ask.ifas.ufl.edu/publication/AE069); 150 cfm per ft² — [UMass](https://www.umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/fan-pad-evaporative-cooling-systems) `[tier_2 | medium | conflicting: 140 vs 150, both recorded]`
- Pad area (cellulose): "up to 230 CFM per square foot of pad" — [UF/IFAS](https://ask.ifas.ufl.edu/publication/AE069); 4-inch cellulose 250 cfm/ft², 6-inch cellulose 350 cfm/ft² — [UMass](https://www.umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/fan-pad-evaporative-cooling-systems) `[tier_2 | medium | conflicting for 4-inch class: 230 vs 250]`
- Pad height: 2 ft minimum, 8 ft maximum — [UMass](https://www.umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/fan-pad-evaporative-cooling-systems); about 1 ft of pad height per 20 ft of pad-to-fan distance — [UF/IFAS](https://ask.ifas.ufl.edu/publication/AE069) `[tier_2 | medium | single_source each]`
- Pad-to-fan distance: never more than 200 ft, preferably ≤150 ft; fan spacing no more than 20–30 ft apart; add 10–15% cfm if fans face the prevailing wind; do not exhaust toward another house's pad within 50 ft — [UF/IFAS AE069](https://ask.ifas.ufl.edu/publication/AE069) `[tier_2 | medium | single_source]`
- Pad water: 1/3 gpm per ft pad length (aspen), ½ (4-inch cellulose), ¾ (6-inch cellulose); makeup 1 gpm per 100 ft² of pad; sump ½, ¾ and 1 gal per ft² of pad for 2-, 4- and 6-inch pads — [UMass](https://www.umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/fan-pad-evaporative-cooling-systems). UF gives about 1/3 gal per ft of pad length to keep the surface wet and a sump of 1–1¼ gal per linear ft of pad — [UF/IFAS](https://ask.ifas.ufl.edu/publication/AE069) `[tier_2 | medium | sump rule conflicting in basis (per ft² vs per linear ft)]`
- Evaporative heat: about 8,700 Btu per gallon evaporated (UMass) vs about 8,100 Btu per gallon (UF) — [UMass](https://www.umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/fan-pad-evaporative-cooling-systems); [UF/IFAS](https://ask.ifas.ufl.edu/publication/AE069) `[tier_2 | medium | conflicting, both recorded]`
- Swamp (unit) coolers: 1.2 to 2.0 times the greenhouse volume in cfm — [UMass](https://www.umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/fan-pad-evaporative-cooling-systems) `[tier_2 | medium | single_source]`

### Inferences
- The two extension sources size the same system with different reference conditions (UMass at 0.1 in static pressure, UF at 1/8 in). That likely explains part of the pad-rating difference. This is an inference and neither source says so.

### Gaps
- NHB/ICAR/TNAU ventilation or pad-area rule for Indian polyhouses: not found.
- ASABE standard (EP406 / EP270) values: not retrieved.
- HAF fan sizing (cfm per ft²): source located but not opened. Not found.
- Heating sizing (kW or W per m², U-values of glass and film, W per litre for tank heaters): not found.

## Key question 4: what growers use instead, and what fails

### Takeaway
Indian norms explicitly recognise bamboo and wooden frames as lower-cost alternatives to GI tubular frames for NVPH and shade nets. Failure evidence retrieved covers cooling-system faults only (pad clogging, hot spots, air short-circuiting). No retrieved source covers wind damage or film life in Indian sun.

### Cited Findings
- Alternatives recognised in national norms: NVPH and shade net on wooden or bamboo frames at Rs 540 / 450 and Rs 492 / 360 per m² respectively, against tubular Rs 844 / 710 — [NHB Scheme-1](https://nhb.gov.in/guideline/112.pdf) `[tier_1 | medium | single_source for wood and bamboo]`
- Cable purlin net house (Rs 500–525/m²) appears as a cheaper net-house type in a state scheme — [Haryana HKKP](https://hkkp.org.in/Other_Files/Details%20of%20scheme%20of%20Horticulture%20Dept%20eng.pdf) `[tier_1 | medium | single_source]`
- Swamp/unit coolers as an alternative to full fan-and-pad — [UMass](https://www.umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/fan-pad-evaporative-cooling-systems) `[tier_2 | medium | single_source]`
- Cooling failures: algae and decay clog pads; holes cause hot spots; doors and gaps short-circuit air; sensors drift — [UF/IFAS AE069](https://ask.ifas.ufl.edu/publication/AE069) `[tier_2 | medium | partly corroborated by UMass]`

### Inferences
- None beyond the cited findings.

### Gaps
- Wind damage, film tear and film life under Indian UV: not found.
- DIY hoop houses and insulated sheds (grower practice, forum anecdote): not found.
- Effects on fish and plants of film tear, heater failure or heat stress: not found.
