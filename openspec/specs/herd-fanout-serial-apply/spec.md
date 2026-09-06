# herd-fanout-serial-apply Specification

## Purpose
Tip herd-with-herdr Parallel fan-out default and serial_apply journal when single-agent; arena/I1 stay local; honest tip-lag vs box lead.

## Requirements

### Requirement: Herd defaults to N-arm fan-out for parallel-band briefs

Feature: herd-fanout-serial-apply
Rule: Implement parallelism on exclusive worktrees; not judgment diversity

Tip `pstack-herdr` `herd-with-herdr` MUST document Parallel fan-out as the default when Horizon/Drove ships N parallel-band briefs (P-parallel leaves, one worktree each). For each brief, Herd MUST ensure a shell pane and `herdr agent start <unique-name> --kind <ready> --pane <id>` on **that** worktree only, start prompts per arm without serializing independent waits, and join on evidence paths (all present + done predicates), not on first idle. N× same-kind panes MUST NOT be called an arena or interrogate panel — arena/I1 stay local on Cursor Task. N×agy on N trees is implement parallelism only.

#### Scenario: N parallel-band briefs fan out

- **GIVEN** N independent parallel-band apply briefs with distinct worktrees
- **WHEN** Herd routes session-sized implement roles after Act-on
- **THEN** Herd starts one ready herdr agent per brief on its exclusive worktree
- **AND** prompts are started per arm without forcing a single serialized wait across independent arms
- **AND** join requires evidence paths for each arm

#### Scenario: Arena and interrogate stay local

- **GIVEN** an arena or interrogate judgment panel
- **WHEN** herdr routing is considered
- **THEN** those roles stay on pstack Task (`local` in pstack-herdr-agents)
- **AND** Herd does not spawn N× the same herdr kind as a fake arena
- **AND** prove-it / OpenSpec propose / eng-lead merge stay local

### Requirement: Serial apply is journaled when choosing one

Feature: herd-fanout-serial-apply
Rule: Do not silently default to one agent when N briefs arrived

Herd MUST use a single agent only when there is one brief, or a true gate leaf (validate / archive / Soft-after), or slots are starved. When choosing serial apply, Herd MUST journal herd-journal `class: serial_apply` the same turn with a symptom naming why (`one brief` | `true gate` | `slot starved`). Herd MUST NOT silently default to one agent when N briefs arrived. Pending herdr kinds MUST NOT be treated as live routes.

#### Scenario: serial_apply journaled for true gate

- **GIVEN** a single validate or archive Soft-after brief
- **WHEN** Herd chooses one agent
- **THEN** a herd-journal entry with `class: serial_apply` is written the same turn
- **AND** the symptom names `true gate` or `one brief` as applicable

#### Scenario: N briefs do not silently serialize

- **GIVEN** N parallel-band briefs with exclusive worktrees and ready herdr capacity
- **WHEN** Herd orchestrates apply
- **THEN** it does not collapse to one agent without journaling `serial_apply`
- **AND** if it must serialize due to slot starvation, the journal symptom names `slot starved`

#### Scenario: Honest tip lag vs box lead

- **GIVEN** box workflow `herd-with-herdr` already documents fan-out + serial_apply
- **AND** tip plugin sibling lags before apply
- **WHEN** propose or docs describe tip state
- **THEN** they state tip LAGS box and sync targets the plugin sibling
- **AND** they do not claim tip already patched because box leads
