# Deep research prompt: aquaponics and hydroponics equipment inventory

Copy everything below the line into the deep research tool. Run it once per market group if the tool limits length (for example Netherlands/EU first, then India).

---

## Role and goal

You are a research analyst building an evidence-first equipment inventory for aquaponics and hydroponics farms. The inventory will feed a component database and a configurator that assembles a farm from parts, like choosing bases in a game. Your job is to list every piece of equipment needed to build and run these farms, with dimensions, capacities, power use, lifetimes and prices in several markets. For each item, also report what growers and forums use instead, and the trade-offs.

Do not design a farm or pick a size. Build the inventory only.

## Scope

**System types:** coupled aquaponics, decoupled aquaponics, recirculating hydroponics. Cover each grow method: deep water culture (raft), NFT, media bed, Dutch bucket / drip, vertical towers, ebb and flow.

**Scales:** hobby/backyard (under 20 m2 of grow area), small commercial (20 to 500 m2), commercial (over 500 m2). Say which scale each item suits.

**Markets, in priority order:**
1. Netherlands (and EU sellers that ship there)
2. India, ideally with state differences: Karnataka, Tamil Nadu, Andhra Pradesh, Telangana
3. Global reference prices (US or Alibaba-type B2B) only where 1 and 2 have nothing

## Equipment categories (cover all; add any I missed)

1. Fish tanks and sumps (IBC, PE/HDPE, FRP, PVC tarpaulin/biofloc, concrete, lined frames)
2. Grow units: raft troughs and walls, liners, raft boards, NFT channels, media beds and media, grow towers, buckets, net pots
3. Water pumps (circulation, sump, submersible, inline), with flow vs head
4. Aeration: air pumps, regenerative/ring blowers, diffusers, air stones, venturi, backup oxygen
5. Solids removal: settling tanks, radial flow and swirl separators, drum filters, bead filters, filter socks/mats
6. Biofiltration: MBBR media, trickling filters, bead filters, media beds as biofilters
7. Degassing and mineralisation tanks
8. Plumbing: pipe, fittings, valves, bell siphons, overflows, unions (as a cost per m2 or per system if itemising is impossible)
9. Water treatment and dosing: pH up/down, buffer dosing, UV sterilisers, ozone, RO or filtration for source water
10. Monitoring and control: pH, EC, DO, temperature, ammonia/nitrite/nitrate test kits and probes, controllers, alarms, IoT
11. Climate and structure: glass greenhouse, polyhouse, shade net, indoor/insulated building, fans, pad-and-fan cooling, misting, screens
12. Heating and cooling: water heaters, heat pumps, boilers, chillers, insulation
13. Lighting: LED grow lights (umol/J, W, coverage), supplemental vs sole-source
14. Power: backup generators, UPS/battery, solar
15. Propagation: seed trays, plugs (rockwool, coco, peat, oasis), germination chambers, seedling lights
16. Fish handling: nets, graders, feeders (manual, automatic, demand), purge tanks
17. Harvest and post-harvest: knives, crates, washing, spin dryers, cold storage, packaging
18. Consumables: fish feed by protein %, fingerlings by species, seeds by crop, water, chemicals, replacement media

## For every item, record

| Field | What to give |
|---|---|
| item_name, category, function | plain description of what it does in the system |
| system_types and grow_methods | where it is used (aquaponics, hydroponics, both) |
| scale | hobby / small commercial / commercial |
| dimensions | L x W x H, diameter, volume (L or m3), weight, footprint m2 |
| capacity and sizing rule | what it serves (L/h at a stated head, L/min air, m2 of grow area, kg feed/day, m3 of water), and the sizing rule used to choose it, with its source |
| power | rated W and typical duty hours per day |
| lifetime | years, and whether that is a manufacturer claim, a depreciation life from a study, or user reports |
| maintenance and labour | what has to be done, how often, minutes per task if reported |
| price | per market: price, currency, unit (per piece, per m2, per m), incl. or excl. VAT/GST, seller or source, date read, URL |
| alternatives | what forums, growers and studies use instead (DIY or cheaper or better), and what it costs |
| trade-offs | what you gain and lose with each alternative (cost, reliability, labour, energy, food safety, failure risk) |
| failure modes | how it fails and what happens to fish and plants when it does |

## Alternatives and forum evidence

For each category, search grower forums and communities for what people actually use and why. Examples:
- IBC totes instead of purpose-built tanks
- swirl filters made from barrels instead of drum filters
- airlift pumps instead of water pumps
- media beds as combined solids filter and biofilter
- EPS or XPS insulation boards as rafts
- bamboo or GI frames for Indian polyhouses
- solar plus battery instead of a generator

Good places to look are Reddit (r/aquaponics, r/Hydroponics), the Backyard Aquaponics forum, aquaponics community sites, university extension Q&A, YouTube build logs with cost lists, and Indian hydroponics and biofloc groups and blogs. Record how many independent people report the same thing. Report any failures or warnings they mention, not only successes. Mark forum claims as anecdote, and never present them as fact.

## Source reliability (required on every value)

- **tier_1:** peer-reviewed papers, government statistics or cost norms (for example NHB/MIDH, NFDB/PMMSY, CBS, utility tariffs), university research station reports (for example UVI, SRAC).
- **tier_2:** extension guides, research institute notes (for example WUR/KWIN), industry reports, manufacturer datasheets.
- **tier_3:** retail and B2B listings (for example IndiaMART, Amazon, bol.com, toppy.nl), forums, blogs, videos.

For each value, give the tier, a confidence level (high, medium or low) with one line saying why, and corroboration: corroborated (two or more independent sources agree), single source, or conflicting. When sources conflict, give both values and do not average them. If a value can't be found, write "not found". Never estimate or fill in a number yourself. Don't convert currencies unless you cite the exchange rate and its date.

## Output format

1. A short summary per category: the main options, typical price ranges per market, the most-mentioned alternative, and the biggest gaps.
2. One table per category with the fields above, one row per item and market.
3. A machine-readable version: JSON lines, one object per item and market, using these keys: component_id (lowercase with underscores), name, category, role, function, system_types, grow_methods, scale, region, currency_code, dimensions, sizing {driver, capacity_per_unit, unit_label, rule, rule_source}, capex_per_unit {low, high, price_basis, source_ids}, lifetime_years {low, high, basis}, energy {power_w_per_unit, duty_hours_per_day}, footprint_m2_per_unit, labour_effect, trade_offs [ ], alternatives [ ], failure_modes [ ], source_tier, confidence, confidence_reason, corroboration {status, source_ids}.
4. A source list with an id, the full citation, the URL, the date read and the tier.
5. A gap list: the items and markets where you found no reliable price, dimension or lifetime.

## Do not

- Do not claim profitability, viability, fish safety or aeration adequacy.
- Do not size or design a specific farm.
- Do not invent prices, wages, lifetimes or dimensions. Use "not found" instead.
- Do not treat a single forum post as established practice.
