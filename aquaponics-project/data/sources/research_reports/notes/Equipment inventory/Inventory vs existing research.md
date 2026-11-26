# Equipment inventory vs existing research

Status: review note, 2026-11-25. Candidate data only, nothing here is canon. No repo files were changed.

## Bottom line

- The new inventory and the existing research mostly **agree on design rules**, so several existing values can move from `single_source` to `corroborated`.
- The new inventory adds what the existing research mostly lacked: **prices, power ratings, lifetimes and failure evidence for named products**.
- The existing research and the PR #15 catalog still hold values the inventory **did not reach**. Examples are the Dutch glasshouse cost, Dutch fish feed, electricity tariffs, labour rates and Dutch raft-board prices. These should be kept, not re-researched.
- There are **9 conflicts or risks** that touch values already in the PR #15 catalog (section 3). Two matter most:
  - insulation-board rafts and their 10-year life
  - the shade-net price, which appears to use the hilly-area rate.
- The tier scheme differs between the older reports and the new rule, so tiers are not comparable across files as they stand (section 6).

## What was compared

New: `equipment-inventory/Aquaponics equipment inventory.md` and `.jsonl` (169 rows), plus the seven research notes.

Existing:
- **Repo research packs** in `data/sources/research_reports/markdown/`, the equipment-related ones:
  - Pumps and Aeration
  - Media bed vs DWC vs NFT
  - Architecture-Specific CAPEX Basis
  - Architecture-specific business drivers
  - Operating Economics Input
  - Aeration Capacity and Solids Load
  - Public Benchmark Mapping
  - DWC and NFT for basil
  - First-slice basil economics
  - Greenhouse climate
- **Repo-root PDFs**: the Biofilters and solids filters corroboration report and the Distilled Research Pack.
- **PR #15 catalog**: `data/catalog/components_v0.json` on branch `claude/project-thread-2f4xwr`, which has 25 parts, the design rules and the running inputs.
- **Project files**: `farm-viability/` (cost basis review and inputs).

The species, water chemistry, basil saleability and tank/TAN packs were checked only for equipment values; they have almost none.

## 1. Where they agree (corroboration can be upgraded)

| Value | Existing research | New inventory | Result |
|---|---|---|---|
| UVI depreciation lives | Catalog uses UVI Table 7: tanks 20 yr, liner/walls/rafts 10 yr, pump 5 yr, blower 10 yr | Same table read again: 20 / 10 / 5 / 10 yr | Same source, so no new corroboration, but the transcription is confirmed |
| Pump life | Catalog: 5 yr (UVI depreciation) | FAO 589: 3–5 yr overall, 1–2 yr at full capacity | Two sources overlap at 5 yr. FAO points lower, so keep a 3–5 yr range |
| UVI circulation pump | Pumps pack: 0.37 kW vs 0.74 kW contradiction (CA2 vs CA1) | SRAC 454: ½ hp at 100 gpm (= 0.37 kW) | Supports 0.37 kW for the CA2 system; the contradiction ticket can cite SRAC 454 |
| UVI fish blower | Pumps pack: 1.1 kW | SRAC 454: 1.5 hp | Same value (1.5 hp ≈ 1.1 kW, unit conversion) |
| Air per kg feed | Catalog: 187–249 L/min per kg feed/day (SRAC 453) | SRAC 453: 3 cfm per lb daily feed | Same rule, same source |
| Clarifier retention | All packs and catalog: ~20 min, 9.5 min underperformed, 15–30 min range | Same; adds SRAC 5007 (15–20% of fish-tank volume) and FAO (10–30%) | Agree; the inventory adds two volume-based rules |
| Swirl vs radial settler | Biofilters PDF: 37.1% vs 77.9% TSS removal | Same paper (Davidson & Summerfelt 2005) | Same source |
| MBBR loading | Catalog and Biofilters PDF: 8–16 kg feed/m³/day (SRAC 453, 2013 edition) | Same, plus the 1999 edition (16–23) and the K1 maker claim (5) | Agree on 2013. See section 2 for the other two |
| UVI maintenance | Ops economics pack: clarifier purge 3× daily, filter tanks 1–2× weekly | Same | Agree |
| Feed-to-raft ratio | Media-bed pack: 180 g/m²/day raft treatment capacity, gravel/NFT ≈ 25% of raft ratio | Same, plus FAO 40–50 (leafy) and 50–80 (fruiting) g/m²/day and UVI 60–100 g/m²/day | Agree; FAO is a separate small-scale context |
| India fingerlings | Catalog: NFDB INR 4 each, `single_source` | KVAFSU Hebbal (Karnataka, 2020): INR 4,000 per 1,000 tilapia | **Upgrade to corroborated** (two government sources) |
| India floating feed | Catalog INR 45–47 (IndiaMART) vs NFDB INR 30; ops pack INR 37–47.5 listings | Hyderabad/Guntur listings INR 34–47; NFDB INR 30 | Listings corroborate each other. The conflict with the NFDB norm stays, keep both |
| NL water | Catalog: Vitens EUR 1.34 incl. VAT, high end 1.817 with tap-water tax 0.477 | Vitens 1.34; Dunea 1.45 excl. / 1.58 incl.; tap-water tax 0.44–0.48 | **Upgrade to corroborated** (two utilities) |
| India FRP and tarpaulin tanks | Catalog: FRP 750 L INR 18,500; PVC biofloc 5,000 L INR 4,100 | FRP INR 18,000–25,000 (Tamil Nadu), 10,000–15,500 (Telangana); tarpaulin INR 4,100–10,000 (Andhra Pradesh) | Consistent. The tarpaulin price is probably the same listing, so it is not independent |
| India MBBR media | Catalog: INR 7,200–11,000/m³ (two listings) | INR 6,500–27,500/m³; Hyderabad 9,600; K1-type 19,800 | Consistent; the inventory widens the range and notes most is sewage-grade |
| NL IBC | Catalog: used EUR 90.75 incl. VAT, new EUR 195–205 excl. (binqer) | binqer used 59–115 excl., new 195–205 excl.; Hornbach UV food-grade EUR 369 incl. | Same seller for the plain totes. Hornbach is a different product, so this is not yet corroborated |
| NFT and raft outage behaviour | All grow-method packs: NFT flow loss leads quickly to wilting; DWC is buffered | Same, plus FAO "fish can die within a few hours" and SRAC 453 "restore in under 20 min" | Agree |

