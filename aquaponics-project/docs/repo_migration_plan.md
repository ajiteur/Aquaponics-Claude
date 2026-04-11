# Repo Migration Plan

Generated on: `2026-04-11`

## Goal

Move the repository toward this canonical layout without changing behavior during the planning phase:

- `data/sources/`
- `data/knowledge/`
- `data/simulation/`
- `data/logs/`
- `knowledge-vault/`
- `archive/`

This report is a planning artifact only. No files have been moved yet.

## Canonical Layout Interpretation

### `data/sources/`
Raw source materials, extracted source snippets, source metadata, run configs used for source ingestion, and source-processing outputs.

### `data/knowledge/`
Curated knowledge artifacts: atomic facts, ontology, parameter libraries, evidence maps, digests, learning/update packets, model tickets, and related derived knowledge assets.

### `data/simulation/`
Simulation inputs, scenarios, species/component libraries, simulation outputs needed for current workflows, and simulation-specific observations.

### `data/logs/`
Execution logs, update-cycle logs, tuning logs, review/extraction runs, experiment reports, and transient/generated reports.

### `knowledge-vault/`
Human-readable Obsidian export only.

### `archive/`
Obsolete scratch material, superseded duplicates, historical backups, and files retained for reference but not needed as active sources of truth.

## Classification Summary

| Current Path | Classification | Proposed Destination |
|---|---|---|
| `aquaponics-knowledge/00_meta/` | move | `data/knowledge/meta/` |
| `aquaponics-knowledge/01_sources/` | merge | `data/sources/registry/` |
| `aquaponics-knowledge/02_ontology/` | move | `data/knowledge/ontology/` |
| `aquaponics-knowledge/03_atomic_facts/` | move | `data/knowledge/atomic_facts/` |
| `aquaponics-knowledge/04_process_models/` | move | `data/knowledge/process_models/` |
| `aquaponics-knowledge/05_parameter_library/` | merge | `data/knowledge/parameter_library/` |
| `aquaponics-knowledge/06_evidence_maps/` | move | `data/knowledge/evidence_maps/` |
| `aquaponics-knowledge/07_agent_outputs/extraction_runs/` | move | `data/logs/extraction_runs/` |
| `aquaponics-knowledge/07_agent_outputs/review_runs/` | move | `data/logs/review_runs/` |
| `aquaponics-knowledge/08_validation/` | move | `data/knowledge/validation/` |
| `aquaponics-knowledge/99_scratch/` | archive | `archive/aquaponics-knowledge/99_scratch/` |
| `data/input/` | move | `data/sources/input/` |
| `data/output/` | duplicate to review | likely split between `data/sources/extraction_outputs/` and `data/logs/extraction_runs/` |
| `data/report_digests/` | move | `data/knowledge/report_digests/` |
| `data/research_reports/raw/` | move | `data/sources/research_reports/raw/` |
| `data/research_reports/markdown/` | move | `data/sources/research_reports/markdown/` |
| `data/research_reports/metadata/` | move | `data/sources/research_reports/metadata/` |
| `data/run_configs/` | move | `data/sources/run_configs/` |
| `data/simulation/` | keep in place | `data/simulation/` |
| `data/simulation_observations/` | move | `data/simulation/observations/` |
| `data/learning_packets/` | move | `data/knowledge/learning_packets/` |
| `data/model_tickets/` | move | `data/knowledge/model_tickets/` |
| `data/tuning_packets/` | move | `data/knowledge/tuning_packets/` |
| `data/update_packets/` | move | `data/knowledge/update_packets/` |
| `data/update_logs/` | move | `data/logs/update_logs/` |
| `knowledge-vault/` | keep in place | `knowledge-vault/` |
| `configs/` | keep in place | no change in this migration |
| `schemas/` | keep in place | no change in this migration |
| `src/` | keep in place | no change in this migration |
| `.env` | keep in place | no change |
| `.gitignore` | keep in place | no change |

