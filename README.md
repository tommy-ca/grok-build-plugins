# grok-build-plugins

Grok Build marketplace catalog. Plugin **source of truth** for pstack is [tommy-ca/pstack](https://github.com/tommy-ca/pstack). This repo is an index. It does not vendor `skills/`.

The index uses Grok's remote source form (`url` plus a full commit sha). It does not vendor plugin folders. Cursor wrap and open-pstack-as-Grok-host are not the default. Contract: [SPEC.md](./SPEC.md).

## Install pstack (Grok-native)

xAI Official already publishes a plugin named `pstack` that points at `cursor/plugins`. Bare `grok plugin install pstack` can load that wrap. The first-party tree is **owner/repo**.

```bash
grok plugin install tommy-ca/pstack --trust
```

Optional catalog (browse later siblings; does not replace the owner/repo install):

```bash
grok plugin marketplace add tommy-ca/grok-build-plugins
# or a local checkout:
# grok plugin marketplace add /path/to/grok-build-plugins
```

Playbooks use `spawn_subagent` and persist-then-wake overnight. See [HARNESS.md](https://github.com/tommy-ca/pstack/blob/main/HARNESS.md).

Sync Cursor `pstack/` intent into the plugin tree using [tommy-ca/pstack UPSTREAM](https://github.com/tommy-ca/pstack/blob/main/UPSTREAM): diff since the pin, copy except `make-bot-ui`, `adapt-harness.py`, TUI hand-map, `verify-harness.py`.

## v1 plugins

| Name | Source |
| --- | --- |
| `pstack` | pinned sha of `tommy-ca/pstack` (`marketplace.json`) |

After a pstack release, set `plugins[0].source.sha` to `git -C pstack rev-parse origin/main` (40 hex) and re-run `python3 tests/test_marketplace.py`.

## Later candidates (not in this index)

From `cursor/plugins`, skip unless a Grok-native gap is proven: `cursor-team-kit` (use `/unslop`), `make-bot-ui`, `orchestrate` (Cursor cloud), canvases, `cursor-sdk`. Possible later Grok ports after an adapter: `cli-for-agent`, `continual-learning`, `ralph-loop`, `create-plugin`.