## 2. Conflicts and context splits to record

These are not errors. Each needs both values kept, plus a contradiction ticket or a context tag.

1. **DWC air-stone spacing.**
   - SRAC 5007 (existing packs): 1 stone per 10 ft², about 0.93 m² (derived).
   - FAO 589 (inventory): 1 stone of about 4 L/min every 2–4 m².
   - UVI: 1 diffuser every 4 ft along the trough.
   - FAO spaces stones 2–4 times wider than SRAC 5007. Both are small-scale sources, so this is a real disagreement, not only a scale split.
2. **Biofilter loading, three values.**
   - SRAC 453 (1999): MBBR 16–23, bead 13 kg feed/m³/day.
   - SRAC 453 (2013): MBBR 8–16, bead 16–32. The catalog and the Biofilters PDF use the 2013 figures.
   - K1 maker claim: about 5 kg feed/m³/day.
   - Keep the 2013 figures as the default, and record the other two.
3. **Sodium bicarbonate.**
   - The Biofilters PDF gives the SRAC RAS dosing rule (about 17–20% of daily feed) without an aquaponics caveat.
   - SRAC 454 (inventory) says it should not be used for pH in aquaponics.
   - Tag the rule `RAS only` before anyone uses it in a coupled system.
4. **NFT slope and length.**
   - FAO: about 1% slope and up to 12 m.
   - SRAC 5007 (existing packs and inventory): about 0.42% and under 12 ft (3.66 m).
   - The existing packs carry only the SRAC value.
5. **Raft care after harvest.** FAO says never let rafts dry. A USDA-NIFA project used a chlorine rinse plus 48 h of drying. The existing CAPEX pack names raft sanitation as a cost driver but has neither rule.
6. **DWC depth.** The inventory adds FAO's 30 cm. That fits the existing harmonised range of 15–30 cm, so there is no conflict.

## 3. Risks the inventory raises for values in the PR #15 catalog

