# Aquaponics/hydroponics equipment inventory: fish handling, harvest and post-harvest, consumables

Scope note: evidence-first inventory notes for a component database, not a farm design. All prices and pages were read on 2026-11-25 unless a different date is stated. Each value carries `[tier | confidence: level, reason | corroboration]`. Tiers follow the brief: tier_1 = peer-reviewed, government statistics or cost norms, utility tariffs, university research-station reports; tier_2 = extension guides, research-institute notes, industry reports, manufacturer datasheets; tier_3 = retail or B2B listings, forums, blogs, videos. No currency has been converted. No value has been estimated. Coverage limit: the shared WebFetch budget for this session ran out partway through the research, so many items below are "not found" because they were not reached, not because no data exists. The Gaps sections list these items and the unread leads.

## Q1. Item inventory: function, system fit, scale, sizing rule, power, lifetime, maintenance, failure modes

### Takeaway
I found sourced attributes for the following:
- Feeding and feed: sizing rules from FAO 589 and SRAC 454.
- Fish harvest practice: draining, or crowding with screens and a fish pump, and grading by selective netting (SRAC 454).
- Cold storage: CoolBot-type rooms and the Ecofrost solar cold room.
- Dosing for iron chelate and the KOH and Ca(OH)2 pH adjusters.
- Fingerlings, seeds and water.

I found no sourced hardware specs or prices in this pass for the following, which are listed in the Gaps section with the fields still missing:
- Fish handling: nets, graders, feeders, purge tanks, transport bags, scales.
- Harvest: knives, crates, wash sinks, spin dryers, packaging, labelling, processing tables.
- Consumables: chemical and nutrient prices, media and plugs.

### Cited Findings

