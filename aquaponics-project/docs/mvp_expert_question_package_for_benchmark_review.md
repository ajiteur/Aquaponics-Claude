# MVP Expert Question Package for Benchmark Review

## 1. Purpose

This package turns the current UVI-like tilapia + basil DWC/raft benchmark
source gaps into targeted expert-review questions.

It is for later expert review of
`uvi_like_tilapia_basil_dwc_raft_benchmark_v0` before dashboard/report UI work.
It does not update the benchmark fixture, the seed-demo report, canonical
open-question tickets, evidence maps, source code, runtime output, or tests.

Expert review may improve wording, metadata, and future data-collection design.
It is not customer validation, commercial proof, real-world operating proof, or
full benchmark validation.

## 2. Relationship to benchmark fixture, seed-demo report, and source-gap backlog

Current artifacts define the working boundary:

- `data/benchmarks/uvi_like_tilapia_basil_dwc_raft_benchmark_v0.json` is a
  pre-customer benchmark fixture.
- `reports/seed_demo/uvi_like_tilapia_basil_dwc_raft_benchmark_v0_report.md`
  is the human-readable seed-demo report.
- `docs/mvp_benchmark_evidence_ingestion_review.md` says the fixture is
  public-evidence-inspired, scaled, and scenario-augmented.
- `docs/mvp_expert_question_backlog_and_source_gap_plan.md` identifies source
  gaps and later expert/customer questions.
- `docs/mvp_goal_drift_checklist.md` keeps future work aligned to the bounded
  tilapia + basil unit-economics path.

This package is a review-preparation artifact only. If answers later justify
repo changes, they should feed a separate review-first update pass.

## 3. Benchmark scenario briefing

The current scenario is a bounded tilapia + basil DWC/raft benchmark fixture
for the Mode A + P1 + P1.5 + P2a MVP spine:

- Mode A: feed/protein to TAN-N load, nitrification oxygen demand, and
  alkalinity demand.
- P1: fish-tank TAN-N/NH3 chemistry context.
- P1.5: supplied DO context and dry-solids potential.
- P2a: selected feed plus electricity cost-pressure example.

The fixture is public-evidence-inspired, scaled, and scenario-augmented. It is
not a direct reproduction of the full UVI commercial system, not canon, not
customer validation, not commercial proof, and not real-world operating proof.

## 4. Intended expert/reviewer types

| reviewer type | useful role | boundary |
|---|---|---|
| Aquaponics/RAS technical advisor | Review system boundary, water-quality display, aeration/power assumptions, and blocked claims. | Advisor review does not prove safety or real-world operation. |
| Commercial aquaponics operator | Later review of whether assumptions resemble practical records and operating constraints. | Operator review is later-stage unless needed for a blocker. |
| Academic/extension expert | Review public benchmark interpretation and source-fit caveats. | Source-fit review does not promote assumptions into canon. |
| Future customer/operator reviewer | Later review of required observed data and usability. | Customer/operator review is not currently available. |

## 5. Question format and priority system

Each question uses this format:

| field | meaning |
|---|---|
| question | The answerable expert-review question. |
| why it matters | The decision or claim boundary affected. |
| current assumption or gap | What the current fixture/report says or lacks. |
| answer resolves | What a good answer can improve. |
| answer does not resolve | Claims that must remain blocked after the answer. |
| impact if unresolved | What should stay cautious, blocked, or scenario-only. |
| affected artifacts | Benchmark fixture, seed-demo report, dashboard UI, future data contract, or later plan. |
| repo-side outcome | `update fixture metadata`, `update report wording`, `add dashboard guardrail`, `defer to customer/operator data`, or `keep blocked`. |
| priority | `high`, `medium`, or `low`. |

High priority means the question should be answered before a stronger fixture or
dashboard presentation. Medium priority means the answer improves later design
but does not block the current report. Low priority means useful context only.

## 6. Module scope and system-boundary questions

