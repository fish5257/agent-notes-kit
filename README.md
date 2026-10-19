# Agent Notes Kit

A small, portable workflow for preserving engineering decisions in coding-agent repositories. It packages one reusable Skill, project-level Notes rules, lifecycle templates, a format checker, and a GitHub Actions gate.

Agent Notes are durable decision records, not chat transcripts, requirements indexes, or per-task activity logs. The Skill does not create a Note after every change and does not depend on an automatic RAG service; it searches the repository's own Notes when relevant.

## Quick start

Clone the kit:

```sh
git clone https://github.com/fish5257/agent-notes-kit.git
```

To use it in a project, merge these paths into the target repository rather than replacing existing files:

- `.agents/skills/agent-notes/` — reusable Capture, Finalize, Retrieve, and Maintain workflow.
- `.agents/notes/` — local governance, templates, and format checker. Keep the target project's existing Notes.
- `AGENTS.md` — copy the short Skill trigger into the project's existing instructions.

To install the Skill for Codex globally, copy `.agents/skills/agent-notes/` to `~/.codex/skills/agent-notes/`. Keep decision Notes in each project so they stay close to the code and its current constraints.

Add a trigger like this to the target project's root `AGENTS.md`:

```markdown
- For durable architecture/API/state/persistence/compatibility decisions, use `$agent-notes` to retrieve related Notes before implementation. Only capture/finalize a Note after implementation and relevant verification, and only when the rationale is not already carried by code, tests, or docs. Skip routine fixes and local UI changes.
- When delegating such work, include the `$agent-notes` trigger and the required operation in the assignment.
```

Check active Notes from the target project root:

```sh
python3 .agents/notes/verify_format.py
```

The checker validates lifecycle folders, status lines, and required headings. It cannot judge whether a decision is worth recording or whether its technical rationale is correct. The Skill owns that reasoning.

## Lifecycle

| Operation | Use |
| --- | --- |
| Capture | Record a lasting decision after checking for an existing owner and possible supersession. |
| Finalize | Rewrite a proposal as shipped reality only after implementation and relevant verification. |
| Retrieve | Search relevant Notes before a substantial design, simplification, or review. |
| Maintain | Review full and partial supersession; archive completed decisions only when their rationale no longer guides current work. |

`proposed/`, `implemented/`, and `rejected/` represent active decision states. `archived/` contains frozen historical records and is excluded from the active-format checker.

## 中文说明

这是给代码智能体仓库使用的工程决策记录工具包，包含一个通用 `agent-notes` Skill、项目侧 Notes 规则、状态模板、格式校验器和 GitHub Actions 校验门禁。

Note 只记录代码、测试和现有文档无法充分表达、且未来维护仍有价值的决策理由。它不是聊天记录、需求索引或每个任务的流水账。每次新增只检查相关主题的旧 Note，不顺带清理整个知识库。

四种操作分别是：Capture（捕获长期决策）、Finalize（实现和验证后将提案改写成已交付事实）、Retrieve（设计/审查前检索相关决定）、Maintain（检查取代、归档或淘汰）。普通修复和局部 UI 调整不需要创建 Note。

在项目中安装时，合并 `.agents/skills/agent-notes/` 和 `.agents/notes/`，保留目标项目已有规则与 Notes；再把 README 中的短触发规则合并进项目根 `AGENTS.md`。Codex 全局安装只放 Skill，决策 Note 仍应保存在各自项目里。

运行 `python3 .agents/notes/verify_format.py` 检查活跃 Note 的状态与格式。这个脚本不判断决策是否正确，也不替代 Agent 的同主题查重和 supersession 审查。

## Inspiration and license

The lifecycle is adapted from the public [DeepSeek Harness Agent Note workflow](https://github.com/deepseek-ai/deepseek-harness/tree/master/.agents/notes) and `dsh-archive-agent-notes` Skill. This repository is an independent, portable implementation; it does not include DeepSeek Harness runtime code.

Licensed under the MIT License. See [LICENSE](LICENSE).
