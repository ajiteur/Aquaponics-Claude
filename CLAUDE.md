# CLAUDE.md

This is a Claude-based project: Claude Code and Claude projects are the primary agents
working on it. The rules for every agent live in `aquaponics-project/AGENTS.md` and
apply in full.

@aquaponics-project/AGENTS.md

## Claude-specific notes

- The git repo root is this folder. The code, data and tests live in `aquaponics-project/`,
  so run Python commands from there.
- Quick health check: `python scripts/check_mvp_integrity.py --quick`, then
  `python -m unittest discover -s tests`.
- The PDFs and the distilled research pack in this folder are source evidence, not canon.
- Work on a branch, keep commits small and scoped, and do not commit or push unless the
  user asks.
