#!/usr/bin/env python3
"""Read-only helper to report likely glossary or explainer link candidates.

This script scans markdown notes under the vault, skips the glossary and
explainer source notes themselves, and reports likely first-meaningful-mention
link opportunities for manual review. It does not edit files.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence


DEFAULT_ROOT = Path("knowledge-vault")
GLOSSARY_PATH = Path("knowledge-vault/Reference/Glossary and Naming Conventions.md")
EXPLAINER_PATHS = {
    Path("knowledge-vault/Reference/Explainers/TAN.md"),
    Path("knowledge-vault/Reference/Explainers/Unionized Ammonia NH3.md"),
    Path("knowledge-vault/Reference/Explainers/Nitrification.md"),
    Path("knowledge-vault/Reference/Explainers/pH.md"),
}

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
NORMALIZE_TEXT_RE = re.compile(r"[^A-Za-z0-9+]+")
LIBRARY_NOTE_KEYWORDS = ("library", "index", "hub")


@dataclass(frozen=True)
class TermSpec:
    """One reportable concept plus its candidate link target."""

    name: str
    aliases: tuple[str, ...]
    suggestion: str
    target: str
    case_sensitive: bool = False

    def regexes(self) -> tuple[re.Pattern[str], ...]:
        flags = 0 if self.case_sensitive else re.IGNORECASE
        compiled: list[re.Pattern[str]] = []
        for alias in self.aliases:
            escaped = re.escape(alias)
            compiled.append(re.compile(rf"(?<!\w){escaped}(?!\w)", flags))
        return tuple(compiled)


@dataclass(frozen=True)
class Candidate:
    """One suggested review-only link opportunity."""

    file: str
    term: str
    line: int
    excerpt: str
    suggestion: str


@dataclass
class ScanSummary:
    """Terminal- and JSON-friendly summary details."""

    files_scanned: int = 0
    files_skipped: int = 0
    candidates_found: int = 0
    notes_with_no_change_needed: int = 0


def build_default_terms() -> list[TermSpec]:
    """Seed the initial link targets for glossary and explainer scans."""

    return [
        TermSpec(
            name="TAN",
            aliases=("TAN",),
            suggestion="[[Reference/Explainers/TAN|TAN]]",
            target="Reference/Explainers/TAN",
            case_sensitive=True,
        ),
        TermSpec(
            name="NH3",
            aliases=("NH3", "Unionized Ammonia / NH3"),
            suggestion="[[Reference/Explainers/Unionized Ammonia NH3|NH3]]",
            target="Reference/Explainers/Unionized Ammonia NH3",
            case_sensitive=True,
        ),
        TermSpec(
            name="pH",
            aliases=("pH",),
            suggestion="[[Reference/Explainers/pH|pH]]",
            target="Reference/Explainers/pH",
            case_sensitive=True,
        ),
        TermSpec(
            name="Nitrification",
            aliases=("Nitrification", "nitrification"),
            suggestion="[[Reference/Explainers/Nitrification|Nitrification]]",
            target="Reference/Explainers/Nitrification",
        ),
        TermSpec(
            name="Lettuce",
            aliases=("Lettuce", "lettuce"),
            suggestion="[[Reference/Glossary and Naming Conventions#Lettuce|Lettuce]]",
            target="Reference/Glossary and Naming Conventions#Lettuce",
        ),
        TermSpec(
            name="Basil",
            aliases=("Basil", "basil"),
            suggestion="[[Reference/Glossary and Naming Conventions#Basil|Basil]]",
            target="Reference/Glossary and Naming Conventions#Basil",
        ),
        TermSpec(
            name="Tilapia",
            aliases=("Tilapia", "tilapia"),
            suggestion="[[Reference/Glossary and Naming Conventions#Tilapia|Tilapia]]",
            target="Reference/Glossary and Naming Conventions#Tilapia",
        ),
        TermSpec(
            name="Media Bed",
            aliases=("Media Bed", "media bed"),
            suggestion="[[Reference/Glossary and Naming Conventions#Media Bed|Media Bed]]",
            target="Reference/Glossary and Naming Conventions#Media Bed",
        ),
        TermSpec(
            name="DWC / Raft",
            aliases=("DWC / Raft", "DWC / raft", "DWC"),
            suggestion="[[Reference/Glossary and Naming Conventions#DWC / Raft|DWC / Raft]]",
            target="Reference/Glossary and Naming Conventions#DWC / Raft",
            case_sensitive=False,
        ),
        TermSpec(
            name="NFT",
            aliases=("NFT",),
            suggestion="[[Reference/Glossary and Naming Conventions#NFT|NFT]]",
            target="Reference/Glossary and Naming Conventions#NFT",
            case_sensitive=True,
        ),
        TermSpec(
            name="canonical",
            aliases=("canonical",),
            suggestion="[[Reference/Glossary and Naming Conventions#Canonical|canonical]]",
            target="Reference/Glossary and Naming Conventions#Canonical",
        ),
        TermSpec(
            name="derived",
            aliases=("derived",),
            suggestion="[[Reference/Glossary and Naming Conventions#Derived|derived]]",
            target="Reference/Glossary and Naming Conventions#Derived",
        ),
        TermSpec(
            name="deferred",
            aliases=("deferred",),
            suggestion="[[Reference/Glossary and Naming Conventions#Deferred|deferred]]",
            target="Reference/Glossary and Naming Conventions#Deferred",
        ),
    ]


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Report likely glossary or explainer link candidates in vault notes."
    )
    parser.add_argument(
        "--root",
        default=str(DEFAULT_ROOT),
        help="Root folder to scan. Defaults to knowledge-vault.",
    )
    parser.add_argument(
        "--include-term",
        action="append",
        default=[],
        help="Limit scanning to one or more configured term names or aliases.",
    )
    parser.add_argument(
        "--exclude-term",
        action="append",
        default=[],
        help="Exclude one or more configured term names or aliases.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of the default terminal report.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Limit the number of reported candidates. Summary still reflects the full scan.",
    )
    return parser.parse_args(argv)


def normalize_filter_name(value: str) -> str:
    return value.strip().casefold()


def filter_terms(
    terms: Iterable[TermSpec], include_terms: Sequence[str], exclude_terms: Sequence[str]
) -> list[TermSpec]:
    """Filter configured terms by name or alias."""

    include_set = {normalize_filter_name(item) for item in include_terms if item.strip()}
    exclude_set = {normalize_filter_name(item) for item in exclude_terms if item.strip()}

    filtered: list[TermSpec] = []
    for term in terms:
        names = {normalize_filter_name(term.name), *(normalize_filter_name(alias) for alias in term.aliases)}
        if include_set and include_set.isdisjoint(names):
            continue
        if exclude_set and not exclude_set.isdisjoint(names):
            continue
        filtered.append(term)
    return filtered


def should_skip_file(path: Path, root: Path) -> bool:
    """Skip glossary and explainer source notes and anything under .obsidian."""

    parts = {part.casefold() for part in path.parts}
    if ".obsidian" in parts:
        return True
    rel = path
    if path.is_absolute():
        try:
            rel = path.resolve().relative_to(Path.cwd().resolve())
        except ValueError:
            rel = path.resolve()
    return rel == GLOSSARY_PATH or rel in EXPLAINER_PATHS


def mask_non_candidate_regions(text: str) -> str:
    """Hide existing wikilinks and inline code before term matching."""

    masked = INLINE_CODE_RE.sub(lambda match: " " * len(match.group(0)), text)
    return WIKILINK_RE.sub(lambda match: " " * len(match.group(0)), masked)


def collect_note_lines(text: str) -> list[tuple[int, str, str, bool]]:
    """Return line metadata outside fenced code blocks."""

    records: list[tuple[int, str, str, bool]] = []
    in_fence = False
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        stripped = raw_line.strip()
        if FENCE_RE.match(raw_line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        search_line = mask_non_candidate_regions(raw_line)
        is_heading = stripped.startswith("#")
        records.append((line_number, raw_line, search_line, is_heading))
    return records


def collect_existing_targets(lines: Iterable[tuple[int, str, str, bool]]) -> set[str]:
    """Collect wikilink targets already present in the note."""

    targets: set[str] = set()
    for _, raw_line, _, _ in lines:
        for match in WIKILINK_RE.finditer(raw_line):
            targets.add(match.group(1).strip())
    return targets


def shorten_excerpt(text: str, width: int = 120) -> str:
    cleaned = text.strip()
    if len(cleaned) <= width:
        return cleaned
    return cleaned[: width - 3].rstrip() + "..."


def normalize_compare_text(text: str) -> str:
    """Normalize headings, filenames, and aliases for lightweight subject checks."""

    normalized = re.sub(r"^#+\s*", "", text.strip())
    normalized = re.sub(r"\.md$", "", normalized, flags=re.IGNORECASE)
    normalized = normalized.replace("_", " ").replace("/", " ").replace("-", " ")
    normalized = NORMALIZE_TEXT_RE.sub(" ", normalized)
    return re.sub(r"\s+", " ", normalized).strip().casefold()


def collect_note_subjects(
    file_path: Path, lines: Sequence[tuple[int, str, str, bool]]
) -> tuple[str, ...]:
    """Collect the note's own title-like subjects for self-match suppression."""

    subjects = [normalize_compare_text(file_path.stem)]
    for line_number, raw_line, _, is_heading in lines:
        if line_number == 1 and is_heading:
            title = normalize_compare_text(raw_line)
            if title:
                subjects.append(title)
            break
    return tuple(subject for subject in subjects if subject)


