## ADDED Requirements

### Requirement: Intent-driven tasks template exposes Parallel bands

Feature: openspec-tasks-parallel-bands
Rule: Parallel band markup is the convention home (A2); serial only for true gates

The intent-driven OpenSpec `tasks.md` template MUST include `## Parallel band A` and `## Parallel band B` (or later lettered bands) headings for independent leaves. Leaves that may run concurrently MUST be tagged `P-parallel` (inline comment or checkbox suffix). Numbered serial sections (`## 1.` / `## 2.` style) MUST be reserved for true gates: propose validate, STOP handoff, Todd-go apply authority, archive. Soft-after leaves MUST be marked Soft-after and MUST NOT be forced into a fake total order with unrelated P-parallel leaves. The template MUST NOT invent Drove `max_concurrent` quota numbers. The convention home MUST be the OpenSpec template (+ openspec-intent-flow + SPEC scenarios), not tommy-mode and not herdr-only markup.

#### Scenario: Template ships Parallel band headings

- **GIVEN** tip `openspec/schemas/intent-driven/templates/tasks.md` after this change applies
- **WHEN** an author drafts a new change `tasks.md` from the template
- **THEN** the template includes `## Parallel band A` and `## Parallel band B` headings
- **AND** it documents `P-parallel` leaf tags for independent checkboxes
- **AND** it documents serial-only use for validate → STOP → Todd-go → archive gates

#### Scenario: Serial sections stay for true gates only

- **GIVEN** a change with independent apply leaves and a validate gate
- **WHEN** `tasks.md` is authored from the template
- **THEN** independent leaves sit under Parallel band headings with `P-parallel` tags
- **AND** validate / STOP / Todd-go / archive remain serial gate sections
- **AND** Soft-after leaves are marked Soft-after rather than serialized with unrelated P-parallel work

#### Scenario: Convention home is not tommy-mode or herdr-only

- **GIVEN** Arena A2 locked lean (template + openspec-intent-flow + SPEC)
- **WHEN** authors place Parallel band markup
- **THEN** the primary home is the intent-driven tasks template and openspec-intent-flow narrative
- **AND** tommy-mode is not required as markup SoT
- **AND** herdr skill text is not the tasks markup home

### Requirement: openspec-intent-flow narrates N-briefs after tasks

Feature: openspec-tasks-parallel-bands
Rule: B1 orch language — N briefs / parallel bands; not Drove caps

The `openspec-intent-flow` skill (and SPEC scenarios that accept it) MUST state that after `tasks.md` exists and validates, Horizon/Drove MAY spawn N briefs for `P-parallel` leaves — one exclusive worktree (or conceptKey write target) per arm — and join on evidence. Specs and design MAY still proceed in parallel after proposal (existing gate). The skill MUST keep the propose gate (proposal → specs/design → adr → tasks) serial. The skill MUST NOT document Drove `max_concurrent` standing-order numbers inside gbp product text. The skill MUST NOT claim parallelism-sync done from propose prose alone.

#### Scenario: N-briefs unlock after tasks.md

- **GIVEN** a validated OpenSpec change folder with `tasks.md` containing Parallel band `P-parallel` leaves
- **WHEN** Horizon/Drove builds apply briefs
- **THEN** it MAY emit one brief per independent P-parallel leaf
- **AND** each brief names a distinct worktree or exclusive write target
- **AND** join waits on evidence paths, not first idle alone

#### Scenario: Propose gate stays serial (B8 KEEP)

- **GIVEN** an OpenSpec change missing `tasks.md`
- **WHEN** an implementer spawn is considered
- **THEN** spawn is refused until proposal, specs, design, adr, and tasks validate
- **AND** specs∥design after proposal remains allowed
- **AND** the refuse reason names the tasks / propose gate

#### Scenario: No Drove quota invent in gbp narrative

- **GIVEN** openspec-intent-flow or SPEC parallel-band text after this change
- **WHEN** orch language for N-briefs is read
- **THEN** it describes band/P-parallel semantics and exclusive worktrees
- **AND** it does not invent or prescribe Drove `max_concurrent` standing-order numbers for gbp
