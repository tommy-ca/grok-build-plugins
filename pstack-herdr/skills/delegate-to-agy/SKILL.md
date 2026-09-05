---
name: Delegate to agy
description: >-
  Use when the workhorse is agy — spawn interactive agy via herdr by default
  (allowed); bare agy --print only as journaled fallback when herdr is down or
  stalled.
---
# Delegate to agy

Use when the workhorse kind is **agy** under Grok Bot meta-orch. Pair with [External coding agents](skill:external-coding-agents) and [Herd with herdr](skill:herd-with-herdr).

## Lane

**workhorse only.** Mechanical apply with a clear done predicate. Interactive session inside herdr is the product — not one-shot `--print`.

## Spawn (Todd 2026-09-05)

**Default: interactive via herdr** (Herd owns the pane):

```bash
# NAME is required; kind=agy starts the interactive CLI in an existing shell pane
herdr agent start <name> --kind agy --pane <pane_id> --timeout 60000
# optional friction-cutters only when the brief authorizes this exact worktree:
# herdr agent start <name> --kind agy --pane <pane_id> -- \
#   --mode accept-edits --dangerously-skip-permissions

herdr agent prompt <name> "$(cat path/to/brief.txt)" --wait --timeout 600000
# multi-turn: read → follow-up prompt → wait; on blocked: inspect then send-keys
herdr agent read <name> --source recent-unwrapped --lines 120
```

Interactive agy through herdr is **allowed** (not against ToS). Prefer multi-turn `prompt` over bare print.

**Exception only** (journal `action:fallback` first): herdr server down or `agent prompt` still stalled after heal + focus:

```bash
export PATH="$HOME/.local/bin:$PATH"
agy --print "$(cat path/to/brief.txt)"
```

Then return to herdr interactive — do not normalize bare CLI.

## Install / auth

agy via Antigravity CLI; integration `antigravity-cli` should show `current` under `herdr integration status`. Opus owns install; auth / folder-trust blocks → inspect via herdr, else Secretary.

## After

Evidence file + Prove It Works + eng-lead merge. Never merge on agy self-report or idle/done alone.
