# grok-build-plugins

Grok Build marketplace catalog. Plugin **source of truth** for pstack is [tommy-ca/pstack](https://github.com/tommy-ca/pstack). This repo is an index. It does not vendor `skills/`.

The index uses Grok's remote source form (`url` plus a full commit sha). It does not vendor plugin folders. Cursor wrap and open-pstack-as-Grok-host are not the default. Contract: [SPEC.md](./SPEC.md).

## Install pstack (Grok-native)

xAI Official already publishes a plugin named `pstack` that points at `cursor/plugins`. Bare `grok plugin install pstack` can load that wrap. The first-party tree is **owner/repo**.

```bash
grok plugin install tommy-ca/pstack --trust
grok plugin enable pstack
```

`inspect` listing pstack as enabled is trust, not `[plugins].enabled`. Skills and `pstack:how-explorer` agents load only after enable. Enable rewrites `~/.grok/config.toml`. Inside a sandboxed agent that is EROFS (os error 30). Run enable from a host shell (`grok --sandbox off plugin enable pstack`). After enable, spawn `pstack:how-explorer`, not `how-explorer`. After marketplace add, still install `tommy-ca/pstack`, never bare `pstack`.

Optional catalog (browse later siblings; does not replace the owner/repo install):

```bash
grok plugin marketplace add tommy-ca/grok-build-plugins
# or a local checkout:
# grok plugin marketplace add /path/to/grok-build-plugins
```

Run that from a **host shell**, not from a Grok agent turn. This TUI sandboxes tools with bubblewrap (`__GROK_INSIDE_BWRAP=1`). `[sandbox] profile` `homelab` extends `workspace`. `~/.grok/config.toml` is bind-mounted read-only. Nested `grok plugin marketplace add` then fails with EROFS (os error 30). `grok plugin install tommy-ca/pstack --trust` still works. It writes `installed-plugins/`, not `config.toml`.

Playbooks use `spawn_subagent` and persist-then-wake overnight. See [HARNESS.md](https://github.com/tommy-ca/pstack/blob/main/HARNESS.md).

When Cursor `pstack/` moves, run `python3 scripts/sync-from-upstream.py --log` then `--recipe` in [tommy-ca/pstack](https://github.com/tommy-ca/pstack). The script is print-only. Then copy except `make-bot-ui`, run `adapt-harness.py`, TUI hand-map, `verify-harness.py`. Pin is [UPSTREAM](https://github.com/tommy-ca/pstack/blob/main/UPSTREAM).

## v1 plugins

| Name | Source |
| --- | --- |
| `pstack` | pinned sha of `tommy-ca/pstack` (`marketplace.json`) |

After a pstack release, set `plugins[0].source.sha` to `git -C pstack rev-parse origin/main` (40 hex) and re-run `python3 tests/test_marketplace.py`.

## Later candidates (not in this index)

From `cursor/plugins`, skip unless a Grok-native gap is proven: `cursor-team-kit` (use `/unslop`), `make-bot-ui`, `orchestrate` (Cursor cloud), canvases, `cursor-sdk`. Possible later Grok ports after an adapter: `cli-for-agent`, `continual-learning`, `ralph-loop`, `create-plugin`. Do not nest tommy-ca/pstack as `plugins/pstack` to match cursor/plugins or open-pstack. A later plugin is another `plugins[]` row with `url` and sha. See [adr/0001-catalog-is-index-not-plugin-monorepo.md](./adr/0001-catalog-is-index-not-plugin-monorepo.md).
