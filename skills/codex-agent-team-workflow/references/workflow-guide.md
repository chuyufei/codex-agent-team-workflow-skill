# Workflow Guide

## First Move

Start from the user's actual request, not from a fixed profile.

1. Restate the task outcome and the risk of doing it in one thread.
2. Propose the smallest useful collaboration mechanism.
3. Name the real ownership boundaries, such as requirements, design, data, implementation, validation, documentation, or release.
4. Define each proposed agent's input, output, allowed paths, forbidden paths, and validation gate.
5. Ask the user to confirm before creating threads, dispatching agents, or generating coordination files.

Chinese principle: decompose the mechanism first, then ask the user to confirm it. `generic`, `web-static`, and `content-team` are starting points, not fixed organization structures.

## Decision Rule

Use a multi-agent workflow when at least one of these is true:

- The task spans strategy and execution.
- The result needs independent validation.
- The project has separate domains such as data, UI, assets, release, and documentation.
- Work can proceed asynchronously.
- The user wants durable project memory across future Codex windows.

Avoid multi-agent overhead when the task is a small direct edit, a single command, or a short explanation.

## Minimum Team

Start with three agents unless the project already proves a more specific split:

| Agent | Owns | Does not own |
| --- | --- | --- |
| Manager | direction, requirements, task brief, acceptance criteria | implementation |
| Executor | concrete implementation or production artifact | requirement expansion |
| Validator | independent checking against criteria | implementation |

This prevents one thread from making the plan, writing the work, and judging itself.

## Extended Team Patterns

### Product/software project

- `product` or Manager: product direction, scope, acceptance criteria.
- `design`: UX structure, information hierarchy, visual brief.
- `preview`: isolated static previews or screenshots, not production code.
- `code`: production implementation, focused file edits, local tests.
- `data`: source data, schema, generated files, audits, data facts.
- `research`: external references, competitor or library research, no edits.
- `release`: git status, diff checks, commit/push/deploy after explicit approval.
- `docs`: project memory, changelog, handoff docs.

### Content operations team

- `topic`: topic planning and content calendar.
- `content`: outline, copy, publishing notes.
- `material`: covers, images, screenshots, asset preparation.
- `review`: data pull, performance review, lessons, strategy adjustment.

Profiles should be adapted or reduced when the user's request is narrower than the template. A confirmed two-agent or single-thread plan is better than an oversized team.

## Standard Loop

1. Manager writes a brief with scope and acceptance criteria.
2. Executor performs only the scoped work.
3. Executor sends evidence to Validator.
4. Validator checks against the acceptance criteria.
5. If failing, Validator sends concrete failures back to Executor.
6. Main agent reports only after the loop passes or a real blocker appears.

## Human Intervention Points

Pause for the user when:

- The direction is ambiguous and a wrong assumption would change the product.
- The proposed collaboration mechanism has not been confirmed.
- A production edit or release action needs explicit approval.
- A generated preview needs user selection before implementation.
- External credentials, login, payment, or private accounts are required.

## Traceability Requirements

Every non-trivial handoff must preserve:

- task ID
- source agent
- target agent
- source thread ID if available
- target thread ID if available
- scope
- allowed paths
- forbidden paths
- acceptance criteria
- evidence requested
- current status

Use this as the agent communication ledger so later debugging can answer who asked for what, who executed it, and why.
