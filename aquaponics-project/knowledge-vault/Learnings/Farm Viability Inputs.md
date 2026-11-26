# Farm Viability Inputs

Status: candidate, scenario estimate, not validated. Not canon.

Inputs record: `data/scenarios/farm_viability_inputs_v0.json`
Review: `docs/farm_viability_cost_basis_review.md`

## Learnings (2026-11-25)

- The UVI commercial aquaponics system (about 214 m2 of rafts) used about 3,120 labour hours and 23,360 kWh a year for fish, lettuce and basil together (Heidemann and Bailey 2015). The source does not split these by crop.
- At Dutch hired-labour rates (EUR 16 to 19/h), that labour alone works out to about EUR 10 to 20 per kg of basil, above the EUR 7 to 9/kg wholesale benchmark. This is an upper bound, since fish and lettuce share the hours.
- So whether the owner's own hours are costed is the most decisive input for a go/no-go.
- The EUR 500 batch fixed cost has no sourced replacement yet; it should be rebuilt from the real setup budget.
- Dutch non-household gas, smallest band, was about EUR 1.34 to 1.45 per m3 incl. VAT and tax in 2024 to 2026 H1 (CBS 85666ENG). Heat demand for basil is still unknown.

## India comparison (2026-11-25)

- Ajit wants India and the Netherlands compared side by side.
- India electricity is cheap per kg of basil (about INR 35 to 74). Labour per kg depends almost entirely on yield per labour day. Confidence: low.
- The one basil-specific India source, a 2025 Andhra Pradesh hydroponic study, gives about INR 650 to 850 per kg at legal minimum wage, about equal to its INR 600 to 1,000 price band. Confidence: low.
- That study's yield (about 0.95 kg/m2) is about 25x below UVI's, so it needs re-reading before use.
- India prices and tariffs are weaker evidence than the Dutch ones. Tier, confidence and reason are recorded per value in the inputs file.

## Four Indian states (2026-11-25)

- Ajit chose Karnataka, Tamil Nadu, Andhra Pradesh and Telangana. Values: `data/scenarios/india_state_location_inputs_v0.json`.
- Burdened minimum wage is about INR 70 to 100 per hour in all four. Only Telangana has a current state agriculture rate (G.O.Ms.No.6, June 2026). Confidence: low to medium.
- Electricity energy charges run about INR 3.5 to 10.5 per kWh. Which tariff category an aquaponic farm falls into (agri, horticulture, aquaculture or commercial) moves the rate more than the state does. Confidence: low to medium.
- Andhra Pradesh gives horticultural nurseries free power and aquaculture a Rs 1.50/unit concession. Eligibility for aquaponics is unknown.
- Bengaluru B2B listings for fresh Italian basil (IndiaMART, Nov 2026) ask Rs 65 to 180 per kg, median about Rs 110, across 10 sellers, including hydroponic growers. That is 5 to 15 times below the Rs 600 to 1,000 band used so far. Confidence: low (asking prices, market level unclear), but it is the biggest open risk for the India case.

## Waiting on Ajit

Grow area, building type, setup budget, electricity tariff, heating, sales channel and price, hours per week, and whether his own hours count as a cost.

Related: [[Simulation Learnings]]