**Fish handling: feeding and feed management (applies to manual, automatic and demand feeders as the sizing basis)**
- Feed-rate ratio for leafy greens: 40-50 g of fish feed per m2 of plant growing area per day. For fruiting vegetables: 50-80 g/m2/day. Both assume a standard feed with 32% protein. Applies to coupled aquaponics (FAO 589 context: small-scale media-bed, NFT and DWC units). [tier_2 (FAO technical manual, read on a mirror) | confidence: high, a widely used FAO manual that states the figure directly | corroboration: single_source (the arktikfish mirror reproduces the same FAO text and is not independent)] — [FAO 589 via farmhub.ag mirror](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/); same text at [arktikfish mirror](https://biblio.arktikfish.com/index.php/small-scale-aquaponic/3003-balancing)
- Fish feeding rate during grow-out: 1-2% of total body weight per day for fish over 50 g. FAO 589 Table 8.1 gives 1% for fish over 100 g. [tier_2 | confidence: high, stated directly | corroboration: context_split with NFDB below, not a conflict] — [FAO 589 via farmhub.ag](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/)
- Feeding rate in an Indian RAS GIFT-tilapia model: "3-5% of the body weight of the fish", fingerling to 500 g over 6 months, with more frequent feeding said to improve growth and FCR. [tier_1 (NFDB, Government of India cost norm) | confidence: medium, the document is undated and has internal arithmetic inconsistencies | corroboration: context_split vs FAO 589 (different life stage and system type: RAS fingerling-to-harvest vs aquaponics grow-out >50 g)] — [NFDB, Recent Trends in Aquaculture: RAS](https://nfdb.gov.in/PDF/RAS%20RT.pdf)
- FAO 589 says to treat the feed rate as a guide and adjust it to nitrate tests. If nitrate is below 5 mg/L, increase daily feed slowly. If nitrate is stable, check for deficiencies, especially calcium, potassium and iron. If nitrate rises above 150 mg/L, exchange water occasionally. This links the "chemicals" consumables (Ca, K and Fe supplements) to an operating trigger. [tier_2 | confidence: high | corroboration: single_source] — [FAO 589 via farmhub.ag](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/)
- Stocking-density guidance in FAO 589: 10-20 kg of fish per 1,000 L, and new farmers should not exceed 20 kg/1,000 L. For tanks under 500 L, halve it to 1 kg/100 L. FAO 589 does not recommend growing fish for food in tanks that small. Reference tilapia sizes are about 50 g at stocking and 500 g at harvest. [tier_2 | confidence: high | corroboration: single_source] — [FAO 589 via farmhub.ag](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/)
- Failure mode (affects holding, purge and transport tanks, and any high-density fish handling): at high stocking density without a reliable power supply, "a brief interruption ... can kill all fish within an hour" (FAO 589 paraphrase on the mirror page). FAO 589 names high density as a common root cause of fish stress. [tier_2 | confidence: medium, the mirror page paraphrases the statement | corroboration: single_source] — [FAO 589 via farmhub.ag](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/)
- The FAO 589 mirror page gives no grading or purging rules. [n/a] — [FAO 589 via farmhub.ag](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/)
- SRAC 454 describes fish-handling practice in commercial raft (UVI-type) coupled aquaponics. At harvest, "the rearing tank is drained and all of the fish are removed". The alternative is "to crowd the fish with screens and pump them to another tank with a fish pump". Sequential rearing uses selective netting with a grading system. SRAC 454 does not mention purging or seining, and it names no feeder type: feed is judged by watching the ad libitum feeding response. [tier_2 (USDA SRAC extension fact sheet, Rakocy, Masser & Losordo; undated excerpt, possibly a 2016 reprint) | confidence: medium, a practice description without quantities | corroboration: single_source] — [SRAC 454, Recirculating Aquaculture Tank Production Systems: Aquaponics](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)
- SRAC 454 says salt is added to commercial fish feed during manufacture. A producer could request feed without added salt if fish health is not affected. This is a feed-specification note for coupled systems. [tier_2 | confidence: medium | corroboration: single_source] — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)

**Fish handling: other hardware**
- Dip nets, seine nets, bar graders, grading boxes, automatic belt/clockwork feeders, demand feeders, purge/depuration tanks, transport bags and tanks, and scales: not found. See Gaps.

**Harvest and post-harvest: cold storage**

*Item: CoolBot-type walk-in cooler (controller plus window or split air conditioner in an insulated room)*
- Function: holds a DIY insulated room at chill temperatures with a standard room air conditioner. The CoolBot controller overrides the AC thermostat and cycles the unit to prevent ice on the AC coils. [tier_2 (Engineering for Change product library) | confidence: medium, a solutions database with no dated spec | corroboration: single_source] — [E4C: CoolBot walk-in cooler](https://www.engineeringforchange.org/solutions/product/coolbot-walk-cooler/)
- Sizing rule: room size versus AC size, for a room held at 38 F (3.3 C) and opened no more than 4 times per hour. 6x8x8 ft room: 10,000 BTU. 8x8x8 ft: 12,000 BTU. 8x10x8 ft: 15,000 BTU. 8x12x8 ft: 18,000 BTU. 10x14x8 ft: 24,000 BTU. [tier_2 | confidence: medium, a vendor-derived table republished by E4C | corroboration: single_source] — [E4C: CoolBot](https://www.engineeringforchange.org/solutions/product/coolbot-walk-cooler/)
- Sizing and undersizing failure: "A 5,000 BTU unit won't cool a 10 ft x 15 ft room efficiently." An 8x8 ft room with an 18,000 BTU AC can reach and hold below 36 F (2 C). Even in ideal conditions a 24,000 BTU AC bottoms out at 33 F (1 C). [tier_2 (retailer technical sheet) | confidence: medium | corroboration: single_source] — [Johnny's Selected Seeds: CoolBot limitations](https://www.johnnyseeds.com/on/demandware.static/-/Library-Sites-JSSSharedLibrary/default/dw5a0081d0/assets/information/8274-coolbot-limitations.pdf)
- Power and duty: a well-insulated room with a properly sized AC "may need to run less than 25% of the time". No wattage is given. Pull-down from 30 C: about 20 minutes to 7 C, about 30 more minutes to 4 C, and about 30 more to 3 C. [tier_2 | confidence: low for duty hours, stated as "may" | corroboration: single_source] — [Johnny's CoolBot limitations](https://www.johnnyseeds.com/on/demandware.static/-/Library-Sites-JSSSharedLibrary/default/dw5a0081d0/assets/information/8274-coolbot-limitations.pdf)
- Insulation requirement: "Industry standard for walk-in coolers is R-25" for operation below 40 F (5 C), roughly at least 4 inches of rigid foam, installed over the studs rather than between them. [tier_2 | confidence: medium | corroboration: single_source] — [Johnny's CoolBot limitations](https://www.johnnyseeds.com/on/demandware.static/-/Library-Sites-JSSSharedLibrary/default/dw5a0081d0/assets/information/8274-coolbot-limitations.pdf)
- Minimum temperature: the two sources conflict. Johnny's says the CoolBot cannot reach or hold freezing and has a floor of 33 F (1 C). E4C lists a minimum internal temperature of 0 C. [tier_2 both | confidence: medium | corroboration: conflicting] — [Johnny's](https://www.johnnyseeds.com/on/demandware.static/-/Library-Sites-JSSSharedLibrary/default/dw5a0081d0/assets/information/8274-coolbot-limitations.pdf); [E4C](https://www.engineeringforchange.org/solutions/product/coolbot-walk-cooler/)
- Lifetime: 5 years expected, with a 1-year warranty (basis: E4C listing, not field data). [tier_2 | confidence: low, no stated basis for the 5 years | corroboration: single_source] — [E4C: CoolBot](https://www.engineeringforchange.org/solutions/product/coolbot-walk-cooler/)
- Maintenance and labour: minutes per task were not found. E4C lists the AC and compressor as the replacement components. [tier_2 | confidence: low | corroboration: single_source] — [E4C: CoolBot](https://www.engineeringforchange.org/solutions/product/coolbot-walk-cooler/)
- Failure modes:
  - More than 6 door openings per hour may make a CoolBot a poor fit, so strip curtains are recommended.
  - Some AC units do not auto-restart after a power blink and must be switched back on by hand. The CoolBot itself restarts and keeps its settings.
  - Winter operation depends on the AC model.
  - [tier_2 | confidence: medium | corroboration: single_source] — [Johnny's CoolBot limitations](https://www.johnnyseeds.com/on/demandware.static/-/Library-Sites-JSSSharedLibrary/default/dw5a0081d0/assets/information/8274-coolbot-limitations.pdf)
- Price: USD 4,200 "Market Suggested Retail Price". The listing gives no date for the price (page updated 2023-12-26), and it is not clear whether the figure covers the controller alone or a full cooler package. Read 2026-11-25. [tier_2 | confidence: low, undated and the scope is ambiguous | corroboration: single_source] — [E4C: CoolBot](https://www.engineeringforchange.org/solutions/product/coolbot-walk-cooler/)
- Scale: no source states a scale fit. See Inferences.

*Item: Ecofrost solar micro cold room (Ecozen, India)*
- Function: off-grid solar-powered cold room with thermal (not battery) energy storage. [tier_2 (E4C product library, manufacturer-supplied data) | confidence: medium | corroboration: single_source] — [E4C: Ecofrost](https://www.engineeringforchange.org/solutions/product/ecofrost-micro-cold-storage/)
- Capacity and dimensions: about 5-6 tonnes. External size 20 x 8 x 8 ft. [tier_2 | confidence: medium | corroboration: single_source] — [E4C: Ecofrost](https://www.engineeringforchange.org/solutions/product/ecofrost-micro-cold-storage/)
- Power: 2.5-3.5 kW of PV panels. The unit stores energy as heat and can run about 36 hours on backup in cloudy weather. A control-system battery has a 5-year warranty. Power consumption is not stated. The unit "runs constantly", so duty is 24 h. [tier_2 | confidence: medium | corroboration: single_source] — [E4C: Ecofrost](https://www.engineeringforchange.org/solutions/product/ecofrost-micro-cold-storage/)
- Temperature: minimum 2 C, with selectable ranges of 2-10 C and 10-20 C. [tier_2 | confidence: medium | corroboration: single_source] — [E4C: Ecofrost](https://www.engineeringforchange.org/solutions/product/ecofrost-micro-cold-storage/)
- Maintenance: the first year of maintenance and on-site support is free. Parts and technical support come from Ecozen. The unit is assembled in Pune. Lifetime: not stated. [tier_2 | confidence: medium | corroboration: single_source] — [E4C: Ecofrost](https://www.engineeringforchange.org/solutions/product/ecofrost-micro-cold-storage/)
- Price: USD 18,058.00 "market suggested retail price", undated (E4C page updated 2023-12-26). Read 2026-11-25. An INR price from Ecozen was not found. [tier_2 | confidence: low, undated and in USD for an Indian product | corroboration: single_source] — [E4C: Ecofrost](https://www.engineeringforchange.org/solutions/product/ecofrost-micro-cold-storage/)

*Cold-store volume rule (general, meat context)*
- In FAO's meat cold-store manual, gross volume is "about 50 percent greater than net volume" and gross area is about 25% greater than net area. Storage density is defined per net (useful) m3 but is most commonly quoted against gross volume. The stacking limit is 40-60 cm below the ceiling. These are meat cold-store figures, not produce or fish figures, so treat them as a context split. [tier_2 (FAO manual) | confidence: medium, the table of per-m3 densities was garbled in extraction | corroboration: single_source] — [FAO: Manual on meat cold store operation and management](https://www.fao.org/4/t0098e/T0098E03.htm)

*Walk-in cold room (conventional), reefer container, home freezer*: not found. See Gaps.

**Harvest and post-harvest: knives, crates, wash tanks, spin dryers, packaging, labelling, fish processing tables**: not found. See Gaps.

**Consumables: fish feed**
- NFDB RAS model for GIFT tilapia: feed 28-30% protein floating pellets at Rs 30/kg, FCR 1:1.3, 3.51 MT of feed for 6,000 fish per 90 m3 tank over a 6-month crop to 500 g harvest size. The document's own arithmetic is inconsistent: 3.51 MT at Rs 30/kg does not equal the Rs 0.77 lakh feed line. [tier_1 | confidence: medium, undated, with internal inconsistencies | corroboration: single_source for the norm] — [NFDB RAS](https://nfdb.gov.in/PDF/RAS%20RT.pdf)
- Feed prices by market: see Q2.

**Consumables: fingerlings**: see Q2 and Q3.

**Consumables: seeds**: see Q2.

**Consumables: water**
- Make-up water norm in an Indian RAS: "not more than 10% of the total water volume of the system is replaced daily" (RAS, not aquaponics). [tier_1 | confidence: medium | corroboration: single_source] — [NFDB RAS](https://nfdb.gov.in/PDF/RAS%20RT.pdf)
- Tariffs: see Q4.

**Consumables: chemicals, nutrients, media and plugs**
- Iron chelate in coupled raft aquaponics: iron "must be supplemented with chelated Fe+2 so that the concentration of Fe+2 is 2.0 milligrams per liter". [tier_2 (SRAC extension fact sheet) | confidence: medium, a dosing target with no product or pack size | corroboration: single_source in this pass] — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)
- pH adjusters that also supply K and Ca: KOH and Ca(OH)2 are added in equal amounts, "usually 500 to 1,000 g", alternated several times weekly to hold pH near 7.0. SRAC 454 does not state the system volume this dose applies to; the UVI system is the context. Dolomite can serve as the pH base when Mg is limiting. Sodium bicarbonate should not be used for pH control. [tier_2 | confidence: medium, the dose is tied to an unstated system volume | corroboration: single_source] — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)
- FAO 589 trigger (see above): stable nitrate is a cue to check Ca, K and Fe. [tier_2] — [FAO 589 via farmhub.ag](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/)
- Prices for KOH, Ca(OH)2, Fe-DTPA or Fe-EDDHA chelate, A+B hydroponic nutrients, clay pebbles, rockwool and plugs: not found.

### Inferences
- CoolBot-type rooms appear suited to hobby and small-commercial scales, because the published sizing table stops at a 10x14x8 ft room with a 24,000 BTU AC. This scale fit is my inference and no source states it.
- The Ecofrost unit is a single 5-6 t room that runs continuously on solar. It seems aimed at small-commercial use in off-grid or weak-grid India, but no source states that scale fit.
- The FAO meat cold-store gross-to-net rule is the only generic volume rule found. Applying it to leafy greens or fish would be a context transfer, not an evidence-backed rule.
- The FAO 589 feed-rate ratio (g feed per m2 of grow area per day) is the natural sizing input for feeder capacity and for feed as a consumable in coupled aquaponics. NFDB's % of body weight and FCR norms apply to RAS fish-side sizing. Keep them as separate context-tagged facts.

### Gaps
- Not found in this pass (fetch budget ran out), with every field still missing (function details, dimensions, capacity, power, lifetime, labour minutes, price, failure modes):
  - Fish handling: dip nets, seine nets, bar graders, grading boxes, automatic belt/clockwork feeders, demand feeders, purge/depuration tanks, fish transport bags (including oxygen packing) and tanks, scales.
  - Harvest and post-harvest: harvest knives and shears, food-grade crates, washing tanks and sinks, commercial salad spinners and spin dryers, conventional walk-in cold rooms, reefer containers, packaging (clamshells, sleeves, bags), labelling, fish processing tables.
  - Consumables: prices and pack sizes for pH adjusters (KOH, Ca(OH)2, acids), iron chelate (DTPA or EDDHA), and potassium and calcium supplements. Only SRAC 454 dosing practice was found. Nothing at all was found for hydroponic A+B nutrient, replacement media (clay pebbles, rockwool, coco), or rockwool or peat plugs.
- Labour minutes per task were not found for any item.
- No duty-hours figure was found for a conventional cold room, only the CoolBot "<25% of the time" statement.
- The FAO 589 harvesting and fish-processing sections (purging, humane slaughter) were not read. They are likely in FAO 589 chapters 7-8 on the same mirror site but were not fetched.

## Q2. Price ranges per market

### Takeaway
India had the most usable prices in this pass: IndiaMART feed at Rs 34-47/kg for 24-30% protein floating feed in Hyderabad and Guntur, government fingerling rates, and one basil seed packet price. Netherlands/EU prices were found only for water. Feed, fingerling and seed prices for NL/EU were not found. Global (US) prices were found only for cold rooms (CoolBot, and Ecofrost in USD).

### Cited Findings

**(1) Netherlands / EU**
- Fish feed: Alltech Coppens GmbH (Nettetal, Germany) lists a 25 kg, 4.5 mm sinking trout feed on faie.at (Austria). The listing showed no price, protein or fat values when fetched. [tier_3 | confidence: low, no price shown | corroboration: n/a] — [faie.at listing](https://www.faie.at/en/artikel/fattening-food-trout-ultra-sinking/130041)
- Skretting and Aller Aqua EU tilapia feed prices: not found.
- Tilapia fingerlings: Til-Aqua (Someren, NL) supplies all-male-producing broodstock (YY "Natural Male Tilapia", silver and red strains) to hatcheries. The article does not say it sells fingerlings to grow-out farms, and it gives no prices. [tier_2 (trade press, 2016-10-13) | confidence: low, a 2016 article whose current status is unknown | corroboration: single_source] — [Hatchery International](https://www.hatcheryinternational.com/dutch-tilapia-producer-highlights-global-water-and-hormone-c-1428/)
- African catfish fingerlings: the Fleuren & Nooijen hatchery is listed in a Dutch business directory. No price was found. [tier_3 | confidence: low | corroboration: n/a] — [liza.nl directory](https://www.liza.nl/en/17057232/fleuren-nooijen)
- Seeds: Rijk Zwaan publishes NL assortment booklets for lettuce under glass. Prices per 1000 seeds were not found, and the booklets were not read. Enza and Bejo retail-pack prices were not found. — [Rijk Zwaan lettuce-under-glass booklet 2024](https://visuals.rijkzwaan.com/m/67ebd3dc704aa96e/original/RZNL_Assortimentsboekje-Sla-en-andijvie-onder-glas-2024.pdf)
- Water: see Q4. Vitens EUR 1.34/m3 incl. 9% VAT. Dunea EUR 1.45/m3 excl. VAT or EUR 1.58 incl. VAT. Both are 2026 tariffs.
- bol.com nets, feeders, scales, spinners and packaging: not found.

**(2) India (state-tagged where possible)**

*Fish feed (IndiaMART, read 2026-11-25; all on the page [IndiaMART Growel floating fish feed](https://m.indiamart.com/proddetail/growel-floating-fish-feed-2856379022933.html))*

| Product | Protein | Pellet | Pack | Price | Tax | Seller, city (state) | Reliability |
|---|---|---|---|---|---|---|---|
| Growel Floating Fish Feed | not listed | 3 mm | 35 kg bag | Rs 41/kg | excl. all taxes | Hi Pro Feeds, Hyderabad (Telangana) | tier_3; confidence low (B2B list price, protein unknown); single_source |
| Premium Floating Fish Feed | 30% | 3 mm | 35 kg | Rs 47/kg | not stated | Hi Pro Feeds, Hyderabad (Telangana) | tier_3; low; single_source |
| Floating Fish Feed (pangasius) | 24% | not listed | 40 kg | Rs 34/kg | not stated | Auxogene Aqua Pvt Ltd, Guntur (Andhra Pradesh) | tier_3; low; single_source |
| Growel Nutrila Murrel Feed | not listed | not listed | 10 kg | Rs 98/kg | not stated | Surya Aqua Feeds, Hyderabad (Telangana) | tier_3; low; single_source |

- An aquarium-feed listing on the same page at "Rs 2,100/kg" (SS Enterprises, Hyderabad) looks like a per-pack price or a listing error and is excluded here. [tier_3 | confidence: low] — [IndiaMART](https://m.indiamart.com/proddetail/growel-floating-fish-feed-2856379022933.html)
- Government cost norm for comparison: 28-30% protein floating pellets at Rs 30/kg (NFDB RAS model, undated). It differs from the IndiaMART Rs 47/kg for 30% protein feed. I am reporting both values without averaging. [tier_1 vs tier_3 | corroboration: conflicting (the norm and the market listing differ; dates differ)] — [NFDB RAS](https://nfdb.gov.in/PDF/RAS%20RT.pdf); [IndiaMART](https://m.indiamart.com/proddetail/growel-floating-fish-feed-2856379022933.html)
- Karnataka government aquarium feed: Rs 100 per 100 g at FRIC Hebbal, Bengaluru (rate list dated 2020-01-06). [tier_1 | confidence: medium, a 2020 order | single_source] — [KVAFSU FRIC Hebbal rate list](https://www.kvafsu.edu.in/services_and_inputs/FRIC-Hebbal-Benagaluru-1.pdf)
- Avanti, CP and Godrej tilapia feed prices per kg: not found.

*Fingerlings*: see Q3 for government rates. Karnataka: tilapia fingerlings Rs 4,000 per 1000. NFDB norm: GIFT seed Rs 4 per piece.

*Seeds*
- Italian basil, about 1,000 seeds per pack: Rs 99 sale price (Rs 230 MRP, shown as 57% off), "Tax included". Seller: Utkarsh Agrochem Pvt Ltd, Surat (Gujarat). Pelleted or raw is not stated, nor is a germination %. [tier_3 | confidence: low, a discounted retail price whose seed count is approximate | corroboration: single_source] — [Utkarsh Agro](https://utkarshagro.com/products/utkarsh-italian-basil-herb-seeds-for-home-kitchen-garden-green-approx-1000-seeds-per-pack)
- Flipkart lists "WILLVINE Hybrid Basil Seeds (1000 Seeds)" and "Biosnyg Lettuce Lollo Bionda (1000 Seeds)". Prices were not read. — [Flipkart WILLVINE basil](https://www.flipkart.com/willvine-hybrid-basil-seeds-1000-seeds-seed/p/itmfccd93cabd297); [Flipkart Biosnyg lettuce](https://www.flipkart.com/biosnyg-lettuce-lollo-bionda-seeds-1000-seeds-seed/p/itmed49b7e697bed)

*Cold storage (India)*
- Ecofrost 5-6 t solar cold room: USD 18,058 MSRP, undated (see Q1). An INR price was not found. — [E4C: Ecofrost](https://www.engineeringforchange.org/solutions/product/ecofrost-micro-cold-storage/)

*Water*: see Q4.

**(3) Global / US reference**
- CoolBot: USD 4,200 MSRP, undated, scope ambiguous (see Q1). [tier_2 | low | single_source] — [E4C: CoolBot](https://www.engineeringforchange.org/solutions/product/coolbot-walk-cooler/)

### Inferences
- The India feed range found is Rs 34-47/kg (IndiaMART listings, tax status mostly unstated) for 24-30% protein floating feed. The NFDB norm of Rs 30/kg sits below that range, possibly because the norm is older. The NFDB document is undated, so this is unconfirmed.
- The per-1000 price for Indian retail basil seed packets is near the pack price, because packs are sold as about 1,000 seeds. This holds for one listing only.

### Gaps
- NL/EU feed prices (Coppens, Skretting, Aller Aqua; tilapia 28/32/40%; fingerling vs grow-out) were not found.
- Dutch tilapia and catfish fingerling prices were not found. Til-Aqua appears to sell broodstock, not fingerlings.
- Rijk Zwaan, Enza and Bejo retail-pack prices and NL pelleted lettuce prices per 1000 seeds were not found.
- bol.com prices for nets, scales, feeders, crates, spinners and packaging were not found.
- India: Avanti, CP and Godrej feed prices, Tamil Nadu and Karnataka feed dealer prices, and Indian lettuce pelleted-seed prices were not found.
- No packaging, crate, knife, spinner or processing-table price was found in any market.
- India solar cold room INR prices (Ecofrost, Inficold, IndiaMART solar cold rooms) were not found. The leads below were not read:
  - [IndiaMART solar cold storage category](https://m.indiamart.com/impcat/solar-cold-storage.html)
  - [Ecofrost brochure](https://www.ecozensolutions.com/wp-content/uploads/2019/11/Ecofrost-brochure.pdf)

## Q3. Government fingerling rates and feed norms (India; NL equivalents)

### Takeaway
Karnataka (KVAFSU FRIC Hebbal, 2020 rate list) sells tilapia fingerlings at Rs 4,000 per 1000, pangasius at Rs 2,000 per 1000 and common carp at Rs 1,000 per 1000. This matches NFDB's PMMSY RAS norm of Rs 4 per GIFT fingerling. For feed, NFDB's RAS norm is 28-30% protein floating feed at Rs 30/kg, FCR 1.3 and feeding at 3-5% of body weight. No Dutch government equivalent was found.

### Cited Findings
- **Karnataka, FRIC Hebbal, Bengaluru (KVAFSU), office order No. FRIC(I)/Hebbal/112/2019-20 dated 2020-01-06.** Prices in Rs per 1000. [tier_1 (state veterinary/fisheries university research station rate list) | confidence: medium, the 2020 order may since have been revised and the size bands are not defined in mm in the extract | corroboration: tilapia rate corroborated by NFDB Rs 4/piece; others single_source] — [KVAFSU FRIC Hebbal rate list](https://www.kvafsu.edu.in/services_and_inputs/FRIC-Hebbal-Benagaluru-1.pdf)

| Species | Spawn | Fry | Fingerlings | Advanced fingerlings | Stunted fingerlings |
|---|---|---|---|---|---|
| Tilapia | 40 | 400 | 4,000 | 6,000 | 8,000 |
| Pangasius | 30 | 300 | 2,000 | 4,000 | 8,000 |
| Common carp | 20 | 200 | 1,000 | 2,000 | 4,000 |
| Amur (common carp strain) | 20 | 200 | 2,000 | 4,000 | 5,000 |
| Catla / Rohu / Mrigal / Grass carp / Silver carp / L. fimbriatus | 20 | 200 | 1,000 | 2,000 | 4,000 |

- The same Karnataka list sells live and bulk fish at Rs 125/kg. The extract also shows Rs 200/kg next to Catla, and the layout was unclear. [tier_1 | confidence: low, ambiguous layout | single_source] — [KVAFSU FRIC Hebbal](https://www.kvafsu.edu.in/services_and_inputs/FRIC-Hebbal-Benagaluru-1.pdf)
- **NFDB (national, PMMSY RAS model), undated:**
  - GIFT tilapia seed Rs 4/piece, fingerling stocking size.
  - The model specifies 6,000 fish per 90 m3 tank, with 90% survival and a 6-month crop to 500 g.
  - Its cost table instead uses 4,500 fingerlings (Rs 0.18 lakh), which is internally inconsistent.
  - Other inputs: feed 28-30% protein floating at Rs 30/kg, FCR 1:1.3, electricity Rs 0.40 lakh per crop line, probiotics Rs 0.05 lakh.
  - [tier_1 | confidence: medium, undated with internal inconsistencies | corroboration: seed price corroborated by KVAFSU tilapia Rs 4,000/1000] — [NFDB RAS](https://nfdb.gov.in/PDF/RAS%20RT.pdf)
  - The source also contains revenue and profit statements. They are not carried here, per the project's blocked-claims rule.
- **PMMSY RAS unit costs (Rs lakh), from the NFDB RAS document:**
  - Large RAS: 50.00 (8 tanks, 40 t/crop).
  - Medium RAS: 25.00. The document's two tables conflict on its configuration: 4 x ≥90 m3 tanks vs 6 tanks of ≥30 m3.
  - Small RAS: 7.50 (1 tank, 100 m3).
  - Backyard mini RAS: 0.50.
  - Subsidy limit: one unit per individual. Groups may hold 2 large, 3 medium or 4 small units.
  - [tier_1 | confidence: medium | corroboration: single_source; the Medium RAS configuration conflicts within the source] — [NFDB RAS](https://nfdb.gov.in/PDF/RAS%20RT.pdf)
- **Tamil Nadu (Dept. of Fisheries, "Start a Business – Inland", June 2019):**
  - IMC fingerlings stocked in wetlands at 2,000 per ha, with a ceiling of Rs 2.50 per fingerling. This is a scheme ceiling, not a sale price.
  - Fish seed, feed and manure input assistance up to Rs 1.50 lakh/ha for finfish and Rs 2.50 lakh/ha for freshwater prawn and trout.
  - The document has no feed price, FCR or protein norm. Subsidy % values are in images that were not extracted.
  - [tier_1 | confidence: medium, a 2019 scheme document | corroboration: single_source] — [TN Fisheries: Start a Business Inland](https://fisheries.tn.gov.in/includes/assets/pdf/Start-A-Business/Start_a_Business_Inland.pdf)
- PMMSY general rules: unit costs sit in Annexures I-III of the operational guidelines, which the fetched text did not reach. A markup of up to 20% over unit costs is allowed for islands, Himalayan states and UTs, and the North East. [tier_1 | confidence: high for the rule text | corroboration: single_source] — [NFDB PMMSY guidelines PDF](https://nfdb.gov.in/PDF/PMMSYG/04.pdf)
- Netherlands: the Til-Aqua finding is in Q2. No Dutch government fingerling rate or feed norm was found.

### Inferences
- For Nile tilapia (GIFT) fingerlings in South India, a Karnataka university rate and a national cost norm independently give Rs 4 per fingerling. The two differ in date (2020 vs undated) and in purpose (sale price vs subsidy cost norm).
- The Tamil Nadu Rs 2.50 ceiling is for IMC carp fingerlings in wetland stocking. It should not be compared directly with tilapia rates.

### Gaps
- PMMSY aquaponics unit costs (backyard, medium, commercial) and biofloc, cold storage, ice plant and insulated or refrigerated vehicle unit costs were not obtained. The J&K PMMSY pattern-of-assistance PDF was unreachable (robots.txt error). — [J&K PMMSY Pattern of Financial Assistance (not read)](https://fisheries.jk.gov.in/PMMSY/PMMSY-Pattern%20of%20Financial%20Assistance.pdf)
- Fingerling rate lists for Andhra Pradesh, Telangana, TNFDC and KSFDC, and size definitions in mm, were not found. The NFDB fish-seed directory PDF was found but could not be fetched. — [NFDB Fish seed website V3 (not read)](https://nfdb.gov.in/PDF/Fish%20seed%20website%20V3.pdf)
- Catfish, koi/goldfish and trout fingerling rates were not found, apart from Karnataka "feed fish" goldfish and common carp at Rs 1.50-2.00 per piece. That entry's unit was ambiguous in the extract, so it is not used.
- Whether the FRIC Hebbal 2020 rates are still current is unknown.

## Q4. Water tariffs (municipal, per m3)

### Takeaway
The Netherlands 2026 drinking-water tariffs are EUR 1.34/m3 incl. VAT (Vitens) and EUR 1.45 excl. VAT or EUR 1.58 incl. VAT (Dunea), plus Belasting op Leidingwater (BoL) of about EUR 0.44-0.48/m3 and an annual fixed charge. Chennai's commercial rate is Rs 99/kL up to 500 kL (from April 2025). The Hyderabad figures found are 2014 rates. The Bengaluru 2025 rates could not be verified.

### Cited Findings
- **Vitens (NL), 2026 consumer tariff:**
  - Drinking water EUR 1.34 per m3 incl. 9% VAT.
  - Fixed capacity charge (vastrecht) EUR 56.68 per year incl. 9% VAT.
  - BoL EUR 0.477 per m3 over the first 50,000 m3 per year per WOZ object. VAT status is not stated on the page.
  - Read 2026-11-25. Vitens' business (zakelijk) 2026 tariff was not read.
  - [tier_1 (utility tariff) | confidence: high, an official tariff document | corroboration: single_source per utility] — [Vitens Tarieven 2026 Consument](https://www.vitens.nl/-/media/Project/Vitens/VitensNl/Tarieven/Documenten-tarieven-2026/050004-31_Vitens-Tarieven-2026-Consument.pdf)
- **Dunea (NL), 2026 tariff regulation:**
  - Water supply EUR 1.45 per m3 excl. 9% VAT, or EUR 1.58 incl.
  - Vastrecht per year by capacity: 1.5 m3/h (Q3 2.5 meter) EUR 90.41 excl. or EUR 98.55 incl.; 2.5 m3/h EUR 181.11 excl. or EUR 197.41 incl.; 6 m3/h EUR 992.86 excl.; 15 m3/h EUR 3,452.13 excl. Connections above 15 m3/h are quoted individually.
  - BoL EUR 0.437 per m3 excl. VAT, or EUR 0.476 incl., capped at 50,000 m3 per WOZ object per year.
  - Read 2026-11-25.
  - [tier_1 | confidence: high | corroboration: single_source per utility. The BoL level agrees with Vitens' EUR 0.477 to within EUR 0.001, so it is corroborated across two utilities] — [Dunea Tarievenregeling 2026](https://www.dunea.nl/-/media/bestanden/over-dunea/tarievenregeling/dunea-tarievenregeling-2026.pdf)
- **Evides (NL)**: the 2026 tariff was not found. ACM's 2026 advice contains no tariff table. It notes that every company must publish its tariff overview before 1 December. [tier_1 | confidence: high | single_source] — [ACM advies drinkwatertarieven 2026](https://www.acm.nl/system/files/documents/adviies-drinkwatertarieven-2026.pdf)
- **Chennai Metro Water (CMWSSB, Tamil Nadu), metered, effective 2025-04-01:**
  - Domestic: Rs 7/kL up to 10 kL, Rs 19/kL for 11-15 kL, Rs 30/kL for 16-25 kL, Rs 48/kL above 25 kL. Minimum charge Rs 105 per month.
  - Partly commercial: Rs 11, 31 and 48/kL. Minimum charge Rs 291 per month.
  - Commercial (all others except private hospitals): Rs 99/kL up to 500 kL, with a Rs 1,049 per month minimum (non water-intensive). Above 500 kL, Rs 163/kL on the entire quantity, with a Rs 1,934 minimum (water-intensive).
  - Industrial: Rs 99/kL up to 500 kL. Above 500 kL, Rs 194/kL on the entire quantity.
  - Sewerage adds 25% of water charges for commercial and industrial users where connected.
  - Read 2026-11-25.
  - [tier_1 (utility tariff page) | confidence: high | corroboration: single_source] — [CMWSSB tariff](https://www.cmwssb.tn.gov.in/tariff)
- **Hyderabad (HMWSSB, Telangana), commercial and industrial rates as reported in February 2014:**
  - Commercial within GHMC: Rs 40/kL for 0-15 kL, Rs 70 for 16-100 kL, Rs 100 for 101-200 kL, and Rs 100 on the entire quantity above 200 kL.
  - Industrial within GHMC: Rs 50, 80 and 120/kL by the same slabs. Water-based industry: Rs 200/kL within GHMC and Rs 240 outside.
  - Outside GHMC: Rs 180/kL on the entire quantity.
  - Sewerage adds 35% within GHMC.
  - [tier_3 (news report) | confidence: low, a 2014 figure that was likely revised later (a later Siasat headline reports planned 5% annual increases) | corroboration: single_source] — [fullhyderabad.com, 2014-02-07](https://news.fullhyderabad.com/hyderabad-news/water-tariff-in-hyderabad-increased-for-commercial-industrial-consumers-11274.html); later headline only (not read): [Siasat: water bills to rise 5% annually](https://www.siasat.com/water-bills-to-rise-by-5-pc-annually-as-hmwssb-looks-to-recover-revenue-3543386/)
- **Bengaluru (BWSSB, Karnataka), revision effective 2025-04-10 (bills from May 2025):**
  - One article gives per-litre figures for domestic (0.15 to 1.00 by slab) and non-domestic (1.00 to 1.90 by slab) use. These look like the size of the increase (paise per litre), not the full tariff. An IndiaTV headline reads "revise water tariffs by 0.15 paise to Rs 1.90 depending on usage".
  - Read as rupees per litre, these would mean Rs 150-1,900/kL, which is implausible next to Chennai's Rs 7-194/kL.
  - The article's non-domestic slab for 75,001-100,000 L is also lower than the preceding slab.
  - [tier_3 (news) | confidence: low, the unit is ambiguous and the figures are likely increments | corroboration: conflicting/unverified] — [Goodreturns](https://www.goodreturns.in/news/bengaluru-water-bills-to-rise-starting-today-bwssb-revises-tariffs-check-new-charges-slabs-bill-1418301.html); headline: [IndiaTV News](https://www.indiatvnews.com/karnataka/bengaluru-to-revise-water-tariffs-by-0-15-paise-to-rs-1-90-check-category-wise-proposed-hike-2025-04-09-984743)

### Inferences
- Vitens' BoL of EUR 0.477/m3 is very close to Dunea's incl.-VAT BoL of EUR 0.476, so the Vitens figure is probably also incl. VAT. The Vitens page does not say so.
- A farm's tariff category (domestic, commercial, industrial or agricultural) decides the Indian rate band. None of the Indian tariffs read has an aquaculture or horticulture category, so the category that applies to a farm is unknown.

### Gaps
- The Evides 2026 tariff and Vitens' business (zakelijk) 2026 tariff were not read.
- The official BWSSB 2025 tariff notification, with full slab rates per kL, was not found. The Deccan Herald article could not be fetched because the budget ran out.
- The current HMWSSB commercial and industrial tariff (post-2014) was not found.
- Andhra Pradesh municipal tariffs (e.g., Vijayawada or Visakhapatnam) were not searched.
- Groundwater or borewell costs, the common alternative to municipal water in India, were not found.

## Q5. Sizing rules (feeding-rate ratio, feeding rate, cold room sizing)

### Takeaway
The firmest sizing rules found are these:
- FAO 589's feed-rate ratio: 40-50 g feed per m2 per day for leafy greens and 50-80 for fruiting crops, at 32% protein.
- SRAC 454's raft (UVI-type) ratio: 60-100 g/m2/day, with gravel and NFT at about 25% of that. This is a context split with FAO 589.
- Fish feeding rates: FAO 589 gives 1-2% of body weight per day for fish over 50 g. NFDB gives 3-5% for RAS tilapia from fingerling. These are a context split.
- The CoolBot room-size-to-AC-BTU table, the R-25 insulation standard, and FAO's gross-to-net cold-store volume ratio (meat context).

No source gave a produce or fish cold-room m3 per tonne figure.

### Cited Findings
- Feed-rate ratio: leafy greens 40-50 g/m2/day and fruiting vegetables 50-80 g/m2/day, for 32% protein feed. [tier_2 | high | single_source] — [FAO 589 via farmhub.ag](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/)
- Feed-rate ratio for raft (UVI-type) systems: "a ratio in the range of 60 to 100 grams of fish feed per square meter of plant growing area per day should be used". Use the low end for small plants such as Bibb lettuce and the high end for larger plants such as romaine and Chinese cabbage. Gravel and NFT systems should use about 25% of the raft ratio. No separate fruiting-crop ratio is given. [tier_2 (SRAC extension fact sheet by the UVI system's developer, Rakocy) | confidence: medium-high, stated directly | corroboration: context_split with FAO 589 (raft commercial vs small-scale mixed units). This is not a conflict to average.] — [SRAC 454](https://pods.okstate.edu/fact-sheets/SRAC-454pod.pdf)
- Fish feeding rate: 1-2% of body weight per day for fish over 50 g, and 1% for fish over 100 g (FAO 589). The NFDB RAS model uses 3-5% of body weight from fingerling stage. [tier_2 / tier_1 | context_split] — [FAO 589 via farmhub.ag](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/); [NFDB RAS](https://nfdb.gov.in/PDF/RAS%20RT.pdf)
- FCR: 1:1.3 for GIFT tilapia in the NFDB RAS model. [tier_1 | medium | single_source] — [NFDB RAS](https://nfdb.gov.in/PDF/RAS%20RT.pdf)
- Stocking: up to 20 kg/1,000 L for beginners (FAO 589), and 6,000 GIFT fingerlings per 90 m3 tank (NFDB RAS). Both are context-specific. [tier_2 / tier_1] — [FAO 589 via farmhub.ag](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/); [NFDB RAS](https://nfdb.gov.in/PDF/RAS%20RT.pdf)
- CoolBot AC sizing: from 10,000 BTU for a 6x8x8 ft room up to 24,000 BTU for a 10x14x8 ft room, at 38 F with no more than 4 door openings per hour. Insulation of R-25 or better is needed below 5 C. [tier_2 | medium | single_source each] — [E4C](https://www.engineeringforchange.org/solutions/product/coolbot-walk-cooler/); [Johnny's](https://www.johnnyseeds.com/on/demandware.static/-/Library-Sites-JSSSharedLibrary/default/dw5a0081d0/assets/information/8274-coolbot-limitations.pdf)
- Cold-store volume: gross volume is about 1.5 times net volume, and gross area about 1.25 times net area, in meat cold stores. Stacking stops 40-60 cm below the ceiling. [tier_2 | medium | single_source] — [FAO meat cold store manual](https://www.fao.org/4/t0098e/T0098E03.htm)
- Ecofrost: about 5-6 t capacity in a 20 x 8 x 8 ft unit, which is the manufacturer's capacity figure, not a sizing rule. [tier_2 | medium | single_source] — [E4C: Ecofrost](https://www.engineeringforchange.org/solutions/product/ecofrost-micro-cold-storage/)
- Make-up water: no more than 10% of system volume per day in an Indian RAS. [tier_1 | medium | single_source] — [NFDB RAS](https://nfdb.gov.in/PDF/RAS%20RT.pdf)

### Inferences
- A per-tonne cold-room volume for leafy greens or fish could in principle be derived from the Ecofrost capacity and external dimensions. I have not calculated it, because the source gives no net storage volume or product type, and the result would be an unsourced sizing rule.
- Feeder sizing in a coupled system can be expressed through the FAO 589 ratio (daily feed = ratio x grow area). Feeder hardware capacity specs were not found, so nothing can yet be checked against that ratio.

### Gaps
- No source gave a cold-room storage density for leafy greens, herbs or chilled whole fish (kg per m3 net or gross). Refrigeration load per m3 was also not found.
- The SRAC 454 raft ratio is now cited above. The original UVI papers were not read, so the ratio has not been corroborated against a peer-reviewed UVI source. Unread leads:
  - [Rakocy, UVI aquaponic system (archive.uvi.edu)](https://archive.uvi.edu/files/documents/Research_and_Public_Service/WRRI/UVIAquaponicSystem.pdf)
  - [Rakocy ISTA9 paper](https://cales.arizona.edu/azaqua/ista/ISTA9/PDF's/RakocyAquaponicSystem.pdf)
- Purge or depuration duration and tank-volume rules, and transport-bag loading density (kg fish per L water, O2 fill), were not found.

## Q6. What growers use instead (homemade feed, duckweed, BSF larvae, home freezers, local seeds) and what fails

### Takeaway
The only sourced "instead" options in this pass are cold-chain ones:
- CoolBot plus room AC instead of a commercial refrigeration unit. It has documented limits: no freezing, a floor of about 1 C, poor fit above about 6 door openings per hour, and AC models that do not auto-restart.
- Solar thermal-storage cold rooms (Ecofrost) for off-grid India.
- Low-cost local seed packets in India (about Rs 99 per ~1,000 basil seeds).

Duckweed, black soldier fly larvae, homemade feed and home-freezer evidence was found as leads but not read.

### Cited Findings
- CoolBot vs a conventional walk-in: holding at or above 38 F (3 C) with fewer than 5 door openings per hour "may limit upfront costs and reduce electricity bills". At 36 F (2 C) with infrequent door use there are "less electricity savings than a conventional walk-in, but still lower upfront costs". 34 F (1 C) works only with an oversized AC, a room better than R-25, and rare door openings. [tier_2 | medium | single_source] — [Johnny's CoolBot limitations](https://www.johnnyseeds.com/on/demandware.static/-/Library-Sites-JSSSharedLibrary/default/dw5a0081d0/assets/information/8274-coolbot-limitations.pdf)
- CoolBot failure modes:
  - It cannot reach or hold freezing, so it cannot replace a fish freezer.
  - An undersized AC fails to cool (5,000 BTU in a 10x15 ft room).
  - Frequent door openings break the hold temperature.
  - Some ACs do not auto-restart after a power blink.
  - Winter operation depends on the AC model.
  - [tier_2 | medium | single_source] — [Johnny's CoolBot limitations](https://www.johnnyseeds.com/on/demandware.static/-/Library-Sites-JSSSharedLibrary/default/dw5a0081d0/assets/information/8274-coolbot-limitations.pdf)
- Solar cold room in India: thermal storage instead of batteries, about 36 h of cloudy-weather backup, and a 2 C minimum (Ecofrost). [tier_2 | medium | single_source] — [E4C: Ecofrost](https://www.engineeringforchange.org/solutions/product/ecofrost-micro-cold-storage/)
- Local, low-cost seeds in India: basil at about 1,000 seeds for Rs 99 (tax included, discounted from Rs 230 MRP). Germination % is not stated, so no quality comparison against professional seed is possible. [tier_3 | low | single_source] — [Utkarsh Agro](https://utkarshagro.com/products/utkarsh-italian-basil-herb-seeds-for-home-kitchen-garden-green-approx-1000-seeds-per-pack)
- Failure mode affecting all feed alternatives: FAO 589 links stable nitrate to possible Ca, K and Fe deficiencies that need checking. This is relevant whenever feed composition changes. [tier_2 | high | single_source] — [FAO 589 via farmhub.ag](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/8-management-and-troubleshooting/component-calculations-and-ratios/)

### Inferences
- In aquaponics, CoolBot-type rooms fit leafy-green and herb chilling, where the 1-3 C floor is acceptable. They do not fit frozen fish storage. This is my inference from the stated temperature floor.
- A shift from commercial pellets to homemade or alternative feeds changes the feed-rate ratio's 32% protein assumption. The FAO 589 ratio then no longer applies as stated. This is my inference; no source tested it here.

### Gaps
- Black soldier fly larvae, duckweed and homemade feed in aquaponics: performance (growth, FCR) and failure data were not read. Unread leads:
  - [PLoS ONE 2024 (PMC10798475)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10798475)
  - [SARE project FNE22-015](https://projects.sare.org/project-reports/fne22-015)
  - [Univ. Lisbon thesis: alternative fish feed and electricity-independent oxygenation in decoupled aquaponics](https://repositorio.ulisboa.pt/bitstream/10400.5/23561/1/Effect%20of%20alternative%20fish%20feed%20and%20electricity%20independent%20oxygenation%20in%20decoupled%20aquaponic%20systems.pdf)
  - [Georgia Tech repository item](https://repository.gatech.edu/server/api/core/bitstreams/e5c9db2f-ec52-445f-91f6-85bfa8bbccb4/content)
- Evidence on home chest freezers or domestic refrigerators as cold storage, and on their failure modes, was not found.
- Forum or grower anecdotes on what fails were not collected, so none are reported.
- Evidence on reusing grow media or plugs, or on homemade nutrient solutions in decoupled and hydroponic systems, was not found.