def is_library_like_note(file_path: Path, note_subjects: Sequence[str]) -> bool:
    """Treat library, index, and hub notes as browse-oriented rather than explanatory."""

    candidates = [normalize_compare_text(file_path.stem), *note_subjects]
    for candidate in candidates:
        words = set(candidate.split())
        if words.intersection(LIBRARY_NOTE_KEYWORDS):
            return True
    return False


def is_component_note(file_path: Path) -> bool:
    """Treat notes under Components as subject pages for self-match suppression."""

    return any(part.casefold() == "components" for part in file_path.parts)


def heading_level(raw_line: str) -> int:
    """Return markdown heading depth or zero for non-headings."""

    match = re.match(r"^(#+)\s+", raw_line.strip())
    return len(match.group(1)) if match else 0


def collect_local_section_subjects(
    lines: Sequence[tuple[int, str, str, bool]]
) -> tuple[tuple[int, str], ...]:
    """Collect major local section headings for library-note subject checks."""

    subjects: list[tuple[int, str]] = []
    for line_number, raw_line, _, is_heading in lines:
        level = heading_level(raw_line)
        if not is_heading or level == 0 or level > 3:
            continue
        subject = normalize_compare_text(raw_line)
        if subject:
            subjects.append((line_number, subject))
    return tuple(subjects)