| id | priority | question | why it matters | current assumption or gap | answer resolves | answer does not resolve | impact if unresolved | affected artifacts | repo-side outcome |
|---|---|---|---|---|---|---|---|---|---|
| MS1 | high | What exact module boundary should this fixture represent: full UVI system, one fish tank plus proportional raft area, smaller demo module, or another bounded unit? | Controls how feed, raft area, power, and water volume should be described. | Module scope is an expert-question candidate. | Better fixture framing and report language. | Customer validation, commercial proof, or real-world operating proof. | Keep `feed_kg_day` and equipment power as scaled scenario inputs. | Benchmark fixture; seed-demo report; dashboard UI | update fixture metadata; update report wording; add dashboard guardrail |
| MS2 | high | Which public UVI/SRAC/extension reference should be treated as the closest comparison for this bounded module? | Prevents an overly broad "UVI-like" claim. | Source mapping is public-evidence-inspired but not a direct reproduction. | A clearer source-fit caveat. | Canon promotion or direct-UVI reproduction. | Keep public-benchmark language soft. | Benchmark fixture; seed-demo report | update fixture metadata; update report wording |
| MS3 | medium | What minimum system-boundary fields should be shown with any public-facing benchmark table? | Prevents hidden scope assumptions. | Current fixture carries scenario identity and metadata, but dashboard layout is not designed. | Required visible boundary fields for future UI. | Any stronger operating claim. | Dashboard UI must remain review-first. | Dashboard UI; future data contract | add dashboard guardrail |

## 7. Raft area and plant-production boundary questions

| id | priority | question | why it matters | current assumption or gap | answer resolves | answer does not resolve | impact if unresolved | affected artifacts | repo-side outcome |
|---|---|---|---|---|---|---|---|---|---|
| RA1 | high | What raft growing area is implied by `feed_kg_day = 1.0` under UVI-like feed-to-area logic? | Ties the feed scalar to plant-production boundary language. | `feed_kg_day = 1.0` is a scaled scenario input, not a full-UVI feed benchmark. | Whether a smaller raft-area interpretation is defensible. | Basil saleable harvest mass or revenue. | Keep raft area unresolved and avoid direct-UVI module visuals. | Benchmark fixture; seed-demo report; dashboard UI | update fixture metadata; add dashboard guardrail |
| RA2 | high | Should the fixture describe basil as biological production context only, or include a bounded plant-area placeholder? | Keeps plant-side framing honest without inventing output. | Basil production context is benchmarkable, but saleable output is blocked. | Whether plant area can be shown as scenario metadata. | `saleable_harvest_mass_kg` or basil saleability. | Keep plant-area display absent or clearly marked as unresolved. | Benchmark fixture; dashboard UI; future data contract | update fixture metadata; keep blocked |
| RA3 | medium | What plant-production boundary wording should appear beside any future raft diagram? | Prevents visuals from implying a validated crop-output module. | No dashboard/report UI exists yet. | Guardrail copy for future diagrams. | Customer/operator validation or commercial operation. | Future UI must use cautious labels. | Dashboard UI; seed-demo report | add dashboard guardrail; update report wording |

## 8. Fish-tank versus total-system display questions

| id | priority | question | why it matters | current assumption or gap | answer resolves | answer does not resolve | impact if unresolved | affected artifacts | repo-side outcome |
|---|---|---|---|---|---|---|---|---|---|
| WD1 | high | Should future reports show only fish-tank concentration context, or also a separately labelled total-system dilution context? | Prevents misreading `effective_water_volume_l = 7800` as total-system volume. | Current concentration scope is `fish_tank`. | Display rules for water-quality context. | Fish safety, system safety, or observed UVI measurements. | Keep only fish-tank scope with explicit warning. | Seed-demo report; dashboard UI; future data contract | update report wording; add dashboard guardrail |
| WD2 | high | What label should be used for `effective_water_volume_l = 7800` so readers know it is fish-tank scoped? | Keeps the benchmark-backed volume anchor scoped correctly. | Fish-tank scope is required for the current P1 context. | Standard display wording. | Whole-system average concentration. | Dashboard/report UI could overstate the water-quality basis. | Benchmark fixture; seed-demo report; dashboard UI | update fixture metadata; update report wording |
| WD3 | medium | What water-volume metadata should be required before any expanded concentration display is allowed? | Sets future data-contract expectations. | Total-system context is not part of current outputs. | Required field list for later design. | Safety or operating proof. | Expanded display should stay blocked. | Future data contract; dashboard UI | add dashboard guardrail; keep blocked |

## 9. Feed rate and stocking interpretation questions

| id | priority | question | why it matters | current assumption or gap | answer resolves | answer does not resolve | impact if unresolved | affected artifacts | repo-side outcome |
|---|---|---|---|---|---|---|---|---|---|
| FS1 | high | How should `feed_kg_day = 1.0` be described if the module boundary remains unresolved? | Avoids turning a scaled input into a benchmark feed default. | Current value is a scenario input and expert-question candidate. | Safer wording for fixture and report. | Biomass-derived feeding or stocking proof. | Keep Mode A direct-feed wording only. | Benchmark fixture; seed-demo report | update fixture metadata; update report wording |
| FS2 | medium | What fish stocking or biomass metadata would be needed before Mode B biomass feeding is reviewed? | Keeps biomass feeding out of the current technical spine. | Current MVP uses Mode A direct feed only. | Future data-contract fields and stop conditions. | Current benchmark output values or unit-economics proof. | Do not implement Mode B. | Future data contract; roadmap | keep blocked |
| FS3 | medium | What feed-class and feed-record metadata should accompany future real or reviewed feed data? | Improves later evidence quality without changing calculations. | `feed_class` exists as context only. | Metadata requirements for future records. | Fish growth, safety, or profitability. | Feed inputs remain scenario-labelled. | Future data contract | update fixture metadata later |

