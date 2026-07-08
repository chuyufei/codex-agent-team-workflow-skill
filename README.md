# Codex Agent Team Workflow Skill / Codex 多 Agent 协作流程

Reusable Codex Skill for organizing multiple Codex threads or subagents into a traceable agent team.

这个 Skill 用来把复杂任务拆成可追踪、可交接、可验证的协作流程：明确职责、交接消息、工作日志、证据和验证闭环。适用于项目开发、产品迭代、内容运营、设计预览、数据工作、测试、文档和发布协调。

## What This Is For / 适用场景

- Starting a new project with clear planning, execution, and validation roles.
- Iterating an existing codebase without mixing product, data, UI, implementation, and release decisions.
- Running design previews before editing production files.
- Keeping data facts, implementation, review, and publishing under separate ownership.
- Turning repeated project conversations into durable project memory.

## First Step / 使用前先确认

接到用户需求后，先不要被固定 profile 绑住。应先拆解这个项目真正需要的协作机制，并向用户确认：

- 任务是否值得多 Agent 协作，还是单线程更简单。
- 需要哪些责任边界，例如产品、设计、数据、代码、验证、文档或发布。
- 每个 Agent 的输入、输出、允许路径、禁止路径和验收标准。
- 采用 `generic`、`web-static`、`content-team`，还是按项目定制更小的组合。

After receiving a request, decompose the collaboration mechanism first and ask the user to confirm it. Profiles are starting points, not constraints.

## Repository Layout / 仓库结构

```text
skills/codex-agent-team-workflow/     Codex Skill package / Skill 包
docs/USAGE.md                         Usage workflow / 使用流程
docs/中文说明.md                      Chinese overview / 中文说明
docs/EXAMPLE_PROJECT_SETUP.md         Example team setups / 示例
scripts/prepublish_check.py           Pre-publish safety check / 发布前检查
```

## Install / 安装

Copy the skill folder into your local Codex skills directory:

```powershell
Copy-Item -Recurse .\skills\codex-agent-team-workflow "$env:USERPROFILE\.codex\skills\codex-agent-team-workflow"
```

Restart Codex, then invoke it with:

```text
Use $codex-agent-team-workflow to set up a multi-agent workflow for this project.
```

## Generate Project Coordination Files / 生成协作文件

From this repository checkout:

```powershell
python .\skills\codex-agent-team-workflow\scripts\bootstrap_agent_docs.py "<project-path>" --profile generic
```

Generate Chinese templates:

```powershell
python .\skills\codex-agent-team-workflow\scripts\bootstrap_agent_docs.py "<project-path>" --profile generic --language zh
```

From an installed Codex skill:

```powershell
python "$env:USERPROFILE\.codex\skills\codex-agent-team-workflow\scripts\bootstrap_agent_docs.py" "<project-path>" --profile generic --language zh
```

Available profiles:

- `generic`: manager, executor, validator.
- `web-static`: product/design/preview/code/data/assets/research/release/docs split for static or frontend-heavy projects.
- `content-team`: topic/content/material/data-review split for media or content operations.

Profiles are optional shortcuts. If the user's project needs a different split, write the custom mechanism first and confirm it before generating or editing coordination files.

The script does not overwrite existing files unless `--force` is passed.

## Capability Boundary / 能力边界

This Skill defines a workflow and durable templates. It does not guarantee that every Codex surface can create, list, rename, read, or message separate threads.

When thread-management tools are available, use them for agent setup and handoff. When they are not available, use the same `AGENT_REGISTRY.md` and handoff templates manually by copying messages between threads.

## Core Principles / 核心原则

- Split context to reduce contamination.
- Split responsibilities so one agent is not both player and referee.
- Register each agent with a name, role, thread ID, workspace, and worklog.
- Use standard handoff messages for traceability.
- Keep evidence: changed files, command output, screenshots, reports, or written conclusions.
- Send failed validation back to the responsible agent.
- Keep release actions behind explicit human approval.

## Publish Checklist / 发布检查

Before publishing or packaging this repository:

```powershell
python .\scripts\prepublish_check.py
```

Also confirm:

- Run the bootstrap script once with at least one profile and once with `--language zh`.
- Check that `SKILL.md` frontmatter contains only `name` and `description`.
- Confirm `agents/openai.yaml` matches the Skill.
- Confirm no local paths, private thread IDs, tokens, API keys, or temporary output files are tracked.
- Do not package local `tmp/`, `.agents/`, `.codex/`, or `__pycache__/` directories.
