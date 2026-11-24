# Aquaponics Project — Chat Handoff Master Reference
_Last updated: 2026-04-20_

## Purpose

This file is a branch / handoff reference for continuing the Aquaponics project in a new chat.
It summarizes what was done in this chat, what was applied vs only proposed, what the current rules are, and what the next likely workstreams should be.

It is **not** the canonical source of truth for the repo.
Canonical repo truth remains:
- `data/knowledge/**` = canonical
- `data/simulation/**` = derived runtime
- `docs/**` = human-readable contracts / plans / governance
- `knowledge-vault/**` = human-readable note/navigation layer

---

## 1. Core repo boundary established in this chat

### Canonical vs derived
The project clarified and repeatedly enforced this boundary:

- `data/knowledge/**` is canonical
- `data/simulation/**` is derived runtime output / compatibility surface

This rule was used in:
- knowledge-layer reconciliation
- runtime-sync design
- evidence-promotion guidance
- business-layer prompts
- compatibility-audit prompts

### Important rule
Do **not** treat `data/simulation/**` as proof of canonical schema truth.
It can prove compatibility needs, but not biological/business truth.

---

## 2. Major work completed in this chat

## 2.1 Knowledge-layer reconciliation
A reconciliation pass was done to move important model content into canonical knowledge files instead of leaving it only in simulation-oriented locations.

### Applied Batch 4
Created:
- `data/knowledge/models/nitrification_models.json`
- `data/knowledge/models/solids_models.json`
- `data/knowledge/models/pump_aeration_models.json`
- `data/knowledge/models/greenhouse_climate_models.json`

Updated:
- `data/knowledge/models/plant_system_models.json`

Important note from the chat:
- `nitrification_models.json` explicitly included the direct **Biofilters and solids filters** corroboration report in `source_basis.primary_sources`
- no `data/simulation/**` files were modified in that batch

A commit was referenced:
- `Apply Batch 4 model reconciliation`
- commit shown in chat: `21de6cb`

## 2.2 Open questions / contradiction tracking cleanup
A follow-up pass proposed and then applied updates to:
- `data/knowledge/model_tickets/open_questions.json`
- `data/knowledge/evidence_maps/contradiction_log.yaml`
- `data/knowledge/evidence_maps/simulation_validation_map.json`

Notable ticket additions / updates included:
- refined `UQ-001`
- existing unresolved gap around aeration-energy modeling
- new context-split tickets for:
  - DWC depth
  - NFT biofilter requirement
  - solids-removal strategy
  - lettuce downy mildew wetness windows

---

## 3. Knowledge-to-runtime sync scaffold

A major piece of repo plumbing built in this chat was the first explicit sync flow from canonical knowledge to derived runtime files.

### Created
- `docs/knowledge_to_runtime_sync_plan.md`
- `src/build_runtime_from_knowledge.py`

### Intent
This scaffold makes the knowledge-to-runtime rule explicit:

- canonical knowledge is authored in `data/knowledge/**`
- runtime-compatible copies live in `data/simulation/**`
- runtime artifacts are regenerated from canon
- dry-run comes first
- apply mode writes only after preview + backup

### Supported scopes
The sync script was built for:
- `parameters`
- `species`
- `species_evidence`

### Key behavior of the sync script
- discovers canonical files under `data/knowledge/**`
- resolves runtime target paths, using `source_basis.derived_from_simulation_path` where needed
- applies compatibility transforms
- preserves runtime-only fields where appropriate
- adds a `runtime_sync` block
- validates generated payload shape
- supports:
  - `--dry-run`
  - `--apply`
  - scoped runs with repeated `--scope`

### Backups
Apply mode writes timestamped backups under:
- `data/simulation/_sync_backups/<timestamp>/...`

### Commit referenced in chat
- `Add knowledge-to-runtime sync scaffold`
- commit shown in chat: `87a627e`

---

## 4. Validation, summary reporting, and tests added to the sync flow