## 10. Pump/blower scaling and energy-assumption questions

| id | priority | question | why it matters | current assumption or gap | answer resolves | answer does not resolve | impact if unresolved | affected artifacts | repo-side outcome |
|---|---|---|---|---|---|---|---|---|---|
| PB1 | high | How should the 0.2 kW pump and 0.1 kW blower values be scaled from public UVI equipment context, if at all? | Power assumptions drive the P2a selected cost-pressure example. | Current device kW values are scaled engineering assumptions. | Scaling caveat and metadata needs. | Metered power, aeration adequacy, or system safety. | Keep values as scenario nameplate assumptions. | Benchmark fixture; seed-demo report; dashboard UI | update fixture metadata; add dashboard guardrail |
| PB2 | high | Should future reports prefer nameplate, metered, duty-cycle adjusted, or supplier-estimated power basis? | Controls how power inputs should be interpreted. | Current basis is `nameplate_kw`. | Power-basis vocabulary for future reporting. | Total operating cost or real operating proof. | Keep `nameplate_kw` caveat visible. | Future data contract; dashboard UI | add dashboard guardrail |
| PB3 | medium | What equipment metadata should be collected before any stronger power-cost confidence label is shown? | Prevents scenario power from looking measured. | No metered power record is present. | Required metadata for later P2c or real-world data. | Commercial operation or profitability. | Keep power cost as selected scenario pressure. | Future data contract; dashboard UI | defer to customer/operator data |

## 11. Aeration and backup-power questions

| id | priority | question | why it matters | current assumption or gap | answer resolves | answer does not resolve | impact if unresolved | affected artifacts | repo-side outcome |
|---|---|---|---|---|---|---|---|---|---|
| AB1 | high | What backup power or backup aeration status must be collected before reliability-adjacent wording is allowed? | Prevents hidden reliability or safety claims. | Backup status is absent and flagged as expert-question candidate. | Future evidence requirement. | Fish safety, system safety, or reliability proof. | Keep reliability-adjacent wording blocked. | Dashboard UI; future data contract | add dashboard guardrail; keep blocked |
| AB2 | high | What aeration records are needed before any later oxygen-transfer or adequacy evaluation can be considered? | Separates DO context from adequacy. | `measured_do_mg_l = 5.0` is supplied context only. | Data requirements for a future review. | Aeration adequacy in the current report. | Keep P1.5 as context only. | Future data contract; dashboard UI | keep blocked |
| AB3 | medium | Should future UI show nitrification oxygen demand beside supplied DO context, and with what warning? | Prevents comparing demand and DO as if they prove capacity. | Current report separates them but no dashboard exists. | Guardrail wording for future visuals. | Capacity proof or safety margin. | Keep any visual design review-first. | Dashboard UI | add dashboard guardrail |

## 12. Solids handling questions

| id | priority | question | why it matters | current assumption or gap | answer resolves | answer does not resolve | impact if unresolved | affected artifacts | repo-side outcome |
|---|---|---|---|---|---|---|---|---|---|
| SH1 | high | What solids-removal records are needed before dry-solids potential can be connected to actual removal practice? | Prevents dry-solids potential from becoming capacity language. | Current output is generated potential only. | Record requirements for future solids handling. | Solids-removal capacity or root-zone cleanliness. | Keep solids output as potential only. | Future data contract; dashboard UI | keep blocked |
| SH2 | medium | Which filter, clarifier, or purge-schedule metadata should be collected for later cost and maintenance review? | Links solids handling to later labor/maintenance data. | Labor and maintenance basis is a source gap. | Future data-contract fields. | Total operating cost. | Defer broader cost scope. | Future data contract | defer to customer/operator data |
| SH3 | medium | What wording should distinguish generated dry solids from captured or disposed solids? | Keeps the P1.5 output clear to non-technical readers. | Current report says potential only. | Better dashboard/report copy. | Capacity or disposal proof. | Keep guardrail panel mandatory. | Seed-demo report; dashboard UI | update report wording; add dashboard guardrail |