## Detailed Plan

### 1. Active Simulation Area

| Current Path | Classification | Proposed Destination | Notes |
|---|---|---|---|
| `data/simulation/scenario_defaults.json` | keep in place | `data/simulation/scenario_defaults.json` | Canonical simulation config. |
| `data/simulation/parameter_library.json` | keep in place for now | `data/simulation/parameter_library.json` | Possible later merge with `data/knowledge/parameter_library/`, but leave in place during first migration to avoid simulation breakage. |
| `data/simulation/tradeoff_matrix_results.json` | keep in place | `data/simulation/tradeoff_matrix_results.json` | Simulation result artifact used by current workflows. |
| `data/simulation/multi_day_summary.json` | keep in place | `data/simulation/multi_day_summary.json` | Actively overwritten by current scripts. |
| `data/simulation/scenarios/` | keep in place | `data/simulation/scenarios/` | Core scenario inputs and generated scenario snapshots. |
| `data/simulation/species/` | keep in place | `data/simulation/species/` | Core simulation species profiles. |
| `data/simulation/species_evidence/` | keep in place for now | `data/simulation/species_evidence/` | Closely coupled to profile-writing scripts; can later be reviewed for duplication with `data/knowledge/evidence_maps/`. |
| `data/simulation/day_logs/` | keep in place for now | `data/simulation/day_logs/` | Simulation execution output; optional future move to `data/logs/simulation/day_logs/`, but first migration should avoid changing active simulation paths. |
| `data/simulation/components/component_library.json` | keep in place | `data/simulation/components/component_library.json` | Active simulation component library. |
| `data/simulation/components/component_variants.json` | keep in place | `data/simulation/components/component_variants.json` | Active simulation component variants. |
| `data/simulation_observations/` | move | `data/simulation/observations/` | Better grouped under simulation. |

### 2. Source Material and Ingestion

| Current Path | Classification | Proposed Destination | Notes |
|---|---|---|---|
| `data/input/*.txt` | move | `data/sources/input/` | Raw source excerpts. |
| `data/input/run_config.yaml` | move | `data/sources/input/run_config.yaml` | Ingestion config should live with source input. |
| `data/run_configs/*.yaml` | move | `data/sources/run_configs/` | Source/extraction run configs. |
| `data/research_reports/raw/*.pdf` | move | `data/sources/research_reports/raw/` | Primary PDFs. |
| `data/research_reports/markdown/*.md` | move | `data/sources/research_reports/markdown/` | Human-readable source report derivatives. |
| `data/research_reports/metadata/` | move | `data/sources/research_reports/metadata/` | Source metadata belongs with sources. |
| `aquaponics-knowledge/01_sources/` | merge | `data/sources/registry/` | Review for overlap with `data/research_reports` and `data/input`. |
| `data/output/*.json` | duplicate to review | see notes below | This directory appears to duplicate extraction artifacts in `aquaponics-knowledge/07_agent_outputs/extraction_runs/`. |

### 3. Knowledge Assets

