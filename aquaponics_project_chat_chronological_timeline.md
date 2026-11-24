# Aquaponics Project — Chronological Chat Timeline
_Last updated: 2026-04-20_

## Purpose

This is a chronological timeline of the major decisions, changes, checks, and prompts from the source chat.
It is meant to help a new chat pick up the sequence of work, not just the current state.

It complements:
- `aquaponics_project_chat_handoff_master_reference.md`

Use this file when a new chat needs:
- sequence
- rationale
- what happened first vs later
- what was applied vs what remained draft

---

## 1. Knowledge-layer reconciliation began

The chat started with repo-cleanup and knowledge-layer reconciliation work.

Main direction established early:
- `data/knowledge/**` should become canonical
- `data/simulation/**` should be treated as derived/runtime
- simulation-side mirrors should not remain the primary source of truth

The user then moved through a batch-based reconciliation process.

---

## 2. Batch 4 was applied

The user reported that **Batch 4 only** was applied.

Created:
- `data/knowledge/models/nitrification_models.json`
- `data/knowledge/models/solids_models.json`
- `data/knowledge/models/pump_aeration_models.json`
- `data/knowledge/models/greenhouse_climate_models.json`

Updated:
- `data/knowledge/models/plant_system_models.json`

Important note explicitly recorded:
- `nitrification_models.json` included the direct **Biofilters and solids filters** corroboration report in `source_basis.primary_sources`
- no `data/simulation/**` files were modified in that pass

Later a commit was shown:
- `Apply Batch 4 model reconciliation`
- commit hash shown in chat: `21de6cb`

---

## 3. Batch 5 diffs were proposed and then applied

A later batch proposed updates to:
- `data/knowledge/model_tickets/open_questions.json`
- `data/knowledge/evidence_maps/contradiction_log.yaml`
- `data/knowledge/evidence_maps/simulation_validation_map.json`

The user later confirmed:
- “Done. Do we want to do a quick check? What is the next step?”

This established that the contradiction/open-question tracking layer was being formalized alongside the canonical model cleanup.

---

## 4. Repo and vault state checks happened

The user showed repo status and Obsidian export output.

Notable repo signals seen during this phase:
- branch often in use: `repo-migration-phase-1`
- vault exports updated many `knowledge-vault/**` files
- Obsidian churn touched multiple markdown notes
- `.obsidian/**` files appeared in warnings
- temporary files and ignored-path issues appeared intermittently

This helped establish a practical repo rule used later:
- keep vault changes separate from canon/business/runtime work
- do not treat vault churn as meaningful repo progress

---

## 5. Knowledge-to-runtime sync scaffold was designed

A major turning point in the chat was moving from ad hoc knowledge/runtime drift toward an explicit sync mechanism.

The sync plan and script were drafted to cover:
- `data/knowledge/parameters/**`
- `data/knowledge/species/**`
- `data/knowledge/species_evidence/**`

Main goals:
- dry-run first
- apply only after preview
- write backups before overwriting runtime outputs
- preserve runtime-only compatibility fields where necessary
- add runtime provenance metadata

New files created in that workflow:
- `docs/knowledge_to_runtime_sync_plan.md`
- `src/build_runtime_from_knowledge.py`

Later the user committed:
- `Add knowledge-to-runtime sync scaffold`
- commit shown in chat: `87a627e`

---

## 6. PowerShell / Python execution problems were discovered

When trying to run the new sync flow, the environment exposed a common Windows issue:

- `python` pointed to the Windows Store stub
- `py` was also not reliably runnable in that shell
- ripgrep (`rg`) was not available in at least one context

The chat then identified a real interpreter path:
- `C:\Users\ajith\AppData\Local\Python\bin\python.exe`

This became an important practical lesson:
- when working in that shell, use the real interpreter path rather than trusting `python`

---

## 7. Sync flow was strengthened with validation, summary reporting, and tests

The sync script was then extended with:
- payload validation
- alias-consistency validation
- dry-run summary reporting
- per-scope counts
- snapshot tests and fixtures

New test file:
- `tests/test_build_runtime_from_knowledge.py`

Representative fixtures were created for:
- runtime water chemistry
- runtime tilapia species
- runtime tilapia species evidence

A successful run was later reported:
- `Ran 10 tests in 0.019s`
- `OK`

This was a major stability milestone for the runtime-sync scaffold.

---

## 8. Species compatibility audit was performed

The next key phase was a compatibility audit of current runtime/species consumers.

The audit found real code consumers in:
- `src/simulate_overlap_score.py`

