# Nitrification

- Status: `draft`

## Purpose

- Explain nitrification as a treatment process the project relies on when reasoning about ammonia control, pH drift, and biofilter importance.

## What it is

- Nitrification is the microbial conversion path that moves ammonia toward nitrate.
- In current repo language, that path runs through nitrite before reaching nitrate.
- This is a biological conversion process, not a solids-separation step.

## Why it matters in aquaponics

- Aquaponics depends on turning ammonia released by fish waste and feed into forms the system can tolerate and plants can use later in the chain.
- Good nitrification supports water quality stability.
- Weak nitrification can leave more ammonia or nitrite pressure in the loop.

## How this project uses it

- The repo treats nitrification as one of the core water-chemistry processes affecting pH.
- The biofilter component note treats it as a central treatment role and includes stoichiometry anchors for oxygen demand and alkalinity demand.
- Business and operations layers reference nitrification indirectly through water-quality outputs, labor, chemistry management, and treatment components rather than as a direct revenue item.

## How it is measured or interpreted

- The project does not reduce nitrification to one single direct field.
- Instead, it is interpreted through related signals such as TAN, nitrite, nitrate, pH movement, and biofilter performance context.
- Oxygen and pH matter because the current atomic truths say microbes nitrify better in slightly to moderately alkaline pH ranges, while the biofilter note flags oxygen limitation as a failure mode.
- Current repo notes also support that nitrification consumes alkalinity and tends to push pH downward over time.

## Common Mistakes or Confusions

- Confusing nitrification with solids removal.
- Treating a biofilter as only a mechanical filter.
- Reading falling pH without considering whether nitrification demand is part of the reason.

## Related Terms

- [[Reference/Glossary and Naming Conventions#Nitrification|Nitrification]]
- [[Reference/Glossary and Naming Conventions#Biofilter|biofilter]]
- [[Reference/Glossary and Naming Conventions#TAN|TAN]]
- [[Reference/Glossary and Naming Conventions#Nitrite|nitrite]]
- [[Reference/Glossary and Naming Conventions#pH|pH]]
- [[Reference/Glossary and Naming Conventions#Alkalinity|alkalinity]]
- [[Reference/Glossary and Naming Conventions#Dissolved Oxygen / DO|dissolved oxygen / DO]]

## Related Notes

- [[Reference/Glossary and Naming Conventions|Glossary and Naming Conventions]]
- [[Reference/Explainers/TAN|TAN]]
- [[Reference/Explainers/pH|pH]]
- [[Components/Water Loop/Biofilter|Biofilter]]
- [[Atomic Truths/Core Atomic Truths|Core Atomic Truths]]

## Open Questions or Caveats

- The repo has useful stoichiometry anchors for oxygen and alkalinity demand, but those should remain treatment-context anchors rather than being over-read as universal operating thresholds.
- Nitrification performance remains context-sensitive to design, maturity, temperature, oxygen, and chemistry management.
