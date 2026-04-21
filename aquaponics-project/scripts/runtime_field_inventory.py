#!/usr/bin/env python3
"""Read-only inventory helper for runtime-facing simulation outputs.

This helper scans runtime-facing derived outputs under ``data/simulation`` and
reports file-family counts plus observed nested field paths. It ignores backup
copies and reference/config files by default so the inventory stays focused on
scenario snapshots, day logs, and result rollups that matter for adapter prep.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


DEFAULT_ROOT = Path("data/simulation")


@dataclass
class FamilySummary:
    name: str
    count: int
    examples: list[str]
    top_level_keys: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inventory runtime-facing field paths under data/simulation."
    )
    parser.add_argument(
        "--root",
        default=str(DEFAULT_ROOT),
        help="Root folder to scan. Defaults to data/simulation.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of the default terminal report.",
    )
    parser.add_argument(
        "--include-support-files",
        action="store_true",
        help="Include support/config files instead of only runtime-facing outputs.",
    )
    parser.add_argument(
        "--limit-paths",
        type=int,
        default=50,
        help="Maximum paths per family to print in terminal mode.",
    )
    return parser.parse_args()


def classify_file(path: Path) -> str:
    """Classify a simulation JSON file into a stable family."""

    parts = tuple(part.casefold() for part in path.parts)
    name = path.name.casefold()
    if "_sync_backups" in parts:
        return "backup"
    if "day_logs" in parts:
        return "day_log"
    if "scenarios" in parts:
        return "scenario_snapshot"
    if name == "multi_day_summary.json":
        return "multi_day_summary"
    if name == "tradeoff_matrix_results.json":
        return "tradeoff_results"
    if "components" in parts:
        return "support_components"
    if "models" in parts:
        return "support_models"
    if "parameters" in parts:
        return "support_parameters"
    if "species_evidence" in parts:
        return "support_species_evidence"
    if "species" in parts:
        return "support_species"
    return "support_misc"


def is_runtime_family(family: str) -> bool:
    return family in {
        "scenario_snapshot",
        "day_log",
        "multi_day_summary",
        "tradeoff_results",
    }


def walk_paths(value: Any, prefix: str = "") -> set[str]:
    """Collect nested object and leaf paths from JSON data."""

    paths: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            child_prefix = f"{prefix}.{key}" if prefix else key
            paths.add(child_prefix)
            paths.update(walk_paths(child, child_prefix))
    elif isinstance(value, list):
        list_prefix = f"{prefix}[]" if prefix else "[]"
        paths.add(list_prefix)
        for item in value:
            if isinstance(item, dict):
                for key, child in item.items():
                    child_prefix = f"{list_prefix}.{key}"
                    paths.add(child_prefix)
                    paths.update(walk_paths(child, child_prefix))
            elif isinstance(item, list):
                paths.update(walk_paths(item, list_prefix))
    return paths


def top_level_keys(data: Any) -> list[str]:
    if isinstance(data, dict):
        return sorted(data.keys())
    if isinstance(data, list) and data and isinstance(data[0], dict):
        return sorted(data[0].keys())
    return []


def load_inventory(root: Path, include_support_files: bool) -> dict[str, Any]:
    file_counts: Counter[str] = Counter()
    family_examples: dict[str, list[str]] = defaultdict(list)
    family_top_keys: dict[str, Counter[str]] = defaultdict(Counter)
    family_path_counts: dict[str, Counter[str]] = defaultdict(Counter)
    family_record_counts: Counter[str] = Counter()
    skipped_non_json = 0
    parse_errors: list[dict[str, str]] = []

    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() != ".json":
            skipped_non_json += 1
            continue
        family = classify_file(path.relative_to(root))
        if not include_support_files and not is_runtime_family(family):
            continue

        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            parse_errors.append({"file": path.as_posix(), "error": str(exc)})
            continue

        rel_path = path.relative_to(root).as_posix()
        file_counts[family] += 1
        family_examples[family].append(rel_path)

        if isinstance(data, list) and family in {"multi_day_summary", "tradeoff_results"}:
            items = [item for item in data if isinstance(item, dict)]
            family_record_counts[family] += len(items)
            for item in items:
                for key in top_level_keys(item):
                    family_top_keys[family][key] += 1
                for field_path in walk_paths(item):
                    family_path_counts[family][field_path] += 1
        else:
            family_record_counts[family] += 1
            for key in top_level_keys(data):
                family_top_keys[family][key] += 1
            for field_path in walk_paths(data):
                family_path_counts[family][field_path] += 1

    family_summaries: list[FamilySummary] = []
    for family in sorted(file_counts):
        top_keys = sorted(
            key
            for key, count in family_top_keys[family].items()
            if count == max(1, family_record_counts[family])
        )
        family_summaries.append(
            FamilySummary(
                name=family,
                count=file_counts[family],
                examples=family_examples[family][:5],
                top_level_keys=top_keys,
            )
        )

    return {
        "root": root.as_posix(),
        "include_support_files": include_support_files,
        "family_summaries": [asdict(item) for item in family_summaries],
        "family_record_counts": dict(sorted(family_record_counts.items())),
        "family_path_counts": {
            family: dict(sorted(counter.items()))
            for family, counter in sorted(family_path_counts.items())
        },
        "parse_errors": parse_errors,
        "skipped_non_json": skipped_non_json,
    }


def print_terminal_report(inventory: dict[str, Any], limit_paths: int) -> None:
    print(f"Root: {inventory['root']}")
    print(f"Include support files: {inventory['include_support_files']}")
    print()
    print("Families")
    for summary in inventory["family_summaries"]:
        print(f"  - {summary['name']}: {summary['count']} file(s)")
        if summary["examples"]:
            print(f"    examples: {', '.join(summary['examples'])}")
        if summary["top_level_keys"]:
            print(f"    stable top-level keys: {', '.join(summary['top_level_keys'])}")
    print()
    print("Observed paths")
    for family, paths in inventory["family_path_counts"].items():
        print(f"  {family}:")
        items = list(paths.items())[:limit_paths]
        for field_path, count in items:
            print(f"    - {field_path} ({count})")
        if len(paths) > limit_paths:
            print(f"    ... {len(paths) - limit_paths} more path(s)")
    if inventory["parse_errors"]:
        print()
        print("Parse errors")
        for item in inventory["parse_errors"]:
            print(f"  - {item['file']}: {item['error']}")


def main() -> int:
    args = parse_args()
    root = Path(args.root)
    if not root.exists() or not root.is_dir():
        print(f"error: root does not exist or is not a directory: {root}", file=sys.stderr)
        return 2

    inventory = load_inventory(root, include_support_files=args.include_support_files)
    if args.json:
        json.dump(inventory, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        print_terminal_report(inventory, limit_paths=args.limit_paths)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
