# TAN

- Status: `draft`

## Purpose

- Explain what Total Ammonia Nitrogen means in project terms and why it should not be read as a stand-alone toxicity signal.

## What it is

- Total Ammonia Nitrogen (TAN) is the combined ammonia pool made up of `NH3` and `NH4+` in water.
- In repo chemistry language, TAN is a combined measure rather than the toxic fraction by itself.

## Why it matters in aquaponics

- Fish waste and uneaten feed release ammonia into recirculating water.
- TAN matters because it shows how much ammonia-related load the system is carrying before plant uptake and microbial conversion move that load onward.
- High TAN can become operationally important, but TAN alone does not determine toxicity.

## How this project uses it

- The business-layer contract expects `observed_tan_mg_l` as a system operating output.
- The current atomic truths treat TAN as a core water-chemistry term and note that common ammonia test kits often measure TAN.
- The project should interpret TAN together with [[Reference/Explainers/pH|pH]] and temperature rather than treating one TAN value as universally safe or unsafe.

## How it is measured or interpreted

- In practical aquaponics workflows, TAN often comes from the ammonia test result available to operators.
- The current repo language treats TAN as the combined reading and then uses pH and temperature context to interpret how much of that pool may be in the more toxic `NH3` form.
- Current evidence in the repo supports cautious interpretation rather than a universal TAN cutoff.

## Common Mistakes or Confusions

- Confusing TAN with [[Reference/Explainers/Unionized Ammonia NH3|NH3]].
- Treating TAN as a direct toxicity reading without checking pH and temperature.
- Assuming one species or one operating benchmark should become a universal TAN rule.

## Related Terms

- [[Reference/Glossary and Naming Conventions#TAN|TAN]]
- [[Reference/Glossary and Naming Conventions#NH4+|NH4+]]
- [[Reference/Glossary and Naming Conventions#Unionized Ammonia / NH3|Unionized Ammonia / NH3]]
- [[Reference/Glossary and Naming Conventions#Temperature|temperature]]
- [[Reference/Glossary and Naming Conventions#pH|pH]]

## Related Notes

- [[Reference/Glossary and Naming Conventions|Glossary and Naming Conventions]]
- [[Reference/Explainers/Unionized Ammonia NH3|Unionized Ammonia / NH3]]
- [[Reference/Explainers/pH|pH]]
- [[Reference/Explainers/Nitrification|Nitrification]]
- [[Atomic Truths/Core Atomic Truths|Core Atomic Truths]]

## Open Questions or Caveats

- The repo currently supports the statement that fish can tolerate higher TAN when pH is below `7.0`, but that should be read as context-dependent chemistry guidance rather than a stand-alone operating rule.
- Species-specific warning or tolerance interpretation should stay species- and context-aware.
