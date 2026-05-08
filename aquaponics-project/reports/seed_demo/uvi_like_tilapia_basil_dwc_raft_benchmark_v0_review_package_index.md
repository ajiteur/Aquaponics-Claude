# Aquaponics MVP Seed-Demo Review Package Index

## 1. Purpose

This index is the entry point for reviewing the current Aquaponics MVP seed-demo package for `uvi_like_tilapia_basil_dwc_raft_benchmark_v0`.

Use it to navigate the accepted static dashboard prototype, the seed-demo benchmark report, the expert-question package, and the supporting fixture/design context. It is a review navigation artifact only. It is not a new report, product spec, dashboard, pitch deck, commercial proof packet, or implementation artifact.

## 2. Package status

- Static dashboard prototype: accepted as Phase 5A complete.
- Prototype status: static, read-only, guardrailed, and presentation-only.
- Benchmark fixture status: public-evidence-inspired, scaled, and scenario-augmented.
- Evidence ceiling: mostly L1/L2, not L4 observed customer/operator data or L5 reviewed commercial data.
- Benchmark boundary: not direct UVI reproduction, not canon, not customer validation, not commercial proof, and not real-world operating proof.

## 3. Intended reviewers

| Reviewer | What to focus on |
| --- | --- |
| Technical investor/advisor | Whether the MVP spine, evidence labels, and blocked-claim discipline are clear enough for seed-demo discussion. |
| Aquaponics/RAS expert | Module scope, fish-tank concentration display, aeration/solids boundaries, pump/blower scaling, and benchmark-fit questions. |
| Future operator/customer reviewer | Which later observed records would be needed before the package can move beyond pre-customer benchmark context. |

## 4. Recommended review order

1. Open the [static dashboard prototype](uvi_like_tilapia_basil_dwc_raft_benchmark_v0_dashboard_prototype.html) first for the visual summary and visible guardrails.
2. Read the [seed-demo benchmark report](uvi_like_tilapia_basil_dwc_raft_benchmark_v0_report.md) for the written four-level MVP walkthrough and value traceability.
3. Read the [expert-question package](../../docs/mvp_expert_question_package_for_benchmark_review.md) for the review questions that should guide advisor feedback.
4. Inspect the [benchmark fixture JSON](../../data/benchmarks/uvi_like_tilapia_basil_dwc_raft_benchmark_v0.json) only if reviewing field-level evidence/readiness metadata.
5. Use the data contract and design docs only for deeper review of future data needs or UI/report design boundaries.

## 5. Artifact map

| Artifact | Path | Use |
| --- | --- | --- |
| Static dashboard prototype | [reports/seed_demo/uvi_like_tilapia_basil_dwc_raft_benchmark_v0_dashboard_prototype.html](uvi_like_tilapia_basil_dwc_raft_benchmark_v0_dashboard_prototype.html) | First-pass visual review surface with evidence/readiness badges, scope labels, and visible blocked claims. |
| Seed-demo benchmark report | [reports/seed_demo/uvi_like_tilapia_basil_dwc_raft_benchmark_v0_report.md](uvi_like_tilapia_basil_dwc_raft_benchmark_v0_report.md) | Written report explaining the four-level MVP output path, values, assumptions, evidence classes, and guardrails. |
| Benchmark fixture JSON | [data/benchmarks/uvi_like_tilapia_basil_dwc_raft_benchmark_v0.json](../../data/benchmarks/uvi_like_tilapia_basil_dwc_raft_benchmark_v0.json) | Source fixture for scenario identity, inputs, expected current outputs, evidence labels, readiness levels, and blocked/null fields. |
| Expert-question package | [docs/mvp_expert_question_package_for_benchmark_review.md](../../docs/mvp_expert_question_package_for_benchmark_review.md) | Review questions for module scope, raft area, water-quality display, pump/blower scaling, backup status, and basil saleability evidence. |
| Dashboard/report UI design | [docs/mvp_seed_demo_dashboard_report_ui_design.md](../../docs/mvp_seed_demo_dashboard_report_ui_design.md) | Design guardrails for the static dashboard/report presentation layer. |
| Evidence ingestion review | [docs/mvp_benchmark_evidence_ingestion_review.md](../../docs/mvp_benchmark_evidence_ingestion_review.md) | Source review and classification basis for benchmark-backed, scenario, scaled, business-overlay, modelled, blocked, and expert-question labels. |
| Unit-economics data contract | [docs/mvp_unit_economics_data_contract.md](../../docs/mvp_unit_economics_data_contract.md) | Future data requirements and null/blocked behavior for unit-economics review. |
| Seed-goal reset | [docs/mvp_unit_economics_seed_goal_reset.md](../../docs/mvp_unit_economics_seed_goal_reset.md) | Strategic framing for why current work stays pre-customer and guardrailed. |
| Goal-drift checklist | [docs/mvp_goal_drift_checklist.md](../../docs/mvp_goal_drift_checklist.md) | Checklist for preventing dashboard/report review from drifting into proof, product, or implementation work. |
| Operating manual decision playbook | [docs/mvp_operating_manual_decision_playbook.md](../../docs/mvp_operating_manual_decision_playbook.md) | Current MVP operating rules and stop conditions. |

