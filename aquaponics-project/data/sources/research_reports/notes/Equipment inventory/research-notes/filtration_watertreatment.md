# Aquaponics equipment inventory: solids removal, biofiltration, degassing and mineralisation, water treatment and dosing

Reliability key used on every value: `[tier | confidence: one-line reason | corroboration]`.
- tier_1 = peer-reviewed, government cost norms, university research station / SRAC / UVI / FAO (FAO 589 is Tier 1 in the repo's Trusted Source Map PDF). tier_2 = manufacturer datasheets, extension notes, research institute notes, trade-press summaries of peer-reviewed work. tier_3 = retail/B2B listings, forums, blogs.
- corroboration: `corroborated` (2+ independent sources agree), `single_source`, `conflicting` (both values are given; nothing is averaged).
- "read 2026-11-25" = fetched in this session. "via repo report" = the value was taken from the repo's own `Biofilters and solids filters_Corroboration report for aquaponics Layer 1.pdf` or `Water Chemistry and pH Management_..._Corroboration Report.pdf` (repo root). Those reports cite the primary URL given, but I did not re-read that URL today.
- Prices: as listed. No currency conversion. No exchange rates used. All prices are tier_3 unless they come from a government cost norm.
- **Research limit:** the shared web-fetch budget (100 calls/hour across all agents) ran out partway through this task. Many retail price pages were found but could not be read. They are listed under Gaps so that a later pass can read them. No value below was estimated or filled in.
- Nothing below is a farm design, a sizing of a specific farm, or a claim of fish safety, aeration adequacy, solids-removal capacity, profitability or viability.

## Item inventory records (function, system fit, scale, sizing, power, lifetime, maintenance, price, alternatives, failure modes)

### Takeaway
The best-documented items are the UVI-style conical clarifier, the orchard-netting filter tanks, the degassing tank and base-addition tank (all in SRAC 454). Also well documented: radial-flow vs swirl settler efficiency (Davidson & Summerfelt 2005), bead/trickling/RBC/fluidised-sand/moving-bed biofilter loading criteria (SRAC 453, 1999 and 2013 editions, which conflict), and K1 MBBR media (500 m²/m³; area-based nitrification 0.14–0.97 g N/m²/day in Kamstra et al. 2017). Retail evidence was only partly gathered: drum filter and UV-C prices for NL, drum filter and MBBR media prices for India, plus PMMSY whole-RAS cost norms. Most dosing and source-water items still have no price or sizing source.

### Cited Findings

#### A. Solids removal

**A1. Conical clarifier / settling tank (UVI-style)**
- item_name: conical-bottom clarifier (UVI commercial raft aquaponics system). Function: removes settleable solids after the rearing tanks. — [SRAC 454, Rakocy, Masser & Losordo](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf) (read 2026-11-25)
- system_types / grow methods: coupled aquaponics with DWC raft (UVI). Settling devices are also listed in general RAS practice. — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf); [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)
- dimensions: 1,000 US gal each. Cylinder 6 ft diameter × 4 ft high. Cone depth 3.6 ft. Cone slope 45°. `[tier_1 | high: UVI design published by SRAC | single_source]` — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf). (Unit conversion by note-writer at 1 US gal = 3.785 L: about 3.8 m³.)
- capacity / efficiency: the clarifier removes about 50% of total particulate solids; the filter tanks remove the remaining 50%. `[tier_1 | medium: design-description statement, not a controlled trial | single_source]` — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)
- sizing rule (HRT): RAS design practice gives an HRT of 15–30 min, minimum depth >1.2 m, and rectangular basin L:W of 4:1 to 8:1, sized by surface-area:flow ratio ("overflow rate"). `[tier_1 | high: SRAC design-practice sheet | corroborated by UVI anchor below]` — [SRAC 453 (2013, Review of Current Design Practice), via repo report](https://agrilife.org/fisheries/files/2013/09/SRAC-Publication-No.-453-Recirculating-Aquaculture-Tank-Production-Systems-A-Review-of-Current-Design-Practice.pdf)
- sizing rule (UVI anchor): clarifier retention time was raised to about 19–20 min. The earlier ~9.5 min retention captured less solids. `[tier_1 | high: long-running research station operating record | corroborated (UVI 25-years PDF and UVI web page)]` — [UVI "25 Years of Research", via repo report](https://www.tag2grow.org/wp-content/uploads/2021/09/UVI-Aquaponics.pdf); [UVI Aquaponic Systems page, via repo report](https://www.uvi.edu/research/agricultural-experiment-station/aquaculture-home/aquaponic-systems/index.html). (Repo canon `data/knowledge/models/solids_models.json` already holds 15–30 min / 19–20 min / 9.5 min as draft anchors.)
- system flow anchor: total flow 100 GPM. `[tier_1 | high | corroborated with "378 L/min" in UVI 25-years PDF via repo report]` — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf); [UVI 25 Years, via repo report](https://www.tag2grow.org/wp-content/uploads/2021/09/UVI-Aquaponics.pdf)
- solids load driver: at least 25% of feed becomes solid waste (dry weight). `[tier_1 | medium: rule of thumb on UVI page | single_source]` — [UVI page, via repo report](https://www.uvi.edu/research/agricultural-experiment-station/aquaculture-home/aquaponic-systems/index.html)
- power: none of its own (gravity, inside the pumped loop). No rated W found.
- lifetime: not found.
- maintenance / labour: clarifier sludge is removed three times daily. `[tier_1 | high | single_source]` — [UVI 25 Years, via repo report](https://www.tag2grow.org/wp-content/uploads/2021/09/UVI-Aquaponics.pdf). About 30 male tilapia fingerlings are kept in the clarifier to graze the cone walls and are replaced with 50 g fingerlings about every 4 months, because performance drops above 200 g. `[tier_1 | high | corroborated (UVI 25 Years reports solids adhering to cone walls, mitigated by fish grazing)]` — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf). Minutes per task: not found.
- failure modes: settled solids adhere to cone walls — [UVI 25 Years, via repo report](https://www.tag2grow.org/wp-content/uploads/2021/09/UVI-Aquaponics.pdf). Uncleaned settling basins let solids decompose, which adds ammonia and oxygen demand to the water. `[tier_1 | high | single_source]` — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)
- trade-offs: basins are large and need regular cleaning — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf). Tube/lamella settlers (usually 60° to horizontal) reduce settling distance and basin size — same source.
- price: not found (NL, India). Global: not found.

**A2. Radial-flow settler**
- function: settleable-solids removal fed by the bottom-centre drain of a dual-drain tank.
- capacity / efficiency: mean TSS removal 77.9 ± 1.6% (radial-flow) vs 37.1 ± 3.3% (swirl separator) at the same surface loading of 0.0031 m³/s per m² of settling area. Daily TSS mass removed: about 48% (radial) vs about 23% (swirl). Test context: 150 m³ Cornell-type dual-drain tank, 4,500–4,800 L/min recirculating flow, bottom drain carrying about 7–8% of flow. `[tier_1 | high: peer-reviewed controlled comparison (Davidson & Summerfelt 2005, Aquacultural Engineering), read via a trade-press summary | single_source (the repo report cites the same study via a whitepaper, which is not independent)]` — [GSA Advocate summary of Davidson & Summerfelt 2005](https://www.globalseafood.org/advocate/settler-evaluation-radial-flow-vs-tangential-flow/); [Radial flow settler whitepaper, via repo report](https://cdn.aquaponicsassociation.org/uploads/2019/10/Radial_Flow_Settler_Whitepaper.pdf)
- context tags: cold-water RAS (Freshwater Institute), commercial scale. Not aquaponics-specific.
- sizing rule: settling area ≥ Q / 0.0031 (Q in m³/s) as a performance anchor, not a universal rule. HRT and settler dimensions are not reported in the summary.
- power / lifetime / maintenance / price: not found.

**A3. Swirl separator (hydrocyclone / vortex; includes DIY barrel swirl filters)**
- capacity / efficiency: 37.1 ± 3.3% mean TSS removal in the controlled comparison above `[tier_1 | high | single_source]` — [GSA Advocate / Davidson & Summerfelt 2005](https://www.globalseafood.org/advocate/settler-evaluation-radial-flow-vs-tangential-flow/)
- dimensions: RAS swirl separators are "generally 1–2 m in diameter", and texts recommend a centre cylinder of at least 25% of tank diameter `[tier_2 | medium: background statement in a trade summary | single_source]` — [GSA Advocate](https://www.globalseafood.org/advocate/settler-evaluation-radial-flow-vs-tangential-flow/)
- trade-offs: compact size (advantage). Large replacement water volume (drawback). No sizing rule is given. `[tier_1 | high | single_source]` — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)
- small-scale sizing (FAO "mechanical separator", which includes swirl/radial types): 10–30% of fish tank volume. Required for NFT and DWC. Required for media beds when stocking is above 20 kg per 1,000 L. FAO Table 8.1 examples: 200 L tank → 20 L filter; 1,000 L → 100–200 L; 3,000 L → 400–500 L. `[tier_1 | medium: FAO 589 content read via a third-party reproduction, not the FAO PDF | single_source]` — [FAO 589 via FarmHub](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/); original [FAO 589 PDF](https://openknowledge.fao.org/server/api/core/bitstreams/2ca21047-390f-42cd-bd1d-0c2ebc9c1df2/content) (not read)
- power / lifetime / maintenance minutes / price: not found.

**A4. Rotating drum (microscreen) filter**
- function: removes fine suspended solids by rotating screen, with automatic spray backwash.
- capacity (RAS evidence): the smallest commercial unit processes about 475 L/min (125 gpm) at 25 mg/L suspended solids. Vacuum-cleaned drum filters handle 375–1,800 L/min. A drum filter used on average 13.4% of the backwash water that a settling basin needed (Libey 1993, tilapia system). `[tier_1 | high: SRAC synthesis citing original studies | single_source]` — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)
- efficiency: a microscreen drum filter removed 40–45% of daily TSS mass in the Davidson & Summerfelt system `[tier_1 | high | single_source]` — [GSA Advocate](https://www.globalseafood.org/advocate/settler-evaluation-radial-flow-vs-tangential-flow/)
- mesh: the repo report lists "typical 20–60 µm" for microscreen polishing `[tier_2 | low: the footnote in the repo report was not resolved to a primary source | single_source]` — [repo report, citing SRAC 453 (2013)](https://agrilife.org/fisheries/files/2013/09/SRAC-Publication-No.-453-Recirculating-Aquaculture-Tank-Production-Systems-A-Review-of-Current-Design-Practice.pdf). AquaForte retail unit: 60 µm (below).
- example retail unit (NL): AquaForte Trommelfilter with lid and controller. Max flow 25 m³/h. Ponds up to 50 m³. 60 µm screen elements. "80 w excl. Spoelpomp en UV" (80 W excluding rinse pump and UV). 48 VDC motor. 50 × 70 × 43 cm. 2-year warranty. €983.20 incl. BTW (reduced from €1,229), marked "Niet meer leverbaar" (no longer available). Seller toppy.nl, read 2026-11-25. `[tier_3 | medium: retailer spec sheet; product discontinued | single_source]` — [toppy.nl AquaForte trommelfilter](https://www.toppy.nl/product/7172/aquaforte-trommelfilter.html)
- duty hours/day: not found. Backwash water per cycle: not found.
- maintenance (RAS): microscreens do not need daily wash-downs but generate backwash water — [SRAC 453 (2013), via repo report](https://agrilife.org/fisheries/files/2013/09/SRAC-Publication-No.-453-Recirculating-Aquaculture-Tank-Production-Systems-A-Review-of-Current-Design-Practice.pdf)
- lifetime: not found (only the 2-year warranty above, which is not a lifetime).
- price India and global: see "Typical price ranges per market".

**A5. Bead filter (as solids filter and/or "bioclarifier")**
- function: a floating plastic bead bed that captures solids and hosts nitrifiers. It is backwashed by bubbles or a propeller.
- specific surface area: 1,150–1,475 m²/m³ (350–450 ft²/ft³) `[tier_1 | high | single_source]` — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)
- capacity: design criterion 13 kg feed/day per m³ of beads (0.81 lb/day/ft³), with the manufacturer recommending 1.0 lb/day/ft³. Nitrification about 325 g TAN/m³/day (Beecher et al. 1997). Assumes 2.5% of feed becomes TAN. — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf). **Conflicting:** bead bioclarifiers "can be sized to 16–32 kg feed/m³/day (under optimised washing)" — [SRAC 453 (2013, Malone), via repo report](https://agrilife.org/fisheries/files/2013/09/SRAC-Publication-No.-453-Recirculating-Aquaculture-Tank-Production-Systems-A-Review-of-Current-Design-Practice.pdf). `[tier_1 | medium: two SRAC editions disagree; the difference is plausibly the washing regime (context split) | conflicting]`
- maintenance: 1 to 48 hours between backwashes (bubble- or propeller-washed) `[tier_1 | high | single_source]` — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)
- FAO 589 lists bead filters among the recommended solids filter types — [SRAC 5007, via repo report](https://srac.msstate.edu/pdfs/Fact%20Sheets/5007%20Principles%20of%20Small-Scale%20Aquaponics.pdf)
- price: NL AquaForte EconoBead EB 40/100/140 pages were found but could not be read (budget) — see Gaps. India / global: not found.

**A6. Filter socks, filter mats, filter brushes**
- function, sizing, lifetime, price: not found in this pass. No SRAC/FAO/UVI sizing rule was surfaced.

**A7. Sand filters (pressurised down-flow)**
- trade-off / failure mode: they need frequent backwashing under heavy feeding, which wastes water. No numeric sizing rule. `[tier_1 | high | single_source]` — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)
- fluidised sand (as biofilter): see B5.
- price, lifetime, power: not found.

**A8. Dual-drain / particle trap (upstream of solids units)**
- about 5% of tank outflow carries the settleable solids (ECO-TRAP, Hobbs et al. 1997). Sludge averages 6% dry solids. In high-flow systems, settleable solids carry 20–50% of total tank flow. `[tier_1 | high | single_source]` — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf). The repo report lists a 5–20% dual-drain fraction from Davidson & Summerfelt — [via repo report](https://cdn.aquaponicsassociation.org/uploads/2019/10/Radial_Flow_Settler_Whitepaper.pdf). The GSA summary gives 7–8% — [GSA Advocate](https://www.globalseafood.org/advocate/settler-evaluation-radial-flow-vs-tangential-flow/). `[context split: different tanks and studies]`

#### B. Biofiltration

**B1. MBBR media (Kaldnes K1 and generic "K1-type")**
- specific surface area: K1 = 500 m²/m³ `[tier_1 | high | corroborated: Kamstra et al. 2017 states "Kaldnes K-1 with a specific surface of 500 m2·m-3"; Indian K1-type listing also states 500 m²/m³]` — [Kamstra, Blom & Terjesen 2017, Aquacultural Engineering](https://core.ac.uk/download/249978494.pdf); [IndiaMART MBBR listings](https://m.indiamart.com/impcat/mbbr-media.html). The manufacturer sheet gives K1 "Total surface area 800 m², Total protected surface 500 m²" and K3 "584 m² / 500 m²", with no stated per-m³ basis `[tier_2 | medium: distributor-hosted datasheet with ambiguous units | single_source]` — [K1/K3 media sheet (Evolution Aqua)](https://absolute-koi.com/pdf/K1K3media.pdf)
- TAN removal rate (area-based, the unit asked for): 0.85 (SD 0.18) g N/m²/day in a 200 L MBBR at 35% then 50% fill, 24.9 ± 0.5 °C. Small reactors: 0.85 at 25% fill vs 0.55 at 50% fill. Means 0.97 (35% fill) and 0.72 (50% fill). Commercial farms: 0.45/0.31 (farm 1, K1), 0.29/0.22 (farm 3, K1), 0.17/0.14 (farm 2, Curler X-1, 800 m²/m³), large vs small reactors. Treatment means span 0.24–2.63 g N/m²/day depending on TAN level, scale, fill and air velocity. `[tier_1 | high: peer-reviewed, multi-scale trials | single_source]` — [Kamstra et al. 2017](https://core.ac.uk/download/249978494.pdf)
- feed-based sizing: **conflicting.** (a) "Mixed bed (moving bed)": 800–1,150 m²/m³ and 16–23 kg feed/day/m³ (1.0–1.4 lb/day/ft³) — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf). (b) MBBR about 8–16 kg feed/m³ media/day (about ¼–½ of fluidised-bed capacity) — [SRAC 453 (2013, Malone), via repo report](https://agrilife.org/fisheries/files/2013/09/SRAC-Publication-No.-453-Recirculating-Aquaculture-Tank-Production-Systems-A-Review-of-Current-Design-Practice.pdf). (c) Manufacturer: "50 litres of K1 will handle up to 250 gramme of food per day" (K3: 225 g/day per 50 L) — [K1/K3 sheet](https://absolute-koi.com/pdf/K1K3media.pdf); same claim repeated on [Pondkeeper UK listing](https://www.pondkeeper.co.uk/evolution-aqua-kaldnes-k1-bio-media-50-litres) (not independent). Arithmetic by note-writer: (c) equals 5 kg feed/m³ media/day. `[tier_1/tier_2 | medium: sources differ by edition and context (koi pond vs RAS) | conflicting]`. Note: the 1999 SRAC value of 800–1,150 m²/m³ is above K1's 500 m²/m³ protected area, so it likely refers to other media or total area. Not resolved.
- aeration / degassing: MBBR needs significant air to keep the media moving. That airflow also adds aeration and degassing. — [SRAC 453 (2013), via repo report](https://agrilife.org/fisheries/files/2013/09/SRAC-Publication-No.-453-Recirculating-Aquaculture-Tank-Production-Systems-A-Review-of-Current-Design-Practice.pdf). Manufacturer air-pump pairing: Airtech 40 for 100 L of media, Airtech 80 for 100–200 L, Airtech 120 for 200+ L — [K1/K3 sheet](https://absolute-koi.com/pdf/K1K3media.pdf). Rated W of those pumps: not read.
- fill fraction effect: a higher fill (50%) gave a lower area rate than 25–35% in Kamstra et al. — [Kamstra et al. 2017](https://core.ac.uk/download/249978494.pdf)
- lifetime: no lifetime claim. The manufacturer says the process has been "scientifically tried and tested in fish farming and waste water treatment for over 10 years". The media is described as self-cleaning and "requires no maintenance". `[tier_2 | low: marketing claim, not a measured lifetime | single_source]` — [K1/K3 sheet](https://absolute-koi.com/pdf/K1K3media.pdf)
- price: see the price section (UK £85.95 per 50 L; India ₹6,500–₹27,500 per m³).
- failure modes: not found from a primary source. Low DO below 2 mg/L makes nitrifiers inefficient (applies to all biofilters) — [SRAC 452, via repo report](https://www.ncrac.org/files/inline-files/SRAC0452.pdf)

**B2. Moving-bed tank (MBBR vessel)** — vessel-specific sizing, price and power: not found beyond B1.

**B3. Trickling filter**
- specific surface area: generally less than 330 m²/m³ (100 ft²/ft³). Nitrification about 90 g TAN/m³/day (Losordo, unpublished). Design criterion 3.6 kg feed/day/m³ (0.225 lb/day/ft³). `[tier_1 | medium: the TAN rate rests on unpublished data | single_source]` — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)
- RBC (for comparison): up to 200 m²/m³. About 76 g TAN/m³/day (Wheaton et al. 1994). About 40% of the medium is submerged. Medium weight can rise up to 10-fold, so supports must allow for it. A 4 ft RBC turns at 3–4 rpm. The extracted feed criterion reads "3.6 kg/day/m³ (0.189 lb/day/ft³)", but 0.189 lb/ft³ does not equal 3.6 kg/m³. One of the two numbers was mis-transcribed, so re-check against the PDF before use. — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)
- price / lifetime / power: not found.

**B4. Bead filter as biofilter** — see A5 (13 kg feed/m³/day in 1999 vs 16–32 kg feed/m³/day in 2013; 325 g TAN/m³/day).

**B5. Fluidised sand biofilter** (in scope as a sand-based biofilter)
- 20–40 kg feed/day/m³ (1.25–2.5 lb/day/ft³) — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf). **Conflicting:** 16–32 kg feed/m³ media/day — [SRAC 453 (2013), via repo report](https://agrilife.org/fisheries/files/2013/09/SRAC-Publication-No.-453-Recirculating-Aquaculture-Tank-Production-Systems-A-Review-of-Current-Design-Practice.pdf). Fine sand beds can hold NH₃/NO₂ below 0.2 mg/L-N — same 2013 source. `[tier_1 | medium | conflicting]`

**B6. Media bed as biofilter (and combined solids filter)**
- volcanic gravel 300 m²/m³: 1 L media per g of daily feed. Bioballs 600 m²/m³ (for NFT/DWC): 0.5 L per g daily feed. These are minimums, and oversizing is advised for cold periods. `[tier_1 | medium: FAO content via third-party reproduction | single_source]` — [FAO 589 via FarmHub](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/)
- UVI gravel rule: 1 ft³ of fish tank to 2 ft³ of pea gravel. The gravel and NFT feeding-rate ratio is about 25% of the raft ratio. `[tier_1 | high | single_source]` — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)
- trade-off and failure mode: media beds often act as combined mechanical and biological filter. Solids build up, clog the bed and create anaerobic zones that can kill roots, which drives maintenance. — [repo report "Media bed vs DWC vs NFT_Corroboration report" (repo root PDF; primary URLs not re-read)](https://extension.okstate.edu/fact-sheets/print-publications/hla/nitrification-and-maintenance-in-media-bed-aquaponics-hla-6729.pdf) `[tier_1/2 | medium: via repo report | corroborated across several extension sources per that report]`
- scale: FAO table covers 200–3,000 L tanks and 1–12 m² growing area (leafy greens) — [FAO 589 via FarmHub](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/)

**B7. DWC raft surface as biofilter (UVI)**
- UVI sizes no separate biofilter. Raft hydroponics alone is reported to treat waste equivalent to 180 g feed/m²/day (about 1.2 lb feed per 8 × 4 ft raft sheet). Optimal nitrification conditions: 77–86 °F, pH 7.0–9.0, BOD <20 mg/L, alkalinity ≥100 mg/L. `[tier_1 | high | single_source]` — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)
- small-scale rule: biofilter tank about 15–20% of fish tank volume, with DO kept above 5 mg/L in the biofilter — [SRAC 5007, via repo report](https://srac.msstate.edu/pdfs/Fact%20Sheets/5007%20Principles%20of%20Small-Scale%20Aquaponics.pdf) `[tier_1 | medium: rule of thumb | single_source]`

**B8. Static sponge / Japanese mat** — function, sizing, specific surface area, price and lifetime: not found.

#### C. Degassing, mineralisation and orchard/bird-netting filter tanks

**C1. Filter tanks with orchard netting (UVI)**
- dimensions: two tanks, each 185 US gal, 6 ft × 2.5 ft × 2 ft deep (conversion by note-writer: about 0.7 m³ each) `[tier_1 | high | single_source]` — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)
- function: they capture the fine solids that pass the clarifier (about 50% of total particulate solids, per the 50/50 split above). Suspended solids stay in the tanks for 3–7 days between cleanings. — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)
- maintenance: cleaned "once or twice each week" with a high-pressure spray `[tier_1 | high | single_source]` — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf). Minutes per cleaning: not found.
- price of orchard/bird netting (NL/India): not found.

**C2. Degassing tank (UVI)**
- dimensions: 185 US gal, 6 ft × 2.5 ft × 2 ft. An internal standpipe splits the flow to three sets of hydroponic tanks. `[tier_1 | high | single_source]` — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)
- RAS degassing (packed column aerator): about 0.75 kg O₂/kWh at 4 mg/L influent DO. Water must be lifted about 1.0–1.25 m. For CO₂ stripping, air volume should be at least 5× water volume. Target CO₂ below 25 mg/L. `[tier_1 | high | single_source]` — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf). (These are oxygen-transfer and CO₂ figures for packed columns. They are not an aeration-adequacy claim.)
- India: PMMSY/NFDB lists a "carbon dioxide trapper system (degasser)" as a RAS component, with no cost or capacity — [NFDB RAS booklet (vikaspedia)](https://static.vikaspedia.in/mediastorage/document/Ras_Booklet_Eng.pdf)
- price / power / lifetime: not found.

**C3. Mineralisation tank / sludge reactor**
- UVI: the filter tanks double as the place where captured solids sit for 3–7 days before cleaning (C1). No mineralisation rate is quantified. — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)
- FAO small-scale: no mineralisation sizing rule in the reproduced calculations chapter — [FAO 589 via FarmHub](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/)
- trade-off (repo canon already models this): keeping solids for mineralisation adds nutrients, but it also raises clogging risk and the work of managing anaerobic zones — `data/knowledge/component_variants/component_variants.json` variant `solids_strategy_low_removal_mineralisation` (repo canon, draft).
- decoupled-system aerobic/anaerobic sludge reactors: candidate sources found but not read (budget): [Springer "Aquaponics Food Production Systems" ch.10](https://link.springer.com/chapter/10.1007%2F978-3-030-15943-6_10), [Delaide 2018 thesis](https://orbi.uliege.be/bitstream/2268/225286/1/N%c2%b0674%20-%20Delaide%202018.pdf), [WUR edepot 630704](https://edepot.wur.nl/630704). No values recorded.

#### D. Water treatment and dosing

**D1. pH up: KOH and Ca(OH)₂ (UVI practice)**
- dose practice: equal amounts of KOH and Ca(OH)₂, usually 500–1,000 g each, added alternately several times weekly to hold pH near 7.0. This is in the UVI system with about 29,375 US gal total water volume (context, not a per-m³ rule). `[tier_1 | high: UVI operating practice | corroborated (NMSU CR680 and Texas A&M also say to alternate Ca(OH)₂/KOH, via repo water-chemistry report)]` — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf); [NMSU CR680, via repo report](https://pubs.nmsu.edu/_circulars/CR680.pdf); [Texas A&M Water Quality in Aquaponics, via repo report](https://extension.rwfm.tamu.edu/wp-content/uploads/sites/8/2020/10/Water-Quality-In-Aquaponics-Sink-Masabni.pdf)
- trigger: when pH drops below 6.4, add Ca(OH)₂ or KOH, alternating the two — [NMSU CR680, via repo report](https://pubs.nmsu.edu/_circulars/CR680.pdf)
- equipment: base addition tank 2 ft diameter × 3 ft high, 50 US gal. 0.75 in feed line. 1.25 in return to sump. — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)
- failure mode (chemistry context, not a fish-safety claim): adding base too fast raises pH, which shifts TAN toward NH₃. The sources advise slow addition via a separate tank. — [repo water-chemistry report, citing UVI/SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)
- K₂CO₃ (potassium carbonate): no sizing, dose or price found in this pass.
- prices (KOH, Ca(OH)₂): not found in NL or India.

**D2. Buffer dosing (alkalinity)**
- targets: alkalinity ≥100 mg/L for biofilter optimum — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf). About 100–150 mg/L as CaCO₃ in low-exchange systems — [Ebeling et al. 2006, via repo report](https://www.researchgate.net/profile/James-Ebeling-2/publication/222912406_Engineering_analysis_of_the_stoichiometry_of_photoautotrophic_autotrophic_and_heterotrophic_removal_of_ammonia-nitrogen_in_aquaculture_systems/links/02e7e52dff9afe1088000000/Engineering-analysis-of-the-stoichiometry-of-photoautotrophic-autotrophic-and-heterotrophic-removal-of-ammonia-nitrogen-in-aquaculture-systems.pdf). Operating minimum 50–100 mg/L as CaCO₃ or higher — [SRAC 452, via repo report](https://www.ncrac.org/files/inline-files/SRAC0452.pdf). `[tier_1 | medium | context split, not a contradiction: different system types]`
- demand rule: 7.14 g alkalinity (as CaCO₃) and 4.57 g O₂ per g ammonia-N nitrified. TAN production PTAN (kg/day) = F (kg feed/day) × PC (protein fraction) × 0.092. — [Ebeling, Timmons & Bisogni 2006, via repo report](https://www.researchgate.net/profile/James-Ebeling-2/publication/222912406_Engineering_analysis_of_the_stoichiometry_of_photoautotrophic_autotrophic_and_heterotrophic_removal_of_ammonia-nitrogen_in_aquaculture_systems/links/02e7e52dff9afe1088000000/Engineering-analysis-of-the-stoichiometry-of-photoautotrophic-autotrophic-and-heterotrophic-removal-of-ammonia-nitrogen-in-aquaculture-systems.pdf) `[tier_1 | high | single_source]`. (This is a TAN-N load, not a concentration.)
- **Conflicting by system type:** for RAS, SRAC 452 suggests sodium bicarbonate at about 17–20% of the daily feeding rate — [SRAC 452, via repo report](https://www.ncrac.org/files/inline-files/SRAC0452.pdf). An aquaponics extension source cited in the repo water-chemistry report says "NaHCO₃ should never be added" and recommends alternating KOH/Ca(OH)₂ plus dolomite for Mg. My extraction did not resolve which source that is (footnote 31), so treat it as unverified. `[tier_1 vs unresolved | medium | conflicting (RAS vs aquaponics context split)]`

**D3. pH down: phosphoric or nitric acid** — dose rules, equipment and prices: not found in this pass. The only finding is the pH trade-off: nitrification works best at pH 7–9, hydroponics at 5.8–6.2 (acceptable 5.5–6.5), and UVI compromises at about 7.0 — [repo water-chemistry report citing UVI page](https://www.uvi.edu/research/agricultural-experiment-station/aquaculture-home/aquaponic-systems/index.html); [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)

**D4. Peristaltic dosing pumps / pH controllers** — candidate NL/EU listings were found but not read (budget; see Gaps). No price, flow, power or tubing-life value is recorded.

**D5. UV steriliser (UV-C)**
- function / constraint: microorganisms must pass within about 0.5 cm of the lamp. Pre-filtration is required. Units are rated by flow capacity, and lower flow through the unit improves efficiency. No dose value is given. `[tier_1 | high | single_source]` — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)
- example retail unit (NL): AquaForte RVS Power Plus UV-C 75 W (stainless housing, T5 lamp). Max 23,000 L/h. Ponds up to 75 m³ without fish, 37.5 m³ with fish, 18.75 m³ for koi. €264.95 incl. BTW. toppy.nl, read 2026-11-25. `[tier_3 | medium: retailer copy of manufacturer specs | single_source]` — [toppy.nl AquaForte RVS Power UV-C 75 W](https://www.toppy.nl/product/5328/aquaforte-rvs-power-uv-c-t5-75-watt.html)
- lifetime: T5 lamp about 9,000 burning hours (about one year), still giving 80% UV-C output after that. Ballast about 5 years. Replacement lamp: €49.95 incl. BTW, 9,000 h, "vervang je de UV-C lamp jaarlijks" (replace the lamp yearly). `[tier_3 | medium: two retailer pages from the same seller, which is not independent | single_source]` — [toppy.nl UV-C unit](https://www.toppy.nl/product/5328/aquaforte-rvs-power-uv-c-t5-75-watt.html); [toppy.nl replacement lamp](https://www.toppy.nl/product/5330/aquaforte-uv-c-lamp-t5-75w-voor-power-uv-c-en-power-signal.html)
- power: 75 W UV-C rating. Total electrical draw is not stated.
- India: UV units are listed as a RAS component in the NFDB booklet, with no cost — [NFDB RAS booklet](https://static.vikaspedia.in/mediastorage/document/Ras_Booklet_Eng.pdf). The IndiaMART UV category page failed to load.

**D6. Ozone generator**
- constraints: ozone must be generated on site because it breaks down within 10–20 minutes. Residual ozone entering the culture tank "is toxic to fish and crustaceans" (source statement). No dose or contact time is given. `[tier_1 | high | single_source]` — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)
- NL "AquaForte T5 Ozon Redox UVC 75 watt" exists (combined UV/ozone unit) but was not read — [toppy.nl](https://www.toppy.nl/product/5628/aquaforte-t5-ozon-redox-uvc-75-watt.html). India ozone listings were found but not read (see Gaps). No price recorded.

**D7. Source-water treatment (RO, sediment and carbon filtration, dechlorination)**
- UVI: make-up water enters through an automatic valve from a dechlorinated source `[tier_1 | high | single_source]` — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)
- RO unit, sediment and carbon cartridge sizing, lifetimes and prices: not found in this pass.

**D8. Iron chelate and nutrient supplements**
- iron: target Fe about 2.0 mg/L using chelated iron. Fe-DTPA is preferred because it stays soluble at pH 7.0. No gram dose is given. `[tier_1 | high | single_source]` — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)
- K and Ca are supplied through the KOH/Ca(OH)₂ base additions (D1). Dolomite is used for Mg (unresolved source, see D2).
- nutrient context: TDS 200–400 ppm (EC 0.3–0.6 mmho/cm) is typical in UVI. Phytotoxicity occurs above 2,000 ppm TDS or 3.5 mmho/cm EC. Nitrate is regulated between 1 and 100 mg/L through cleaning frequency (i.e. how often the filter tanks are cleaned). — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)
- prices for Fe-DTPA, Fe-EDDHA and supplements: not found.

### Inferences
- Scale suitability (inference from source context, not from a source statement):
  - FAO-type mechanical separators (swirl or radial, 20–500 L), media beds as biofilters, and bioballs fit hobby scale. The FAO table stops at 12 m² of growing area.
  - The UVI clarifier + orchard-netting filter tanks + degassing tank train fits small-commercial to commercial coupled DWC.
  - Radial-flow settlers, microscreen drum filters at 375–1,800 L/min, bead filters and MBBR fit small-commercial to commercial RAS and decoupled systems.
  - The 25 m³/h AquaForte drum filter is a koi-pond product, at the upper hobby to small-commercial range.
- NFT and DWC have lower solids tolerance than media beds, so they depend more on separate solids removal (FAO says a mechanical separator is required for NFT/DWC). Dutch bucket, tower and ebb-and-flow systems were not covered by any source read.
- Several sources treat solids capture and mineralisation as competing goals. UVI captures 100% of particulates in two stages but holds them for days in the filter tanks. Decoupled systems move this to separate reactors. Neither path has a quantified mineralisation rate in the evidence gathered.
- The two SRAC 453 editions should be stored as separate context-tagged values (1999 vs 2013), not merged.

### Gaps
- Filter socks, mats and brushes, Japanese mat or static sponge, K₂CO₃, phosphoric and nitric acid, RO, sediment and carbon units, ozone sizing, peristaltic pump specs, and mineralisation reactor rates: no source read in this pass.
- Timmons & Ebeling, *Recirculating Aquaculture* (textbook): not accessed. Only the Ebeling, Timmons & Bisogni 2006 TAN/alkalinity stoichiometry was obtained, via the repo report. Radial-flow, swirl, bead and MBBR design equations from the textbook remain a gap.
- FAO 589 original PDF: not read directly. Values come from a FarmHub reproduction. FAO's degassing, mineralisation, bird-netting and swirl-filter text still needs to be read from the original.
- SRAC 454 extraction listed clarifier retention as "<1 day" in the context of settleable solids. This is ambiguous and was not used. The UVI 20-minute figure is used instead.
- Power (rated W and duty hours) is missing for almost everything except the AquaForte drum filter (80 W excl. rinse pump) and the UV-C (75 W UV-C rating).
- Minutes per maintenance task: not found for any item.

## Typical price ranges per market

### Takeaway
NL/EU: one koi-grade AquaForte drum filter (25 m³/h) was last listed at €983.20 incl. BTW (discontinued). A 75 W stainless UV-C costs €264.95 incl. BTW and its replacement lamp €49.95. India: IndiaMART RAS drum filters run from ₹75,000 to ₹5,00,000 per unit (GST status not stated), and MBBR media from ₹6,500 to ₹27,500 per m³ (mostly wastewater-grade). PMMSY whole-RAS cost norms are ₹0.5 lakh (backyard), ₹7.5 lakh (small), ₹25 lakh (medium) and ₹50 lakh (large). Bead filters, dosing, RO, ozone and chemicals have no price yet.

### Cited Findings
**Netherlands / EU (priority 1)** — all tier_3, read 2026-11-25
- AquaForte Trommelfilter incl. lid + controller: €983.20 incl. BTW (was €1,229). Seller toppy.nl. Unit: each. Status "Niet meer leverbaar". — [toppy.nl](https://www.toppy.nl/product/7172/aquaforte-trommelfilter.html) `[tier_3 | medium: retail listing of a discontinued item | single_source]`
- AquaForte RVS Power Plus UV-C 75 W: €264.95 incl. BTW, each, toppy.nl — [toppy.nl](https://www.toppy.nl/product/5328/aquaforte-rvs-power-uv-c-t5-75-watt.html) `[tier_3 | medium | single_source]`
- AquaForte UV-C T5 75 W replacement lamp: €49.95 incl. BTW, each, toppy.nl — [toppy.nl](https://www.toppy.nl/product/5330/aquaforte-uv-c-lamp-t5-75w-voor-power-uv-c-en-power-signal.html) `[tier_3 | medium | single_source]`
- Evolution Aqua Kaldnes K1, 50 L bag: £85.95 (RRP £95.95). VAT status not stated. Seller Pondkeeper (UK). Shipping to NL not verified. Recorded as a near-market reference only. — [Pondkeeper](https://www.pondkeeper.co.uk/evolution-aqua-kaldnes-k1-bio-media-50-litres) `[tier_3 | medium | single_source]`

**India (priority 2)** — tier_3 listings, read 2026-11-25. GST status not stated in the extracted listings. Unit not stated for drum filters (single listed figure).
- Drum filters (RAS / aquaculture) on IndiaMART — [IndiaMART drum filters](https://m.indiamart.com/impcat/drum-filters.html):
  - ₹75,000 — Water Treatment Technologies Company, Gurgaon. SS, "10,000 LPH to 5,00,000 LPH".
  - ₹78,900 — Pureflow Biofloc Innovations, **Bengaluru (Karnataka)**. "All In One Combi Drum Filter". Use not stated.
  - ₹89,000 — Bharat Aquaculture Technology, Gwalior. Aluminium, 20 m³/h.
  - ₹1,00,000 — Sharp Engineering Associates, Pune. "Fish Farm Drum Filter".
  - ₹1,35,000 — Macsun Technologies, Gurugram. SS.
  - ₹1,50,000 — Global Aquaculture Solution, Kurukshetra. SS, for RAS.
  - ₹1,95,000 — R S Polymers, New Delhi. 25,000 L/h, 1 HP. Title says aluminium but "MAKE: SS 304" (internal conflict in listing).
  - ₹2,50,000 — Sai Systems, Vadodara. SS.
  - ₹5,00,000 — Vivek Industries, Thane. SS, 100 m³/h.
  - `[tier_3 | low: B2B "starting" prices with no mesh/specs on most | single_source per listing]`
- MBBR media on IndiaMART (all per m³) — [IndiaMART MBBR media](https://m.indiamart.com/impcat/mbbr-media.html):
  - K1-type, 25 mm, 500 m²/m³, HDPE, 100 kg/m³ bulk density: ₹19,800/m³ (BK Enviro Tech, Faridabad).
  - 22 mm PP, 400 m²/m³: ₹6,500–₹9,600/m³ across several sellers, including ₹9,600/m³ from Bajrang Enviro Engineers, **Hyderabad (Telangana)**.
  - "Virgin White HDPE" (the only listing that mentions aquaculture farms): ₹13,000/m³ (Netroflux, New Delhi).
  - Full range of the 25 listings: ₹6,500–₹27,500/m³. One carousel price of ₹1,000/m³ looks like an error and is excluded.
  - `[tier_3 | low: mostly sewage-treatment-grade products; food or virgin-material grade not verified | single_source per listing]`
- PMMSY/NFDB RAS unit cost norms (whole RAS units, not per item) — [NFDB RAS booklet (vikaspedia mirror)](https://static.vikaspedia.in/mediastorage/document/Ras_Booklet_Eng.pdf) `[tier_1 | medium: government cost norm, but no year stated in the document and the medium-RAS description is internally inconsistent | single_source]`:
  - Large RAS: ₹50.00 lakh — 8 tanks, minimum 90 m³ per tank, 40 t/crop.
  - Medium RAS: ₹25.00 lakh — 6 tanks, minimum 30 m³ per tank. The cost breakup says 4 tanks of minimum 90 m³ (conflict inside the document).
  - Small RAS: ₹7.50 lakh — 1 tank, 100 m³.
  - Backyard mini RAS: ₹0.50 lakh.
  - Capital cost per tank: ₹4.5 lakh. Electricity cost line: ₹3.00 lakh (large), ₹1.50 lakh (medium), ₹0.40 lakh (small). The period is not stated.
  - The equipment list includes drum filter, biofilters, UV, degasser ("carbon dioxide trapper"), settling tanks and sump, with no per-item cost.
- State differences: only one Karnataka seller (Bengaluru, drum filter) and one Telangana seller (Hyderabad, MBBR) appeared. No Tamil Nadu or Andhra Pradesh seller appeared in the listings read.

**Global reference (priority 3)**
- Drum filters (US, 1999 prices): the smallest commercial unit (about 475 L/min at 25 mg/L SS) cost about $6,000. A 950 L/min unit cost about $9,000. "Doubling capacity raises cost about 50%." `[tier_1 | medium: authoritative source, but prices are about 27 years old | single_source]` — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)

### Inferences
- Indian drum filter prices span almost 7× (₹75,000 to ₹5,00,000) with mostly undisclosed flow and mesh, so they cannot be compared per m³/h without the specs.
- Generic Indian "K1-type" media (₹19,800/m³ at 500 m²/m³) appears to be the local equivalent of Kaldnes knockoffs. Whether it performs like the Kamstra et al. K1 rates is not evidenced.
- PMMSY norms are whole-system capital norms and should not be split into per-item prices.

### Gaps
- Pages found but not read (fetch budget exhausted). These are the next reads:
  - NL bead filters: [EB 40](https://www.toppy.nl/product/2928/beadfilter-aquaforte-econobead-eb-40.html), [EB 100](https://www.toppy.nl/product/2931/beadfilter-aquaforte-econobead-eb-100.html) (a later retry returned a site-side client error, so the page may no longer exist), [EB 140](https://www.toppy.nl/product/2932/beadfilter-aquaforte-econobead-eb-140.html), [beadfilter category](https://www.toppy.nl/category/1169/vijverfilter/beadfilters.html).
  - Other NL drum filters: [AquaForte Drumfilter XL (sibo.nl)](https://sibo.nl/en/product-groups/koi-pond/aquaforte-drumfilter-xl), [vijverleven.nl AquaForte trommelfilter](https://vijverleven.nl/en/products/aquaforte-trommelfilter), [aqua-forte.com Drum filter P (manufacturer)](https://aqua-forte.com/products/pond-swimming-pond-filters/drum-filters/drum-filter-p).
  - Pressure filter with UV on bol.com: [BluPressure Smart Control 10.000](https://www.bol.com/nl/nl/p/blupressure-smart-control-10-000-drukfilter-voor-vijver-inclusief-11w-uv-c-backwashfunctie-uv-timer/9300000174746038/).
  - Dosing: [W'eau peristaltic pump (toppy)](https://www.toppy.nl/product/22951/w-eau-peristaltische-doseerpomp.html), [Verder MP2 Speedy pH](https://www.verderliquids.com/be/nl/microdos/mp2-serie/mp2-speedy-ph), [Hanna GroLine HI981412](https://www.hannaservice.eu/groline-ph-dosing-system-hi981412-00-product), [AC Infinity dosing kit (US)](https://acinfinity.com/peristaltic-pump-two-outlet-dosing-kit-for-hydroponics-10-level-control-210-ml-min/).
  - UV/ozone: [AquaForte T5 Ozon Redox UVC 75 W](https://www.toppy.nl/product/5628/aquaforte-t5-ozon-redox-uvc-75-watt.html), [IndiaMART water ozonizer](https://m.indiamart.com/impcat/water-ozonizer.html), [IndiaMART ozone generators](https://m.indiamart.com/impcat/ozone-generators.html).
- PMMSY subsidy percentages and the cost-norm year: not in the document read. The [J&K PMMSY pattern-of-assistance PDF](https://fisheries.jk.gov.in/PMMSY/PMMSY-Pattern%20of%20Financial%20Assistance.pdf) and [NFDB RAS 2017 PDF](https://nfdb.gov.in/PDF/E%20Publications/8%20Recirculatory%20Aquaculture%20System_RAS%202017.pdf) failed to load (robots.txt unreachable).
- No price found for: bead filters, filter socks/mats/brushes, Japanese mat, sand filters, orchard netting, KOH, Ca(OH)₂, K₂CO₃, phosphoric/nitric acid, iron chelate, RO, sediment/carbon, ozone, dosing pumps, or any Amazon.in listing. No NL K1 price, and no PR Aqua or Dutch RAS-supplier prices.

## Sizing rules from UVI, FAO 589, SRAC and Timmons & Ebeling

### Takeaway
UVI (SRAC 454) gives a complete coupled-DWC solids train: a 3.8 m³ cone clarifier at about 20 min HRT, two 0.7 m³ orchard-netting tanks and a 0.7 m³ degassing tank, with feed ratios of 60–100 g/m²/day for raft. FAO 589 gives small-scale ratios: mechanical separator at 10–30% of fish tank volume, 1 L gravel or 0.5 L bioballs per g of daily feed, and 40–50 g/m²/day (leafy) or 50–80 g/m²/day (fruiting). SRAC 453 gives feed-loading criteria per biofilter type, and its 1999 and 2013 editions conflict.

### Cited Findings
- UVI clarifier train, base tank and iron target: see A1, C1, C2, D1, D8 — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf) `[tier_1 | high | single_source except clarifier HRT, which is corroborated by UVI 25 Years]`
- Feeding-rate ratio: **context split.** UVI raft: 60–100 g feed/m²/day, with 80 used in the worked example — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf). FAO small-scale: 40–50 g/m²/day for leafy greens and 50–80 for fruiting crops, 32% protein feed — [FAO 589 via FarmHub](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/). `[tier_1 | high | conflicting values explained by context (commercial tilapia raft vs small-scale mixed systems)]`
- FAO biofilter and separator rules: see A3 and B6 — [FAO 589 via FarmHub](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/)
- FAO stocking used with those rules: maximum 20 kg fish per 1,000 L (range 10–20). Halve that below 500 L tanks. — [FAO 589 via FarmHub](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/)
- SRAC 453 (1999) biofilter loading (kg feed/day per m³ medium): RBC 3.6 (see B3 note on the transcription mismatch), trickling 3.6, bead 13, moving bed 16–23, fluidised sand 20–40. All assume 2.5% of feed becomes TAN. — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)
- SRAC 453 (2013) loading: fluidised sand 16–32, bead 16–32 under optimised washing, MBBR 8–16 kg feed/m³/day. Clarifier HRT 15–30 min, depth >1.2 m, L:W 4:1–8:1. — [SRAC 453 (2013), via repo report](https://agrilife.org/fisheries/files/2013/09/SRAC-Publication-No.-453-Recirculating-Aquaculture-Tank-Production-Systems-A-Review-of-Current-Design-Practice.pdf)
- Surface-loading anchor for settlers: 0.0031 m³/s per m² — [Davidson & Summerfelt 2005 via GSA Advocate](https://www.globalseafood.org/advocate/settler-evaluation-radial-flow-vs-tangential-flow/)
- Area-based MBBR nitrification: 0.14–0.97 g N/m²/day (farm to lab scale). Treatment means span 0.24–2.63. — [Kamstra et al. 2017](https://core.ac.uk/download/249978494.pdf)
- Timmons/Ebeling stoichiometry: PTAN = F × PC × 0.092. 4.57 g O₂ and 7.14 g alkalinity per g N nitrified. — [Ebeling, Timmons & Bisogni 2006, via repo report](https://www.researchgate.net/profile/James-Ebeling-2/publication/222912406_Engineering_analysis_of_the_stoichiometry_of_photoautotrophic_autotrophic_and_heterotrophic_removal_of_ammonia-nitrogen_in_aquaculture_systems/links/02e7e52dff9afe1088000000/Engineering-analysis-of-the-stoichiometry-of-photoautotrophic-autotrophic-and-heterotrophic-removal-of-ammonia-nitrogen-in-aquaculture-systems.pdf)
- System oxygen-demand rule of thumb: about 0.5 kg O₂ per kg feed in a well-designed system. This is a source statement used for sizing context, not a total-oxygen-demand claim. — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)

### Inferences
- The SRAC loading criteria imply that feed rate, not fish tank volume, is the common sizing driver across sources. FAO also states its rules per g of daily feed, which makes these rules compatible with the repo's feed-input Mode A.
- The manufacturer's K1 claim (5 kg feed/m³/day, derived) is below both SRAC editions. A component database should keep it as a separate `manufacturer_claim` context.

### Gaps
- Timmons & Ebeling textbook design tables (radial-flow and swirl overflow rates, drum filter hydraulic loading, MBBR volumetric TAN rates), the UVI mineralisation rate and FAO degassing/mineralisation tank sizing were not obtained.
- No sizing rule was found for UV dose (mJ/cm²) or ozone dose (g O₃/kg feed).

## Reported lifetimes, maintenance and labour

### Takeaway
Hardly any lifetime data exists in the sources read. The only figures are a UV-C T5 lamp at about 9,000 h (about 1 year, still 80% output after that), a ballast at about 5 years, and a 2-year drum filter warranty (which is not a lifetime), all from one retailer. Maintenance frequencies are better documented: UVI removes clarifier sludge 3× daily, cleans the netting tanks 1–2× weekly, replaces the clarifier grazer fish about every 4 months, and adds base several times weekly. Bead filters backwash every 1–48 h. Minutes per task were not found for any item.

### Cited Findings
- UV-C lamp 9,000 h, replace yearly, 80% output after 9,000 h, ballast about 5 years — [toppy.nl UV-C](https://www.toppy.nl/product/5328/aquaforte-rvs-power-uv-c-t5-75-watt.html); [toppy.nl lamp](https://www.toppy.nl/product/5330/aquaforte-uv-c-lamp-t5-75w-voor-power-uv-c-en-power-signal.html) `[tier_3 | medium: retailer restating manufacturer specs | single_source]`
- Drum filter warranty "2 jaar" — [toppy.nl](https://www.toppy.nl/product/7172/aquaforte-trommelfilter.html) `[tier_3 | medium | single_source]`
- K1: no lifetime claim. "Self-cleaning", "requires no maintenance" — [K1/K3 sheet](https://absolute-koi.com/pdf/K1K3media.pdf) `[tier_2 | low: marketing | single_source]`
- UVI clarifier sludge removal 3× daily — [UVI 25 Years, via repo report](https://www.tag2grow.org/wp-content/uploads/2021/09/UVI-Aquaponics.pdf). Netting tanks cleaned 1–2× weekly. Clarifier tilapia replaced about every 4 months. Base added several times weekly. — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf) `[tier_1 | high | single_source]`
- Bead filter backwash interval 1–48 h — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)
- Drum filter backwash water about 13.4% of the settling-basin equivalent (Libey 1993) — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)
- RBC medium weight can increase up to 10-fold with biofilm, which is a structural maintenance consideration — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)
- pH measured daily at UVI — [repo water-chemistry report citing UVI page](https://www.uvi.edu/research/agricultural-experiment-station/aquaculture-home/aquaponic-systems/index.html)

### Inferences
- Labour for the UVI-style solids train is frequent but low-skill (sludge draining, spray cleaning). The source gives frequencies but no durations, so labour minutes cannot be filled.

### Gaps
- No service lifetime in years was found for drum filters, bead filters, clarifiers, MBBR media, trickling media, dosing pump tubing, RO membranes, carbon or sediment cartridges, ozone generators or pH probes.
- Minutes per task: not found for any item.

## What growers use instead and what fails

### Takeaway
Documented alternatives include raft hydroponics as the biofilter (UVI: no separate biofilter), media beds as a combined solids and biofilter (FAO, small scale), swirl separators in place of radial-flow settlers (cheaper and compact, but 37% vs 78% TSS removal in one trial), and generic "K1-type" MBBR media sold in India for wastewater. Documented failures are: solids decaying in unclean basins (adds ammonia and oxygen demand), solids sticking to clarifier cone walls, short clarifier HRT capturing less, media-bed clogging creating anaerobic root zones, sand-filter water waste, residual ozone toxicity and UV ineffectiveness without pre-filtration. No forum or anecdote evidence was collected.

### Cited Findings
- Raft surface as biofilter: about 180 g feed/m²/day treated with no separate biofilter (UVI) — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf) `[tier_1 | high | single_source]`
- Media bed as combined filter, and its clogging failure mode — [FAO 589 via FarmHub](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/); repo "Media bed vs DWC vs NFT" corroboration report citing [OSU HLA-6729](https://extension.okstate.edu/fact-sheets/print-publications/hla/nitrification-and-maintenance-in-media-bed-aquaponics-hla-6729.pdf) `[tier_1 | medium | corroborated per repo report]`
- Swirl vs radial: 37.1% vs 77.9% TSS removal — [GSA Advocate / Davidson & Summerfelt 2005](https://www.globalseafood.org/advocate/settler-evaluation-radial-flow-vs-tangential-flow/) `[tier_1 | high | single_source]`
- Generic MBBR media in India: 22–25 mm PP/HDPE at 400–500 m²/m³, ₹6,500–₹19,800/m³, mostly sold for STPs — [IndiaMART](https://m.indiamart.com/impcat/mbbr-media.html) `[tier_3 | low | single_source]`
- Failure modes:
  - Uncleaned settling basins add ammonia and oxygen demand. Swirl separators need a lot of replacement water. Sand filters waste water under heavy feeding. Residual ozone is toxic to fish (source statement). UV needs pre-filtration and 0.5 cm proximity. — [SRAC 453 (1999)](https://aquaculture.o2.boa.ca.uky.edu/sites/aquaculture.ca.uky.edu/files/srac_453_recirculating_aquaculture_tank_production_systems_a_review_of_component_options.pdf)
  - Clarifier cone-wall adhesion. HRT of 9.5 min captured less solids. — [UVI 25 Years, via repo report](https://www.tag2grow.org/wp-content/uploads/2021/09/UVI-Aquaponics.pdf)
  - Nitrifiers become inefficient below 2 mg/L DO — [SRAC 452, via repo report](https://www.ncrac.org/files/inline-files/SRAC0452.pdf)
  - In NFT, solids coat roots and flow interruptions cause rapid wilting. In gravel beds, clogging creates anaerobic zones that kill roots. — repo "Media bed vs DWC vs NFT" corroboration report (repo root PDF). Primary sources not re-read today.
  - Base added too fast shifts TAN to NH₃ (chemistry context) — repo water-chemistry report citing [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)
- Bicarbonate vs hydroxide: RAS practice uses NaHCO₃ (SRAC 452). The aquaponics practice cited in the repo report rejects NaHCO₃ in favour of KOH/Ca(OH)₂, which also supplies plant K and Ca. — see D2 `[conflicting by context]`

### Inferences
- The likely failure chain to model across alternatives is: weak solids capture, then more organic load on the biofilter and roots, then clogging or anaerobic zones. Repo canon already holds this as `solids_carryover_penalties` (draft).

### Gaps
- No forum, blog or video evidence was gathered on DIY barrel swirl filters, DIY MBBR, Kaldnes knockoff performance, filter-sock clogging or Japanese-mat use. Any later claims from such sources must be marked anecdote (tier_3).
- No source documented failure modes of drum filters (e.g. nozzle clogging, motor failure), dosing pumps (tubing wear) or RO units, or what those failures do to fish and plants.