The sync scaffold was later strengthened with:

- generated-payload validation
- alias-consistency validation
- dry-run summary reporting
- snapshot-based tests / fixtures

### Main script behavior added
- per-scope summary counts
- dry-run summary report
- explicit validation pass/fail counts
- protection against alias conflicts
- better failure reporting for malformed payloads

### Test file added
- `tests/test_build_runtime_from_knowledge.py`

### Snapshot fixtures added
Representative snapshots were created for:
- water chemistry runtime output
- tilapia runtime species output
- tilapia runtime species-evidence output

### Confirmed test result from chat
At one point, the user ran:
- `Ran 10 tests in 0.019s`
- `OK`

That confirmed the sync test suite passed at that stage.

---

## 5. Windows / shell issues discovered and solved

A recurring issue in the chat was that PowerShell `python` pointed to the Windows Store stub instead of a runnable interpreter.

Known paths surfaced in chat:
- `C:\Users\ajith\AppData\Local\Microsoft\WindowsApps\python.exe`  -> Windows Store stub
- `C:\Users\ajith\AppData\Local\Python\bin\python.exe` -> real local interpreter
- `C:\Users\ajith\AppData\Local\Microsoft\WindowsApps\py.exe` -> stub

### Practical result
Use the real interpreter path when needed, for example:
- `C:\Users\ajith\AppData\Local\Python\bin\python.exe`

### Example commands used successfully
- `python src/build_runtime_from_knowledge.py --dry-run`
- `python -m unittest tests.test_build_runtime_from_knowledge -v`

### PowerShell note
`rg` / ripgrep was not available in one shell context.
Fallback recommended:
- PowerShell `Select-String`
- standard Python or git grep alternatives

---

## 6. Species-profile compatibility audit and minimal-safe canonical additions

A compatibility audit was done to determine what canonical field shapes are currently consumed by code.

### Real consumer findings
`src/simulate_overlap_score.py` was identified as a real consumer of:
- `environment.preferred_pH` as range object with `min` / `max`
- `environment.tolerated_pH` as range object with `min` / `max`
- `chemistry_response.unionized_nh3_critical_mg_L` as scalar

This led to the safe migration rule:

### Safe migration rule
- do **not** delete current consumed fields
- do **not** change existing field shape
- do **not** convert scalars to objects
- add richer context only as **sibling context fields**
- keep canonical names authoritative
- keep runtime aliases in derived/runtime compatibility surfaces unless canon has a proven need

### Minimal additive canonical changes applied
Applied to:
- `data/knowledge/species/fish/tilapia.json`
- `data/knowledge/species/plants/lettuce.json`
- `data/knowledge/species/plants/basil.json`
- `data/knowledge/model_tickets/open_questions.json`

These minimal additive changes were:

#### Tilapia
- added sibling context for prolonged-exposure NH3 interpretation
- added sibling context tying broader preferred temperature context to existing fields
- kept `unionized_nh3_critical_mg_L` unchanged

#### Lettuce
- added small-system / home-system pH context under `validation_benchmarks.aquaponics_context`
- kept `environment.preferred_pH` and `environment.tolerated_pH` unchanged

#### Basil
- kept scalar `nutrient_response.aquaponics_nitrateN_anchor_mg_L`
- added sibling context object for detailed UVI nitrate benchmark values
- did **not** add new alias fields into canon

#### Open questions
- added `UQ-011`
- topic: species-profile compatibility contract cleanup

---

## 7. Post-addition runtime/test state

After the above additive species changes, a dry-run showed:

- files scanned: 8
- files with proposed changes: 3
- unchanged: 5
- changed runtime outputs were:
  - `data/simulation/species/fish/tilapia.json`
  - `data/simulation/species/plants/basil.json`
  - `data/simulation/species/plants/lettuce.json`

### Important test status after those additions
A later test run showed:

- 10 tests ran
- 1 failure

