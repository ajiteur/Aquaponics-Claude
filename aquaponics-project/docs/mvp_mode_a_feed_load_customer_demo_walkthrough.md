# MVP Mode A Feed Load Customer Demo Walkthrough

## 1. Purpose

This note gives a concise walkthrough for using the implemented Mode A
feed-load demo runner with customers, growers, technical advisors, or seed-stage
advisors.

The walkthrough explains what the demo proves now, what it deliberately does not
prove yet, and what feedback to collect before building the next MVP layer.

## 2. Scope

This is a demo walkthrough only. It is not a product spec, code plan, canonical
biology update, runtime schema plan, economics model, or basil saleability pass.

The current demo remains Mode A only:

- direct daily feed input
- supplied protein fraction
- load-only TAN-N, oxygen-demand, and alkalinity-demand outputs
- missing-context labels for layers that are not ready to calculate

Basil `saleable_harvest_mass_kg` remains unresolved unless observed or
explicitly reviewed.

## 3. Seed-MVP Goal

The seed-MVP goal is to show a defensible aquaponics planning spine:

```text
fish feed input
-> TAN-N load
-> oxygen and alkalinity demand
-> missing context for concentration, NH3 risk, cost, sizing, and saleability
```

In plain language, the demo answers: "If this tilapia system feeds this much
feed with this protein level, what daily nitrogen load and nitrification support
demand does that create?"

It also shows disciplined uncertainty. When the system lacks water volume, pH,
temperature, feed price, tank volume, stocking density, biofilter capacity, or
observed basil saleable output, the report says those layers are unavailable
instead of inventing conclusions.

## 4. What The Mode A Demo Does

The demo command:

- reads an explicit JSON input file
- reads direct `feed_kg_day`
- reads direct `protein_fraction`
- calculates TAN-N / ammonia-N load
- calculates nitrification-support oxygen demand
- calculates nitrification-support CaCO3 alkalinity demand
- emits missing-context warning labels
- prints deterministic JSON to stdout

The demo does not write output files or runtime artifacts.

## 5. Demo Command

Run:

```powershell
python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_feed_load_inputs.json
```

This command was run before writing this walkthrough. Its actual output was used
as the basis for the example values and labels below.

## 6. Example Input Summary

The example input file is
`scripts/example_mvp_mode_a_feed_load_inputs.json`.

Input summary:

| Field | Value |
| --- | --- |
| `scenario_id` | `demo_mode_a_tilapia_basil_dwc` |
| `input_mode` | `mode_a_direct_feed` |
| `feed_kg_day` | `1.0` |
| `protein_fraction` | `0.32` |
| `feed_class` | `grow_out` |
| `protein_basis` | `scenario_default_candidate_from_tilapia_feed_research` |
| `architecture_context` | `tilapia_basil_dwc_raft` |

The context booleans for water volume, time basis, exchange/retention, pH,
temperature, feed price, tank volume, stocking density, and biofilter capacity
are explicitly set to `false`. That is why the demo emits missing-context
labels.

## 7. Example Output Values

From the actual demo output:

| Output | Value | Meaning |
| --- | ---: | --- |
| `tan_n_load_kg_day` | `0.02944` | Daily TAN-N / ammonia-N load in kg/day. |
| `tan_n_load_g_day` | `29.44` | Daily TAN-N / ammonia-N load in g/day. |
| `oxygen_demand_g_day` | `134.5408` | Nitrification-support oxygen demand in g O2/day. |
| `alkalinity_demand_g_caco3_day` | `210.2016` | Nitrification-support alkalinity demand in g CaCO3/day. |

These are load and demand values only. They are not water concentration,
toxicity, biofilter removal, cost, tank-sizing, or crop-saleability values.

## 8. How To Explain Missing-Context Labels

Explain the labels as a strength of the MVP, not as a failure. The demo is
showing the next required inputs instead of pretending the model knows them.

| Label | Plain-language explanation |
| --- | --- |
| `tan_concentration_unavailable_without_volume_time_exchange_or_removal` | The demo knows the TAN-N load, but cannot convert it to mg/L without water volume, time basis, exchange/retention, or removal context. |
| `nh3_risk_unavailable_without_ph_and_temperature` | The demo does not claim NH3 toxicity risk because unionized NH3 needs pH and temperature context. |
| `feed_cost_unavailable_without_feed_price` | The demo does not calculate feed cost because no feed price is supplied. |
| `tank_suitability_unavailable_without_volume_and_stocking_density` | The demo does not judge tank suitability without tank volume and stocking density. |
| `biofilter_removal_unavailable_without_capacity_and_conversion_assumption` | The demo shows nitrification demand, not confirmed biofilter conversion or removal. |
| `basil_saleable_output_unresolved_without_observed_or_reviewed_value` | The demo does not know basil saleable output; it remains unresolved until observed or explicitly reviewed. |

## 9. What The Demo Does Not Prove Yet

The demo does not prove:

- TAN concentration
- unionized NH3 toxicity
- fish safety
- system safety
- feed cost
- profitability
- tank suitability
- stocking-density suitability
- actual biofilter removal
- solids load
- Mode B fish-biomass-derived feeding
- basil saleable harvest mass
- basil revenue
- shrink, penalties, buyer acceptance, or saleability rates

The correct message is: the demo proves that the first load-only calculation and
uncertainty boundaries work.

## 10. 10-Minute Customer/Advisor Demo Script

Minute 0-1, opening framing:

- "This is the first working slice of the aquaponics planning engine."
- "It starts from a number growers understand: feed per day."
- "It turns feed and protein into daily nitrogen load and nitrification support
  demand."
