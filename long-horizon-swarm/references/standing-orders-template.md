# Standing orders template

Paste into `long-horizon/<id>/preferences.md` before the first spawn. Numbered. Verbatim in every brief.

1. Planners never write product code. Briefs are the product.
2. Workers never edit plan, the selected unit board, or design docs they do not own.
3. Every spawn reads field-guide/index.md and stays under its line budget.
4. One writer per worktree. Shared mutable files are split first.
5. Every design decision has one conceptKey and one design-docs/<conceptKey>.md owner.
6. Code that embodies a decision cites that design doc.
7. Verification uses the real artifact. Self-report is not a verdict.
8. Verifier model family differs from the worker when a second slug exists. Else family: same-degraded.
9. Megafile threshold is 800 lines of owned code. Cross it and stop; spawn decompose.
10. Ossify-break is allowed as one focused patch that names the new contract in the DesignDoc.
11. Irreversible actions (force-push to shared branches, deploys, data deletion) still pause.
12. No weaker-model fallback. A missing lane is a dropout.
13. Brief.ACCEPTANCE is GIVEN/WHEN/THEN copied from the capability spec scenarios.
14. If openspec/changes/<id>/ exists, do not spawn workers until tasks.md exists.
15. Recurse is parent-owned units. Children do not call spawn_subagent.
16. Lever-first VERIFY: for a non-trivial leaf, Brief.VERIFY MUST name a `verify-*` skill or a `scripts/verify-*.sh` path. Refuse spawn when VERIFY is prose-only. Trivial leaves MAY use `skip: lever, <reason>`. Handoff Verification MUST record lever path + PASS/FAIL/INCONCLUSIVE (INCONCLUSIVE is not a pass). Nightly Audit / maintain-verification refreshes per-repo levers. Do not invent LIVE or LIVE_PASS.
17. Refuse flat-swarm, dual-board (second-board / dual-write), and nested-spawn. Arena and interrogate stay pstack cites — do not clone them into this overlay.
18. Blog failure-mode refuse/stop checklist (https://cursor.com/blog/agent-swarm-model-economics, Wilson Lin, Jul 2026) — keep planner≠worker, CostPolicy, Field Guide, review-lenses, megafile-gate, ossify-break, openspec-intent-flow:
    - split-brain: two live/pending nodes share a conceptKey → refuse spawn
    - planner contention: DesignDoc missing owner or two writers on same design-docs/<conceptKey>.md → refuse
    - merge reconciler: drain on collision without coordination-layer record and pstack:poteto-agent reconciler → drain incomplete
    - megafiles: owned file over megafile-loc (default 800) → ISSUES not PASS; spawn decompose
    - ossify: core change without ossify-break DesignDoc reason → refuse
    - review lenses: land without ≥2 lenses including pstack interrogate → refuse land
    - Field Guide: spawn without field-guide/index.md → spawn-contract miss
    - model economics: spawn without CostPolicy model bind, or drain without a spend.tsv row → incomplete