## 13. Basil production versus saleable basil evidence questions

| id | priority | question | why it matters | current assumption or gap | answer resolves | answer does not resolve | impact if unresolved | affected artifacts | repo-side outcome |
|---|---|---|---|---|---|---|---|---|---|
| BS1 | high | What observed or explicitly reviewed basil handling or buyer evidence is sufficient before `saleable_harvest_mass_kg` can become non-null? | Prevents proxy inference from benchmark production context. | Saleable harvest mass is null/blocked. | Evidence standard for later non-null status. | Revenue, profitability, or current saleable output. | Keep `saleable_harvest_mass_kg` blocked. | Future data contract; revenue/output contract | keep blocked |
| BS2 | high | What distinction should the report make between basil biological production context and saleable basil evidence? | Keeps benchmarkable production context separate from marketable output. | Production context may be benchmarkable; saleability is blocked. | Safer report/dashboard labels. | Known saleable harvest mass. | Keep saleability guardrail prominent. | Seed-demo report; dashboard UI | update report wording; add dashboard guardrail |
| BS3 | medium | What basil rejection, cull, buyer/channel, and handling records should be required later? | Prepares future observed-data collection. | No observed crop-output records are present. | Future data-contract fields. | Any current revenue or profitability output. | Defer to customer/operator data. | Future data contract | defer to customer/operator data |

## 14. Operating-cost overlay questions

| id | priority | question | why it matters | current assumption or gap | answer resolves | answer does not resolve | impact if unresolved | affected artifacts | repo-side outcome |
|---|---|---|---|---|---|---|---|---|---|
| OC1 | high | What metadata should accompany scenario feed price before it is shown externally? | Keeps feed price as traceable scenario input. | INR feed price is a non-benchmark business overlay. | Metadata checklist for supplier/source evidence. | Revenue, profitability, or total operating cost. | Keep feed price as scenario overlay. | Benchmark fixture; dashboard UI | update fixture metadata; add dashboard guardrail |
| OC2 | high | What metadata should accompany scenario electricity tariff before it is shown externally? | Keeps power cost geographically and temporally explicit. | INR tariff is a non-benchmark business overlay. | Metadata checklist for tariff evidence. | Total operating cost or economic viability. | Keep tariff as scenario overlay. | Benchmark fixture; dashboard UI | update fixture metadata; add dashboard guardrail |
| OC3 | medium | Which operating-cost categories must remain excluded from P2a selected cost-pressure wording? | Prevents P2a from reading as complete cost scope. | Current output is selected feed plus electricity subtotal only. | Future UI exclusions list. | Total operating cost. | Keep subtotal label and blocked total-cost claim. | Seed-demo report; dashboard UI; future data contract | add dashboard guardrail; keep blocked |

## 15. Dashboard/report guardrail questions

| id | priority | question | why it matters | current assumption or gap | answer resolves | answer does not resolve | impact if unresolved | affected artifacts | repo-side outcome |
|---|---|---|---|---|---|---|---|---|---|
| DG1 | high | Which guardrail panels must be visible before any dashboard/report UI work proceeds? | UI can imply stronger evidence than text if guardrails are hidden. | No dashboard exists. | Required panels for evidence class, readiness, scope, modelled status, and blocked claims. | Customer validation or commercial proof. | Dashboard work should stay review-first. | Dashboard UI | add dashboard guardrail |
| DG2 | high | How should each displayed value show evidence class and readiness level? | Prevents L1/L2 fixture values from reading like L4/L5 data. | Fixture metadata now has evidence classes. | Display convention for future UI. | Real-world operating proof. | UI should not proceed without visible labels. | Dashboard UI; benchmark fixture | add dashboard guardrail |
| DG3 | medium | What wording should appear next to the scenario title to prevent direct-UVI-reproduction interpretation? | Keeps the title from overclaiming. | Current report uses public-evidence-inspired, scaled, scenario-augmented language. | Title/subtitle guardrail. | Direct UVI reproduction or canon. | Any dashboard title must include caution wording. | Dashboard UI; seed-demo report | update report wording; add dashboard guardrail |

## 16. Questions to ask before dashboard UI

Ask these before any dashboard/report UI design moves beyond review-first
wireframes:

- MS1: exact module boundary.
- RA1: raft area implied by `feed_kg_day = 1.0`.
- WD1 and WD2: fish-tank versus total-system display and volume label.
- PB1 and PB2: pump/blower scaling and power-basis display.
- AB1 and AB3: backup/aeration-status boundaries and oxygen-demand display.
- BS2: basil production versus saleable-output wording.
- DG1, DG2, and DG3: required dashboard guardrail panels and title language.