- "It also tells us what it is not allowed to conclude yet."

Minute 1-2, show the input:

- Open `scripts/example_mvp_mode_a_feed_load_inputs.json`.
- Point to `feed_kg_day = 1.0`.
- Point to `protein_fraction = 0.32`.
- Explain that feed class and architecture are context only.

Minute 2-3, run the command:

```powershell
python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_feed_load_inputs.json
```

Minute 3-5, explain the load outputs:

- "One kg of feed per day at 32 percent protein creates `0.02944 kg/day`, or
  `29.44 g/day`, of TAN-N load."
- "That load implies `134.5408 g O2/day` of nitrification-support oxygen
  demand."
- "It also implies `210.2016 g CaCO3/day` of alkalinity demand."
- "These values are pressure on water quality and biofilter support, not proof
  of safety or removal."

Minute 5-7, explain missing-context labels:

- "The report refuses to calculate concentration because we did not give it
  water volume and exchange/removal context."
- "It refuses to calculate NH3 risk because we did not give it pH and
  temperature."
- "It refuses to calculate feed cost, tank suitability, and biofilter removal
  without the needed inputs."
- "It also keeps basil saleable output unresolved."

Minute 7-9, ask feedback questions:

- "Is daily feed input easy for you to provide?"
- "Would this load report help you discuss biofilter, aeration, or pH risk?"
- "Which missing input would you expect to add next?"
- "Which label is confusing?"
- "Which claim would you not trust yet?"

Minute 9-10, close with roadmap:

- "The next layer should add the customer/advisor inputs that matter most."
- "Possible next layers are concentration/NH3 risk, biofilter capacity,
  aeration/DO context, or feed-cost economics."
- "We should choose that next layer based on which missing-context labels are
  most valuable to resolve."

## 11. Audience-Specific Discovery Questions

Grower/operator questions:

- Do you know daily feed in kg/day, or is it easier to provide feed bags per
  week?
- Is feed protein available from the label?
- Does the feed class change by fish size or supplier?
- How often do you adjust feed rate?
- Which water-quality values do you measure reliably: TAN, pH, temperature, DO,
  alkalinity, or NH3?
- Do you know system water volume and tank volume?
- What biofilter type and media volume do you use?
- Which operational warning would help you most before a problem appears?

Technical advisor questions:

- Is the feed-to-TAN-N basis acceptable for first-pass load planning?
- Should the next layer prioritize TAN concentration, unionized NH3 risk,
  biofilter sizing, aeration, pH/alkalinity stability, or solids load?
- What minimum input set would make the concentration layer defensible?
- What context is needed before comparing nitrification demand to biofilter
  capacity?
- Which wording prevents users from mistaking demand for actual removal?
- Which units or labels are most likely to cause confusion?

Investor/advisor questions:

- Does this demo make the engine's causal spine clear?
- Is the missing-context behavior credible, or does it need a clearer UI/report
  explanation?
- Which unresolved label maps most directly to business risk?
- Is this enough to show technical discipline in a seed conversation?
- Which next layer would make the demo more fundable: NH3 risk, biofilter
  sizing, aeration risk, or feed-cost economics?
- What claims should the team avoid until more data exists?

## 12. Feedback-Capture Rubric

Use this rubric during or immediately after the demo.

| Category | Capture |
| --- | --- |
| Must-have for demo credibility | Inputs, outputs, or explanations the audience says are necessary before they trust the demo. |
| Confusing or unclear | Labels, units, field names, or boundaries the audience misunderstands. |
| Not valuable | Outputs or labels the audience says they would not use. |
| Next input customers expect | The next data fields users naturally want to provide, such as water volume, pH, temperature, feed price, biofilter media, or stocking density. |
| Claims we should avoid making | Any safety, profitability, sizing, removal, or saleability claim the audience says is not yet justified. |

Record whether each comment came from an operator, technical advisor, or
investor/advisor. The same feedback has different weight depending on the
audience.

## 13. How Feedback Informs The Next Layer

Use feedback to choose the next implementation layer:

- If users ask, "Is this TAN load dangerous?", prioritize TAN concentration and
  NH3 risk design.
- If users ask, "Can my biofilter handle this?", prioritize biofilter capacity
  and conversion-assumption design.
- If users ask, "Do I have enough oxygen?", prioritize aeration/DO context.
- If users ask, "What does this cost?", prioritize feed-cost economics only
  when feed price is supplied.
- If users ask, "What basil output does this produce?", keep saleable harvest
  out of scope and explain that observed or reviewed saleable mass is required.

The next layer should be selected by repeated customer/advisor pull, not by
adding every possible calculation at once.

## 14. Claims To Avoid

Avoid saying:

- "The system is safe."
- "The fish are safe from NH3."
- "The tank size is suitable."
- "The biofilter removes this load."
- "This is the feed cost."
- "This proves profitability."
- "This predicts basil saleable harvest."
- "Mode B biomass-derived feeding is implemented."
- "DWC/raft is the permanent best architecture."
- "The missing-context labels are failures."

Say instead:

- "This demo calculates daily feed-derived TAN-N load and nitrification support
  demand."
- "The report identifies the exact missing context needed for later risk,
  sizing, and economics layers."

## 15. Recommended Next Action

Run the walkthrough with at least one grower/operator and one technical advisor.
Capture which missing-context label they most want resolved next.

Recommended next repo-side planning pass:

- Review demo feedback.
- Choose one next layer only:
  - TAN concentration/NH3 risk
  - biofilter capacity
  - aeration/DO context
  - feed-cost economics
- Keep basil `saleable_harvest_mass_kg` unresolved until observed or explicitly
  reviewed.
