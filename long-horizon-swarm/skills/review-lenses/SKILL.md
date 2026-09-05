---
name: review-lenses
description: >
  Stack decorrelated review lenses before landing long-horizon work. Use for
  /review-lenses, merge-ready swarm verify, or when interrogate alone is one lens.
disable-model-invocation: true
---

# Review lenses

No single view catches every class of error. Stack decorrelated lenses. Review compute is cheaper than audited rework.

Builds on `/interrogate`, `playbooks/shipping.md` swarm-verify, show-me-your-work Attention.
Does not auto-apply fixes.

## Lenses

| id | Sees | Catches |
|---|---|---|
| full-transcript | agent transcript | hidden assumptions, skipped steps |
| output-only | handoff + diff | claimed vs delivered |
| codebase-only | repo at SHA, no chat | integration damage, megafiles |
| live | running app via the real surface | proxy-test lies |
| regression | trunk vs SHA | collateral breakage |
| interrogate | pstack `/interrogate` | adversarial review |

## Steps

1. Pick at least two lenses that do not share a model family when two families exist. Default merge-ready set: output-only plus codebase-only. Add live when the unit is behavioral. Add regression when the blast radius is more than one module.
2. Parent fans out. Output-only and live use `pstack:independent-verifier`. Codebase-only may use `pstack:how-explorer`. The interrogate lens is `/interrogate`. Do not send extra spawn fields.
3. Synthesize with the interrogate categories: Act on, Consider, Noted, Dismissed.
4. Write the HostStore ledger row only after the stacked verdict. All-clean (no Act on) is required to land. PASS+NOTES may land if every note is Dismissed or Noted with a reason.
5. Record which lenses ran in the show-me-your-work trail.

## Invariants

- Verifier model family differs from the worker when a second slug exists. Else `family: same-degraded`.
- Interrogate alone does not meet the two-lens bar.
- A lens that only rereads the worker's self-report is not a lens.
- CI green is an input, not a verdict.
