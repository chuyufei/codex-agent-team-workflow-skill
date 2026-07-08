# Workflow Principles

These principles should be preserved when adapting the workflow to a specific project.

## Long-lived threads can become agents

A Codex conversation can be treated as a durable agent when it has:

- a stable name
- a role boundary
- a thread ID when available
- a log
- a workspace or output area
- a known communication path

The value is accumulated context and continuity, not roleplay.

## Register agents before delegating

Maintain an agent registry like a team address book. Store each agent's name, responsibility, thread ID when available, and workspace. Message delivery is easier when the coordinator can say "send this to the development agent" instead of rediscovering thread IDs.

## Confirm the mechanism before expanding the team

Start by decomposing the user's request into ownership surfaces, evidence needs, validation gates, and handoff points. Then ask the user to confirm the proposed collaboration mechanism before creating threads or generating files, unless they explicitly requested an immediate bootstrap.

Built-in profiles are starter templates. They should not prevent a better task-specific topology for SaaS work, data analysis, GitHub PRs, content publishing, or other specialized workflows.

## Use a standard message format

Free-form chat creates ambiguity. Handoffs should follow a reusable format so messages are traceable, comparable, and easy to audit.

## Let agents communicate, but keep evidence

The coordinator does not need to inspect every intermediate artifact, but the system must keep worklogs, handoff records, and output paths so later debugging can reconstruct what happened.

## Build a loop, not a one-way chain

The core loop is:

```text
planner -> executor -> validator -> executor repair -> validator re-check
```

Continue until the version matches the planned expectations or a blocker is explicit.

## Split work to reduce context pollution

Separate agents because each thread should focus on a domain: planning, implementation, validation, topic selection, content creation, material production, data review, release, documentation, etc. The split keeps irrelevant context from contaminating the judgment of another role.

## Run the pipeline asynchronously when possible

Some tasks are slow, such as asset generation, data review, or implementation. Splitting agents lets one workstream continue while another waits for output.

## Start with three agents when unsure

If the right team shape is unclear, start with:

1. Management/planning
2. Execution
3. Validation/testing

Add specialized agents only after the project proves a repeated boundary.

## Avoid fake specialization

Do not claim the model becomes better at writing or coding merely because it is called a writer or developer. The useful part is ownership, context isolation, validation, and traceability.
