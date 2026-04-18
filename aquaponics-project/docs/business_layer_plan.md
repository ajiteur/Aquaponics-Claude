# Business Layer Plan

## Objective

Build a first-pass business foundation that stays fully inside the knowledge layer and prepares the project for later pricing, margin, payback, and scenario-comparison work.

This plan is intentionally operational and phased. It does not define simulation-side integration work in this pass.

## Phase 0 - Foundation created in this pass

### Scope

- add a normative business-layer contract
- add canonical draft business knowledge files under `data/knowledge/business/**`
- keep missing business values explicit instead of guessed
- define what simulation outputs the business layer will eventually need

### Deliverables

- `docs/business_layer_contract.md`
- `docs/business_layer_plan.md`
- `data/knowledge/business/pricing_models.json`
- `data/knowledge/business/cost_models.json`
- `data/knowledge/business/capex_models.json`
- `data/knowledge/business/labor_models.json`
- `data/knowledge/business/yield_to_revenue_rules.json`
- `data/knowledge/business/risk_penalty_models.json`
- `data/knowledge/business/channel_assumptions.json`

### Non-goals

- no simulation logic changes
- no runtime sync changes
- no migrations
- no consumer updates
- no real price or wage calibration unless already present in canonical repo knowledge

## Phase 1 - Read-only interface mapping

### Goal

Map current simulation/runtime outputs into the business-layer contract without changing simulation behavior.

### Tasks

1. inspect current runtime outputs actually available under `data/simulation/**`
2. map existing field names to the contract fields in `docs/business_layer_contract.md`
3. identify which required-now fields already exist, which are derivable, and which are missing
4. produce a gap matrix for:
   - saleable yield
   - culls/downgrades
   - harvest timing
   - mortality
   - energy
   - feed
   - event/risk outputs

### Expected output

A read-only mapping note or audit document, not code changes.

## Phase 2 - Canonical business input completion

### Goal

Replace placeholder business inputs with sourced, reviewable, canonical assumptions.

### Fill order

1. currency and currency date basis
2. channel definitions and channel-specific sales units
3. product pricing records by channel and unit
4. variable cost records
5. labor activity standards and labor rates
6. CAPEX records and useful-life assumptions
7. risk penalty assumptions

### Review discipline

- keep `status` explicit: `draft`, `provisional`, `accepted`
- keep contradictory business assumptions separated by context rather than flattened prematurely
- document provenance before promoting from `draft` to `provisional` or `accepted`
- keep the current `0.1.0` version format provisional until a repo-wide version convention is confirmed
- when a rule depends on optional future upstream fields, mark it explicitly deferred with `enabled_by_default: false` and `activation_status: "optional_future"` rather than silently treating the dependency as required-now

## Phase 3 - Calculation layer design

### Goal

Define the later business-calculation module without implementing it yet.

### Design targets

- translate saleable yield into billable units
- attach price and cost assumptions by product and channel
- attach labor standards by activity driver
- calculate contribution margin before CAPEX
- annualize repeatable scenarios carefully
- calculate simple payback only when CAPEX and annualized cash contribution are available
- propagate nulls when required assumptions are still missing

### Important guardrails

- do not price culls as first-quality output
- do not use total biomass when only saleable biomass should be billed
- do not treat TAN or pH warnings directly as business outputs; translate them through explicit risk rules
- do not annualize from tiny sample windows without marking the result as provisional

## Phase 4 - Scenario comparison and presentation

### Goal

Compare alternative scenarios using a shared accounting basis.

### Comparison dimensions

- revenue
- variable cost
- labor
- contribution margin
- risk-adjusted margin
- utilization
- CAPEX intensity
- simple payback

### Presentation discipline

Internal decision support should come first. User-facing summaries should be derived from the internal metrics, not replace them.

## Schema strategy

### Keep the schemas simple

- use `records` for assumption libraries
- use `rules` for translation and penalty logic
- prefer a small number of readable records over a generic meta-framework
- keep explicit units everywhere a later numeric input is expected

### Placeholder policy

For missing required business inputs, use:

- `value: null`
- `assumption_status: "todo"`
- `assumption_note: "..."`

This keeps the data model stable while making uncertainty explicit.

## Known integration dependencies

Later business evaluation will need clean links to the following runtime outputs:

- plant saleable yield
- fish harvestable output
- fish mortality
- repeated-harvest survival decline
- harvest dates or harvest windows
- feed consumption
- energy consumption
- supplement usage where available
- quality/disease event signals
- downtime or backup-power events where available

## Key unresolved decisions for later review

1. primary geography and currency basis
2. product list and sale units to support first
3. channel mix to support first
4. whether lettuce is evaluated by head, kg, or both
5. whether basil is evaluated by bunch, kg, or both
6. whether fish is evaluated by live weight, whole fish, or processed yield
7. what utilization denominator should be canonical
8. whether risk penalties are modeled as revenue loss, extra cost, or both
9. which outputs should remain internal-only during the first user-facing iteration

## Recommended next step after this pass

Run a separate read-only audit of current simulation outputs against the new contract and produce a missing-field matrix.

That is the cleanest next move because it preserves the current boundary:

- business knowledge stays canonical,
- simulation stays untouched,
- integration gaps become explicit before any implementation work begins.
