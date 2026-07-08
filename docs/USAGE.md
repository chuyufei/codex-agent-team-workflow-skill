# Usage Workflow

## 1. Decide Whether Multi-Agent Coordination Is Worth It

Use this workflow when:

- The task spans product, design, data, code, testing, docs, or release.
- The work needs independent validation.
- The project will keep evolving over time.
- You need a traceable responsibility chain and durable project memory.

Keep the workflow simple when:

- The task is a small one-file fix.
- The request is only an explanation.
- A single command or direct edit is enough.

## 2. Start With Three Agents

```text
Manager agent: direction, requirements, task brief, acceptance criteria
Executor agent: scoped implementation or artifact production
Validator agent: independent checking against acceptance criteria
```

Do not create many agents at the start. Add design, data, assets, release, docs, or research agents only after those boundaries become real in the project.

## 3. Bootstrap Coordination Files

From a repository checkout:

```powershell
python .\skills\codex-agent-team-workflow\scripts\bootstrap_agent_docs.py "<project-path>" --profile generic
```

From an installed local skill:

```powershell
python "$env:USERPROFILE\.codex\skills\codex-agent-team-workflow\scripts\bootstrap_agent_docs.py" "<project-path>" --profile generic
```

The script creates:

- `AGENTS.md`
- `AGENT_REGISTRY.md`
- `docs/agent-handoff-template.md`
- `docs/agent-worklog-template.md`
- `docs/agent-retrospective-template.md`

## 4. Maintain The Agent Registry

In `AGENT_REGISTRY.md`, record:

- agent name
- thread ID when available
- role
- allowed paths
- forbidden paths
- workspace or worklog path

If the current Codex environment supports thread tools, use those tools to create, rename, read, and message threads. If it does not, use the same handoff template manually.

## 5. Use Standard Handoff Messages

Every non-trivial handoff should include:

- `task_id`
- from / to
- background
- objective
- scope
- what not to do
- allowed paths
- forbidden paths
- acceptance criteria
- required evidence
- next recipient

This is the core of the mechanism. Without standard messages, multiple agents become disconnected chat windows.

## 6. Run The Loop

```text
Manager writes the brief
-> Executor produces the work
-> Validator checks the work
-> Failed items return to Executor
-> Passing work returns to Coordinator for final report
```

The coordinator dispatches, collects, validates, and reports. It should not replace specialist ownership when specialist judgment is required.

## 7. Preserve Lessons

At the end of each meaningful task, record:

- what was done
- which files or artifacts changed
- what evidence proves the result
- which failures required rework
- which rule or template should be updated

For long-running projects, durable files are more reliable than chat memory alone.
