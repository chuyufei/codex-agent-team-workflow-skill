# Templates

## Collaboration Mechanism Proposal

Use this before creating threads or applying a profile.

```markdown
# Collaboration Mechanism Proposal

## User Request

{one_paragraph_summary}

## Recommended Shape

- Use multi-agent workflow: yes | no
- Reason:
- Proposed profile: generic | web-static | content-team | custom | none
- Why this profile is only a starting point:

## Proposed Agents

| Agent | Owns | Input | Output | Allowed paths | Forbidden paths | Validation gate |
| --- | --- | --- | --- | --- | --- | --- |
| manager | requirements, scope, acceptance criteria | user request | task brief | docs/, coordination files | production implementation | user confirms scope |
| executor | scoped work | manager brief | changed files or artifact | assigned files | out-of-scope files | evidence ready for validator |
| validator | independent check | brief and executor evidence | pass/fail report | tests, reports, screenshots | implementation unless asked | criteria pass |

## Please Confirm

Reply with approval or changes before I create threads, dispatch agents, or generate coordination files.
```

## Agent Registry

```markdown
# Agent Registry

Updated: YYYY-MM-DD

## Rules

- Current project files and live state are authoritative.
- The coordinator dispatches, collects, validates, and reports.
- Specialist agents own specialist judgments.
- No agent edits outside its allowed paths without a new handoff.
- Release actions require explicit user approval.
- Profiles are starting points; confirmed project boundaries override default templates.

## Agents

| Agent | Thread ID | Role | Allowed paths | Forbidden paths | Workspace/log |
| --- | --- | --- | --- | --- | --- |
| manager |  | Direction, briefs, acceptance criteria | docs/, AGENTS.md | production implementation | docs/agent-logs/manager.md |
| executor |  | Implementation or artifact production | assigned files | out-of-scope files | docs/agent-logs/executor.md |
| validator |  | Independent validation | tests, reports, screenshots | implementation unless asked | docs/agent-logs/validator.md |
```

## Initialization Prompt

```text
You are the {agent_name} agent for this project.

Role:
{role}

You own:
{owned_decisions}

You do not own:
{forbidden_decisions}

Allowed paths:
{allowed_paths}

Forbidden paths:
{forbidden_paths}

Required output for every task:
1. What you did
2. Files or artifacts touched
3. Evidence or validation
4. Risks or unresolved questions
5. Next agent, if any

Do not expand scope. If the task conflicts with your role boundary, report it to the coordinator.
```

## Handoff Message

```markdown
# Agent Handoff

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

- path/or/module

## Forbidden Paths

- path/or/module

## Acceptance Criteria

1. Criterion with observable evidence.
2. Criterion with observable evidence.

## Required Evidence

- command output, screenshot, diff summary, generated file, or written conclusion

## Return To

Send completion evidence to `{next_agent}`. If blocked, send a blocker report to the coordinator.
```

## Completion Report

```markdown
# Agent Completion

task_id: PROJECT-YYYYMMDD-001
from: executor
to: validator
status: ready_for_validation

## Completed Work

-

## Files/Artifacts

-

## Validation Performed

-

## Known Risks

-

## Validation Request

Please validate against the acceptance criteria from the original handoff.
```

## Validator Report

```markdown
# Validator Report

task_id: PROJECT-YYYYMMDD-001
from: validator
to: coordinator
status: pass | fail | blocked

## Result

Pass/fail summary.

## Evidence

-

## Failures

1. Concrete failing item, reproduction, and expected behavior.

## Send Back To Executor

Use this section verbatim when returning the task for repair.
```

## Worklog

```markdown
# Agent Worklog

## YYYY-MM-DD

### task_id

- Input:
- Action:
- Output:
- Evidence:
- Next:
```