The failing test was:
- `tests.test_build_runtime_from_knowledge.BuildRuntimeFromKnowledgeTests.test_species_snapshot_tilapia`

Reason:
- the tilapia species runtime snapshot fixture no longer matched after the approved additive tilapia sibling context fields

### Implication
The next minimal fix after those additive canonical changes is:
- update the tilapia runtime snapshot fixture only
- rerun sync dry-run and the unittest suite

This issue was explicitly recognized in the chat as the likely remaining follow-up risk.

---

## 8. Business-layer foundation work

A major separate workstream in this chat was the first-pass business layer.

### Business-layer intent
Create canonical business-layer scaffolding so the project can later evaluate:
- economic viability
- pricing / revenue translation structure
- CAPEX framing
- labor structure
- risk penalties
- channel assumptions

without yet implementing business integration logic

### Business-layer files discussed / created in the repo workflow
- `docs/business_layer_contract.md`
- `docs/business_layer_plan.md`
- `data/knowledge/business/pricing_models.json`
- `data/knowledge/business/cost_models.json`
- `data/knowledge/business/capex_models.json`
- `data/knowledge/business/labor_models.json`
- `data/knowledge/business/yield_to_revenue_rules.json`
- `data/knowledge/business/risk_penalty_models.json`
- `data/knowledge/business/channel_assumptions.json`

### Important business-layer rules established in prompts and reviews
- do not invent prices, wages, financing, utilization, or market assumptions
- use placeholder structures with explicit TODO assumptions
- keep schema simple and readable
- treat `data/knowledge/**` as canonical
- treat simulation outputs only as derived upstream inputs, not a frozen interface
- prefer explicit schema-choice TODOs when basis or driver choices are unresolved
- keep optional/deferred paths explicit
- do not do integration work in the foundation pass

### Important business-layer review themes
The cleanup and review passes emphasized:
- exact `canonical_owner` paths
- repo-addressable `source_basis.primary_sources`
- schema-choice TODOs for ambiguous bases
- consistent deferred / optional activation patterns
- risk penalty vocabularies kept in `draft` until normalized
- no redesign during cleanup passes

---

## 9. Architecture-specific business-layer strengthening (draft research/design state)

This chat then moved toward strengthening the business layer using architecture-aware distinctions for:
- media bed
- DWC / raft
- NFT

### Important status
This architecture-aware strengthening was discussed in detail and revised through prompts, but the chat evidence does **not** confirm a final applied/committed integration of all those diffs.
Treat this area as **draft / review state unless verified in the repo**.

### Main design direction agreed
Architecture-specific strengthening is useful for:
- CAPEX basis choices
- maintenance task libraries
- labor-driver basis
- output form / channel-fit interpretation
- architecture-conditioned risk penalties

### Important discipline point agreed
Do **not** force fake numbers.
Use deep research to improve:
- basis choice
- task categories
- architecture-conditioned structure
- what should remain TODO / deferred

---

## 10. AGENTS.md and automation guidance

The chat also moved into agent readiness and safe automation.

### AGENTS.md
The user drafted and applied an `AGENTS.md` file to govern:
- repo contract
- global safety rules
- branch discipline
- evidence/canon rules
- business-layer rules
- vault-linking rules
- automation ladder
- commit rules
- expected output style

The guidance was broadly approved as a solid start.

### Additional governance / planning docs discussed
A project roadmap/status doc was also drafted / refined:
- `docs/project_status_and_roadmap.md`

A suggested additional doc was also proposed:
- `docs/decision_rule_research_simulation_business.md`

That decision-rule doc explains when to use:
- deep research
- simulation
- business calculation
- repo audit / compatibility checks

### Automation candidate register
A future planning doc was discussed as a useful next governance artifact:
- `docs/automation_candidates.md`

Purpose:
- decide when repeated work should remain manual
- remain agent-assisted
- become hybrid
- or become local Python automation

