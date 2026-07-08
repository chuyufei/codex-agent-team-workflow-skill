# Usage Workflow / 使用流程

## 1. Confirm The Collaboration Mechanism / 先确认协作机制

Before creating agents or applying a profile, read the user's request and propose the smallest useful coordination plan.

在创建 Agent 或套用 profile 之前，先根据用户需求拆解协作机制，并请用户确认：

- 这件事是否真的需要多 Agent，还是单线程直接完成更好。
- 哪些责任边界必须拆开，例如需求、设计、数据、实现、验证、文档、发布。
- 每个 Agent 的输入、输出、允许路径、禁止路径和验收标准。
- 是否使用现有 profile，或为当前项目定制更小、更准确的组合。

Profiles are shortcuts, not rules. Do not force `generic`, `web-static`, or `content-team` if the project needs a different split.

## 2. Decide Whether Multi-Agent Coordination Is Worth It / 判断是否值得多 Agent

Use this workflow when:

- The task spans product, design, data, code, testing, docs, or release.
- The work needs independent validation.
- The project will keep evolving over time.
- You need a traceable responsibility chain and durable project memory.

Keep the workflow simple when:

- The task is a small one-file fix.
- The request is only an explanation.
- A single command or direct edit is enough.

## 3. Start With Three Agents / 默认三 Agent 起步

```text
Manager agent: direction, requirements, task brief, acceptance criteria
Executor agent: scoped implementation or artifact production
Validator agent: independent checking against acceptance criteria
```

Do not create many agents at the start. Add design, data, assets, release, docs, or research agents only after those boundaries become real in the project.

## 4. Bootstrap Coordination Files / 生成协作文件

From a repository checkout:

```powershell
python .\skills\codex-agent-team-workflow\scripts\bootstrap_agent_docs.py "<project-path>" --profile generic
```

Generate Chinese templates:

```powershell
python .\skills\codex-agent-team-workflow\scripts\bootstrap_agent_docs.py "<project-path>" --profile generic --language zh
```

From an installed local skill:

```powershell
python "$env:USERPROFILE\.codex\skills\codex-agent-team-workflow\scripts\bootstrap_agent_docs.py" "<project-path>" --profile generic --language zh
```

The script creates:

- `AGENTS.md`
- `AGENT_REGISTRY.md`
- `docs/agent-handoff-template.md`
- `docs/agent-worklog-template.md`
- `docs/agent-retrospective-template.md`

## 5. Maintain The Agent Registry / 维护 Agent 注册表

In `AGENT_REGISTRY.md`, record:

- agent name
- thread ID when available
- role
- allowed paths
- forbidden paths
- workspace or worklog path

If the current Codex environment supports thread tools, use those tools to create, rename, read, and message threads. If it does not, use the same handoff template manually.

## 6. Use Standard Handoff Messages / 使用标准交接消息

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

## 7. Run The Loop / 执行闭环

```text
Manager writes the brief
-> Executor produces the work
-> Validator checks the work
-> Failed items return to Executor
-> Passing work returns to Coordinator for final report
```

The coordinator dispatches, collects, validates, and reports. It should not replace specialist ownership when specialist judgment is required.

## 8. Preserve Lessons / 沉淀经验

At the end of each meaningful task, record:

- what was done
- which files or artifacts changed
- what evidence proves the result
- which failures required rework
- which rule or template should be updated

For long-running projects, durable files are more reliable than chat memory alone.
