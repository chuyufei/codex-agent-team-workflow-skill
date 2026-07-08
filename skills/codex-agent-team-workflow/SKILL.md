---
name: codex-agent-team-workflow
description: Build and run a traceable Codex multi-agent workflow for project development, iteration, research, content operations, design preview, testing, release, or handoff work. Use when the user wants multiple Codex threads/subagents to collaborate, asks to create an agent team, needs AGENTS.md/AGENT_REGISTRY.md/handoff templates, wants planner-executor-validator loops, or needs clean ownership boundaries across product, design, data, implementation, validation, documentation, and publishing. Always decompose the needed collaboration mechanism from the user's request first, ask the user to confirm it, and treat profiles as optional starting points rather than fixed constraints.
---

# Codex Agent Team Workflow

## Overview

Use this skill to turn scattered Codex conversations into a small, traceable agent team. The goal is not to make the model "smarter by roleplay"; the goal is to split context, ownership, validation, and handoff so a project can iterate without one thread doing strategy, execution, and judging its own work.

## Core Model

Default to the smallest useful team:

1. **Manager agent**: clarify direction, write task briefs, define scope and acceptance criteria.
2. **Executor agent**: implement or produce the artifact from the brief; do not re-plan or expand scope.
3. **Validator agent**: check the result against the Manager's criteria; do not implement.

Expand only when the project already has separate ownership surfaces, such as design, data, implementation, research, assets, release, or documentation.

## Workflow

1. Inspect the current project state first: project docs, `AGENTS.md`, git status, test commands, and user-provided requirements.
2. Decompose the needed collaboration mechanism before applying any profile:
   - Identify whether the task needs multiple agents or a single direct thread.
   - Identify real ownership boundaries such as requirements, design, data, implementation, validation, documentation, or release.
   - Define each proposed agent's inputs, outputs, allowed paths, forbidden paths, and validation gate.
   - Ask the user to confirm the mechanism before creating threads, dispatching subagents, or generating coordination files.
3. Decide whether multi-agent coordination is worth the overhead. For a tiny one-file fix, keep the workflow simple and state that choice.
4. Create or update durable coordination artifacts:
   - `AGENTS.md` for rules and role boundaries.
   - `AGENT_REGISTRY.md` for agent names, thread IDs, responsibilities, allowed paths, forbidden paths, workspaces, and log locations.
   - A handoff template for messages between agents.
   - A worklog template for each agent's actions and evidence.
5. If Codex thread-management tools are available, use them to create/list/read/rename threads and send messages. If not, use the same handoff protocol in Markdown and ask the user to copy messages between threads.
6. Run the loop:
   - Manager sends a scoped brief to Executor.
   - Executor completes work and sends evidence to Validator.
   - Validator passes or sends concrete failures back to Executor.
   - Repeat until acceptance criteria are met or the loop is blocked.
7. Main/coordinator agent summarizes the path, evidence, tests, risks, and remaining work for the user.

## Guardrails

- Do not let one agent be both player and referee on non-trivial work.
- Do not use agent roles as vague personality prompts. Define responsibility, allowed files, forbidden files, inputs, outputs, and validation gates.
- Do not let built-in profiles dictate the team shape. Start from the user's project, then choose or customize the smallest useful structure.
- Do not silently merge ownership. Data facts belong to the data agent; design decisions belong to the design agent; release actions belong to the release agent.
- Do not let split threads become isolated islands. Every handoff must include task ID, source, target, scope, evidence, and next action.
- Do not commit, push, publish, or modify production systems unless the user explicitly asked for that action.
- Keep all decisions grounded in current files and live state, not old chat memory.

## When Bootstrapping A Project

Use `scripts/bootstrap_agent_docs.py` to create starter coordination files in a target project:

```bash
python scripts/bootstrap_agent_docs.py /path/to/project --profile generic
```

Generate Chinese coordination templates:

```bash
python scripts/bootstrap_agent_docs.py /path/to/project --profile generic --language zh
```

Profiles:

- `generic`: manager, executor, validator.
- `web-static`: product/design/preview/code/data/assets/research/release/docs split for static or frontend-heavy projects.
- `content-team`: topic/content/material/data-review split for media or content operations.

Use a profile only after confirming it fits the user's requested collaboration mechanism. If it does not fit, customize the agent split and templates.

The script does not overwrite existing files unless `--force` is passed.

## References

- Read `references/workflow-guide.md` when designing a team topology or deciding whether multi-agent coordination is justified.
- Read `references/templates.md` when writing `AGENT_REGISTRY.md`, handoff messages, initialization prompts, worklogs, or acceptance loops.
- Read `references/principles.md` when preserving the core collaboration principles.
