---
name: check-agent-compatibility
description: Run the full repository compatibility pass. Scanner score, startup path, validation loop, and docs reliability.
---

# Check agent compatibility

Read [`../../HARNESS.md`](../../HARNESS.md) first.

## Trigger

Use when the user wants the full compatibility pass for a repo.

## Workflow

Grok `MAX_SUBAGENT_DEPTH` is 1. This skill runs in the parent. Fan out four children in **one** message. Each `spawn_subagent` needs `prompt`, `description` (3-5 words), `subagent_type`, `background: true` (TUI default is false), and `isolation: "none"` unless HARNESS says otherwise. Omit `model` to inherit. Do not send effort on spawn. Children do not spawn.

1. `spawn_subagent` `subagent_type` `agent-compatibility:compatibility-scan-review` to run the CLI and capture the raw repository score.
2. `spawn_subagent` `subagent_type` `agent-compatibility:startup-review` to verify whether the repo can be booted by an agent.
3. `spawn_subagent` `subagent_type` `agent-compatibility:validation-review` to check whether an agent can verify a small change without an unnecessarily heavy loop.
4. `spawn_subagent` `subagent_type` `agent-compatibility:docs-reliability-review` to see whether the documented setup and run paths match reality.
5. Use one subagent per task. Do not collapse these checks into one agent prompt.
6. Join with `get_command_or_subagent_output` using `task_ids` and a positive `timeout_ms`.
7. Compute an internal workflow score as the rounded average of Startup, Validation Loop, and Docs Reliability scores.
8. Compute an Agent Compatibility Score as `round((deterministic_score * 0.7) + (workflow_score * 0.3))`.
9. Synthesize the results into one final response.

When scoring internally, use specific non-round workflow scores for the behavioral checks rather than coarse round buckets. If startup, validation, or docs mostly work, treat them as good-with-friction rather than defaulting to the mid-60s. Do not create a low workflow score just because logs are noisy or the error text is rough.

If the deterministic scanner cannot be run because of tool environment issues, say that separately and do not treat it as a repo defect or penalize the repo.

## Output

Respond in markdown, but keep it minimal. Do not use fenced code blocks.

Show only one score, as a level-two heading. `## Agent Compatibility Score: N/100`. Do not show how it was computed unless the user explicitly asks for a breakdown.

Then a flat, prioritized list labeled `Top fixes` with one issue per line, each line starting with `- `.

Fold deterministic and behavioral findings into that one list. Focus on the fixes that would most improve real agent workflows.