| Current Path | Classification | Proposed Destination | Notes |
|---|---|---|---|
| `aquaponics-knowledge/00_meta/assumptions.yaml` | move | `data/knowledge/meta/assumptions.yaml` | Knowledge governance metadata. |
| `aquaponics-knowledge/00_meta/project_scope.yaml` | move | `data/knowledge/meta/project_scope.yaml` | Knowledge governance metadata. |
| `aquaponics-knowledge/00_meta/version_log.md` | move | `data/knowledge/meta/version_log.md` | Knowledge governance metadata. |
| `aquaponics-knowledge/02_ontology/*.yaml` | move | `data/knowledge/ontology/` | Canonical ontology. |
| `aquaponics-knowledge/03_atomic_facts/*.json` | move | `data/knowledge/atomic_facts/` | Primary truth-source set. |
| `aquaponics-knowledge/04_process_models/*.yaml` | move | `data/knowledge/process_models/` | Knowledge models, not simulation runtime data. |
| `aquaponics-knowledge/05_parameter_library/*.yaml` | merge | `data/knowledge/parameter_library/` | Potential overlap with `data/simulation/parameter_library.json`. |
| `aquaponics-knowledge/06_evidence_maps/*` | move | `data/knowledge/evidence_maps/` | Evidence linkage and promotion artifacts. |
| `aquaponics-knowledge/08_validation/*.yaml` | move | `data/knowledge/validation/` | Knowledge validation assets. |
| `data/report_digests/*.json` | move | `data/knowledge/report_digests/` | Curated derived knowledge. |
| `data/learning_packets/latest_learning_packet.json` | move | `data/knowledge/learning_packets/latest_learning_packet.json` | Derived knowledge packet. |
| `data/model_tickets/latest_model_tickets.json` | move | `data/knowledge/model_tickets/latest_model_tickets.json` | Derived knowledge ticketing. |
| `data/tuning_packets/latest_scenario_tuning_packet.json` | move | `data/knowledge/tuning_packets/latest_scenario_tuning_packet.json` | Knowledge-to-simulation packet. |
| `data/update_packets/latest_update_packet.json` | move | `data/knowledge/update_packets/latest_update_packet.json` | Derived update packet. |
| `data/sample_claims.json` | move | `data/knowledge/sample_claims.json` | Better aligned with claim/review workflows than sources. |

### 4. Logs and Run Artifacts

| Current Path | Classification | Proposed Destination | Notes |
|---|---|---|---|
| `data/update_logs/*.json` | move | `data/logs/update_logs/` | Canonical run/update logs. |
| `aquaponics-knowledge/07_agent_outputs/extraction_runs/*.json` | move | `data/logs/extraction_runs/` | Extraction run logs. |
| `aquaponics-knowledge/07_agent_outputs/review_runs/*.json` | move | `data/logs/review_runs/` | Review run logs. |
| `data/output/*.json` | merge | `data/logs/extraction_runs/` or `data/sources/extraction_outputs/` | Must be deduplicated against `aquaponics-knowledge/07_agent_outputs/extraction_runs/`. |
| `data/simulation/day_logs/*.json` | keep in place for now | `data/simulation/day_logs/` | Leave unchanged during first migration to minimize simulation script changes. |
| scenario backup files under `data/update_logs/` | archive after review | `archive/logs/update_logs/` | These are useful historically but clutter active logs. |
| repeated generated scenario snapshots under `data/simulation/scenarios/*_day_*.json` | archive after retention policy is set | `archive/simulation/scenarios/` | Keep live for now if current scripts still inspect them. |

### 5. Vault and Human-Readable Exports

| Current Path | Classification | Proposed Destination | Notes |
|---|---|---|---|
| `knowledge-vault/` | keep in place | `knowledge-vault/` | Already canonical. |
| generated markdown under `knowledge-vault/` | keep in place | same | Human-readable export layer only. |

### 6. Scratch / Historical / Low-Signal Material

| Current Path | Classification | Proposed Destination | Notes |
|---|---|---|---|
| `aquaponics-knowledge/99_scratch/` | archive | `archive/aquaponics-knowledge/99_scratch/` | Non-canonical scratch. |
| `aquaponics-knowledge/03_atomic_facts/approved_facts_backup.json` | archive | `archive/knowledge/atomic_facts/approved_facts_backup.json` | Historical backup, not primary truth source. |
| superseded update-cycle logs and baseline backups | archive | `archive/logs/update_logs/` | Good candidate for staged archival. |
| repeated extraction outputs with same source and different timestamps | duplicate to review | likely `archive/logs/extraction_runs/` for superseded copies | Requires dedupe policy. |

## Duplicate Truth Sources and Merge Risks

### High-risk duplicate truth areas

