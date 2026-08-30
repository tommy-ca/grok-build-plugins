# grok-build-plugins

Grok Build marketplace catalog. Plugin **source of truth** for pstack is [tommy-ca/pstack](https://github.com/tommy-ca/pstack), not a second copy of `skills/` here.

Shape follows Grok [plugins](https://docs.x.ai/build) marketplace layout (`.grok-plugin/marketplace.json`), the same idea as `cursor/plugins` (many plugin folders + an index) and `ericlitman/open-pstack` (index + `plugins/pstack`). Cursor wrap and open-pstack-as-Grok-host are not the default.

## Add this marketplace

```bash
grok plugin marketplace add tommy-ca/grok-build-plugins
# or a local checkout:
# grok plugin marketplace add /home/tommyk/projects/grok-build-plugins
```

Install pstack (already Grok-native: `spawn_subagent`, persist-then-wake overnight):

```bash
grok plugin install pstack --trust
# or directly:
grok plugin install tommy-ca/pstack --trust
```

Sync Cursor `pstack/` intent into the plugin tree using [tommy-ca/pstack UPSTREAM](https://github.com/tommy-ca/pstack/blob/main/UPSTREAM): diff since the pin, copy except `make-bot-ui`, `adapt-harness.py`, TUI hand-map, `verify-harness.py`.

## v1 plugins

| Name | Source |
| --- | --- |
| `pstack` | pinned sha of `tommy-ca/pstack` |

## Later candidates (not in this index)

From `cursor/plugins`, skip unless a Grok-native gap is proven: `cursor-team-kit` (use `/unslop`), `make-bot-ui`, `orchestrate` (Cursor cloud), canvases, `cursor-sdk`. Possible later Grok ports after an adapter: `cli-for-agent`, `continual-learning`, `ralph-loop`, `create-plugin`.
