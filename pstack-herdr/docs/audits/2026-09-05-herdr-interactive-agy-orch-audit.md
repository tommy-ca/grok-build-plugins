# herdr interactive agy orch audit (2026-09-05)

## Verdict

Interactive agy via herdr is the correct fleet orch path. Todd confirmed interactive use is allowed (not against ToS). Bare `agy --print` remains journaled fallback only.

## Sources

- `herdr --skill` (0.8.2) — inside-pane driver; HERDR_ENV=1 gate (Herd **overrides** as outside-driver)
- `herdr agent` CLI: start / prompt / wait / read / send-keys / focus / explain / list / get
- https://herdr.dev/agent-guide.md — multiplexer + agent-aware sidebar; CLI for automation
- ferro overlay `.agents/skills/herdr` — agy args `--mode accept-edits --dangerously-skip-permissions` for authorized worktrees
- Live probe: server 0.8.2 compatible; two interactive `agy` agents listed (`skill-inh-w5` idle, `ferro-parity-w5` working); `antigravity-cli` integration current

## CLI map (orch-critical)

| Command | Role |
| --- | --- |
| `herdr status` | Server/client heal gate |
| `herdr workspace create --cwd --no-focus` | New project container + root pane |
| `herdr pane split --pane --cwd --no-focus` | Sibling shell pane (agent start never creates layout) |
| `herdr agent start <name> --kind agy --pane <id>` | Interactive agy in existing shell pane |
| `herdr agent prompt <t> <text> --wait --timeout` | Submit + wait idle/done/blocked |
| `herdr agent wait <t>` | Settled-state wait |
| `herdr agent read <t> --source recent-unwrapped` | Inspect output (does not mark seen) |
| `herdr agent focus <t>` | Mark seen so idle can settle |
| `herdr agent send-keys <t> …` | Blocked UI after inspect |
| `herdr agent explain --json` | Detection triage |
| `herdr integration status` | antigravity-cli for agy |

## Lifecycle truth

- `idle` / `done` ≠ task complete (need evidence file)
- `idle` requires tab **seen** in focused UI; CLI read does not mark seen
- `blocked` = approval/question — inspect before keys
- `agent_prompt_stalled` ≈ no lifecycle move within 5s from non-working — inspect/focus/heal before fallback

## Gaps vs prior herd-with-herdr (fixed)

1. Too thin — no interactive multi-turn / blocked / focus recipe
2. Implied headless caution overshadowed interactive default
3. `delegate-to-agy` start syntax omitted required `<name>` positional
4. No lifecycle table; idle/done could be misread as done
5. Upstream HERDR_ENV gate not explicitly overridden for outside-driver Herd

## Act-on

Skills rewritten: `herd-with-herdr`, `delegate-to-agy`. Herd persona aligned. Interactive = default.