#### 1. `aquaponics-knowledge/03_atomic_facts/` vs `data/simulation/atomic_facts_*.json`
Current risk:
- [src/export_obsidian_vault.py](C:/Users/ajith/Documents/Aquaponics/aquaponics-project/src/export_obsidian_vault.py) explicitly checks both locations.
- That means the repo already tolerates duplicate truth-source locations.

Recommendation:
- Make `data/knowledge/atomic_facts/` the only canonical home.
- Mark any `data/simulation/atomic_facts_*.json` as duplicate to review and eliminate after script updates.

Classification:
- `aquaponics-knowledge/03_atomic_facts/` -> move to `data/knowledge/atomic_facts/`
- `data/simulation/atomic_facts_*.json` -> duplicate to review, then archive or remove after cutover

#### 2. `aquaponics-knowledge/05_parameter_library/` vs `data/simulation/parameter_library.json`
Current risk:
- There is a YAML knowledge parameter library and a JSON simulation parameter library.
- They are similar in purpose but not identical in structure or consumer scripts.

Recommendation:
- Keep `data/simulation/parameter_library.json` in place as the simulation-facing artifact.
- Move YAML knowledge parameter files into `data/knowledge/parameter_library/`.
- Add an explicit future decision: either generate the simulation JSON from the knowledge library or document them as separate layers.

Classification:
- knowledge YAML -> merge into `data/knowledge/parameter_library/`
- simulation JSON -> keep in place for now

#### 3. `data/output/*.json` vs `aquaponics-knowledge/07_agent_outputs/extraction_runs/*.json`
Current risk:
- Filenames strongly overlap.
- These appear to be duplicate or near-duplicate extraction artifacts.

Recommendation:
- Compare by filename stem and content hash.
- Choose one canonical home for extraction outputs.
- My recommendation is `data/logs/extraction_runs/` for run artifacts, with optional `archive/` for duplicates.

Classification:
- both locations -> duplicate to review

#### 4. `data/report_digests/`, `data/learning_packets/`, `data/update_packets/`, `data/model_tickets/`
Current risk:
- These are all knowledge artifacts derived from source processing and simulation workflows, but they are scattered across `data/`.

Recommendation:
- Consolidate under `data/knowledge/`.
- Keep each subfolder separate to preserve workflow boundaries.

#### 5. `data/simulation/species_evidence/` vs `data/knowledge/evidence_maps/`
Current risk:
- Not direct duplicates, but conceptually overlapping evidence storage.

Recommendation:
- Do not merge in first migration.
- Treat `species_evidence` as simulation-adjacent evidence needed by profile generation.
- Treat `evidence_maps` as repository-wide knowledge governance artifacts.

## Script Update Impact

These path changes will require script updates if the migration is executed.

### Direct references to `aquaponics-knowledge`

