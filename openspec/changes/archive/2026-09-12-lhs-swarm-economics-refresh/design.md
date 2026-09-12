## Context

Tip floor `d03c318c9885b11d07ce5725629874f0e3eb165b` (`d03c318c`) — gbp-external-loop-docs archive #20 MERGED; `EXTERNAL-LOOP.md` live. Overlay `long-horizon-swarm` at `1.1.0-long-horizon-swarm.0` already implements Cursor swarm-economics mechanisms (planner≠worker + CostPolicy, Field Guide, review-lenses, megafile-gate, ossify-break, openspec-intent-flow, refuse flat-swarm/dual-board/nested-spawn). Wave-0 audit: HARNESS/README still Grok-CLI spawn-centric; Brief.VERIFY/handoff allow prose-only; blog failure modes are not a single falsifiable checklist; fleet roles-map/personas lack overlay skill cites; SemVer still 1.1.0. Sole NEW Act-on `lhs-swarm-economics-refresh`. Do not remint thermos or gbp-external-loop-docs.

```mermaid
C4Context
title lhs-swarm-economics-refresh context (propose)
Person(op, "Operator / Todd")
System(gbp, "tommy-ca/grok-build-plugins", "catalog-is-index @ d03c318c")
System_Ext(pstack, "tommy-ca/pstack", "arena / interrogate / poteto / orch")
System_Ext(blog, "Cursor swarm economics", "Wilson Lin Jul 2026")
System_Ext(ext, "EXTERNAL-LOOP.md", "fleet pointer already landed")
System_Ext(box, "box fleet SoT", "roles-map / fleet-roles.mdc / personas")
System_Boundary(lhs, "long-horizon-swarm overlay") {
  Container(harn, "HARNESS + README", "Grok primitives + fleet seats")
  Container(pb, "playbook + standing-orders", "failure-mode checklist")
  Container(sk, "overlay skills", "keep; no arena clone")
  Container(lv, "verify-long-horizon-swarm.sh", "prove lever")
}
Rel(op, gbp, "marketplace install/enable")
Rel(gbp, lhs, "./long-horizon-swarm local source")
Rel(blog, pb, "failure modes as refuse/stop checks")
Rel(ext, harn, "Drove/Horizon/CAO/Herd/Heavilifter bind")
Rel(lhs, pstack, "pstack:<role>; arena/interrogate cite")
Rel(box, ext, "Drove/eggbot cite lines (split apply)")
Rel(op, lv, "rerun falsifiable VERIFY")
```

## Goals / Non-Goals

**Goals:**

- NEW capability `lhs-swarm-economics-refresh` with ADDED requirements for fleet bind, lever-first VERIFY, blog checklist, SemVer + prove lever, and box SoT cite honesty.
- Wave-4 propose-only; validate `--strict` PASS; OpenSpec PR only.
- Wave-5 Apply HOLD: refresh overlay surfaces; bump `1.2.0-long-horizon-swarm.N`; prove verify script + marketplace tests; Drove/eggbot roles-map/persona cites; re-validate.

**Non-Goals:**

- Remint `thermos-grok-port` or `gbp-external-loop-docs`
- Clone arena / interrogate / invent Cursor VCS
- Nest under pstack; Elixir Symphony daemon; invent LIVE_PASS
- Dual orch / flat-swarm / dual-board / nested-spawn
- MODIFY `grok-build-marketplace` (listing + uniqueness already in force)
- Product plugin or box SoT edits in the propose PR
- Docs-only apply

## Refresh map (tip → apply)

| Surface | Tip `d03c318c` | After apply |
| --- | --- | --- |
| `HARNESS.md` | Grok spawn/join/orch/worktree only | + fleet seat table citing EXTERNAL-LOOP |
| `README.md` | install + skill list | + pointer at fleet bind |
| playbook | 10-step TaskTree + article-loop table | + named failure-mode checklist |
| standing-orders | 15 lines; VERIFY = real artifact | + lever-first + checklist predicates |
| handoff-contract | enum only | + lever path + PASS/FAIL/INCONCLUSIVE |
| `plugin.json` / marketplace | `1.1.0-long-horizon-swarm.0` | `1.2.0-long-horizon-swarm.N` |
| overlay skills | keep eight skills; no agents | keep; no clone arena/interrogate |
| `scripts/verify-long-horizon-swarm.sh` | marketplace + validate + orch probe | still green; extend if new assertions needed |
| box roles-map / personas | role keys + RACI; no overlay skill cites | Drove/eggbot adds standing-program cite block |

