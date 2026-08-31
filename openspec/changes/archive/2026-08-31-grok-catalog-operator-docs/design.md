## Context

`/check-agent-compatibility` on this catalog after reload: Deterministic 32 (scanner wants an app), Startup 90, Validation 91, Docs 91. Plugin load passed. Remaining holes are operator docs vs grok 1.0.13.

## Goals / Non-Goals

**Goals:** Fix the operator-doc holes that the live pass named. Lock them in tests.

**Non-Goals:** CI, linter, typechecker, or a fake app layout to raise the published scanner score. Changing grok inspect. Changing pstack.

## Decisions

1. **Docs and AGENTS.md, not a new toolchain.** This repo is a marketplace catalog. The scanner's 32/100 is expected.
2. **New session is required text.** grok snapshots skills and spawn types at session start.
3. **EROFS without the bwrap env var.** Nested enable still cannot rewrite bind-mounted `config.toml`.

## Risks / Trade-offs

- [Scanner still scores the catalog as an unknown app] -> Accept. Do not invent CI.

## Migration Plan

Docs and tests. Reinstall is not required. Operators who already enabled still need a new session for slash names.

## Open Questions

None.