Important field-shape conclusions:
- `environment.preferred_pH` must remain a range object with `min` / `max`
- `environment.tolerated_pH` must remain a range object with `min` / `max`
- `chemistry_response.unionized_nh3_critical_mg_L` must remain a scalar

This led to a core project rule:

### Compatibility rule
- do not delete currently consumed fields
- do not change existing field shape
- do not convert scalars to objects
- add richer meaning only as **sibling context fields**
- keep canonical names authoritative
- keep runtime aliasing out of canon unless there is a real canonical need

This became one of the most important governance decisions in the whole chat.

---

## 9. Minimal-safe canonical species additions were proposed and refined

Using the compatibility audit, the chat refined what was safe to add to canon.

The safe changes were narrowed to minimal additive sibling-context changes only.

Eventually the user applied changes to:
- `data/knowledge/species/fish/tilapia.json`
- `data/knowledge/species/plants/lettuce.json`
- `data/knowledge/species/plants/basil.json`
- `data/knowledge/model_tickets/open_questions.json`

The changes were:
- tilapia: added context-only sibling fields, preserving consumed scalar/range fields
- lettuce: added small-system pH context under validation benchmark context
- basil: added nitrate benchmark context sibling without introducing new alias clutter
- open questions: added `UQ-011`

---

## 10. Runtime dry-run after those additions showed three changed species outputs

After the approved additive canonical species changes, a new dry-run showed:
- 8 files scanned
- 3 proposed runtime updates
- the changed runtime outputs were:
  - tilapia species runtime
  - basil species runtime
  - lettuce species runtime

This confirmed the new canonical sibling fields flowed through runtime sync as expected.

---

## 11. A test failure exposed the next required fix

After those canonical additions, the full unittest run showed:
- 10 tests ran
- 1 failure

Failing test:
- `test_species_snapshot_tilapia`

Cause:
- the expected runtime snapshot fixture for tilapia had not yet been updated to reflect the approved new sibling context fields

This established a very specific next-step fix:
- update the tilapia runtime snapshot fixture only
- do not touch code or canonical species files in that pass

---

## 12. Business-layer foundation became a major second workstream

Once the core knowledge/runtime boundary was stabilizing, the chat opened a separate business-layer workstream.

Primary intent:
- allow later economic evaluation of scenarios
- define canonical business-layer structure without implementing integration yet

Business-layer files discussed and built through prompts/review:
- `docs/business_layer_contract.md`
- `docs/business_layer_plan.md`
- `data/knowledge/business/pricing_models.json`
- `data/knowledge/business/cost_models.json`
- `data/knowledge/business/capex_models.json`
- `data/knowledge/business/labor_models.json`
- `data/knowledge/business/yield_to_revenue_rules.json`
- `data/knowledge/business/risk_penalty_models.json`
- `data/knowledge/business/channel_assumptions.json`

Core business-layer discipline agreed:
- do not invent numbers
- keep placeholders explicit
- keep schemas simple and readable
- use schema-choice TODOs when basis/driver is unresolved
- keep optional or deferred paths explicit
- no integration work yet

---

## 13. Business-layer cleanup prompts were refined heavily

Several rounds of prompt critique were done for business-layer cleanup and strengthening.

Recurring themes in the reviews:
- `canonical_owner` must be exact
- `source_basis.primary_sources` should be repo-addressable where possible
- ambiguous unit strings are really unresolved schema choices
- ambiguous `driver_key` cases should be marked as schema-choice TODOs
- optional business paths should use consistent activation flags
- `risk_penalty_models.json` should stay `draft` until vocabulary normalization is done
- do not turn missing evidence into fake numbers

This part of the chat produced a lot of schema/governance insight even when not every diff was applied immediately.

---

## 14. Architecture-specific business-layer strengthening emerged as the next big theme

After the foundation pass, the chat shifted toward architecture-specific business differences for:
- media bed
- DWC / raft
- NFT

The architecture-specific strengthening focused on:
- CAPEX basis choice
- maintenance task structure
- labor-driver basis
- output-form and channel-fit interpretation
- architecture-specific risk sensitivity

The strongest consensus from the chat:
- research should improve **structure**
- simulation should later estimate **frequency, severity, and realized burden**
- business calculation should later interpret that economically

This led directly into deep-research prompt design.

---

## 15. Deep-research prompt design became more disciplined

The chat then designed and evaluated deep-research packets, especially:

### A. Highest-value packet
Research:
- architecture-specific CAPEX basis choices
- maintenance-task libraries
- maintenance/labor driver bases
for media bed vs DWC/raft vs NFT