| # | Catalog value | What the inventory found | Suggested action |
|---|---|---|---|
| 1 | `dwc_raft_xps_30mm_nl` and `dwc_raft_eps_40mm_nl/in`: Gamma and IndiaMART insulation boards with a 10-yr life (UVI raft class) | USDA-NIFA: homemade EPS rafts gained more than 300% in weight from water and broke at a 5.9 kg load. XPS was judged unsuitable because of its mandatory fire retardants. The UVI 10 yr applies to purpose-made rafts | Mark the life as `not transferable` with low confidence. Add a food-safety and fire-retardant flag to the XPS part |
| 2 | `structure_shade_net_in` high end INR 414/m², labelled "MIDH HMNEH bamboo shade net" | NHB/MIDH norms: bamboo shade net INR 360 on the plains, INR 414 in hilly areas | 414 looks like the hilly or north-east rate, which does not apply to the four southern states. Check it, and probably use 360 |
| 3 | `raft_air_share_of_fish_air` 0.67 (1 hp plants ÷ 1.5 hp fish) | The UVI costing lists a 2 hp plant blower; SRAC 454 lists 1 hp | Record both. At 2 hp the ratio would be 1.33 (derived) |
| 4 | IBC tanks with a 10–20 yr life, transferred from UVI tank life | Two conflicting forum anecdotes: about 5 yr in direct light vs about 8 yr outdoors | Keep the UVI basis, add the anecdote range as a low-confidence warning. Outdoor IBCs need UV cover |
| 5 | `air_hailea_aco500_nl` with a 10-yr life, transferred from UVI regenerative blowers | Hiblow: replace diaphragms and valves every 1–1.5 yr. No life found for piston or diaphragm pumps | The transfer from a ring blower to a piston pump is weak. Add the wear-part interval as maintenance |
| 6 | `media_bed_depth_m` 0.30–0.35 (repo CAPEX pack) | FAO 15–30 cm (30 only for large fruiting crops); SRAC 5007 6–12 in (15–30 cm) | The catalog range sits at or above both sources. Re-check where 0.35 came from |
| 7 | `nft_channel_upvc_100x50_in` INR 23.8/m, derived from plain uPVC pipe | Purpose-made NFT channels on IndiaMART: INR 112–1,500 per piece (INR 310 in Chennai) | These are different products, so the catalog value may understate NFT cost. Keep both as alternatives |
| 8 | `dwc_liner_epdm_1mm_nl` EUR 12.65/m², a sale price on a discontinued item | Hornbach EPDM 0.6 mm: EUR 12.63–18.46/m² incl. VAT | The catalog price is a clearance price for a thicker liner. Add Hornbach as a second seller |
| 9 | `pump_submersible_0_5hp_in` with no price (catalog gap) | Crompton 0.5 HP openwell pump: MRP INR 13,400 incl. GST, 72–140 L/min, 18 m max head | This fills the gap, but it is a well pump, not a pond or aquaculture pump. Label it that way |

## 4. Gaps the inventory fills

The catalog's `known_gaps` and the earlier packs had nothing for these:

- **India circulation pump**: Crompton 0.5 HP, INR 13,400 (see item 9 above).
- **India seed**: basil about INR 99 per ~1,000 seeds (one listing).
- **India water**: Chennai commercial INR 99–163/kL. The Hyderabad figure is from 2014, and Bengaluru is unverified.
- **India structure life**: treated bamboo 8–10 yr (ICAR); cellulose cooling pads about 10 yr (UF/IFAS).
- **India structure norms by frame type and area slab**:
  - polyhouse: tubular INR 844–1,060, wooden 540, bamboo 450, fan-and-pad 1,400
  - shade net: tubular 710, wooden 492, bamboo 360
  - The catalog had only two polyhouse points and two shade-net points.
- **NL second air pump option**: toppy.nl Hailea ACO-208 EUR 36.95 (18 W), Hiblow EUR 289–329.
- **Biofilter media near-EUR**: K1 GBP 85.95 per 50 L (UK).
- **Sensors and test kits**:
  - Bluelab EU prices, Hanna NL EUR 76.05, IndiaMART Bengaluru pH meters
  - calibration intervals, and DO sensor types (galvanic vs optical)
- **Propagation**: Grodan 150-plug tray EUR 14.90; germination and transplant rules.
- **Lighting rules**: DLC 2.30 µmol/J floor; WUR's LED saving of 10–25% vs the common 40% claim.
- **Backup power**:
  - Honda generator list (2020, stale), Kirloskar 3 kVA fuel use
  - Victron LiFePO4 cycle rating, PM Surya Ghar subsidy
