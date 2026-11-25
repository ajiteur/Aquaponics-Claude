# Aquaponics — evidence-first aquaponics brain

A Claude-based project, built with Claude Code and Claude projects.

An evidence-first aquaponics knowledge and simulation engine (tilapia, basil, lettuce;
media bed, DWC/raft and NFT). Research and corroboration reports feed a canonical
knowledge layer, which feeds simulation and a business layer. The goal is to use the
engine for predictions and for a go/no-go on a real farm, with an original aquaponics
simulation game as the fallback path.

- `aquaponics-project/` holds the code, data, tests and docs.
- `aquaponics-project/AGENTS.md` holds the rules every agent follows. `CLAUDE.md` loads it for Claude Code.
- `aquaponics-project/data/knowledge/` is canonical; `data/simulation/` is derived.

Setup: Python 3.13+. The MVP path needs only the standard library; the research scripts
need `pip install -r aquaponics-project/requirements.txt`.

Run it yourself: `cd aquaponics-project` then `.\run.bat` (Windows) or `python run.py` to list the runs,
and `python run.py <name>` to run one. See `knowledge-vault/Project/How to Run Locally.md`.
