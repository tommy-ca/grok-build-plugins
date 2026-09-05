# grok-build-plugins

Grok Build marketplace catalog. Plugin **source of truth** for pstack is [tommy-ca/pstack](https://github.com/tommy-ca/pstack). pstack stays a remote `url` plus sha. Grok-native siblings live as folders next to this README (`agent-compatibility/`, `cli-for-agent/`, `tommy-mode/`, `long-horizon-swarm/`). That is the Cursor sibling layout for grok-native ports. It does not mean adding `pstack/` here. This repo does not vendor `cursor/plugins`. It does not nest pstack. Contract: [SPEC.md](./SPEC.md).

## Install pstack (Grok-native)

xAI Official already publishes a plugin named `pstack` that points at `cursor/plugins`. Bare `grok plugin install pstack` can load that wrap. The first-party tree is **owner/repo**.

```bash
grok plugin install tommy-ca/pstack --trust
grok plugin enable pstack
```

`[plugins].enabled` is the enable list. `inspect` may still print a plugin as enabled after `--trust` and before enable. Skills and `pstack:how-explorer` agents load only after enable. Then start a **new session**. grok snapshots slash names and spawn types at session start.

Live roles are `inspect.agents[]`. `inspect.plugins[].provides.agents` is the agents **directory count** (often `1`), not the number of `pstack:` or `agent-compatibility:` types.

Enable rewrites `~/.grok/config.toml`. Nested `grok plugin enable` and `grok plugin marketplace add` fail with EROFS (os error 30) when that file is bind-mounted read-only. That happens from a nested grok in this TUI even if `__GROK_INSIDE_BWRAP` is unset. Run add and enable from a **host shell** (`grok --sandbox off plugin enable pstack`). After enable, spawn `pstack:how-explorer`, not `how-explorer`. After marketplace add, still install `tommy-ca/pstack`, never bare `pstack`.

Optional catalog (does not replace the owner/repo pstack install):

```bash
grok plugin marketplace add tommy-ca/grok-build-plugins
# or a local checkout:
# grok plugin marketplace add /path/to/grok-build-plugins
```

`grok plugin marketplace list` prints source URLs only. Browse plugin names with `grok plugin list --json --available`. Nested add still hits EROFS on `config.toml`. `grok plugin install tommy-ca/pstack --trust` still works from the agent. It writes `installed-plugins/`, not `config.toml`.

## Herdr grok SessionStart

`herdr integration install grok` writes `~/.grok/hooks/herdr.json` and `herdr-agent-state.sh`. `grok --sandbox devbox` is correctly tracked for that install because `devbox` skips Direct global hook write protection (`18-sandbox.md`). Daily `homelab` extends `workspace`, so `~/.grok/hooks/` is bind-mounted read-only. Adding `read_write` of that path on `homelab` does not unbind it.

SessionStart tracking does not write the hooks dir. The script copies stdin to `$TMPDIR` and sends `pane.report_agent_session` to `$HERDR_SOCKET_PATH` (`~/.config/herdr/herdr.sock`). That report can succeed on `homelab` when the files already exist.

To install or update the grok integration, use a host shell:

```bash
./scripts/install-herdr-grok-hooks.sh
# or:
grok --sandbox herdr-install
# then herdr integration install grok
# or grok --sandbox off / grok --sandbox devbox
```

`[profiles.herdr-install]` lives in this repo's `.grok/sandbox.toml`. It extends `devbox`. Do not use it as the daily driver.

Playbooks use `spawn_subagent` and persist-then-wake overnight. See [HARNESS.md](https://github.com/tommy-ca/pstack/blob/main/HARNESS.md).

When Cursor `pstack/` moves, run `python3 scripts/sync-from-upstream.py --log` then `--recipe` in [tommy-ca/pstack](https://github.com/tommy-ca/pstack). The script is print-only. Then copy except `make-bot-ui`, run `adapt-harness.py`, TUI hand-map, `verify-harness.py`. Pin is [UPSTREAM](https://github.com/tommy-ca/pstack/blob/main/UPSTREAM).

## Plugins

| Name | Source |
| --- | --- |
| `pstack` | pinned sha of `tommy-ca/pstack` (`marketplace.json`) |
| `agent-compatibility` | `./agent-compatibility` |
| `cli-for-agent` | `./cli-for-agent` |
| `tommy-mode` | `./tommy-mode` |
| `long-horizon-swarm` | `./long-horizon-swarm` |

After a pstack release, set the pstack `source.sha` to `git -C pstack rev-parse origin/main` (40 hex) and re-run `python3 tests/test_marketplace.py`. Do not tag pstack from this repo.

Local sibling versions are SemVer `MAJOR.MINOR.PATCH-<plugin-name>.N` so git tags cannot collide. Do not copy pstack `-grokbuild.N` onto locals; that was the `v1.0.0-grokbuild.0` collision. Marketplace pstack version may still be pstack's grokbuild string. That row is a url+sha pin, not a catalog tag. Do not use CalVer or a ship date as uniqueness. Ship day is on the GitHub Release. After `release.yml` is on `origin/main`, tag from a host shell:

```bash
./scripts/release.sh
./scripts/release.sh agent-compatibility
```

That runs `grok --sandbox off plugin tag --push` on each local folder. If the local tag exists and origin does not, it `git push origin` that ref. Then `gh release view` or `gh release create --verify-tag --latest=false`. Nested grok cannot write `.git/refs/tags`.

Install siblings after marketplace add (host shell):

```bash
grok plugin install agent-compatibility --trust
grok plugin enable agent-compatibility
grok plugin install cli-for-agent --trust
grok plugin enable cli-for-agent
grok plugin install tommy-mode --trust
grok --sandbox off plugin enable tommy-mode
grok plugin install long-horizon-swarm --trust
grok --sandbox off plugin enable long-horizon-swarm
```

Spawn `agent-compatibility:startup-review`, not `startup-review`. Start a new session after enable.

## Skip list

From `cursor/plugins`, skip unless a Grok-native gap is proven: `cursor-team-kit` (use `/unslop`), `make-bot-ui`, `orchestrate` (Cursor cloud), canvases, `cursor-sdk`, `continual-learning`, `ralph-loop`, `create-plugin`. Do not nest tommy-ca/pstack as `plugins/pstack` to match open-pstack. Do not add a `pstack/` sibling to match cursor/plugins. See [adr/0001-catalog-is-index-not-plugin-monorepo.md](./adr/0001-catalog-is-index-not-plugin-monorepo.md) and [adr/0002-grok-native-sibling-plugins.md](./adr/0002-grok-native-sibling-plugins.md).
