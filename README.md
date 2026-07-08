# Codex Agent Team Workflow Skill

A reusable Codex Skill for organizing multiple Codex threads or subagents into a traceable agent team.

The workflow turns long-running conversations into durable agents with explicit responsibilities, handoff messages, worklogs, evidence, and validation loops. It is designed for project development, product iteration, content operations, design previews, data work, testing, documentation, and release coordination.

## What This Is For

- Starting a new project with clear planning, execution, and validation roles.
- Iterating an existing codebase without mixing product, data, UI, implementation, and release decisions.
- Running design previews before editing production files.
- Keeping data facts, implementation, review, and publishing under separate ownership.
- Turning repeated project conversations into durable project memory.

## Repository Layout

```text
skills/codex-agent-team-workflow/     Codex Skill package
docs/USAGE.md                         Usage workflow
docs/VIDEO_KEY_POINTS.md              Source transcript principle summary
docs/EXAMPLE_PROJECT_SETUP.md         Example team setups
```

## Install

Copy the skill folder into your local Codex skills directory:

```powershell
Copy-Item -Recurse .\skills\codex-agent-team-workflow "$env:USERPROFILE\.codex\skills\codex-agent-team-workflow"
```

Restart Codex, then invoke it with:

```text
Use $codex-agent-team-workflow to set up a multi-agent workflow for this project.
```

## Generate Project Coordination Files

### From this repository checkout

Run the bootstrap script from the repository root:

```powershell
python .\skills\codex-agent-team-workflow\scripts\bootstrap_agent_docs.py "<project-path>" --profile web-static
```

### From an installed Codex skill

Run the script from the installed skill path:

```powershell
python "$env:USERPROFILE\.codex\skills\codex-agent-team-workflow\scripts\bootstrap_agent_docs.py" "<project-path>" --profile web-static
```

On macOS or Linux, use the equivalent installed path:

```bash
python ~/.codex/skills/codex-agent-team-workflow/scripts/bootstrap_agent_docs.py /path/to/project --profile web-static
```

Available profiles:

- `generic`: manager, executor, validator.
- `web-static`: product/design/preview/code/data/assets/research/release/docs split for static or frontend-heavy projects.
- `content-team`: topic/content/material/data-review split for media or content operations.

The script does not overwrite existing files unless `--force` is passed.

## Capability Boundary

This Skill defines a workflow and durable templates. It does not guarantee that every Codex surface can create, list, rename, read, or message separate threads.

When thread-management tools are available, use them for agent setup and handoff. When they are not available, use the same `AGENT_REGISTRY.md` and handoff templates manually by copying messages between threads.

## Core Principles

- Split context to reduce contamination.
- Split responsibilities so one agent is not both player and referee.
- Register each agent with a name, role, thread ID, workspace, and worklog.
- Use standard handoff messages for traceability.
- Keep evidence: changed files, command output, screenshots, reports, or written conclusions.
- Send failed validation back to the responsible agent.
- Keep release actions behind explicit human approval.

## Publish Checklist

Before publishing or packaging this repository:

- Run the bootstrap script once with at least one profile.
- Check that `SKILL.md` frontmatter contains only `name` and `description`.
- Confirm `agents/openai.yaml` matches the Skill.
- Confirm no local paths, private thread IDs, tokens, API keys, or temporary output files are tracked.
- Do not package local `tmp/`, `.agents/`, `.codex/`, or `__pycache__/` directories.