## VERIFY levers (falsifiable)

| Lever | Proves |
| --- | --- |
| `scripts/verify-long-horizon-swarm.sh` | marketplace functions, release tests, `grok plugin validate ./long-horizon-swarm`, orch init when bun/node |
| `python3 tests/test_marketplace.py` | sibling list + SemVer uniqueness after bump |
| Static: HARNESS/README | fleet seats + dual-orch forbidden + Grok primitives remain |
| Static: playbook + standing-orders | eight blog failure modes as refuse/stop checks |
| Static: Brief.VERIFY / handoff | named `verify-*` or `scripts/verify-*.sh`; prose-only refuse |
| Metadata: box SoT | roles-map heading + skill cites; `fleet-roles.mdc` twin; persona one-liners |
| `openspec validate lhs-swarm-economics-refresh --type change --strict` | intent-driven artefacts |

Reject docs-only. Do not invent LIVE_PASS. Catalog prove claims wait on the verify script, not self-report.

## Decisions

1. **Change id `lhs-swarm-economics-refresh`.** Refresh, not a new sibling and not a remint of thermos / external-loop docs.
2. **NEW capability only.** Marketplace already lists `./long-horizon-swarm` and already requires unique `MAJOR.MINOR.PATCH-<plugin-name>.N`. No full-body MODIFY.
3. **SemVer minor `1.2.0-long-horizon-swarm.N`.** Fleet bind + VERIFY contract + checklist are additive capabilities (MINOR), not a patch and not a breaking MAJOR. N chosen at apply; first land typically `.0`. Do not move tags (ADR 0003–0005).
4. **Pointer, don't vendor.** HARNESS cites `EXTERNAL-LOOP.md` + sand-workflow ids already named there. Skill bodies stay in the overlay / pstack / sand-data.
5. **Arena/interrogate stay pstack cites.** Do not copy those trees into this plugin (playbook already calls them by name; GLOSSARY already says not shipped).
6. **Split apply ownership.** gbp git Apply (Horizon leaf) lands overlay + SemVer + OpenSpec merge. Drove/eggbot lands box roles-map / `fleet-roles.mdc` / personas, same shape as rooms-map on `gbp-external-loop-docs`.
7. **No new durable ADR.** Catalog ADRs 0001–0006 plus fleet RACI / EXTERNAL-LOOP already constrain packaging and orch. This change cites.
8. **Propose-only Wave-4.** Product refresh and box cites land Wave-5 after Todd/Horizon go.

## Risks / Trade-offs

- [HARNESS becomes a second SoT for fleet RACI] → Cite EXTERNAL-LOOP; keep the table to seats + Grok primitives only.
- [Operators treat article-loop table as enough] → Checklist MUST be refuse/stop predicates, not a second blog summary.
- [SemVer N collision] → uniqueness still enforced by marketplace tests; apply picks next free N.
- [Box cites claimed from propose prose] → Spec + tasks require Metadata verify; gbp PR does not fake the rows.
- [Docs-only pressure] → Prove bars reject README-only; HARNESS/playbook/lever/SemVer required.
- [Confusion with thermos / external-loop remint] → Explicit non-goal; cite those trails only.

## Migration Plan

1. Propose artefacts on worktree `chore/openspec-lhs-swarm-economics-refresh` from tip `d03c318c`.
2. `openspec validate lhs-swarm-economics-refresh --type change --strict` → PASS.
3. OpenSpec-only PR; do not merge as apply; do not edit product overlay in propose PR.
4. Wave-5 after Todd/Horizon go: refresh HARNESS/playbook/skills/references; bump SemVer; prove verify script + marketplace tests; Drove/eggbot box cites; merge capability; re-validate; archive.
5. No tag move. No Elixir daemon. No LIVE invent. No arena clone.

## Open Questions

None that block propose. Exact `N` in `1.2.0-long-horizon-swarm.N` and whether the verify script gains extra Static assertions are Wave-5 author choice within the SHALL map.
