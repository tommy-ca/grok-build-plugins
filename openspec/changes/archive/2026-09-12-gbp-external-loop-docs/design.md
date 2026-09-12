## Context

Tip floor `35c8c6c13b98a61fffab388a23f523090a470a53` (`35c8c6c`) — thermos archive #17 MERGED. Todd + room Act-on after Horizon audit of Symphony-class external loop: (1) rooms-map row for gbp room `91ada72e-0abc-40f8-bb44-971a584fbdf3`, (2) thin `EXTERNAL-LOOP.md` pointer in gbp. Fleet skills already own RACI / inner-outer / Drove tick / herdr; research audit already maps Symphony↔Drove. gbp tip lacks the pointer; box rooms-map lacks the gbp row.

## Goals / Non-Goals

**Goals:**

- NEW capability `gbp-external-loop-docs` with ADDED requirements for EXTERNAL-LOOP.md + rooms-map row honesty.
- Wave-4 propose-only; validate `--strict` PASS; OpenSpec PR only.
- Wave-5 Apply HOLD: land EXTERNAL-LOOP.md; Drove updates rooms-map; re-validate.

**Non-Goals:**

- Second SoT duplicating sand-workflow skill bodies
- Elixir Symphony daemon
- Remint `thermos-grok-port` or closed gbp Act-ons
- Invent LIVE / LIVE_PASS
- Dual orch
- Product EXTERNAL-LOOP.md or box rooms-map edit in the propose PR

## Decisions

1. **Change id `gbp-external-loop-docs`** (prefer over `gbp-symphony-external-loop`) — docs/honesty Act-on, not a Symphony port.
2. **NEW capability only** — no MODIFY of living tip specs; cite thermos trail as example, do not remint.
3. **Pointer, don't vendor** — EXTERNAL-LOOP.md cites `sand-workflow:*` ids + fleet audit path; skill bodies stay in sand-data/agent-data workflows.
4. **Split apply ownership** — gbp git Apply lands EXTERNAL-LOOP.md + OpenSpec merge (Horizon leaf); Drove/eggbot lands rooms-map row on box SoT.
5. **No new durable ADR** — role RACI and external-loop posture already live in fleet-org-raci / drove-external-loop / inner-outer-orch; this change cites.
6. **Propose-only Wave-4** — product pointer and box row land Wave-5 after Todd/Horizon go.

## Risks / Trade-offs

- [Pointer bitrots if skill ids rename] → Cite stable sand-workflow ids; update on churn.
- [Operators treat EXTERNAL-LOOP.md as full SoT] → Spec SHALL say thin pointer; lead with skill cites.
- [rooms-map row claimed from propose prose] → Spec + tasks require Metadata verify on box SoT; gbp PR does not fake the row.
- [Confusion with thermos remint] → Explicit non-goal; cite #15→#17 as worked example only.

## Migration Plan

1. Propose artefacts on worktree `docs/openspec-gbp-external-loop` from tip `35c8c6c`.
2. `openspec validate gbp-external-loop-docs --type change --strict` → PASS.
3. OpenSpec-only PR; do not merge as apply; do not write product EXTERNAL-LOOP.md in propose PR.
4. Wave-5 after Todd/Horizon go: land EXTERNAL-LOOP.md; Drove/eggbot update rooms-map; merge capability; re-validate; archive.
5. No tag move. No Elixir daemon. No LIVE invent.

## Open Questions

None that block propose. Exact one-page layout of EXTERNAL-LOOP.md (tables vs short bullets) is Wave-5 author choice within the SHALL map.