def find_local_section_subject(
    line_number: int, local_section_subjects: Sequence[tuple[int, str]]
) -> str | None:
    """Find the nearest enclosing major section heading for the current line."""

    subject: str | None = None
    for subject_line, subject_text in local_section_subjects:
        if subject_line >= line_number:
            break
        subject = subject_text
    return subject


def is_obvious_self_subject_match(term: TermSpec, note_subjects: Sequence[str]) -> bool:
    """Check whether the term is the direct subject of the current note."""

    alias_norms = {
        normalize_compare_text(term.name),
        *(normalize_compare_text(alias) for alias in term.aliases),
    }
    subject_tokens = [set(subject.split()) for subject in note_subjects]
    for alias_norm in alias_norms:
        if not alias_norm:
            continue
        alias_words = set(alias_norm.split())
        for subject_norm, subject_word_set in zip(note_subjects, subject_tokens):
            if alias_norm == subject_norm:
                return True
            if alias_words and alias_words.issubset(subject_word_set):
                return True
    return False


def is_short_local_label_line(raw_line: str, is_heading: bool) -> bool:
    """Treat short headings or label-like lines as weak candidates in library notes."""

    if is_heading:
        return True
    stripped = raw_line.strip()
    stripped = re.sub(r"^[-*+]\s*", "", stripped)
    stripped = re.sub(r"^[0-9]+\.\s*", "", stripped)
    if not stripped:
        return False
    if any(punct in stripped for punct in (".", ":", ";", "!", "?")):
        return False
    return 0 < len(normalize_compare_text(stripped).split()) <= 4


def is_low_signal_library_body_line(raw_line: str) -> bool:
    """Treat placeholder and short local role/description lines as weak library matches."""

    stripped = raw_line.strip()
    stripped = re.sub(r"^[-*+]\s*", "", stripped)
    if not stripped:
        return False
    lowered = stripped.casefold()
    if "placeholder" in lowered:
        return True
    if lowered.startswith("role:"):
        return True
    word_count = len(normalize_compare_text(stripped).split())
    if stripped.endswith(".") and word_count <= 9:
        return True
    return False


