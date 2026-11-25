# How to Run Locally

Run the simulation and the unit-economics comparison on your own PC, without Claude. Everything here is a scenario estimate, not validated.

## One-time setup

1. Open PowerShell in `Documents\Aquaponics-Claude` and get the latest code: `git pull`.
2. Go into the project folder: `cd aquaponics-project`.
3. Check Python works: `python --version` (3.9 or newer). If that opens the Microsoft Store or fails, use the real install instead: `C:\Users\ajith\AppData\Local\Python\bin\python.exe --version`, and use that full path wherever these notes say `python`.
4. Optional, for the research and LLM scripts only (`run.py` needs nothing extra):
   - `python -m venv .venv`
   - `.\.venv\Scripts\Activate.ps1` (if PowerShell blocks it, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once)
   - `pip install -r requirements.txt`

## Commands

From `aquaponics-project`:

| What | Command |
|---|---|
| List the runs | `.\run.bat` or `python run.py` |
| Basil crop cycle + Netherlands vs India economics | `.\run.bat basil_nl_vs_india` |
| Economics for all-India and the four southern states | `.\run.bat india_states` |
| Configurator: build a system from parts, cost per kg (NL / Karnataka) | `.\run.bat configure_basil_dwc_nl` or `.\run.bat configure_basil_dwc_karnataka` |
| Health check | `python scripts/check_mvp_integrity.py --quick` then `python -m unittest discover -s tests` |

`run.bat` picks `.venv` if it exists, else the real Python path above, else `python`.

The summary prints in the terminal. Files go to `data/simulation/results/local_runs/<run name>/`:

- `summary.txt`: the same summary
- `simulation_daily.csv`: one row per simulated day (growth, TAN, NH3, nitrate, pH, harvests); opens in Excel
- `unit_economics.csv`: one row per configuration, location and case (low / mid / high)
- `configurator_cost_breakdown.csv`: one row per cost line and case, with its cost per kg and share; edit parts in the run file's `configurator.build` block (see [[Project/How to Add Components|How to Add Components]])
- `*_result.json`: the full raw output

These files are ignored by git, so running things never changes the repo.

The unit-economics part needs the unit-economics pull request (#10) merged. Until then the run prints "skipped" for that part and still runs the simulation.

## How to change inputs

A run is a small JSON file in `aquaponics-project/runs/`. To try your own numbers:

1. Copy a run file, e.g. `runs/basil_nl_vs_india.json` to `runs/my_test.json`.
2. Edit it in Notepad or VS Code. The parts you can change:
   - `farm_area_m2`: a number gives headroom for the whole farm as well as per m2. `null` = per m2 only.
   - `simulation.scenario` and `simulation.days`: which system to simulate and for how long.
   - `simulation.overrides`: change scenario values, e.g. `"feeding.feed_rate_percent_body_weight_per_day": <number>` or `"fish_batch.count": <number>`.
   - `unit_economics.configs` and `unit_economics.locations`: which unit designs and places to compare. Empty list = all.
   - `unit_economics.overrides`: change prices, wages, power, labour or yield, always as a `{"low": ..., "high": ...}` range. Examples:
     - (replace `<low>` and `<high>` with plain numbers, no quotes)
     - `"locations.india.basil_wholesale_price_per_kg": {"low": <low>, "high": <high>}`
     - `"locations.netherlands.wage_per_hour": {"low": <low>, "high": <high>}`
     - `"configurations.C_representative_farm_basil_purdue_labour.labour_h_per_unit": {"low": <low>, "high": <high>}`
3. Run it: `.\run.bat my_test`.

How overrides work: each key is a dotted path into the base file (the scenario file, or `data/scenarios/unit_configuration_candidates_v0.json`). In the list of configurations, use the `config_id` as the path step. A typo stops the run and lists the names that exist. Keys starting with `_` are comments. The summary lists every change you made, so you can see which numbers are yours.

Rules of thumb:

- Put your own numbers in a run file, not in the base files. The base files hold sourced values with their reliability notes.
- Numbers you type are your assumptions. If one should become a project input, tell Claude so it can be checked and recorded with its source.
- Headroom is revenue minus labour and electricity only. It still has to pay for heating, building cost, consumables and any unpaid owner time, so it is not profit.

## Related Notes

- [[Project/Project|Project]]
- [[Learnings/Simulation Findings Log|Simulation Findings Log]]
