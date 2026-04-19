# Unionized Ammonia / NH3

- Status: `draft`

## Purpose

- Explain why `NH3` is the operationally dangerous part of the ammonia pool and how the current project distinguishes it from TAN.

## What it is

- Unionized ammonia (`NH3`) is the more toxic ammonia fraction within the total ammonia pool measured as TAN.
- It is distinct from `NH4+`, which is the ionized form and generally less immediately toxic in the same way.

## Why it matters in aquaponics

- NH3 is one of the clearest fish-risk signals in the current project chemistry set.
- Even when TAN looks moderate, the NH3 fraction can become more important if pH rises or water gets warmer.
- That makes NH3 an operational warning concept, not just a chemistry definition.

## How this project uses it

- The business-layer contract expects `observed_unionized_nh3_mg_l`.
- Current atomic truths support two key interpretations: the NH3 fraction depends on pH, and warmer water has more toxic NH3 at a given pH.
- The current tilapia profile includes `unionized_nh3_warning_mg_L` and `unionized_nh3_critical_mg_L`, but those values belong to that species profile and should not be treated as universal.

## How it is measured or interpreted

- In project terms, NH3 should be interpreted alongside TAN, pH, and temperature.
- The repo supports the idea that rising pH and rising temperature can both push more of the total ammonia pool into the NH3 fraction.
- That means the same TAN reading can imply different risk under different water conditions.

## Common Mistakes or Confusions

- Treating NH3 and TAN as interchangeable.
- Reading a TAN value without checking whether pH or temperature makes the NH3 fraction more dangerous.
- Taking species-specific NH3 warning values as canon for all species and all aquaponics contexts.

## Related Terms

- [[Reference/Glossary and Naming Conventions#Unionized Ammonia / NH3|Unionized Ammonia / NH3]]
- [[Reference/Glossary and Naming Conventions#TAN|TAN]]
- [[Reference/Glossary and Naming Conventions#NH4+|NH4+]]
- [[Reference/Glossary and Naming Conventions#Temperature|temperature]]
- [[Reference/Glossary and Naming Conventions#pH|pH]]

## Related Notes

- [[Reference/Glossary and Naming Conventions|Glossary and Naming Conventions]]
- [[Reference/Explainers/TAN|TAN]]
- [[Reference/Explainers/pH|pH]]
- [[Atomic Truths/Core Atomic Truths|Core Atomic Truths]]
- [[Atomic Truths/Warnings and Cautions Atomic Truths|Warnings and Cautions Atomic Truths]]

## Open Questions or Caveats

- Direct NH3 measurement and NH3 estimation should not be conflated casually in later workflow design.
- Current warning framing is strongest for fish-risk interpretation; business outputs should still translate this through explicit risk rules rather than treating NH3 as a business outcome by itself.
