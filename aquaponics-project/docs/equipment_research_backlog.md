# Equipment research backlog

Status: plan, 2026-11-25. Built from three gap lists:

- the equipment inventory gap list (82 rows)
- `known_gaps` and the null values in `data/catalog/components_v0.json`
- the comparison note *Inventory vs existing research*

Nothing here is a value. Every number found later goes in as a candidate with its tier, confidence and corroboration.

## 1. Components still missing from the catalog

The catalog holds 25 parts. These are what it still lacks.

**Parts with a slot but no price or life:**
- DWC trough walls, NL and India: no price.
- Polyhouse and shade-net life, India: none recorded.
- Venlo glasshouse heating installation, NL: excluded from the EUR 50.2-63/m² figure.

**Running inputs still missing:**
- **NL:** fingerlings, seed per plant, tilapia feed (only Coppens koi and sturgeon lines so far).
- **India:**
  - seed: one listing in the inventory, about Rs 99 per ~1,000 basil seeds, not imported yet
  - water: Chennai Rs 99-163/kL is in the inventory but not imported, and Bengaluru and Hyderabad have no current official tariff

**Categories in the schema with no parts at all:** heating, lighting, backup_power and monitoring.

**Categories not in the schema yet.** Real farms need these, so each needs a schema slot:
- propagation (trays, plugs, germination)
- media-bed media and net pots
- plumbing (it is a 36.9% fraction rule today, not parts)
- water treatment and dosing (base, acid, iron chelate, UV, dosing pumps)
- fish handling (nets, feeders, graders, purge tank)
- harvest and post-harvest (crates, wash, spinner, cold room, packaging)
- solids-removal hardware beyond a settling tank (drum, bead, swirl, radial-flow)
- degassing and mineralisation tanks

**Grow methods with no parts:** media bed, Dutch bucket, vertical towers, and ebb and flow. Only DWC and one NFT channel exist.

## 2. Research needed, in priority order

Priority follows what changes cost per kg in the current configurator runs (NL and Karnataka basil DWC) first, then what opens new configurations.

### P1. Fills gaps in today's configurator results

| # | Item | Market | What to find | Best leads (from the inventory notes) |
|---|---|---|---|---|
| 1 | DWC trough walls (timber, block, steel frame) | NL, IN | price per m of wall or per m² of trough, life | builder merchants; UVI used 1,148 USD per raceway wall (2014) as a reference |
| 2 | Polyhouse film and frame life; film replacement cost | IN | years for 200-micron UV film, GI frame and bamboo frame | NHB/MIDH guidelines; TNAU agritech portal; Haryana gives film replacement at Rs 153/m² (context only) |
| 3 | State protected-cultivation rates | KA, AP, TS | Rs/m² by structure type and subsidy % | MIDH 2025 Annexure V; Telangana 2025-26 guideline (pages 121-147); AP horticulture site (blocked by robots.txt, try another copy) |
| 4 | Glasshouse heating installation and heat demand for basil | NL | EUR/m² installed; m³ gas or kWh per m²/yr | KWIN (paid); WEcR reports; Blueterra 2025 heat-pump report |
| 5 | Tilapia (or catfish) feed, fingerlings, basil and lettuce seed | NL | EUR/kg feed by protein; EUR per fingerling; EUR per 1,000 seeds | Coppens or Skretting dealers; Dutch catfish hatcheries; Rijk Zwaan and Enza price lists |
| 6 | Current official water tariffs | Bengaluru, Hyderabad | Rs/kL, commercial and agricultural | BWSSB and HMWSSB tariff orders |
| 7 | Circulation pump made for low head | IN | price and flow curve for a pond or aquaculture pump, by state | Kirloskar Chhotu, CRI and Crompton pages already located |
| 8 | Backup power | NL, IN | current generator, UPS and LiFePO4 prices; Indian genset prices; PV cost per kW in the four states | bol.com, 123accu, L&T SuFin Kirloskar, IEEFA 2025 report |

### P2. Opens new categories in the configurator

| # | Item | Market | What to find |
|---|---|---|---|
| 9 | Monitoring basics: DO meter, test kits, pH/EC pens, alarms | NL, IN | price, calibration and probe life |
| 10 | Water treatment: KOH, Ca(OH)₂, K₂CO₃, acids, Fe-DTPA, UV-C, peristaltic dosing | NL, IN | price per kg or unit; dose per kg feed where sourced |
| 11 | Solids hardware: bead filter, swirl and radial-flow, filter socks and mats | NL, IN | price, kg feed/day served, cleaning frequency |
| 12 | Lighting: LED fixtures with PPF and µmol/J | NL, IN | W, PPF, price; HPS reference |
| 13 | Heating hardware for small systems: aquarium and immersion heaters, heat pumps | NL | W per L sizing, price, COP |
| 14 | Propagation: trays, rockwool, coco or peat plugs, heat mats, domes | NL, IN | price per plant start; germination loss |
| 15 | Media beds and other grow methods: LECA, gravel, net pots, NFT sets, towers, Dutch buckets | NL, IN | price, sizing rule from a tier_1 or tier_2 source |
| 16 | Harvest and cold chain: crates, spinners, cold rooms in INR and EUR, packaging | NL, IN | price, W and duty hours for cold rooms |

### P3. Completes the inventory

| # | Item | What to find |
|---|---|---|
| 17 | Fish handling: nets, graders, feeders, purge tanks | price, use |
| 18 | Grower alternatives: Reddit, Backyard Aquaponics, YouTube build logs, Indian biofloc groups | count of independent reports; failures (anecdote only) |
| 19 | Minutes per maintenance task, and measured power draw | labour minutes per task; measured kW, not nameplate |
| 20 | Field lifetimes from any source better than depreciation tables | years with basis |

## 3. Checks on existing values

These need checking, not new research:

- Read the FAO 589 original PDF for the values taken from the FarmHub mirror: air-stone spacing, media depth, NFT slope and pump life.
- Confirm the shade-net plains rate (Rs 360/m²) and replace the hilly Rs 414 if confirmed.
- Find the source of the catalog's 0.35 m media-bed depth.
- Resolve the UVI plant-blower rating (1 hp vs 2 hp), which sets `raft_air_share_of_fish_air`.
- Re-grade the tiers in the older research packs to the current rule (peer-reviewed = tier_1), and attach URLs where the inventory read the same source.

## 4. How to run it

- **Batch size.** Run two or three researchers at a time, not seven. Each uses its own share of the shared limit of 100 page reads an hour. The last pass ran seven at once and hit the limit after about 12 reads each.
- **Batch 1.** P1 items 1-8, split by market: one NL researcher and one India researcher.
- **Batch 2.** P2 items 9-16, split the same way.
- **Output.** Save results as JSONL rows in the catalog shape, so they import straight into `data/catalog/components_v0.json` after review.
