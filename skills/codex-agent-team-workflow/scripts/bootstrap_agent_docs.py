#!/usr/bin/env python3
"""Bootstrap durable multi-agent coordination files for a project."""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path


PROFILE_ROLES = {
    "generic": [
        ("manager", "Direction, requirements, task briefs, acceptance criteria", "docs/, AGENTS.md, AGENT_REGISTRY.md", "implementation files"),
        ("executor", "Scoped implementation or artifact production", "assigned files", "out-of-scope files"),
        ("validator", "Independent validation against acceptance criteria", "tests, reports, screenshots, review notes", "implementation unless explicitly assigned"),
    ],
    "web-static": [
        ("manager", "Dispatch, collect, validate, report", "docs/, AGENTS.md, AGENT_REGISTRY.md", "specialist final judgments"),
        ("design", "UX structure, visual hierarchy, interaction brief", "design-previews/, docs/design-notes.md", "production code"),
        ("preview", "Static previews and screenshots", "design-previews/", "site/ production files"),
        ("code", "Production implementation and local tests", "site/, tools/", "data source changes unless assigned"),
        ("data", "Data generation, schema, audit, data facts", "data scripts, generated data, data docs", "UI and styling"),
        ("assets", "Images, carousel, compression, asset references", "assets/", "search/data/rendering logic"),
        ("research", "External reference research and implementation briefs", "docs/research/", "current project files"),
        ("release", "git status, diff checks, commit/push after approval", "repository metadata", "release without approval"),
        ("docs", "Project memory, changelog, handoff consistency", "Markdown docs", "production code unless assigned"),
    ],
    "content-team": [
        ("manager", "Direction, calendar, priorities, acceptance criteria", "docs/, AGENTS.md, AGENT_REGISTRY.md", "content production"),
        ("topic", "Topic planning and meeting capture", "docs/topics/", "final publishing"),
        ("content", "Outline, script, copy, title, description", "docs/content/", "performance data interpretation"),
        ("material", "Cover, screenshots, asset checklist, generation prompts", "assets/, docs/materials/", "strategy changes"),
        ("review", "Data pull, performance review, lessons, feedback to topic/content", "docs/reviews/", "content implementation"),
    ],
}


def registry_table(profile: str) -> str:
    rows = [
        "| Agent | Thread ID | Role | Allowed paths | Forbidden paths | Workspace/log |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for name, role, allowed, forbidden in PROFILE_ROLES[profile]:
        rows.append(
            f"| {name} |  | {role} | {allowed} | {forbidden} | docs/agent-logs/{name}.md |"
        )
    return "\n".join(rows)


def agents_md(project_name: str, profile: str, today: str) -> str:
    roles = "\n".join(
        f"### {name}\n\n- Owns: {role}\n- Allowed paths: {allowed}\n- Does not own: {forbidden}\n"
        for name, role, allowed, forbidden in PROFILE_ROLES[profile]
    )
    return f"""# Agent Collaboration Rules

Project: {project_name}
Updated: {today}
Profile: {profile}

## Operating Principles

- Read current project files and git state before acting.
- Use the smallest team that preserves ownership and validation.
- The coordinator dispatches, collects, validates, and reports.
- Specialist agents own specialist judgments.
- Every non-trivial handoff must include task ID, scope, allowed paths, forbidden paths, acceptance criteria, and required evidence.
- Failed validation goes back to the responsible agent.
- Do not commit, push, deploy, or publish unless the user explicitly asks.

## Agents

{roles}
## Standard Loop

1. Manager writes the task brief and acceptance criteria.
2. Executor performs only the scoped work.
3. Validator checks the result independently.
4. If validation fails, return concrete failures to the executor.
5. Coordinator reports the path, evidence, risks, and remaining work.
"""


def registry_md(profile: str, today: str) -> str:
    return f"""# Agent Registry

Updated: {today}

## Rules

- Fill in thread IDs as agents are created.
- Keep role boundaries current.
- Store worklogs in `docs/agent-logs/`.
- Use handoff records for cross-agent messages.

## Agents

{registry_table(profile)}
"""


HANDOFF_TEMPLATE = """# Agent Handoff

task_id: PROJECT-YYYYMMDD-001
status: ready
from: manager
to: executor
source_thread_id:
target_thread_id:

## Objective

One-sentence outcome.

## Background

Only the context needed for this agent.

## Scope

- Do:
- Do not:

## Allowed Paths

-

## Forbidden Paths

-

## Acceptance Criteria

1.
2.

## Required Evidence

-

## Return To

Send completion evidence to `{next_agent}`. If blocked, send a blocker report to the coordinator.
"""


WORKLOG_TEMPLATE = """# Agent Worklog

## YYYY-MM-DD

### task_id

- Input:
- Action:
- Output:
- Evidence:
- Next:
"""


RETRO_TEMPLATE = """# Agent Retrospective

## task_id

### What passed

-

### What failed

-

### Responsibility chain

-

### Rule or template to update

-
"""


def write_file(path: Path, content: str, force: bool) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        return f"skipped existing {path}"
    path.write_text(content, encoding="utf-8", newline="\n")
    return f"wrote {path}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Create multi-agent coordination docs.")
    parser.add_argument("project_path", help="Target project directory")
    parser.add_argument("--profile", choices=sorted(PROFILE_ROLES), default="generic")
    parser.add_argument("--project-name", default=None)
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    root = Path(args.project_path).expanduser().resolve()
    project_name = args.project_name or root.name
    today = dt.date.today().isoformat()

    outputs = {
        root / "AGENTS.md": agents_md(project_name, args.profile, today),
        root / "AGENT_REGISTRY.md": registry_md(args.profile, today),
        root / "docs" / "agent-handoff-template.md": HANDOFF_TEMPLATE,
        root / "docs" / "agent-worklog-template.md": WORKLOG_TEMPLATE,
        root / "docs" / "agent-retrospective-template.md": RETRO_TEMPLATE,
    }

    for path, content in outputs.items():
        print(write_file(path, content, args.force))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
