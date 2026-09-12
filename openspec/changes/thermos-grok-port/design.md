## Context

Tip floor `e3cb096cb2d68fefbb1629358e83ee4b69473180` (`e3cb096c`) — gbp #14 fleet-parallelism archive MERGED. Upstream MIT thermos at cursor/plugins provides dual-rubric parallel review + synthesize. Catalog ADRs 0001–0006 lock sibling-at-root packaging and forbid pstack nest. Wave-0 READY; Horizon unlocked; sole NEW Act-on `thermos-grok-port`.

```mermaid
C4Context
title thermos-grok-port context (propose)
Person(op, "Operator / reviewer")
System_Ext(up, "cursor/plugins thermos", "MIT dual-rubric + Task subagents")
System(gbp, "tommy-ca/grok-build-plugins", "catalog-is-index")
System_Ext(pstack, "tommy-ca/pstack", "poteto arena/interrogate/swarm")
System_Boundary(sib, "Sibling thermos/") {
  Container(pj, "plugin.json + HARNESS", "Grok harness map")
  Container(sk, "skills/", "thermos + two rubrics")
  Container(ag, "agents/", "dual review roles")
  Container(lv, "lever VERIFY", "script / verify-* skill")
}
Rel(op, gbp, "marketplace install/enable")
Rel(gbp, sib, "./thermos local source")
Rel(up, sib, "port map (skills/agents intent)")
Rel(sib, pstack, "poteto bind: arena/interrogate/swarm")
Rel(op, lv, "rerun falsifiable VERIFY")
```

## Goals / Non-Goals

**Goals:** Propose OpenSpec contract for grok-native `thermos/` sibling; dual-rubric orchestrator with Grok spawn map; full poteto bind including lever VERIFY; marketplace + SemVer `-thermos.N`; hold ADRs 0001–0006.

**Non-Goals:** Land product `thermos/` in Wave-4 PR; nest in pstack; Cursor Task as sole API; docs-only apply; invent LIVE_PASS; remint closed gbp leaves; new durable repo ADR unless major surprise at apply.

## Decisions

1. **Plugin id / dir = `thermos` (A1).** Match upstream id; catalog-root sibling like `tommy-mode/` and `long-horizon-swarm/`.
2. **Full poteto bind (A2).** Arena + interrogate + swarm/long-horizon handoff + lever VERIFY — not a subset.
3. **Sole NEW Act-on `thermos-grok-port` (A3).** Prefer NEW capability; light MODIFY `grok-build-marketplace` only for listing/version/spawn cite with full-body copies.
4. **Port map (upstream → grok):**

| Upstream | Grok target |
|---|---|
| `.cursor-plugin/plugin.json` | root `plugin.json` (`skills`, `agents`; no hooks/commands/MCP) |
| skill `thermos` | keep; rewrite spawn/join to HARNESS Grok primitives |
| skills `thermo-nuclear-review`, `thermo-nuclear-code-quality-review` | keep rubrics/intent |
| agents `thermo-nuclear-*-subagent` | grok agent defs; spawn as `thermos:<role>` |
| Cursor `Task` + `run_in_background` | `spawn_subagent` / swarm fan-out + `get_command_or_subagent_output` |
| `/add-plugin thermos` | marketplace `./thermos` + `grok plugin install` / enable |

5. **VERIFY levers (falsifiable):** `grok plugin validate` (or repo equivalent) on `thermos/`; skill smoke that orchestrator + both rubrics load; named `scripts/verify-thermos.sh` and/or `verify-thermos` skill; catalog/marketplace tests include thermos in sibling set. Reject docs-only.
6. **Propose-only Wave-4.** Apply HOLD until Todd/Horizon go. No product files in this PR.

## Poteto surfaces

| Surface | Role in thermos-grok |
|---|---|
| arena | Contested residual forks (agent depth vs pstack-role; harness wording) — id already locked |
| interrogate | Post-apply stacked review lens using thermos rubrics |
| swarm / long-horizon | Parallel dual-rubric fan-out when standing program owns the loop |
| lever | Named script/skill VERIFY — not prose-only |

## Risks / Trade-offs

- [Cursor Task recipes leak into skills] → HARNESS + R-THERMOS-02 MUST gate; apply review rejects sole-API Cursor flags
- [Docs-only pressure] → R-THERMOS-04 + tasks reject; Prove bars require installable surfaces
- [Marketplace MODIFY drift] → full-body copy of modified requirements; prefer NEW capability for port contract
- [SemVer collision] → `-thermos.N` namespace per ADR 0003–0005

## Migration Plan

1. Merge propose PR (OpenSpec only).
2. Wave-5 after Todd/Horizon go: land `thermos/` from upstream adapted to HARNESS; marketplace row + SemVer; lever scripts + tests; merge capability deltas; `openspec validate --strict`; archive.
3. No tag move of existing siblings. First thermos tag via `scripts/release.sh thermos` when ready.

## Open Questions

None that block propose. Exact agent filename stems vs shortened `thermos:` keys are Wave-5 author choice within R-THERMOS-01/02.
