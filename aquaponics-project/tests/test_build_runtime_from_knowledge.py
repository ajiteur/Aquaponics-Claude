import json
import unittest
from pathlib import Path

from src import build_runtime_from_knowledge as sync


PROJECT_ROOT = Path(__file__).resolve().parent.parent
FIXTURE_ROOT = PROJECT_ROOT / "tests" / "fixtures" / "knowledge_runtime_snapshots"


def normalized_payload(change: sync.PlannedChange) -> dict:
    payload = json.loads(change.after_text)
    payload["runtime_sync"]["generated_at_utc"] = "__TIMESTAMP__"
    return payload


def normalized_runtime_payload(payload: dict) -> dict:
    cloned = json.loads(json.dumps(payload))
    cloned["runtime_sync"]["generated_at_utc"] = "__TIMESTAMP__"
    return cloned


def load_fixture(name: str) -> dict:
    with open(FIXTURE_ROOT / name, "r", encoding="utf-8") as handle:
        return json.load(handle)


class BuildRuntimeFromKnowledgeTests(unittest.TestCase):
    def test_dry_run_summary_has_scope_counts(self) -> None:
        changes = []
        scope_summaries = []
        for scope in sync.SCOPES:
            scoped_changes, scoped_summary = sync.plan_scope_with_summary(scope, "2026-04-14T00:00:00Z")
            changes.extend(scoped_changes)
            scope_summaries.append(scoped_summary)

        summary = sync.build_summary(changes, mode="dry-run", scope_summaries=scope_summaries)

        self.assertEqual(summary["mode"], "dry-run")
        self.assertEqual(summary["files_with_proposed_changes"], len(changes))
        self.assertIn("parameters", summary["scopes"])
        self.assertIn("species", summary["scopes"])
        self.assertIn("species_evidence", summary["scopes"])
        self.assertGreater(summary["files_scanned"], 0)
        self.assertEqual(summary["validation_failed_count"], 0)
        self.assertIn("parameters", summary["scopes_processed"])

    def test_parameters_snapshot_waterchemistry(self) -> None:
        payload = self._build_runtime_payload(
            "parameters",
            "data/knowledge/parameters/waterchemistry.json",
        )
        self.assertEqual(normalized_runtime_payload(payload), load_fixture("parameters_waterchemistry.json"))

    def test_species_snapshot_tilapia(self) -> None:
        payload = self._build_runtime_payload(
            "species",
            "data/knowledge/species/fish/tilapia.json",
        )
        self.assertEqual(normalized_runtime_payload(payload), load_fixture("species_tilapia.json"))

    def test_species_evidence_snapshot_tilapia(self) -> None:
        payload = self._build_runtime_payload(
            "species_evidence",
            "data/knowledge/species_evidence/fish/tilapia.evidence.json",
        )
        self.assertEqual(normalized_runtime_payload(payload), load_fixture("species_evidence_tilapia.json"))

    def test_target_path_resolution_prefers_derived_path(self) -> None:
        source_path = PROJECT_ROOT / "data" / "knowledge" / "species_evidence" / "fish" / "tilapia.evidence.json"
        payload = sync.load_json(source_path)
        target_path = sync.resolve_target_path("species_evidence", source_path, payload)
        self.assertEqual(target_path, PROJECT_ROOT / "data" / "simulation" / "species_evidence" / "tilapia_evidence.json")

    def test_species_transform_adds_aliases_without_overwriting_canonical(self) -> None:
        payload = {
            "species_id": "plant_demo",
            "scientific_name": "Plantus demo",
            "common_name": "Demo plant",
            "category": "plant",
            "status": "draft",
            "environment": {
                "preferred_pH": {"min": 1, "max": 2},
                "preferred_temp_c": {"min": 3, "max": 4},
            },
            "nutrient_response": {
                "aquaponics_nitrateN_anchor_mg_L": 42.0,
                "pH_operating_aquaponics": {"min": 6.8, "max": 7.2},
            },
            "future_fields": {
                "disease_downy_mildew_triggers": {"leaf_wetness_hours_min": 4.0},
                "stress_multi_harvest_root_disease_and_deficiency": {"root_disease_risk": "elevated"},
            },
        }
        transformed = sync.transform_species(payload)
        self.assertEqual(transformed["nutrient_response"]["aquaponics_nitrateN_anchor_mg_L"], 42.0)
        self.assertEqual(transformed["nutrient_response"]["aquaponics_nitrate_n_anchor_mg_L"], 42.0)
        self.assertEqual(
            transformed["future_fields"]["disease_downy_mildew_triggers"],
            transformed["future_fields"]["downy_mildew_triggers"],
        )

    def test_preserve_runtime_only_fields_keeps_existing_runtime_helpers(self) -> None:
        existing_payload = {
            "species_id": "fish_tilapia",
            "generated_at_utc": "old-generated",
            "legacy_runtime_helper": {"mode": "legacy"},
            "environment": {"preferred_pH": {"min": 6.0, "max": 8.0}},
        }
        generated_payload = {
            "species_id": "fish_tilapia",
            "environment": {"preferred_pH": {"min": 6.5, "max": 8.5}},
        }
        merged = sync.preserve_runtime_only_fields("species", existing_payload, generated_payload)
        self.assertEqual(merged["environment"]["preferred_pH"]["min"], 6.5)
        self.assertEqual(merged["generated_at_utc"], "old-generated")
        self.assertEqual(merged["legacy_runtime_helper"], {"mode": "legacy"})

    def test_stabilize_runtime_sync_timestamp_avoids_timestamp_only_diffs(self) -> None:
        existing_payload = {
            "species_id": "fish_tilapia",
            "runtime_sync": {
                "scope": "species",
                "generated_at_utc": "2026-04-14T00:00:00Z",
                "canonical_source": "data/knowledge/species/fish/tilapia.json",
                "runtime_target": "data/simulation/species/fish/tilapia.json",
                "ownership": sync.OWNERSHIP_NOTE,
            },
        }
        generated_payload = {
            "species_id": "fish_tilapia",
            "runtime_sync": {
                "scope": "species",
                "generated_at_utc": "2026-04-15T00:00:00Z",
                "canonical_source": "data/knowledge/species/fish/tilapia.json",
                "runtime_target": "data/simulation/species/fish/tilapia.json",
                "ownership": sync.OWNERSHIP_NOTE,
            },
        }

        stabilized = sync.stabilize_runtime_sync_timestamp(existing_payload, generated_payload)

        self.assertEqual(stabilized["runtime_sync"]["generated_at_utc"], "2026-04-14T00:00:00Z")

    def test_validation_failure_on_malformed_canonical_input(self) -> None:
        source_path = PROJECT_ROOT / "tests" / "fixtures" / "knowledge_runtime_snapshots" / "bad_species.json"
        with self.assertRaises(sync.ValidationError) as ctx:
            sync.validate_generated_payload(
                "species",
                {"category": "plant", "status": "draft", "runtime_sync": {"scope": "species"}},
                source_path,
                PROJECT_ROOT / "tmp" / "target.json",
            )
        self.assertIn("scope=species", str(ctx.exception))
        self.assertIn("path=species.species_id", str(ctx.exception))

    def test_validation_rejects_alias_conflict(self) -> None:
        payload = {
            "species_id": "plant_demo",
            "scientific_name": "Plantus demo",
            "common_name": "Demo plant",
            "category": "plant",
            "status": "draft",
            "environment": {
                "preferred_pH": {"min": 1, "max": 2},
                "preferred_temp_c": {"min": 3, "max": 4},
            },
            "nutrient_response": {
                "aquaponics_nitrateN_anchor_mg_L": 42.0,
                "aquaponics_nitrate_n_anchor_mg_L": 99.0,
            },
            "runtime_sync": {
                "scope": "species",
                "generated_at_utc": "2026-04-14T00:00:00Z",
                "canonical_source": "tmp/source.json",
                "runtime_target": "tmp/target.json",
                "ownership": sync.OWNERSHIP_NOTE,
            },
        }
        source_path = PROJECT_ROOT / "tests" / "fixtures" / "knowledge_runtime_snapshots" / "alias_conflict_species.json"
        with self.assertRaises(sync.ValidationError) as ctx:
            sync.validate_alias_consistency("species", payload, source_path)
        self.assertIn("aquaponics_nitrate_n_anchor_mg_L", str(ctx.exception))

    def _build_runtime_payload(self, scope: str, relative_source: str) -> dict:
        source_path = PROJECT_ROOT / Path(relative_source)
        canonical_payload = sync.load_json(source_path)
        target_path = sync.resolve_target_path(scope, source_path, canonical_payload)
        existing_payload = sync.load_json(target_path) if target_path.exists() else None
        runtime_payload = sync.transform_payload(scope, canonical_payload)
        runtime_payload = sync.preserve_runtime_only_fields(scope, existing_payload, runtime_payload)
        runtime_payload = sync.add_runtime_metadata(
            scope,
            source_path,
            target_path,
            runtime_payload,
            "2026-04-14T00:00:00Z",
        )
        runtime_payload = sync.stabilize_runtime_sync_timestamp(existing_payload, runtime_payload)
        sync.validate_generated_payload(scope, runtime_payload, source_path, target_path)
        sync.validate_alias_consistency(scope, runtime_payload, source_path)
        return runtime_payload


if __name__ == "__main__":
    unittest.main()
