# Agent Notes Kit

A small, portable workflow for preserving engineering decisions in coding-agent repositories. It packages one reusable Skill, project-level Notes rules, lifecycle templates, a format checker, and a GitHub Actions gate.

Agent Notes are durable decision records, not chat transcripts, requirements indexes, or per-task activity logs. The Skill does not create a Note after every change and does not depend on an automatic RAG service; it searches the repository's own Notes when relevant.

The kit keeps one self-contained `agent-notes` Skill and integrates the Note-specific parts of broader development workflows: simplification audits can surface Capture candidates, substantive reviews can use Retrieve, and Note-writing rules preserve rationale and contracts. It does not require separate audit, review, or prose Skills to be installed.

## Ask an agent to apply this repository

Paste this repository URL into the agent working in the target project:

```text
Use https://github.com/fish5257/agent-notes-kit as the source. Read its APPLY.md and apply the project layer to the current repository. Inspect existing AGENTS.md and Notes first, merge without overwriting existing rules or records, do not create a Note during setup, and run the provided format checker. Report the files added or merged and any conflicts.
```

`APPLY.md` is the agent-facing installation procedure. It distinguishes project setup from global Skill installation and tells the agent to preserve the target worktree.

## Quick start

Clone the kit:

```sh
git clone https://github.com/fish5257/agent-notes-kit.git
```

To use it in a project, merge these paths into the target repository rather than replacing existing files:

- `.agents/skills/agent-notes/` — reusable Capture, Finalize, Retrieve, and Maintain workflow.
- `.agents/notes/` — local governance, templates, and format checker. Keep the target project's existing Notes.
- `AGENTS.md` — merge its conditional Note workflow rules into the project's existing instructions.

To install the Skill for Codex globally, copy `.agents/skills/agent-notes/` to `~/.codex/skills/agent-notes/`. Keep decision Notes in each project so they stay close to the code and its current constraints.

Merge the applicable conditional routing bullets from this repository's root `AGENTS.md` into the target project's root `AGENTS.md`. Preserve the target's existing rules; the Note workflow does not require the target to install other Skills.

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

这是给代码智能体仓库使用的工程决策记录工具包，包含一个通用 `agent-notes` Skill、项目侧 Notes 规则、状态模板、格式校验器和 GitHub Actions 校验门禁。它把其他开发工作流中与 Note 有关的部分整合进这一个 Skill：简化审计可以提供 Capture 候选，实质性审查前可执行 Retrieve，Note 写作规则保留理由和契约。无需另外安装审计、审查或文案 Skill。

Note 只记录代码、测试和现有文档无法充分表达、且未来维护仍有价值的决策理由。它不是聊天记录、需求索引或每个任务的流水账。每次新增只检查相关主题的旧 Note，不顺带清理整个知识库。

四种操作分别是：Capture（捕获长期决策）、Finalize（实现和验证后将提案改写成已交付事实）、Retrieve（设计/审查前检索相关决定）、Maintain（检查取代、归档或淘汰）。普通修复和局部 UI 调整不需要创建 Note。

在项目中安装时，合并 `.agents/skills/agent-notes/` 和 `.agents/notes/`，保留目标项目已有规则与 Notes；再把仓库根目录 `AGENTS.md` 中适用的条件触发规则合并进目标项目的根 `AGENTS.md`。Codex 全局安装只放 Skill，决策 Note 仍应保存在各自项目里。

运行 `python3 .agents/notes/verify_format.py` 检查活跃 Note 的状态与格式。这个脚本不判断决策是否正确，也不替代 Agent 的同主题查重和 supersession 审查。

## Upstream references and license

This kit adapts selected ideas from the public [DeepSeek Harness Agent Note workflow](https://github.com/deepseek-ai/deepseek-harness/tree/master/.agents/notes) and related Skills:

- [`dsh-archive-agent-notes`](https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/skills/dsh-archive-agent-notes/SKILL.md) — duplicate and supersession checks, plus decision-value-based retention.
- [`dsh-find-simplifications`](https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/skills/dsh-find-simplifications/SKILL.md) — simplification audits as a source of durable decision candidates.
- [`dsh-code-review`](https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/skills/dsh-code-review/SKILL.md) — consulting Agent Notes for design rationale during review.
- [`dsh-prose-standard`](https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/skills/dsh-prose-standard/SKILL.md) — preserving rationale and contracts while keeping Note prose concise.

These links identify design references, not runtime dependencies. This repository is an independent, portable implementation; it does not bundle DeepSeek Harness Skills or runtime code.

Licensed under the MIT License. See [LICENSE](LICENSE).

### 上游参考

本工具包从公开的 [DeepSeek Harness Agent Note 流程](https://github.com/deepseek-ai/deepseek-harness/tree/master/.agents/notes) 及相关 Skill 中吸收了部分设计思路：

- [`dsh-archive-agent-notes`](https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/skills/dsh-archive-agent-notes/SKILL.md)：决策去重、取代关系检查和按长期价值维护记录。
- [`dsh-find-simplifications`](https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/skills/dsh-find-simplifications/SKILL.md)：简化审计可作为发现长期决策候选的入口。
- [`dsh-code-review`](https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/skills/dsh-code-review/SKILL.md)：审查时查阅 Agent Notes 中的设计理由。
- [`dsh-prose-standard`](https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/skills/dsh-prose-standard/SKILL.md)：保留理由和契约，同时让 Note 文字简洁。

这些链接用于标注设计参考，不是运行依赖。本仓库提供独立、可移植的实现，不包含 DeepSeek Harness 的 Skill 文件或运行时代码。