Why high value:
- resolves current schema-choice TODOs
- improves business-layer canon without inventing economics

### B. Very high-value follow-up packet
Research:
- architecture-conditioned output form
- channel-fit
- packaging implications
- post-harvest handling differences
for lettuce and basil across media bed vs DWC/raft vs NFT

Why useful:
- improves deferred output-form / channel-fit interpretation
- strengthens `yield_to_revenue_rules.json` and `channel_assumptions.json`
- avoids premature pricing/profitability assumptions

A key caution agreed:
- architecture may **condition** channel-fit and handling
- it should not be treated as a deterministic profitability rule

---

## 16. AGENTS.md was introduced

The user drafted and applied an `AGENTS.md` file.

This file established repo-safety rules for future agent/Codex work, including:
- canonical vs derived rules
- global safety rules
- branching rules
- evidence / canon workflow
- business-layer workflow
- vault-linking workflow
- automation ladder
- commit rules
- agent output style expectations

The document was considered a good start and aligned with the project's new discipline.

---

## 17. Project roadmap / status doc was drafted

The user also drafted a roadmap/status document:
- `docs/project_status_and_roadmap.md`

Its role was to:
- summarize what had been built
- estimate current readiness
- identify missing pieces
- sequence next phases
- separate immediate vs later priorities

This reflected a broader shift in the chat:
the project was moving from cleanup/plumbing into more intentional forward planning.

---

## 18. Decision-rule thinking was formalized

A note was proposed to explain when to use:
- deep research
- simulation
- business calculation
- repo audit / compatibility check

The stronger version was reframed as:
- research decides structure
- simulation decides dynamic behavior
- business calculation decides economic meaning
- repo audit decides what current code/tests/files can safely support

This became an important conceptual guardrail for future work.

---

## 19. Automation-governance thinking was introduced

The chat also moved toward deciding when repeated work should:
- stay manual
- stay agent-assisted
- become hybrid
- become local Python automation

A possible future doc was discussed:
- `docs/automation_candidates.md`

Key rule proposed:
- repeated 3 times -> review for automation candidate
- repeated 5 times -> build a script unless judgment is clearly high

The project repeatedly distinguished:
- low-judgment extraction/checking/transformation -> good Python candidate
- high-judgment evidence / canon / contradiction work -> keep agent-first

---

## 20. Knowledge-vault work stayed bounded and secondary

A smaller but repeated side stream in the chat involved Obsidian / knowledge-vault hygiene.

Main guidance:
- touch markdown notes only
- ignore `.obsidian/**` unless explicitly asked
- prefer minimal wikilink improvements
- keep vault work out of commits that touch canon/business/runtime logic

An example task:
- add a `Related Notes` section to `knowledge-vault/Components/Component Library.md`
- link back to `[[Components/Components|Components]]`

Vault work was treated as useful, but secondary to the main repo-contract and business-layer work.

---

## 21. A master handoff file was requested and created

Near the end of the chat, the user requested:
- a complete downloadable handoff file for branching or resuming in a new chat

A master reference file was created:
- `aquaponics_project_chat_handoff_master_reference.md`

That file was designed as:
- a careful state/handoff summary
- not a raw transcript
- focused on applied vs proposed, repo rules, current blockers, and next steps

---

## 22. This chronological timeline was then requested

After the master handoff file, the user asked for:
- a more chronological timeline of what happened in the chat

This file is that timeline.

---

## 23. Safest continuation order after this chat

If continuing from this timeline, the safest next sequence is:

1. verify current repo state
2. confirm whether the tilapia snapshot fixture update is still pending
3. rerun:
   - `python src/build_runtime_from_knowledge.py --dry-run`
   - `python -m unittest tests.test_build_runtime_from_knowledge -v`
4. confirm the exact applied state of the business-layer files
5. continue with deep research on:
   - CAPEX basis + maintenance/labor driver basis first
   - output form / channel-fit / packaging / post-harvest second
6. keep vault work separate
7. keep automation planning separate from canonical schema changes

---

## 24. Final timeline lesson

The biggest project shift in this chat was:

### From:
- scattered repo cleanup
- simulation-first file drift
- prompt-by-prompt local fixes

### To:
- explicit canonical vs derived governance
- validated runtime sync scaffold
- compatibility-aware canonical editing
- business-layer scaffolding
- safer agent rules
- better decision boundaries between research, simulation, business interpretation, and repo audit

That is the core story of this chat.
