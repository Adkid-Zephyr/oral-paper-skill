# Oral Paper Skill · 向优秀论文学习

**我蒸馏了 883 篇顶会 Oral 论文，提炼出其中的共性和值得学习的做法，帮助你应用到自己的 idea 和论文中。**

[English README](README_EN.md) · [完整 Skill](skills/oral-paper-skill/SKILL.md) · [中文提示词](prompts/精简版提示词.txt) · [提炼过程](research/abstract_distillation/RESULTS.md)

[![Oral papers: 883](https://img.shields.io/badge/Oral%20papers-883-blue)](skills/oral-paper-skill/references/oral-patterns.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Adkid-Zephyr/oral-paper-skill/pulls)

已完成摘要层 AI 提炼、来源核查和跨论文综合，整理出 **7 项可选择的做法与 14 个原文核实实例**。这里的“蒸馏”是知识提炼，不是模型训练，也不是 883 篇全文精读。

## 为什么做这个 Skill

我认为，Oral paper 能成为 Oral paper，肯定有值得研究和学习的原因。如果想更快地理解怎样做出、写出一篇好论文，优秀论文就是很直接的学习材料。

接受系统科研训练的第一步，往往是看经典文章。会议往届的 Oral，以及其他有质量、有含金量的论文，也是常用的范例。

想投 ICLR，就看 ICLR 往届的优秀论文；想投 ICML、NeurIPS，也做同样的事。从中找灵感，把 A 的方法接到 B 的场景里，或者做局部优化，再写成一篇新的 paper。

很多人通过这条路发出了论文。但如果最后只学会了 A+B 和局部加点，这样的学习到底留下了什么？组合与改进当然可以有价值，关键是我们有没有理解问题为什么重要、创新为什么成立、证据又如何支持结论。

有了 AI，我觉得这个过程可以更系统：快速整理和比较优秀论文，提炼有用的共性，再把这些做法 apply 到自己的 idea 里，帮助自己学习科研和论文写作。

上次分享 `anti-defensive-writing` Skill 的视频给我涨了几百粉，之后我一直在想该分享什么。我自己积累、私藏了不少好用的 Skill，这次把 Oral Paper Skill 作为这个系列的第二个项目公开。

**我的目标是，把 ICLR、ICML、NeurIPS 近两个已完成周期的官方 Oral 条目及相关优秀论文作为学习材料，经过提取、比较和融会贯通，形成一套可以反复使用的方法。**

这里的“蒸馏”指知识提炼：从论文中整理具体做法、适用条件和例子，写成 Skill。这轮从摘要逐篇提取，再比较、核查与综合；涉及正文或图表的建议，需要另外阅读对应材料。

## 它帮你做两件事

### 1. 对照优秀论文，找到可改进的地方

根据你的问题和论文类型，选择合适的范例，解释它怎样表达贡献、组织证据，再指出你的稿件可以怎样修改。

每条重要建议尽量包含：**原论文做法与出处 → 为什么与你相关 → 你的稿件现状 → 具体改法。**

例如，面对一篇主张降低计算成本的稿件，可以检查它是否给出了相同质量下的端到端成本比较。这是建议形式的示意；实际归因给某篇论文时，需要读取对应原文。

### 2. 学习优秀做法，指导自己的复盘

把值得学习的做法讲清楚：引言怎样推进、创新点怎样与前作区分、主图怎样呈现贡献、关键实验怎样排除其他解释。

同时解释适用条件，帮助你判断自己的工作是否需要采用，而不是把每篇论文改成同一模板。

## 从这些论文里，具体学什么

- **写清研究张力：** 哪个具体限制或现象，让这个问题值得研究？
- **明确贡献增量：** 去掉方法名和“novel”，到底改变了什么？
- **让证据对应主张：** 测到的属性，是否就是标题声称的能力？
- **选择有解释力的比较：** 比较要回答什么，哪些条件相同、哪些不同？
- **结论紧随适用条件：** 哪个模型类别、量词或实验范围不能省略？
- **说明资源支持的研究：** 数据、环境或接口，具体让别人能做什么？
- **提炼有边界的认识：** 除了分数，读者能带走什么，何时不适用？

每项都有论文实例、具体用法和例外，见[七项做法与来源](skills/oral-paper-skill/references/abstract-derived-practices.md)。默认只选与你的工作相关的做法，给三条以内的改进建议或一个复盘练习。

原来的 ORAL 四个问题可以继续作为记忆辅助，但不是全体论文的共同定律，也不是评分表。方法、理论、经验发现、系统、资源和立场论文，不必通过同一套门槛。

## 快速开始

### 复制提示词

复制[中文提示词](prompts/精简版提示词.txt)或[English prompt](prompts/quick-prompt-en.txt)，然后提供你的 idea、稿件或实验计划。提示词本身无需额外依赖；检索和读取参考论文取决于所用 AI 工具的能力。

### 安装 Skill

```bash
git clone https://github.com/Adkid-Zephyr/oral-paper-skill.git
```

将仓库里的 `skills/oral-paper-skill` 目录放入工具的 skills 目录，例如 `~/.codex/skills/` 或 `~/.claude/skills/`。已有同名版本时先比较内容，避免覆盖自己的修改。

对照改进：

```text
使用 $oral-paper-skill 对照适合我这篇工作的优秀论文，
指出最值得改进的三处。给出出处、适用原因和具体修改建议。
```

学习复盘：

```text
使用 $oral-paper-skill，讲解这些参考论文在叙事和实验设计上
值得学习的做法，并帮助我用自己的论文做一次复盘。
```

## 这 883 篇论文来自哪里

2026-09-13 重新核对六个官方名单：

| 会议周期 | Oral 论文数 |
|---|---:|
| ICLR 2025–2026 | 436 |
| ICML 2025–2026 | 288 |
| NeurIPS 2024–2025 | 159 |
| 合计 | 883 |

统计已排除 [workshop 活动](https://icml.cc/virtual/2026/workshop/54094)等非论文条目。这 883 篇论文的摘要均已形成逐篇语义记录，并完成 21 组综合，最终筛选出七项做法。

Luna 负责批量提取，Astra medium 负责来源核查与筛选，Astra xhigh 负责最终综合。原文检查包括 24 篇校准、36 篇固定随机抽查，以及发现疑点后的定向复核；不是人工精读全库，也不意味着全部科学结论已经验证。

[逐篇记录](research/abstract_distillation/cards) · [过程、错误与修正](research/abstract_distillation/RESULTS.md) · [来源与阅读层级](skills/oral-paper-skill/references/oral-patterns.md)

## 怎么理解它的建议

Oral 身份用于选择学习范例；本工具不代表会议官方标准，也不保证录取。摘要只能支持问题表达和作者声称的贡献分析；图表设计、实验细节和证明需要对应全文。

使用效果尚未经过独立对照评测。欢迎提交有原文出处的案例、纠错和真实改稿反馈。

## 论文 Skill 系列

[Anti-Defensive Writing](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)：改进论文表达。

Oral Paper Skill：借助优秀论文，获得对照建议并学习复盘。
