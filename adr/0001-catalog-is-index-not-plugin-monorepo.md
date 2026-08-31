# Catalog is an index, not a plugin monorepo

- Status: accepted
- Date: 2026-08-31

## Context

cursor/plugins is a 63-plugin marketplace with sibling dirs. open-pstack nests one plugin at `plugins/pstack/` so Claude/Codex can `/plugin marketplace add` then install `pstack@open-pstack`. Grok already installs a repo-root `plugin.json` via `grok plugin install tommy-ca/pstack --trust`. This catalog already lists remote `url` plus sha.

## Decision

Keep `tommy-ca/pstack` as a single-plugin repo. Keep this catalog as an index of remote plugins. Do not vendor `cursor/plugins`. Do not nest pstack as `plugins/pstack/`. A later Grok-native plugin is another `plugins[]` entry with its own git `url` and sha.

## Consequences

v1 stays pstack only. `owner/repo#subdir` remains available if a future plugin lives in a monorepo. Bare `grok plugin install pstack` can still hit the xAI Official Cursor wrap.
