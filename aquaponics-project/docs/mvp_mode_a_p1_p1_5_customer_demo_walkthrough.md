# MVP Mode A P1 P1.5 Customer Demo Walkthrough

## 1. Purpose

This walkthrough explains the current three-level MVP demo for customers,
operators, technical advisors, and seed-stage advisors.

It is a communication artifact only. It is not a validation packet, product
spec, implementation plan, runtime contract, economics model, or crop
saleability pass.

## 2. Current Seed-MVP Goal

The seed-MVP goal is to show a defensible aquaponics planning spine for a
tilapia + basil DWC/raft system:

```text
direct fish feed input
-> TAN-N load
-> nitrification oxygen and alkalinity demand
-> optional fish-tank TAN/NH3 chemistry context
-> optional aeration and solids context
-> explicit warning labels for what is still missing
```

The current demo shows useful water-quality and operations context without
claiming fish safety, system safety, profitability, aeration adequacy, solids
removal, or basil saleable harvest mass.

Basil `saleable_harvest_mass_kg` remains unresolved unless observed or
explicitly reviewed.

## 3. What The Three Demo Levels Show

| Demo level | Input file | What it shows | What it still refuses to claim |
| --- | --- | --- | --- |
| Level 1: Mode A load-only | `scripts/example_mvp_mode_a_feed_load_inputs.json` | Direct feed and protein become TAN-N load, nitrification oxygen demand, and alkalinity demand. | TAN concentration, NH3 context, feed cost, tank suitability, biofilter removal, aeration capacity, crop saleability. |
| Level 2: P1 water-quality context | `scripts/example_mvp_mode_a_p1_water_quality_inputs.json` | Adds fish-tank upper-bound/no-removal TAN-N concentration and freshwater NH3 chemistry when volume, time, pH, and temperature are supplied. | Safe/unsafe thresholds, fish safety, system safety, biofilter removal, aeration adequacy. |
| Level 3: P1.5 aeration/solids context | `scripts/example_mvp_mode_a_p1_5_aeration_solids_inputs.json` | Adds measured DO as context and provisional feed-linked dry-solids potential from an explicit scenario coefficient. | Total oxygen demand, fish respiration oxygen demand, oxygen-transfer capacity, aeration adequacy, wet sludge, TSS, solids-removal capacity. |

## 4. Level 1 Demo: Load-Only Explanation

Run:

```powershell
python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_feed_load_inputs.json
```

Level 1 starts with inputs most operators can understand:

| Field | Value |
| --- | --- |
| `scenario_id` | `demo_mode_a_tilapia_basil_dwc` |
| `input_mode` | `mode_a_direct_feed` |
| `feed_kg_day` | `1.0` |
| `protein_fraction` | `0.32` |
| `feed_class` | `grow_out` |
| `architecture_context` | `tilapia_basil_dwc_raft` |

The report calculates only feed-derived daily load values:

| Output | Actual value | Plain-language meaning |
| --- | ---: | --- |
| `tan_n_load_kg_day` | `0.02944` | Daily TAN-N / ammonia-N load in kg/day. |
| `tan_n_load_g_day` | `29.44` | Same TAN-N load in g/day. |
| `oxygen_demand_g_day` | `134.5408` | Nitrification-support oxygen demand, not total oxygen demand. |
| `alkalinity_demand_g_caco3_day` | `210.2016` | Nitrification-support alkalinity demand as CaCO3. |

How to say it:

"With 1 kg/day of grow-out feed at 32 percent protein, the demo estimates
29.44 g/day of TAN-N load. Supporting nitrification of that load would require
134.5408 g O2/day and 210.2016 g CaCO3/day. This is not yet concentration,
toxicity, removal, safety, cost, or profitability."

## 5. Level 2 Demo: P1 TAN/NH3 Water-Quality Context Explanation

Run:

```powershell
python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_p1_water_quality_inputs.json
```

Level 2 keeps the Level 1 load outputs and adds explicit water-quality context:

| Field | Value |
| --- | --- |
| `effective_water_volume_l` | `7800` |
| `accumulation_period_day` | `1` |
| `concentration_scope` | `fish_tank` |
| `concentration_assumption` | `upper_bound_no_removal` |
| `ph` | `7.0` |
| `water_temp_c` | `28.0` |
| `freshwater_assumption` | `true` |

Actual P1 output values:

| Output | Actual value | Plain-language meaning |
| --- | ---: | --- |
| `estimated_tan_n_mg_l` | `3.7743589743589743` | Estimated fish-tank TAN-N concentration under the upper-bound/no-removal assumption. |
| `estimated_unionized_nh3_fraction` | `0.006971085009084945` | Freshwater NH3 fraction at pH 7.0 and 28.0 C. |
| `estimated_nh3_n_mg_l` | `0.026311377265059072` | Estimated unionized ammonia as NH3-N. |
| `estimated_nh3_mg_l` | `0.031949529536143155` | Estimated unionized ammonia as NH3. |

How to say it:

"Level 2 asks a narrower question: if the same daily TAN-N load accumulated for
one day in a 7,800 L fish-tank control volume with no removal, what TAN-N
concentration and NH3 chemistry context would that imply at pH 7.0 and 28.0 C?
It gives chemistry context. It still does not compare against a threshold or
claim the fish are safe."

## 6. Level 3 Demo: P1.5 Aeration/Solids Context Explanation

Run:

```powershell
python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_p1_5_aeration_solids_inputs.json
```

Level 3 keeps Level 1 and Level 2 outputs, then adds aeration and solids
context:

| Field | Value |
| --- | --- |
| `include_aeration_solids_context` | `true` |
| `measured_do_mg_l` | `5.0` |
| `dry_solids_coefficient` | `0.25` |
| `dry_solids_basis` | `demo_scenario_input_not_canon` |
| aeration/solids context booleans | `false` unless explicitly supplied as available |

Actual P1.5 output values:

| Output | Actual value | Plain-language meaning |
| --- | ---: | --- |
| `nitrification_oxygen_demand_g_day` | `134.5408` | Echo of the Level 1 nitrification-support oxygen sub-load. |
| `measured_do_mg_l` | `5.0` | Context measurement only, not future safety proof. |
| `estimated_dry_solids_potential_kg_day` | `0.25` | Provisional feed-linked dry-solids potential from `1.0 * 0.25`. |

How to say it:

"Level 3 shows how the report can carry aeration and solids context without
overclaiming. It echoes the nitrification oxygen demand, echoes measured DO as
a context measurement, and estimates provisional dry-solids potential from an
explicit scenario coefficient. It does not say aeration is adequate, oxygen
transfer is sufficient, solids are removed, wet sludge is known, or TSS is
known."

## 7. What Changed From Level 1 To Level 2

Level 1 calculates load only.

Level 2 adds the minimum context needed for fish-tank TAN/NH3 chemistry:

- effective fish-tank water volume
- accumulation period
- concentration scope
- pH
- water temperature
- freshwater assumption

Level 2 resolves the missing-context labels for TAN concentration and NH3
chemistry because the required inputs are present. It keeps unrelated missing
context labels for feed price, tank suitability, biofilter removal, and basil
saleable output.

Level 2 does not add safety thresholds or safe/unsafe labels.

## 8. What Changed From Level 2 To Level 3

Level 2 adds water-quality chemistry context.

Level 3 adds P1.5 aeration and solids context:

- measured DO is echoed as context
- nitrification oxygen demand is carried as a known sub-load
- dry-solids potential is estimated only because a scenario coefficient is
  explicitly supplied
- P1.5 warning labels live inside `aeration_solids_context.status_labels`

Level 3 still blocks:

- total oxygen demand
- fish respiration oxygen demand
- organic-waste/decomposition oxygen demand
- oxygen-transfer capacity
- aeration adequacy
- wet sludge
- TSS concentration
- solids-removal capacity

## 9. Actual Example Output Values

These values came from running the three demo commands before writing this
walkthrough.