- **Cold chain**: CoolBot costs (US) and the Ecofrost solar cold room (India, USD MSRP).
- **Solids and treatment hardware**:
  - drum filters: NL EUR 983 (discontinued), India INR 75,000–5,00,000
  - UV-C EUR 264.95 plus a EUR 49.95 yearly lamp
- **Design rules not in the existing packs**:
  - FAO bell siphon geometry, FAO NFT pipe sizes and flows, FAO media sizes
  - SRAC 453 circulation flow of 42–84 L/min per kg feed/day
  - fan-and-pad cooling rules (8 cfm/ft², pad ratings)

## 5. Values the existing research has and the inventory missed

Keep these; there is no need to research them again.

| Value | Where it is |
|---|---|
| Venlo glasshouse EUR 50.2–63/m² (2017 builder quotes, excl. heating), 16-yr life | Catalog (WEcR 2017) |
| Dutch greenhouse heat demand 21–30 m³ gas/m²/yr (sweet pepper, transferred) and gas price EUR 1.339–1.454/m³ | Catalog (WEcR, CBS) |
| NL/EU fish feed: Coppens EUR 2.92–3.67/kg; Aller Aqua GBP 46.78 per 25 kg (38%) | Catalog; Operating Economics pack |
| Electricity: CBS NL EUR 0.241/kWh (500–2,000 MWh band) and 0.115; Eurostat EUR 0.1837; four Indian states INR 3.45–10.45 | Operating Economics pack; farm-viability state inputs |
| Labour rates: NL CAO EUR 14.40–16.07/h; India burdened minimum wage INR 70–100/h | Basil economics pack; farm-viability |
| NL raft board (Gamma EPS 40 mm EUR 5.10/m², XPS 30 mm EUR 9.69/m², VAT basis not stated), India HDPE liner INR 130/m², India 1.5 kW blower INR 8,000 | Catalog (the inventory lists these as "not found") |
| Make-up water 1.5% of volume per day; land-to-grow-area ratio 2.34; plumbing at 36.9% of hardware cost | Catalog design rules (UVI) |
| Oxygen-demand envelope 0.3–0.75 kg O₂/kg feed; air-stone transfer efficiency of 40% or less; inject air no deeper than about 5 ft | Aeration Capacity pack |
| UVI 48 air stones per hydroponic tank set at 1.22 m spacing; DO rising from 4.0 to 6.9 mg/L through the rafts | Aeration Capacity pack |

## 6. Inconsistencies in how sources are graded

- **The tier scheme has changed.** In the older packs (Pumps, Media bed, Biofilters), "Tier 1" means extension and university programme material, and peer-reviewed papers are "Tier 2" (Davidson & Summerfelt, Maucieri et al.). Your current rule puts peer-reviewed papers in tier_1. The inventory follows the current rule. A backfill pass should re-grade the older packs before their tiers are compared with the inventory's.
- **The older packs have almost no URLs.** They cite internal search tokens, so their sources cannot be re-opened from the file. Where the inventory read the same source (SRAC 453/454/5007, UVI, Davidson & Summerfelt), its URLs can be attached to the older values.
- **FAO 589 was read from a mirror.** Neither the older packs nor the inventory read the FAO PDF itself, which timed out each time; the inventory used the FarmHub mirror. FAO values should stay at medium confidence until the original is checked.

## 7. Still missing in both

- **NL**:
  - glasshouse heating installation cost, heat pumps and boilers
  - LED fixture prices and µmol/J for named fixtures
  - fingerlings and seeds
  - trough walls
- **India**:
  - state-level structure rates for Karnataka, Andhra Pradesh and Telangana
  - raft trough walls
  - a current Bengaluru water tariff
- **All markets**:
  - DO meter prices
  - dosing chemicals (KOH, Ca(OH)₂, chelates)
  - feeders, nets and graders
  - packaging and crates
  - heaters and chillers
  - minutes per maintenance task
  - measured (not nameplate) power draw
  - field lifetimes for anything

## Suggested next step

One small PR on the catalog branch that does three things:

1. Applies the corroboration upgrades from section 1.
2. Opens contradiction tickets for the conflicts in section 2.
3. Fixes or flags the nine catalog risks in section 3.

After that, the inventory JSONL rows that fill catalog gaps (section 4) can be imported as candidates. A follow-up research pass should cover only section 7, with fewer researchers at a time so it stays under the web page limit.