If these remain unanswered, dashboard work should remain a review-first design
artifact with visible caution panels.

## 17. Questions to ask before benchmark fixture v1 update

Ask these before a future fixture v1 metadata or value-review pass:

- MS1 and MS2: module boundary and closest benchmark reference.
- RA1 and RA2: raft-area interpretation and plant-production placeholder.
- WD2 and WD3: fish-tank scope label and expanded concentration metadata.
- FS1 and FS3: feed-rate wording and feed-record metadata.
- PB1, PB2, and PB3: power scaling, power basis, and equipment metadata.
- OC1 and OC2: feed price and tariff source metadata.

A fixture v1 update should remain metadata/review-first unless a separate value
change review is explicitly approved.

## 18. Questions to ask before revenue/unit-economics work

Ask these before any revenue, broader cost, or unit-economics report work:

- BS1 and BS3: evidence standard for non-null saleable basil mass and crop
  output records.
- OC1, OC2, and OC3: feed price, tariff metadata, and excluded cost categories.
- SH2: labor and maintenance metadata for solids/filter/aeration work.
- PB3: measured or reviewed equipment-power basis.
- Later customer/operator questions about actual sale records, labor records,
  buyer/channel, date, geography, currency, and explicit scenario-versus-actual
  status.

Until these are answered with observed or explicitly reviewed inputs, revenue,
profitability, total operating cost, and commercial operability remain blocked.

## 19. Later customer/operator validation questions

These should wait until customer/operator access exists:

- What daily feed, biomass, mortality, and feed-class records are actually
  available?
- What tank volume, total system volume, equipment, runtime, and metering
  records are available?
- What water-quality measurements are collected, at what cadence, and by whom?
- What fish harvest, mortality, downgrade, buyer/channel, and sale records
  exist?
- What basil harvest, rejection, saleability, buyer/channel, and sale records
  exist?
- Which report outputs are useful to an operator, and which need stronger
  guardrails?

These are later-stage questions. They should not be described as already
answered by the benchmark fixture or expert review.

## 20. Do-not-ask-yet / drift-risk questions

Do not spend expert time on these until the bounded unit proof path is farther
along:

- Which new fish or plant species should be added next?
- What app/game layer should be built before the bounded unit proof?
- Can benchmark assumptions become canon?
- Can the current fixture prove fish safety, system safety, aeration adequacy,
  total operating cost, revenue, profitability, or commercial operability?
- Can public benchmark basil production evidence be used to populate
  `saleable_harvest_mass_kg`?
- Can dashboard polish replace the evidence-class and blocked-claim panels?

These questions create goal drift or imply claims that the current fixture does
not support.

## 21. Expert review briefing

Pasteable briefing:

We have a pre-customer benchmark fixture for a bounded tilapia + basil DWC/raft
aquaponics MVP. It follows the current Mode A + P1 + P1.5 + P2a spine: feed
load, TAN/NH3 chemistry context, aeration/solids context, and selected feed plus
electricity cost-pressure. The fixture is public-evidence-inspired, scaled, and
scenario-augmented. It is not a direct UVI reproduction, not canon, not customer
validation, not commercial proof, and not real-world operating proof.

The main review need is not to approve the model as commercially proven. The
need is to check whether the benchmark framing is honest: what module boundary
the 1.0 kg/day feed scenario represents, what raft area is implied, whether
fish-tank concentration display is sufficient, how pump/blower power should be
scaled or labelled, what backup/aeration evidence is required, and what observed
or reviewed basil evidence would be sufficient before saleable harvest mass can
become non-null.

## 22. Dashboard readiness verdict

Verdict: `caution`

Dashboard/report UI work should not imply the current fixture is a direct UVI
module, customer validation, commercial proof, real-world operating proof, a
safety result, a total-cost result, a revenue/profitability result, or known
basil saleability.

Review-first dashboard design can proceed only if it visibly includes:

- evidence class for every displayed value
- readiness level
- fish-tank versus total-system scope
- modelled-versus-observed status
- scenario business overlay status
- blocked-claim panel
- expert-question panel for module scope, raft area, power scaling, backup
  status, and basil saleability evidence

## 23. Recommended next action

Use this package in a short expert-review session focused on module scope, raft
area, fish-tank versus total-system display, pump/blower scaling, backup
power/aeration status, and basil saleability evidence standard. Capture answers
as review notes first; do not update canonical open-question tickets, fixture
values, the seed-demo report, or dashboard UI until a later explicitly scoped
apply pass is approved.
