---
name: tommy-mode
description: >
  tommy's agent style for pstack-first OpenSpec work, git worktrees, merge-to-main
  with SSH push, and live verification. Use for tommy, /tommy-mode, or requests
  to work in their style.
disable-model-invocation: true
---

# Tommy mode

Personal overlay on `/poteto-mode`. Read that skill for playbooks, principles, skill order, spawn field rules, and unslop. This file only holds standing overrides.

## Non-negotiables

Start multi-step work with a todolist. First item is to read `/poteto-mode` Principles and the host `HARNESS.md`. Then apply this overlay.

- Router is `/poteto-mode`. Do not start from `/workflow` or `/goal`.
- Skill order is pstack, then user, then bundled and builtin. Copy playbook steps in verbatim. Skip with `skip: <reason>`.
- Spawn `pstack:<role>`, never a bare stem. Depth 1. Parent fans out. Do not send effort on spawn.
- OpenSpec is intent-driven. Propose, land the proposal on main, apply, then archive. Do not amend an archived change.
- Prove on the live surface. Inspect, plugin validate, and the repo's test command beat "it compiled."
- Land by merging to `main` and SSH-pushing. Do not open a GitHub PR unless the user names one.

## Autonomy

Reversible work proceeds without asking. Keep going on in-flight loops that say "the above."

Pause for force-push, deploy, data deletion, and customer messages.

Push back when a request recouples two products or invents a host field. A recommendation is a judgment.

## Process

Worktrees live at `$REPO/.worktrees/$BRANCH_NAME`. Preserve slashes in the branch name. Isolation checkout is `main`. Feature work is not that tree.

Commits are signed. Conventional subjects. Merge with `--no-ff` into `main`, then `git push` over SSH.

Do not rewrite published history.

## Review and verify

TDD when the contract is a string or token. Fail first. Then the docs or code.

After GREEN, parent-spawn `pstack:independent-verifier`. Review the child's diff yourself. Do not pass through its summary.

`--trust` is not enable. Skills and `plugin:role` agents load only after `grok plugin enable`. Then start a new session.

`inspect.plugins[].provides.agents` is the agents directory count, often `1`. Live types are `inspect.agents[]`.

Nested `grok inspect` is a new process. It applies `[sandbox] profile` from config. It is not this TUI. Measure this process with `argv`, `__GROK_INSIDE_BWRAP`, session `summary.json` `sandbox_profile`, `/proc/self/mountinfo`, and `~/.grok/sandbox-events.jsonl`. `--sandbox` on the TUI is sticky on resume, including when a built-in profile fail-opens.

Nested `grok plugin enable` and `grok plugin marketplace add` rewrite `~/.grok/config.toml` and hit EROFS. Run them as `grok --sandbox off …`. Daily TUI stays `workspace` or host `homelab` (both workspace-derived). Do not run the all-day TUI as `devbox`. `grok plugin install … --trust` does not need sandbox off.

DestDir writes outside Chezmoi source (`plugin enable` only in live `config.toml`, `cp` into `$HOME`) revert on the next trunk apply. Proof is apply from merged source plus empty `chezmoi diff`.

## Understand first

Nontrivial or "are we sure?" goes through pstack `how`. Playbooks are not slash commands.

Do not clone `commands/` when a skill `/name` already exists.

Do not teach one plugin on another plugin's operator surface.
