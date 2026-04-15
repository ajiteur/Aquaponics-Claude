# Knowledge-to-Runtime Sync Plan

## Goal

Establish the first explicit sync flow from curated knowledge files into simulation-facing runtime files for:

- `data/knowledge/parameters` -> `data/simulation/parameters`
- `data/knowledge/species` -> `data/simulation/species`
- `data/knowledge/species_evidence` -> `data/simulation/species_evidence`

This flow makes ownership and mutation rules explicit:

- `data/knowledge/*` is canonical.
- `data/simulation/*` is derived runtime state.
- Runtime files must be regenerated from knowledge, not hand-edited as a source of truth.

## Ownership Rules

### Canonical

- `data/knowledge/parameters/*.json`
- `data/knowledge/species/**/*.json`
- `data/knowledge/species_evidence/**/*.json`

These files are the human-reviewed Layer 1 knowledge source.

### Derived

- `data/simulation/parameters/*.json`
- `data/simulation/species/**/*.json`
- `data/simulation/species_evidence/**/*.json`

These files exist to support current simulation scripts and legacy runtime readers.

### Allowed Direction

- Knowledge -> Simulation: allowed through the sync script.
- Simulation -> Knowledge: not allowed automatically.
- Manual edits in `data/simulation/*`: tolerated only as temporary runtime edits and should be treated as drift until either discarded or re-expressed in `data/knowledge/*`.

## First Sync Scope

### Parameters

- Copy every JSON file under `data/knowledge/parameters/` into `data/simulation/parameters/`.
- Preserve canonical records.
- Add lightweight runtime compatibility fields so existing simulation-side JSON stays usable while the repo migrates.

### Species

- Copy every JSON file under `data/knowledge/species/` into the matching simulation path.
- Preserve canonical content.
- Add runtime metadata that records the canonical owner and sync timestamp.
- Add a few compatibility aliases where the knowledge schema renamed basil runtime fields.

### Species Evidence

- Copy every JSON file under `data/knowledge/species_evidence/` into the derived simulation path.
- Prefer `source_basis.derived_from_simulation_path` when present because current runtime evidence files use mixed path conventions.
- Preserve canonical evidence records.
- Add runtime metadata and selected compatibility aliases for legacy field names.

## Path Resolution

The sync builder resolves each target path in this order:

1. `source_basis.derived_from_simulation_path` from the knowledge file, if present.
2. Otherwise, the same relative path beneath the matching `data/simulation/<scope>/` directory.

This preserves existing special cases such as:

- `data/knowledge/species_evidence/fish/tilapia.evidence.json`
- `data/simulation/species_evidence/tilapia_evidence.json`

## Safety Rules

### Dry Run

The default operating mode is dry run.

Dry run must:

- read knowledge files
- build derived runtime payloads
- validate generated payload shape before diffing
- compare them with existing simulation files
- print a compact summary report
- print unified diffs
- print the files that would be created or updated
- avoid writing any runtime files

### Apply

Apply mode must:

- show the proposed diff before writing
- fail before writing if validation fails
- create a timestamped backup of every existing file that will change
- only then write the derived runtime file

### Backup Location

Backups are written to:

- `data/simulation/_sync_backups/<timestamp>/...`

The backup tree mirrors the original runtime relative path so restoration is straightforward.

### Non-Destructive Behavior

- No write occurs in dry-run mode.
- No existing runtime file is overwritten in apply mode without a backup.
- Files with no content change are skipped.

## Transform Rules

### Shared Runtime Metadata

Every derived runtime file gets a `runtime_sync` block containing:

- source scope
- canonical source path
- runtime target path
- ownership statement
- generated timestamp

This makes the data provenance explicit inside the derived artifact.

### Validation

The sync builder validates generated runtime payloads for each scope before emitting diffs or writing files:

- `parameters`: validates `version`, `status`, `records`, per-record identifiers, and runtime metadata
- `species`: validates `species_id`, `category`, `status`, `environment`, key lists, and runtime metadata
- `species_evidence`: validates `species_id`, `status`, `target_fields`, `evidence_records`, and runtime metadata

Validation errors must fail fast and include:

- scope
- source file
- failing field path
- reason

The builder also validates:

- `runtime_sync` path consistency
- `source_basis` shape when canonical input provides it
- compatibility alias consistency so aliases never contradict canonical values

### Parameter Compatibility

For parameter records, the builder keeps the canonical structure and adds compatibility helpers:

- `range` -> add `values.min`, `values.max`, `values.unit`
- `scalar` -> add `values.value`, `values.unit`
- `threshold` -> add flattened `operator`, `value`
- threshold-like records keep canonical fields and gain flattened runtime fields where possible

This keeps the knowledge representation intact while making the runtime file easier to consume from older scripts.

### Species Compatibility

Most species files can be copied directly. The first flow adds targeted aliases where the newer knowledge schema renamed basil runtime keys, such as:

- `aquaponics_nitrateN_anchor_mg_L` -> `aquaponics_nitrate_n_anchor_mg_L`
- `pH_operating_aquaponics` -> `aquaponics_operating_pH`
- `disease_downy_mildew_triggers` -> `downy_mildew_triggers`
- `stress_multi_harvest_root_disease_and_deficiency` -> `multi_harvest_stress`

The canonical knowledge names stay present; aliases exist only to reduce runtime breakage during migration.

### Species Evidence Compatibility

The sync builder preserves evidence records but also duplicates selected field names in legacy form where knowledge files renamed them. This is limited to known current drift and should shrink over time as runtime readers move to canonical names.

## Operational Workflow

### Preview

```powershell
python src/build_runtime_from_knowledge.py --dry-run
```

Dry-run output includes a compact summary with:

- files scanned
- files with proposed changes
- files unchanged
- scopes processed
- validation passed count
- validation failed count

### Apply

```powershell
python src/build_runtime_from_knowledge.py --apply
```

### Narrow Scope

```powershell
python src/build_runtime_from_knowledge.py --dry-run --scope species
python src/build_runtime_from_knowledge.py --apply --scope parameters --scope species_evidence
```

## Expected Outcomes

- Clear canonical ownership in `data/knowledge`.
- Explicit derived ownership in `data/simulation`.
- Repeatable regeneration of runtime files.
- Safe preview-first workflow with backups.
- A base layer for later migration of simulation readers to canonical schemas.

## Follow-On Work

- Update runtime readers to prefer canonical knowledge schemas directly where feasible.
- Remove temporary compatibility aliases once consumers are migrated.
- Extend validation toward formal schemas for both canonical and derived payloads.
- Add more snapshot fixtures as additional knowledge domains are synced.

## Test Coverage

The sync flow has fixture-based and isolated unit-test coverage under `tests/` for representative files from each scope.

Current tests cover:

- target path resolution
- representative snapshot outputs for parameters, species, and species evidence
- runtime metadata injection
- compatibility alias generation
- preservation of runtime-only fields
- validation failure on malformed generated payloads