| Value | Level where present | Actual output |
| --- | --- | ---: |
| TAN-N load, kg/day | Levels 1-3 | `0.02944` |
| TAN-N load, g/day | Levels 1-3 | `29.44` |
| nitrification oxygen demand, g O2/day | Levels 1-3 | `134.5408` |
| alkalinity demand, g CaCO3/day | Levels 1-3 | `210.2016` |
| estimated TAN-N, mg/L | Levels 2-3 | `3.7743589743589743` |
| estimated NH3 fraction | Levels 2-3 | `0.006971085009084945` |
| estimated NH3-N, mg/L | Levels 2-3 | `0.026311377265059072` |
| estimated NH3, mg/L | Levels 2-3 | `0.031949529536143155` |
| measured DO context, mg/L | Level 3 | `5.0` |
| provisional dry-solids potential, kg/day | Level 3 | `0.25` |

## 10. Plain-Language Table

| Category | Current examples | Demo wording |
| --- | --- | --- |
| Calculated now | TAN-N load, nitrification oxygen demand, alkalinity demand, fish-tank upper-bound TAN-N concentration when P1 inputs exist, NH3 fraction when pH/temperature/freshwater context exists, provisional dry-solids potential when coefficient is supplied. | "The report can calculate these values from explicit inputs." |
| Context-only now | Feed class, protein basis, DWC/raft architecture context, measured DO, dry-solids basis, P1.5 availability flags. | "These fields frame interpretation but do not change safety or adequacy claims." |
| Warning/missing-context only | Feed price, tank volume and stocking density for suitability, biofilter capacity/conversion assumption, aeration capacity, oxygen-transfer basis, fish respiration oxygen demand, total oxygen demand, DWC/root-zone aeration, solids-removal capacity, clarifier retention, backup aeration/power continuity. | "The report names the missing inputs instead of inventing conclusions." |
| Blocked / not claimed | Fish safety, system safety, aeration adequacy, oxygen-transfer capacity, total oxygen demand, solids-removal capacity, wet sludge, TSS concentration, feed cost, profitability, basil saleable harvest mass. | "These remain out of scope until the required observed or reviewed inputs and threshold bases exist." |

## 11. Claims To Avoid

Do not say:

- "The fish are safe."
- "The system is safe."
- "Aeration is adequate."
- "Oxygen-transfer capacity is known."
- "Total oxygen demand is known."
- "Fish respiration oxygen demand is known."
- "Measured DO proves future safety."
- "The solids filter can remove this load."
- "Wet sludge is known."
- "TSS concentration is known."
- "Feed cost is known."
- "The system is profitable."
- "Basil saleable harvest mass is known."
- "This predicts basil revenue."

Say instead:

- "The demo calculates feed-derived load and selected context values from
  explicit inputs."
- "The report keeps warnings where context is still missing."
- "The current output is useful for advisor discussion, not a safety or
  profitability verdict."

## 12. 10-Minute Advisor/Operator Demo Script

Minute 0-1, framing:

- "This is a three-level MVP demo for the aquaponics planning engine."
- "It starts from feed, then adds water-quality context, then adds aeration and
  solids context."
- "The key feature is disciplined boundaries: it calculates what it can and
  labels what it cannot claim yet."

Minute 1-2, show Level 1 input:

- Open `scripts/example_mvp_mode_a_feed_load_inputs.json`.
- Point to `feed_kg_day = 1.0` and `protein_fraction = 0.32`.
- Explain that this is direct-feed Mode A, not biomass-derived Mode B.

Minute 2-3, run Level 1:

```powershell
python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_feed_load_inputs.json
```

- Explain `29.44 g/day` TAN-N load.
- Explain `134.5408 g O2/day` as nitrification oxygen demand only.
- Explain `210.2016 g CaCO3/day` as alkalinity demand.

Minute 3-5, run Level 2:

```powershell
python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_p1_water_quality_inputs.json
```

- Point to fish-tank scope, 7,800 L, one-day accumulation, pH 7.0, and 28.0 C.
- Explain `3.7743589743589743 mg TAN-N/L`.
- Explain NH3 fraction and NH3-N/NH3 outputs as chemistry context only.
- State clearly that there is no threshold comparison or fish-safety verdict.

Minute 5-7, run Level 3:

```powershell
python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_p1_5_aeration_solids_inputs.json
```