| Script | Current Use | Required Change |
|---|---|---|
| [src/api_bot.py](C:/Users/ajith/Documents/Aquaponics/aquaponics-project/src/api_bot.py) | References `aquaponics-knowledge` as a root search area | Update to `data/knowledge` and possibly `data/sources` |
| [src/apply_learning_packet.py](C:/Users/ajith/Documents/Aquaponics/aquaponics-project/src/apply_learning_packet.py) | Uses `aquaponics-knowledge/06_evidence_maps/simulation_validation_map.json` | Change to `data/knowledge/evidence_maps/simulation_validation_map.json` |
| [src/extract_claims.py](C:/Users/ajith/Documents/Aquaponics/aquaponics-project/src/extract_claims.py) | Writes to `aquaponics-knowledge/07_agent_outputs/extraction_runs` | Change to `data/logs/extraction_runs/` |
| [src/merge_facts.py](C:/Users/ajith/Documents/Aquaponics/aquaponics-project/src/merge_facts.py) | Reads review runs and atomic facts from `aquaponics-knowledge` | Change to `data/logs/review_runs/` and `data/knowledge/atomic_facts/` |
| [src/promote_provisionals.py](C:/Users/ajith/Documents/Aquaponics/aquaponics-project/src/promote_provisionals.py) | Uses atomic facts and evidence maps under `aquaponics-knowledge` | Change to `data/knowledge/atomic_facts/` and `data/knowledge/evidence_maps/` |
| [src/report_promotion_candidates.py](C:/Users/ajith/Documents/Aquaponics/aquaponics-project/src/report_promotion_candidates.py) | Uses atomic facts and writes promotion report under `aquaponics-knowledge` | Change to `data/knowledge/atomic_facts/` and `data/knowledge/evidence_maps/` |
| [src/review_claims.py](C:/Users/ajith/Documents/Aquaponics/aquaponics-project/src/review_claims.py) | Uses extraction and review runs under `aquaponics-knowledge` | Change to `data/logs/extraction_runs/` and `data/logs/review_runs/` |
| [src/export_obsidian_vault.py](C:/Users/ajith/Documents/Aquaponics/aquaponics-project/src/export_obsidian_vault.py) | Looks for atomic facts in both `aquaponics-knowledge` and `data/simulation` | Change to one canonical source: `data/knowledge/atomic_facts/` |

### Direct references to `data/report_digests`, `data/update_logs`, and similar

| Script | Current Use | Required Change |
|---|---|---|
| [src/export_obsidian_vault.py](C:/Users/ajith/Documents/Aquaponics/aquaponics-project/src/export_obsidian_vault.py) | Mentions `data/report_digests/*.json` and `data/update_logs/*.json` | Update to `data/knowledge/report_digests/*.json` and `data/logs/update_logs/*.json` |
| [src/promote_candidate_default.py](C:/Users/ajith/Documents/Aquaponics/aquaponics-project/src/promote_candidate_default.py) | Reads latest reports from `data/update_logs` | Change to `data/logs/update_logs` |
| [src/run_research_to_tuning_cycle.py](C:/Users/ajith/Documents/Aquaponics/aquaponics-project/src/run_research_to_tuning_cycle.py) | Uses `data/update_logs` | Change to `data/logs/update_logs` |
| [src/compare_lettuce_vs_basil.py](C:/Users/ajith/Documents/Aquaponics/aquaponics-project/src/compare_lettuce_vs_basil.py) | Writes reports to `data/update_logs` | Change to `data/logs/update_logs` |
| [src/build_tuning_packet_from_intervention_digest.py](C:/Users/ajith/Documents/Aquaponics/aquaponics-project/src/build_tuning_packet_from_intervention_digest.py) | Likely depends on current digest path | Change to `data/knowledge/report_digests` |
| [src/build_learning_packet_from_simulation.py](C:/Users/ajith/Documents/Aquaponics/aquaponics-project/src/build_learning_packet_from_simulation.py) | Uses learning packet paths | Change to `data/knowledge/learning_packets` |
| [src/build_update_packet_from_report.py](C:/Users/ajith/Documents/Aquaponics/aquaponics-project/src/build_update_packet_from_report.py) | Uses update packet/report paths | Change to `data/knowledge/update_packets` and `data/knowledge/report_digests` |
| [src/apply_update_packet.py](C:/Users/ajith/Documents/Aquaponics/aquaponics-project/src/apply_update_packet.py) | Uses update packet paths | Change to `data/knowledge/update_packets` |

### Lower-risk references

| Area | Recommendation |
|---|---|
| `data/simulation/` | Leave unchanged in first migration to avoid breaking simulation scripts. |
| `knowledge-vault/` | No change needed. |
| `configs/`, `schemas/`, `src/` | No directory move in this migration. |

## Recommended Migration Order

1. Create new canonical directories:
   - `data/sources/`
   - `data/knowledge/`
   - `data/logs/`
   - `archive/`