Escalation rules proposed:
- repeated 3 times -> review for automation candidate
- repeated 5 times -> build a script unless judgment is clearly high

---

## 11. Obsidian / knowledge-vault work

The chat also included a smaller, separate stream for vault hygiene.

### Work discussed
- component-library note linking
- bounded vault-linking passes
- keeping `.obsidian/**` out of routine automation
- touching only markdown notes in vault-linking tasks
- preferring minimal hub-note linking over noisy overlinking

### Example specific fix discussed
- add a Related Notes wikilink from:
  - `knowledge-vault/Components/Component Library.md`
to:
  - `[[Components/Components|Components]]`

---

## 12. Recommended use of Codex vs local Python vs hybrid

A core project lesson from this chat:

### Keep as agent / Codex work when:
- interpretation is high
- evidence is mixed
- context-splitting matters
- canon / policy judgment is required
- contradiction vs context-split decisions are involved

### Prefer local Python when:
- extraction / checking / transformation is repetitive
- input/output pattern is stable
- success can be checked automatically
- JSON validity / field inventory / placeholder scanning / matrix generation is needed

### Prefer hybrid when:
- Python can extract / check / generate candidates
- agent/Codex should still do final wording, ranking, or judgment

### Do not fully automate yet:
- contradiction resolution
- evidence-to-canon promotion judgment
- context-split vs contradiction classification
- business-layer schema decisions where driver or basis is unresolved

---

## 13. High-value deep-research directions agreed in this chat

The chat converged on two especially strong deep-research packets.

### A. Highest value research packet
**Architecture-specific CAPEX basis choices and maintenance-task / labor driver bases for media bed vs DWC/raft vs NFT**

Why high value:
- resolves current schema-choice TODOs
- improves business-layer structure without inventing economics
- helps decide what is strong enough for canon vs what stays deferred

### B. Very high value next packet
**Architecture-conditioned output form, channel-fit, packaging implications, and post-harvest handling differences for lettuce and basil across media bed vs DWC/raft vs NFT**

Why useful:
- improves deferred output-form and channel-fit interpretation
- strengthens `yield_to_revenue_rules.json` and `channel_assumptions.json`
- avoids premature pricing / penalty calibration

Important caution agreed:
- architecture may condition channel-fit and packaging implications
- it should not be treated as the sole determinant of channel or profitability

---

## 14. Current branch / repo state signals captured during chat

At different points, the following repo conditions were reported:

- branch often used: `repo-migration-phase-1`
- at one point it was ahead of origin by multiple commits
- at another point it was up to date with origin
- there were repeated cases where:
  - knowledge-vault files changed due to Obsidian churn
  - `.gitignore` needed attention
  - `data` paths were ignored by git due to existing ignore rules
  - temporary files / logs appeared in working tree

### Practical discipline agreed
- keep commits small and scoped
- do not mix vault changes, business changes, and canonical knowledge changes in one commit
- show diffs before apply / commit
- no auto-commit
- use separate branches for bounded automation experiments

---

## 15. Commands that were practically important in this chat

### Sync dry-run
```powershell
python src/build_runtime_from_knowledge.py --dry-run
```

### Scoped sync
```powershell
python src/build_runtime_from_knowledge.py --dry-run --scope species
python src/build_runtime_from_knowledge.py --apply --scope parameters --scope species_evidence
```

### Unittest suite
```powershell
python -m unittest tests.test_build_runtime_from_knowledge -v
```

### When Windows Store python stub caused issues
Use the real interpreter path instead of the stub.

Example pattern:
```powershell
& "C:\Users\ajith\AppData\Local\Python\bin\python.exe" -u src\build_runtime_from_knowledge.py --dry-run
```

### Debug logging pattern that was suggested
```powershell
& "C:\Users\ajith\AppData\Local\Python\bin\python.exe" -u src\build_runtime_from_knowledge.py --dry-run *>&1 | Tee-Object sync_debug.log
```

---

## 16. Safe current understanding of project state

