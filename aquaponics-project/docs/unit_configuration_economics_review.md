# Unit Configuration Economics Review

Status: `draft`. Scenario estimate, not validated.

- Inputs: `data/scenarios/unit_configuration_candidates_v0.json` (non-canonical)
- Calculator: `scripts/compare_unit_configurations.py`
- Output: `data/simulation/results/unit_configuration_comparison.json`
- Candidate truths: `data/knowledge/atomic_facts/unit_economics_facts.json` (UE_0001 to UE_0011)

## Question

Which aquaponics unit design gets revenue per kg above cost per kg? Ajit asked for this
before the farm go/no-go, with the Netherlands and India compared side by side.

## What is compared

Each configuration is scored on **headroom per m2 per year**: revenue minus labour and
electricity. Headroom still has to pay for heating, CAPEX, consumables and, when owner
time isn't costed, the owner. None of those have sourced values yet, so headroom is an
upper bound on what a design can carry. It is not profit.

The **break-even labour intensity** is also reported: the labour hours per harvested kg
at which revenue just covers labour plus electricity. It is the clearest single target
for a design.

Cases: `low` takes the worst end of every range and `high` the best; `mid` takes the
midpoints.

## Results (scenario estimate, not validated)

Basil yield range for every basil design: 23.4 kg/m2/yr (UVI staggered, canon CROP_0004)
to 26.0 kg/m2/yr (simulated, fish feed sized to the UVI ratio, 2.00 kg/m2 x 13 crops, after PR #11).
Both are tropical-site yields. An under-fed unit yields far less, and Dutch winter light
and heat are not in the range.

India base price (2026-11-25): **INR 65-180/kg**, the Bangalore level Ajit confirmed from
local knowledge, corroborated by ten Bengaluru B2B listings (medium confidence). The old
INR 600-1,000/kg band from one 2025 Andhra hydroponic study is demoted to a sensitivity
case.

| Configuration | NL headroom EUR/m2/yr (low / mid / high) | India headroom INR/m2/yr (low / mid / high), base price |
|---|---|---|
| A. UVI-style DWC basil, hired, UVI labour intensity (0.56-0.62 h/kg) | -166 / -105 / -37 | -1,102 / 599 / 2,618 (about EUR -10 / 5 / 24) |
| B. Large raceway DWC basil, hired, Hawaii lettuce-farm labour per m2 (0.08-0.09 h/kg) | 72 / 121 / 175 | 0 / 1,724 / 3,719 |
| C. Basil farm at Purdue labour per kg (0.53-0.65 h/kg) | -177 / -98 / -13 | -1,153 / 803 / 3,021 |
| D. Large raceway DWC lettuce, Flemish auction price | -42 / -19 / 6 | gap: no India lettuce price |
| E. Owner-operated DWC basil, owner hours not costed | 111 / 156 / 207 | 179 / 1,875 / 3,841 (about EUR 2 / 17 / 35) |

Break-even labour intensity for basil wholesale:

- **Netherlands: 0.25 to 0.50 labour hours per harvested kg** (at EUR 16-19/h). This
  metric barely depends on yield, so it is the most robust result here.
- **India at the base price: about 0.09 to 2.5 hours per kg** (at about INR 60-88/h).
  At the demoted study band it would be 5 to 15 h/kg.

### India by state (base price)

State wages and tariffs come from the Farm inputs thread. The Bangalore price is used in
every state (a transfer outside Karnataka, low confidence there).

| State | Owner-run, INR/m2/yr (low / mid / high) | Hired, UVI labour, INR/m2/yr (low / mid / high) |
|---|---|---|
| Karnataka (listing price; see Ajit's price below) | 441 / 2,151 / 4,092 | -679 / 906 / 2,809 |
| Tamil Nadu | 76 / 1,943 / 3,999 | -1,262 / 582 / 2,744 |
| Andhra Pradesh | 725 / 2,245 / 4,067 | -613 / 967 / 2,864 |
| Telangana | 289 / 2,067 / 4,058 | -1,206 / 607 / 2,738 |

At the base price, electricity becomes a large share of cost, so state tariffs now
matter: Andhra Pradesh (lowest tariff band) leaves the most, Tamil Nadu the least.

### Karnataka at Ajit's Bangalore price (INR 100-250/kg)

Ajit's own read (2026-11-25) is INR 100-250/kg in Bangalore, depending on processed,
fresh or organic. It agrees with the INR 65-180 listings (medium confidence, pending
approval) and is now the Karnataka base; the listings stay as a Karnataka sensitivity case.

| Design (Karnataka, INR 100-250/kg) | INR/m2/yr (low / mid / high) | About EUR/m2/yr |
|---|---|---|
| A. UVI-style, hired, UVI labour | -23 / 2,021 / 4,483 | 0 / 18 / 41 |
| B. Large raceway, hired, lean labour | 940 / 3,109 / 5,609 | 9 / 28 / 51 |
| C. Purdue labour per kg | -68 / 2,149 / 4,710 | -1 / 20 / 43 |
| E. Owner-run | 1,097 / 3,266 / 5,766 | 10 / 30 / 53 |

That is about 50% more headroom than at the listing prices, but still well below the
Dutch owner-run case (EUR 111-207). The top of Ajit's band depends on grade (processed,
fresh, organic), so a defined grade and buyer would decide where in the band a unit sells.

### Demoted sensitivity: the INR 600-1,000/kg study band

At the old band every design clears in every state, with about INR 8,900-23,300/m2/yr
(about EUR 81-214). That band rests on one study's sale price and is now kept only to
show how much the India result depends on price.

## Findings

1. **In the Netherlands, hired labour decides it.** Every sourced basil labour
   intensity (UVI 0.56-0.62 h/kg, Purdue 0.53-0.65 h/kg) is above the 0.25-0.50 h/kg
   break-even, before heating or CAPEX. Only configuration B clears, and it borrows a
   lettuce farm's labour per m2 for basil. Basil-specific harvest and handling hours
   per kg are the most important missing number.
2. **Scale and simple raceways cut labour per m2 about sevenfold** (UVI 14.6 h/m2/yr at
   214 m2 versus Hawaii 2.0 h/m2/yr at about 1,142 m2). Processing and packing was 44%
   of the Hawaii hours, so harvest and pack flow is the design target.
3. **Owner-operated in the Netherlands leaves EUR 111-207/m2/yr** for heating, CAPEX and
   owner pay. In the low case (UVI labour intensity) that is about EUR 7.6 per owner hour
   before heating and CAPEX; in the mid case about EUR 19.
4. **Wholesale lettuce in the Low Countries does not work** at auction prices
   (EUR 0.19-0.72 per head) even at Hawaii labour efficiency. Basil earns about 4 to 11
   times more revenue per m2.
5. **India at the Bangalore price barely covers labour and electricity.** Owner-run
   basil leaves about EUR 2-37/m2/yr (INR 179-4,092), less than the Dutch owner-run case,
   and hired staff at UVI or Purdue labour intensity lose money in the low case. In the
   low case the owner earns about INR 5-50 per hour before CAPEX. India's cheap labour
   does not offset a basil price about 4 to 15 times lower than the Dutch EUR 7-9/kg at
   the comparison rate.

## Leading design candidates

- **Netherlands:** a larger (several hundred m2 or more) simple DWC raceway for basil,
  laid out for fast harvest and packing, fish feed sized to the UVI ratio, either
  owner-operated or with labour under about 0.25-0.5 h/kg. Viable only if heating plus
  CAPEX fit inside the headroom.
- **India:** wholesale basil at Bangalore prices does not leave enough. It would need
  a higher-value channel or crop, which this comparison has not covered yet.

## Deciding assumptions

| Assumption | Why it decides | Evidence now |
|---|---|---|
| Basil labour h/kg | Sets NL result sign | Only whole-system or cross-crop values (T3, medium/low) |
| Owner hours costed or not | Removes the labour line | Ajit's choice (open in Farm inputs thread) |
| Basil wholesale price | Linear driver of revenue | NL: 2020 price lists (low); India: Bangalore INR 65-180/kg, Ajit plus listings (medium) |
| Heating demand in NL | Could eat the headroom | Only a sector average, 0.99 GJ/m2 (not crop-specific) |
| CAPEX per m2 | Must fit the headroom | USD references only (about USD 190-1,110/m2) |
| Real yield | Scales revenue per m2 | UVI canon 23.4 kg/m2/yr; simulator 26.0 kg/m2/yr at the UVI feed ratio; under-fed units far lower |

## Source reliability

Every value in the inputs file carries an origin, and every source carries a tier,
confidence, reason and cross-check. Main internal problems noticed:

- Quagrainie et al. (Purdue): several internal inconsistencies, so confidence is low.
- VBT weekly prices: text extraction was scrambled and the unit is not printed.
- Zappernick et al.: only the methods were read verbatim; its total labour hours are not used.
- Tokunaga et al.: a representative model farm, lettuce only; applying it to basil is a transfer.

## What this does not claim

No profit, margin, ROI, payback, viability or total operating cost. Heating, CAPEX,
consumables and fish revenue are left out on purpose and listed as gaps. Nothing here
is canon or a value for `saleable_harvest_mass_kg`.

## Next steps

- Source basil harvest and pack labour per kg (task timing studies or grower data).
- Dutch heating demand for unlit, low-temperature basil or lettuce glasshouse.
- A Dutch or EU build cost per m2 for a simple greenhouse with DWC.
