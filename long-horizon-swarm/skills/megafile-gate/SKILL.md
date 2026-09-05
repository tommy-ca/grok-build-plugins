---
name: megafile-gate
description: Block commits that grow a hot file past a loc threshold and spawn a decompose worker. Use from long-horizon drain.
disable-model-invocation: true
---

# Megafile gate

Popular files attract collisions and hide split-brain. Workers flag bloat. An outside agent decomposes.

1. Threshold lives in `long-horizon/<id>/preferences.md` (`megafile-loc: <N>`). Default 800.
2. Before a worker reports PASS, it counts loc on files it touched. Over threshold → ISSUES, not PASS.
3. Parent spawns a decompose worker on a different branch whose only job is to split the file behind a seam. Architect first if the seam is new. `spawn_subagent` `pstack:feature` or `pstack:refactoring` if that role exists, else `pstack:feature`.
4. The original unit rebases onto the decompose result or waits. It does not keep growing the megafile.
