# pH

- Status: `draft`

## Purpose

- Explain pH as a practical compromise variable that connects fish health, plant nutrient use, nitrification performance, and ammonia risk.

## What it is

- pH is the current acidity or alkalinity reading of the water.
- It is not the same thing as alkalinity, which is the water's buffering capacity against acid addition.

## Why it matters in aquaponics

- pH matters because aquaponics is balancing more than one biological need at once.
- Current atomic truths say plants absorb some nutrients better in slightly acidic ranges, while nitrifying microbes do better in slightly to moderately alkaline ranges.
- pH also changes how much of the total ammonia pool sits in the more toxic NH3 form.

## How this project uses it

- The business-layer contract expects `observed_pH`.
- Current repo logic treats pH as a system operating output and a risk interpretation input, not as a business result by itself.
- The business-layer plan explicitly warns against treating TAN or pH warnings directly as business outputs; they should flow through explicit risk rules instead.

## How it is measured or interpreted

- In project terms, pH should be read together with TAN, temperature, and nitrification context.
- Changing pH too aggressively can change ammonia-risk interpretation because the NH3 fraction depends on pH.
- The repo also supports reading persistent pH decline as a possible sign that nitrification and buffering demand are active in the system.

## Common Mistakes or Confusions

- Treating pH as interchangeable with alkalinity.
- Optimizing pH for only one part of the system while ignoring fish, plants, or nitrifying microbes.
- Adjusting pH without considering how NH3 interpretation may change.

## Related Terms

- [[Reference/Glossary and Naming Conventions#pH|pH]]
- [[Reference/Glossary and Naming Conventions#Alkalinity|alkalinity]]
- [[Reference/Glossary and Naming Conventions#TAN|TAN]]
- [[Reference/Glossary and Naming Conventions#Unionized Ammonia / NH3|Unionized Ammonia / NH3]]
- [[Reference/Glossary and Naming Conventions#Temperature|temperature]]
- [[Reference/Glossary and Naming Conventions#Nitrification|nitrification]]

## Related Notes

- [[Reference/Glossary and Naming Conventions|Glossary and Naming Conventions]]
- [[Reference/Explainers/TAN|TAN]]
- [[Reference/Explainers/Unionized Ammonia NH3|Unionized Ammonia / NH3]]
- [[Reference/Explainers/Nitrification|Nitrification]]
- [[Components/Sensors/pH Sensor|pH Sensor]]
- [[Atomic Truths/Core Atomic Truths|Core Atomic Truths]]

## Open Questions or Caveats

- The repo has useful species and benchmark pH ranges, but those remain context-sensitive and should not be flattened into one universal target.
- pH interpretation should stay tied to species, temperature regime, and chemistry context.