### Stable / established
- canonical vs derived repo boundary
- first sync scaffold exists
- sync validation / summary / tests exist
- business-layer foundation exists
- species compatibility policy is established:
  - preserve current consumed field shapes
  - add richer meaning as sibling context fields
- AGENTS.md-style governance direction is in place

### Likely still outstanding / needs repo verification
- update tilapia runtime snapshot fixture after approved additive canonical species changes
- rerun full sync dry-run and unittest suite after that fixture update
- confirm exact applied state of architecture-aware business-layer strengthening
- confirm current content of `docs/project_status_and_roadmap.md`
- confirm current content of `docs/decision_rule_research_simulation_business.md` if created

---

## 17. Best next steps if continuing from this handoff

Recommended continuation order:

1. **Verify current repo state**
   - inspect whether the tilapia fixture update was applied
   - rerun:
     - `python src/build_runtime_from_knowledge.py --dry-run`
     - `python -m unittest tests.test_build_runtime_from_knowledge -v`

2. **If tilapia fixture still mismatches**
   - update only the failing tilapia runtime snapshot fixture
   - do not modify code or canon in that pass

3. **Review business-layer applied state**
   - confirm what part of the business foundation is already committed
   - confirm whether architecture-aware strengthening remains draft or was applied later outside this chat

4. **If doing deep research next**
   - prioritize CAPEX-basis + maintenance/labor-driver research first
   - then do output-form / channel-fit / packaging / post-harvest research

5. **If doing repo-governance next**
   - finalize `docs/automation_candidates.md`
   - keep it a planning doc, not a canonical contract

6. **If doing vault work next**
   - keep it bounded, review-first, and isolated from business/canon changes

---

## 18. Suggested continuation prompt for a new chat

Use something like this in a new branch/new chat:

```text
Use the attached handoff file as the master reference for this branch.

First, summarize the current confirmed repo state versus draft-only items.
Treat `data/knowledge/**` as canonical and `data/simulation/**` as derived.
Do not assume draft proposals were applied unless the handoff marks them as applied or the repo confirms them.
Before proposing new work, identify:
1. what is already stable,
2. what is still failing or pending,
3. what the safest next bounded step is.

Then proceed in draft mode only unless I explicitly say apply.
```

---

## 19. Supporting files currently available with this handoff package

These files were uploaded into the working environment alongside this handoff and may be useful as additional source material:

- `Main chat.txt`
- `Architecture-specific business drivers for media bed, DWC, and NFT in aquaponics.md`
- `Architecture-Specific CAPEX Basis and Maintenance Driver Research Pack for Media Bed, DWC, and NFT Aquaponics.md`
- `Greenhouse climate control and disease-trigger variables.md`
- `Media bed vs DWC vs NFT.md`
- `Pumps and Aeration.md`
- `Distilled_Research_Pack_Aquaponics_L1.md`
- `Tilapia Species Profile Corroboration Report for Aquaponics Layer 1.pdf`
- `Lettuce_Corroboration report for aquaponics Layer 1 species profile.pdf`
- `Basil_Corroboration report for aquaponics Layer 1 species profile.pdf`
- `Water Chemistry and pH Management_Aquaponics Layer 1 Parameter Corroboration Report.pdf`
- `Biofilters and solids filters_Corroboration report for aquaponics Layer 1.pdf`
- `Pumps and aeration_Corroboration report for aquaponics Layer 1 component library.pdf`
- `Greenhouse climate control and disease-trigger variables_Corroboration report for aquaponics Layer 1 component and process library.pdf`
- `business_layer_foundation_proposed_v2.patch`
- `business_layer_foundation_cleanup_proposed_v3.patch`

---

## 20. Final caution

This handoff is intentionally careful about the difference between:

- **applied**
- **committed**
- **draft / proposed**
- **validated**
- **still pending repo verification**

If continuing in a new chat, verify the repo state before assuming every discussed proposal was actually applied.