def find_candidate_for_term(
    term: TermSpec,
    file_path: Path,
    lines: Sequence[tuple[int, str, str, bool]],
    note_subjects: Sequence[str],
    library_like: bool,
    component_note: bool,
    local_section_subjects: Sequence[tuple[int, str]],
) -> Candidate | None:
    """Find the first body-text candidate, or fall back to a heading match."""

    body_candidate: Candidate | None = None
    heading_candidate: Candidate | None = None
    for regex in term.regexes():
        for line_number, raw_line, search_line, is_heading in lines:
            if not search_line.strip():
                continue
            match = regex.search(search_line)
            if not match:
                continue
            candidate = Candidate(
                file=file_path.as_posix(),
                term=term.name,
                line=line_number,
                excerpt=shorten_excerpt(raw_line),
                suggestion=term.suggestion,
            )
            if is_heading and line_number == 1:
                continue
            if component_note and is_obvious_self_subject_match(term, note_subjects):
                continue
            if library_like and is_short_local_label_line(raw_line, is_heading):
                continue
            if library_like and not is_heading:
                local_section_subject = find_local_section_subject(line_number, local_section_subjects)
                if local_section_subject and is_obvious_self_subject_match(term, (local_section_subject,)):
                    if is_low_signal_library_body_line(raw_line):
                        continue
            if is_heading and is_obvious_self_subject_match(term, note_subjects):
                continue
            if is_heading and heading_candidate is None:
                heading_candidate = candidate
            if not is_heading:
                if body_candidate is None or line_number < body_candidate.line:
                    body_candidate = candidate
            break
    return body_candidate or heading_candidate


def scan_files(root: Path, terms: Sequence[TermSpec], limit: int | None) -> tuple[list[Candidate], ScanSummary]:
    """Scan markdown notes under the vault root and report candidate links."""

    candidates: list[Candidate] = []
    summary = ScanSummary()

    markdown_files = sorted(path for path in root.rglob("*.md") if path.is_file())
    for path in markdown_files:
        if should_skip_file(path, root):
            summary.files_skipped += 1
            continue

        summary.files_scanned += 1
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"warning: failed to read {path}: {exc}", file=sys.stderr)
            continue

        lines = collect_note_lines(text)
        note_subjects = collect_note_subjects(path, lines)
        library_like = is_library_like_note(path, note_subjects)
        component_note = is_component_note(path)
        local_section_subjects = collect_local_section_subjects(lines)
        linked_targets = collect_existing_targets(lines)
        note_candidates: list[Candidate] = []

        for term in terms:
            if term.target in linked_targets:
                continue
            candidate = find_candidate_for_term(
                term,
                path,
                lines,
                note_subjects,
                library_like,
                component_note,
                local_section_subjects,
            )
            if candidate is not None:
                note_candidates.append(candidate)

        note_candidates.sort(key=lambda candidate: (candidate.line, candidate.term))
        if not note_candidates:
            summary.notes_with_no_change_needed += 1
            continue

        summary.candidates_found += len(note_candidates)
        for candidate in note_candidates:
            if limit is None or len(candidates) < limit:
                candidates.append(candidate)

    return candidates, summary


def print_terminal_report(candidates: Sequence[Candidate], summary: ScanSummary, limit: int | None) -> None:
    """Render a readable grouped report."""

    grouped: dict[str, list[Candidate]] = {}
    for candidate in candidates:
        grouped.setdefault(candidate.file, []).append(candidate)

    if not grouped:
        print("No candidate glossary or explainer links found.")
    else:
        for file_path in sorted(grouped):
            print(file_path)
            for candidate in grouped[file_path]:
                print(f"  - term: {candidate.term}")
                print(f"    line: {candidate.line}")
                print(f"    excerpt: {candidate.excerpt}")
                print(f"    suggest: {candidate.suggestion}")

    print()
    print("Summary")
    print(f"  files scanned: {summary.files_scanned}")
    print(f"  files skipped: {summary.files_skipped}")
    print(f"  candidates found: {summary.candidates_found}")
    print(f"  notes with no change needed: {summary.notes_with_no_change_needed}")
    if limit is not None and len(candidates) < summary.candidates_found:
        print(f"  candidates reported: {len(candidates)} (limit {limit})")


def print_json_report(candidates: Sequence[Candidate], summary: ScanSummary, limit: int | None) -> None:
    """Render the same report as JSON."""

    payload = {
        "summary": asdict(summary),
        "limit": limit,
        "candidates_reported": len(candidates),
        "candidates": [asdict(candidate) for candidate in candidates],
    }
    json.dump(payload, sys.stdout, indent=2)
    sys.stdout.write("\n")


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    root = Path(args.root)
    if not root.exists() or not root.is_dir():
        print(f"error: scan root does not exist or is not a directory: {root}", file=sys.stderr)
        return 2

    terms = filter_terms(build_default_terms(), args.include_term, args.exclude_term)
    if not terms:
        print("error: no terms left to scan after include/exclude filters", file=sys.stderr)
        return 2

    candidates, summary = scan_files(root=root, terms=terms, limit=args.limit)
    if args.json:
        print_json_report(candidates, summary, args.limit)
    else:
        print_terminal_report(candidates, summary, args.limit)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
