---
name: thermos
description: "Launch both thermo-nuclear review agents in parallel via Grok spawn_subagent, then synthesize their findings. Use for thermos, double thermo review, or combined bug/security and code-quality branch audits."
disable-model-invocation: true
---

# Thermos

Run the two thermo review passes as parallel Grok plugin agents, then synthesize their results.

## Workflow

1. Determine the review scope from the user request, PR, current branch, or relevant changed files.
2. Gather the diff and any file/context excerpts needed for reviewers to evaluate the change without guessing (typically `### Git / diff output` and `### Changed file contents`).
3. In **one** message, launch **both** reviewers with `spawn_subagent` and `background: true`:
   - `thermos:thermo-nuclear-review-subagent` for bugs, breakages, security, devex regressions, feature-flag leaks, and other branch-audit risks (loads `thermo-nuclear-review` rubric).
   - `thermos:thermo-nuclear-code-quality-review-subagent` for maintainability, structure, file-size growth, spaghetti, abstractions, and codebase-health risks (loads `thermo-nuclear-code-quality-review` rubric).
4. Pass each agent the same scoped diff/file context and ask it to return prioritized findings with file references and evidence.
5. Join with `get_command_or_subagent_output` using `task_ids` and `timeout_ms` > 0. Cancel with `kill_command_or_subagent` if needed.
6. After both finish, synthesize the results with findings first, deduplicated across reviewers. Weight overlapping findings more heavily, resolve disagreements with your own judgment, and keep summaries brief.

If individual background summaries are already visible to the user, do not restate them wholesale. Surface the unified verdict, the highest-signal findings, and any remaining uncertainty.

Do **not** treat Cursor Task / bare `subagent_type` / `run_in_background` as the sole invoke path. Spawn plugin-qualified `thermos:<role>` via `spawn_subagent`. See `HARNESS.md`.