- Point to measured DO `5.0 mg/L` as context only.
- Point to dry-solids coefficient `0.25` as a demo scenario input, not canon.
- Explain `0.25 kg/day` dry-solids potential.
- Explain that the report still blocks total oxygen demand, aeration adequacy,
  wet sludge, TSS, and solids-removal capacity.

Minute 7-9, ask for feedback:

- "Which input could you provide reliably today?"
- "Which warning label is useful?"
- "Which warning label is confusing?"
- "Which missing layer would matter most in your operation or advisory review?"
- "Which claim would you distrust if we made it now?"

Minute 9-10, close:

- "The next step should be based on feedback, not on adding every possible
  calculation."
- "The strongest next hardening layer is likely input-basis and warning-label
  hardening for P1/P1.5, followed by whichever customer input proves easiest to
  supply reliably."

## 13. Discovery Questions

Operator questions:

- Can you provide daily feed as kg/day, lb/day, bags/week, or another stable
  unit?
- Can you provide feed protein from the feed label?
- Can you provide fish-tank volume separately from total system volume?
- Can you provide pH and water temperature reliably?
- Can you provide measured DO, and where is it measured?
- Can you describe aeration equipment by type, count, location, and backup
  plan?
- Can you describe solids filters, clarifiers, purge frequency, and cleaning
  practice?
- Which warning labels are useful or confusing?

Technical advisor questions:

- Is the Level 1 TAN-N load and nitrification-support demand framing clear?
- Is fish-tank upper-bound/no-removal the right first concentration scope?
- What threshold basis would be needed before any NH3 warning bands are shown?
- What minimum information is needed before aeration adequacy can be discussed?
- What solids coefficient or direct solids input would you accept for a demo?
- What wording best prevents confusion between dry-solids potential, wet sludge,
  TSS, and solids-removal capacity?

Investor/advisor questions:

- Does the three-level demo make the product thesis clear?
- Is the refusal to overclaim credible, or does it need a cleaner presentation?
- Which missing-context label maps most directly to business risk?
- Which next layer would make the MVP more compelling: threshold-labelled NH3
  warnings, aeration capacity inputs, solids-filter context, feed-cost
  scenario input, or customer feedback synthesis?
- Which claim would harm trust if made too early?

## 14. Feedback-Capture Rubric

| Rubric category | What to record |
| --- | --- |
| Must-have for credibility | Inputs, units, labels, or explanations the audience says are required before they trust the demo. |
| Confusing or unclear | Field names, labels, units, or boundaries the audience misreads. |
| Useful now | Outputs or warning labels the audience says they would use in planning or advisory discussion. |
| Not valuable now | Outputs or labels the audience says are not actionable. |
| Next input customers expect | The next data they naturally want to enter, such as water volume, pH, temperature, DO, aeration equipment, solids-filter details, or feed price. |
| Claims to avoid | Any safety, adequacy, profitability, or saleability claim the audience says would be premature. |

Record the audience type with each comment: operator, technical advisor,
investor/advisor, or other.

## 15. Recommended Next Action After Demo Feedback

Run this three-level walkthrough with at least:

- one grower/operator
- one technical aquaculture or aquaponics advisor
- one business or investor advisor

After each demo, classify feedback by:

- which inputs they can actually provide
- which calculated values they trust
- which warning labels help them
- which warning labels confuse them
- which blocked claims they agree should remain blocked

Use repeated feedback to choose one next repo-side pass. Do not broaden into
crop saleability, feed-cost economics, or capacity claims unless the required
inputs are explicit.

## 16. Recommended Next Technical Hardening Layer After This Walkthrough

Recommended next technical hardening layer:

- tighten P1/P1.5 input-basis wording and warning-label presentation after
  customer/advisor feedback
- keep Mode A direct feed as the demo spine
- keep P1 fish-tank concentration and NH3 chemistry separate from thresholds
- keep P1.5 aeration/solids context separate from adequacy and capacity claims
- keep basil `saleable_harvest_mass_kg` unresolved unless observed or
  explicitly reviewed

Do not add a safety verdict, profitability verdict, aeration-capacity
comparison, solids-removal claim, or basil saleable output claim as the next
technical step.
