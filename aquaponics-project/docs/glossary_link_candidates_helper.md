# Glossary Link Candidates Helper

Status: `draft`

## What it does

- Runs a read-only scan of `knowledge-vault/**/*.md` for likely glossary and chemistry-explainer link candidates.
- Prefers first-meaningful-mention candidates and reports them grouped by file for manual review.

## What it does not do

- It does not edit notes.
- It does not auto-insert wikilinks.
- It does not rewrite wording or mass-link repeated terms.

## Example usage

- `python scripts/glossary_link_candidates.py`
- `python scripts/glossary_link_candidates.py --include-term TAN --include-term pH`
- `python scripts/glossary_link_candidates.py --json --limit 20`

## Why it is review-first

- Link quality in the vault still depends on context, clutter, and judgment.
- This helper is meant to generate candidates that Codex or a human can review before any linking pass.