## 6. What this package demonstrates

- A working current technical spine from Mode A feed/load through P1, P1.5, and P2a selected cost pressure.
- Benchmark-backed structure for explaining the current MVP pathway.
- Explicit assumptions, including feed, protein, fish-tank volume scope, measured DO context, dry-solids coefficient, and selected cost-pressure inputs.
- Evidence/readiness labels for current values and assumptions.
- Visible guardrails in the dashboard prototype and report.
- Blocked-claim discipline around safety, total-cost, revenue, profitability, commercial operability, and saleable basil output.

## 7. What this package does not demonstrate

- Does not demonstrate customer validation.
- Does not demonstrate commercial proof.
- Does not demonstrate real-world operating proof.
- Does not demonstrate fish safety or system safety.
- Does not demonstrate aeration adequacy.
- Does not demonstrate solids-removal capacity.
- Does not demonstrate total operating cost.
- Does not demonstrate revenue or profitability.
- Does not demonstrate commercial operability.
- Does not demonstrate known basil saleable harvest mass.

## 8. Current fixture/demo values

| Output | Current value | Review label |
| --- | --- | --- |
| TAN-N load | 29.44 g/day | Modelled current-engine output, L1 scenario-input context. |
| Nitrification oxygen demand | 134.5408 g/day | Modelled sub-load, not aeration capacity. |
| Alkalinity demand | 210.2016 g CaCO3/day | Modelled context, not dosing advice. |
| Estimated fish-tank TAN-N | 3.7743589743589743 mg/L | Modelled fish-tank context, not observed UVI measurement or safety proof. |
| Estimated unionized NH3 fraction | 0.006971085009084945 | Modelled chemistry context, not observed UVI chemistry. |
| Estimated NH3-N | 0.026311377265059072 mg/L | Modelled chemistry context, not fish-safety proof. |
| Estimated NH3 | 0.031949529536143155 mg/L | Modelled chemistry context, not system-safety proof. |
| Measured DO context | 5.0 mg/L | Supplied context only, not aeration adequacy. |
| Dry-solids potential | 0.25 kg/day | Potential only, not wet sludge, TSS, or removal capacity. |
| Scenario feed cost | 45.0 INR/day | Scenario cost-pressure input, non-benchmark business overlay. |
| Scenario power cost | 54.0 INR/day | Scenario cost-pressure input, nameplate-style power context. |
| Selected cost-pressure subtotal | 99.0 INR/day | Selected feed plus electricity pressure only, not total operating cost. |

## 9. Review questions

Focus reviewer feedback on these questions:

1. Module scope: what exact module boundary should this fixture represent?
2. Raft area implied by 1 kg/day feed: what raft growing area, if any, should be paired with the feed scalar?
3. Fish-tank versus total-system display: should future reports show only fish-tank context or a separate total-system context?
4. Pump/blower scaling: how should nameplate pump and blower assumptions be scaled or labelled?
5. Backup aeration/power status: what records are needed before reliability-adjacent wording is allowed?
6. Basil saleability evidence standard: what observed or reviewed handling/buyer evidence is enough before non-null saleable mass?

## 10. How to give useful feedback

- Mark each issue as `blocker`, `caution`, or `non-blocking note`.
- Separate technical-model feedback from business-evidence feedback.
- For technical feedback, identify the affected output, assumption, or display label.
- For evidence feedback, name the source basis or missing record needed.
- Do not request revenue/profitability unless required observed or explicitly reviewed quantity, price, currency, date, geography, buyer/channel, and complete-enough cost inputs exist.
- Do not request non-null `saleable_harvest_mass_kg` unless observed runtime output or explicit reviewed manual input exists.

## 11. Guardrails and blocked claims

The package should keep these guardrails visible during review:

- Benchmark assumptions remain scenario assumptions, not canon.
- The fixture remains public-evidence-inspired, scaled, and scenario-augmented.
- The fixture is not direct UVI reproduction.
- The fixture is not customer validation, commercial proof, or real-world operating proof.
- 7,800 L is fish-tank scoped, not total system volume and not whole-system average concentration context.
- TAN/NH3 values are modelled current-engine context, not observed UVI measurements and not safety proof.
- INR feed/electricity values are scenario inputs and non-benchmark business overlays.
- Selected cost-pressure subtotal is not total operating cost.
- Revenue, profitability, commercial operability, fish safety, system safety, aeration adequacy, solids-removal capacity, and known basil saleable harvest mass remain blocked.

## 12. Next decision after review

After reviewer feedback, decide whether to:

- revise benchmark fixture metadata in a later approved pass;
- revise report/prototype wording in a later scoped pass;
- prepare expert outreach using the current package;
- proceed to a guarded prototype v1;
- keep any claim blocked because required observed or reviewed data is missing.

## 13. Recommended next action

Use this index as the package entry point for expert/advisor review. The immediate next artifact should be an expert/advisor review packet that references this index and asks reviewers to answer the scoped questions above without treating the benchmark fixture as validation, proof, canon, or commercial evidence.