2. Move knowledge assets first:
   - `aquaponics-knowledge/00_meta` -> `data/knowledge/meta`
   - `aquaponics-knowledge/02_ontology` -> `data/knowledge/ontology`
   - `aquaponics-knowledge/03_atomic_facts` -> `data/knowledge/atomic_facts`
   - `aquaponics-knowledge/04_process_models` -> `data/knowledge/process_models`
   - `aquaponics-knowledge/05_parameter_library` -> `data/knowledge/parameter_library`
   - `aquaponics-knowledge/06_evidence_maps` -> `data/knowledge/evidence_maps`
   - `aquaponics-knowledge/08_validation` -> `data/knowledge/validation`

3. Move source materials:
   - `data/input` -> `data/sources/input`
   - `data/run_configs` -> `data/sources/run_configs`
   - `data/research_reports` -> `data/sources/research_reports`

4. Move logs:
   - `aquaponics-knowledge/07_agent_outputs/extraction_runs` -> `data/logs/extraction_runs`
   - `aquaponics-knowledge/07_agent_outputs/review_runs` -> `data/logs/review_runs`
   - `data/update_logs` -> `data/logs/update_logs`

5. Move knowledge packet folders:
   - `data/report_digests` -> `data/knowledge/report_digests`
   - `data/learning_packets` -> `data/knowledge/learning_packets`
   - `data/model_tickets` -> `data/knowledge/model_tickets`
   - `data/tuning_packets` -> `data/knowledge/tuning_packets`
   - `data/update_packets` -> `data/knowledge/update_packets`

6. Move `data/simulation_observations` -> `data/simulation/observations`

7. Deduplicate:
   - compare `data/output/*.json` with `aquaponics-knowledge/07_agent_outputs/extraction_runs/*.json`
   - compare any `data/simulation/atomic_facts_*.json` with atomic facts moved under `data/knowledge/atomic_facts/`

8. Archive:
   - `aquaponics-knowledge/99_scratch`
   - superseded backups
   - duplicate extraction outputs
   - stale generated scenario snapshots once retention policy is approved

## Items To Leave Alone In First Migration

These should not move during the first cut because they are either already canonical or tightly coupled to current runtime behavior:

- `data/simulation/`
- `knowledge-vault/`
- `src/`
- `configs/`
- `schemas/`
- `.env`
- `.gitignore`

## Open Questions Before Execution

1. Should `data/simulation/day_logs/` stay under simulation or move under `data/logs/simulation/` in a second phase?
2. Should `data/simulation/species_evidence/` remain simulation-adjacent or eventually merge into `data/knowledge/evidence_maps/species/`?
3. Should `data/simulation/parameter_library.json` become generated from `data/knowledge/parameter_library/`?
4. Is `data/output/` intended as a working directory, a log directory, or a second extraction output store?
5. Are generated scenario snapshots under `data/simulation/scenarios/*_day_*.json` meant to remain active artifacts or become archival outputs?

## Recommended First Execution Scope

If this plan is executed, the safest first PR is:

- create `data/sources/`, `data/knowledge/`, `data/logs/`, `archive/`
- move only:
  - `aquaponics-knowledge/00_meta`
  - `aquaponics-knowledge/02_ontology`
  - `aquaponics-knowledge/03_atomic_facts`
  - `aquaponics-knowledge/04_process_models`
  - `aquaponics-knowledge/05_parameter_library`
  - `aquaponics-knowledge/06_evidence_maps`
  - `aquaponics-knowledge/08_validation`
  - `aquaponics-knowledge/07_agent_outputs/extraction_runs`
  - `aquaponics-knowledge/07_agent_outputs/review_runs`
  - `data/report_digests`
  - `data/learning_packets`
  - `data/model_tickets`
  - `data/tuning_packets`
  - `data/update_packets`
  - `data/update_logs`
- update only the scripts listed in the Script Update Impact section
- leave all simulation paths unchanged
- defer `data/output/` dedupe and archival cleanup to a second PR
