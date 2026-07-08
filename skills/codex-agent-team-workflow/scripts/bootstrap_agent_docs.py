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


ZH_PROFILE_ROLES = {
    "generic": [
        ("manager", "方向、需求、任务 brief、验收标准", "docs/, AGENTS.md, AGENT_REGISTRY.md", "实现文件"),
        ("executor", "按限定范围实现或产出交付物", "被分配的文件", "范围外文件"),
        ("validator", "按验收标准独立验证", "测试、报告、截图、评审记录", "实现工作，除非明确分配"),
    ],
    "web-static": [
        ("manager", "派发、收集、验证、汇报", "docs/, AGENTS.md, AGENT_REGISTRY.md", "专家最终判断"),
        ("design", "UX 结构、视觉层级、交互 brief", "design-previews/, docs/design-notes.md", "生产代码"),
        ("preview", "静态预览和截图", "design-previews/", "site/ 生产文件"),
        ("code", "生产实现和本地测试", "site/, tools/", "数据源变更，除非明确分配"),
        ("data", "数据生成、结构、审计、数据事实", "数据脚本、生成数据、数据文档", "UI 和样式"),
        ("assets", "图片、轮播、压缩、素材引用", "assets/", "搜索、数据、渲染逻辑"),
        ("research", "外部参考研究和实现 brief", "docs/research/", "当前项目文件"),
        ("release", "git 状态、diff 检查、用户批准后的提交和推送", "仓库元数据", "未经批准的发布动作"),
        ("docs", "项目记忆、变更记录、handoff 一致性", "Markdown 文档", "生产代码，除非明确分配"),
    ],
    "content-team": [
        ("manager", "方向、排期、优先级、验收标准", "docs/, AGENTS.md, AGENT_REGISTRY.md", "内容生产"),
        ("topic", "选题规划和会议记录", "docs/topics/", "最终发布"),
        ("content", "大纲、脚本、文案、标题、描述", "docs/content/", "表现数据解释"),
        ("material", "封面、截图、素材清单、生成提示词", "assets/, docs/materials/", "策略变更"),
        ("review", "数据拉取、表现复盘、经验、反馈给 topic/content", "docs/reviews/", "内容实现"),
    ],
}


def profile_roles(profile: str, language: str):
    if language == "zh":
        return ZH_PROFILE_ROLES[profile]
    return PROFILE_ROLES[profile]


def registry_table(profile: str, language: str) -> str:
    if language == "zh":
        rows = [
            "| Agent | Thread ID | 职责 | 允许路径 | 禁止路径 | 工作区/日志 |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    else:
        rows = [
            "| Agent | Thread ID | Role | Allowed paths | Forbidden paths | Workspace/log |",
            "| --- | --- | --- | --- | --- | --- |",
        ]

    for name, role, allowed, forbidden in profile_roles(profile, language):
        rows.append(f"| {name} |  | {role} | {allowed} | {forbidden} | docs/agent-logs/{name}.md |")
    return "\n".join(rows)


def agents_md(project_name: str, profile: str, today: str, language: str) -> str:
    if language == "zh":
        roles = "\n".join(
            f"### {name}\n\n- 负责：{role}\n- 允许路径：{allowed}\n- 不负责：{forbidden}\n"
            for name, role, allowed, forbidden in profile_roles(profile, language)
        )
        return f"""# Agent 协作规则

项目：{project_name}
更新日期：{today}
Profile：{profile}

## 运行原则

- 先读取当前项目文件和 git 状态，再行动。
- 先拆解协作机制，让用户确认角色、边界和验收方式，再创建 Agent 或生成更多文件。
- 使用能保留职责边界和独立验证的最小团队。
- 协调者负责派发、收集、验证和汇报。
- 专家 Agent 拥有对应领域的判断权。
- 非简单交接必须包含任务 ID、范围、允许路径、禁止路径、验收标准和所需证据。
- 验证失败要回到负责的 Agent 修复。
- 未经用户明确要求，不提交、不推送、不部署、不发布。

## Agents

{roles}
## 标准闭环

1. Manager 写任务 brief 和验收标准。
2. Executor 只执行被限定的工作。
3. Validator 独立检查结果。
4. 如果验证失败，把具体失败项退回 executor。
5. Coordinator 汇报路径、证据、风险和剩余工作。
"""

    roles = "\n".join(
        f"### {name}\n\n- Owns: {role}\n- Allowed paths: {allowed}\n- Does not own: {forbidden}\n"
        for name, role, allowed, forbidden in profile_roles(profile, language)
    )
    return f"""# Agent Collaboration Rules

Project: {project_name}
Updated: {today}
Profile: {profile}

## Operating Principles

- Read current project files and git state before acting.
- Break down the collaboration mechanism and ask the user to confirm roles, boundaries, and validation before creating agents or generating more files.
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


def registry_md(profile: str, today: str, language: str) -> str:
    if language == "zh":
        return f"""# Agent 注册表

更新日期：{today}

## 规则

- 创建 Agent 后填入 thread ID。
- 保持角色边界更新。
- 工作日志存放在 `docs/agent-logs/`。
- 跨 Agent 交接使用 handoff 记录。
- Profile 只是起点模板；真实协作机制应按用户需求拆解后确认。

## Agents

{registry_table(profile, language)}
"""

    return f"""# Agent Registry

Updated: {today}

## Rules

- Fill in thread IDs as agents are created.
- Keep role boundaries current.
- Store worklogs in `docs/agent-logs/`.
- Use handoff records for cross-agent messages.
- Profiles are starter templates; confirm the actual collaboration mechanism from the user's request.

## Agents

{registry_table(profile, language)}
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


HANDOFF_TEMPLATE_ZH = """# Agent Handoff

task_id: PROJECT-YYYYMMDD-001
status: ready
from: manager
to: executor
source_thread_id:
target_thread_id:

## 目标

一句话说明要达成的结果。

## 背景

只写当前 Agent 需要知道的上下文。

## 范围

- 做：
- 不做：

## 允许路径

-

## 禁止路径

-

## 验收标准

1.
2.

## 所需证据

-

## 返回给谁

完成后把证据发送给 `{next_agent}`。如果被阻塞，向 coordinator 发送 blocker 报告。
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


WORKLOG_TEMPLATE_ZH = """# Agent 工作日志

## YYYY-MM-DD

### task_id

- 输入：
- 行动：
- 输出：
- 证据：
- 下一步：
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


RETRO_TEMPLATE_ZH = """# Agent 复盘

## task_id

### 通过项

-

### 失败项

-

### 责任链

-

### 需要更新的规则或模板

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
    parser.add_argument("--language", choices=("en", "zh"), default="en")
    parser.add_argument("--project-name", default=None)
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    root = Path(args.project_path).expanduser().resolve()
    project_name = args.project_name or root.name
    today = dt.date.today().isoformat()

    outputs = {
        root / "AGENTS.md": agents_md(project_name, args.profile, today, args.language),
        root / "AGENT_REGISTRY.md": registry_md(args.profile, today, args.language),
        root / "docs" / "agent-handoff-template.md": HANDOFF_TEMPLATE_ZH if args.language == "zh" else HANDOFF_TEMPLATE,
        root / "docs" / "agent-worklog-template.md": WORKLOG_TEMPLATE_ZH if args.language == "zh" else WORKLOG_TEMPLATE,
        root / "docs" / "agent-retrospective-template.md": RETRO_TEMPLATE_ZH if args.language == "zh" else RETRO_TEMPLATE,
    }

    for path, content in outputs.items():
        print(write_file(path, content, args.force))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
