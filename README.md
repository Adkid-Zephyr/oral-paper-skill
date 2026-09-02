# Oral Paper Skill · 顶会论文校准

**别再只从 Oral 里抄 A+B —— 把 884 篇 ICLR、ICML、NeurIPS 官方 Oral 蒸馏成一个 AI 科研 Skill，校准你的 idea、claim、Figure 1 和实验。**

[English README](README_EN.md) · [完整 Skill](skills/oral-paper-skill/SKILL.md) · [精简版提示词](prompts/精简版提示词.txt)

[![Corpus: 884 Orals](https://img.shields.io/badge/corpus-884%20official%20Orals-blue)](skills/oral-paper-skill/references/oral-patterns.md)
[![Dependencies: Zero](https://img.shields.io/badge/dependencies-zero-brightgreen)](skills/oral-paper-skill/SKILL.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/Adkid-Zephyr/oral-paper-skill/pulls)

---

## 这是什么

很多人接受科研训练的第一步，是读经典论文。

想投 ICLR，就看 ICLR 往届 Oral；想投 ICML、NeurIPS，也做同样的事。学选题、学方法、学实验，再寻找一个 A+B 或局部优化的机会。

这套方法能发论文，但也很容易只学到优秀论文的表面：**换一个模块、加一个场景、多跑几个 benchmark，却始终说不清这篇论文为什么值得存在。**

这叫**表面模仿（Surface Imitation）**。

解法不是让 AI 再拼一篇 A+B，而是让它学习 Oral paper 背后的研究判断：

> **学 Oral，不是抄它做了什么。**
> **是学它为什么值得整篇论文押注，以及它如何让这个主张成立。**

`Oral Paper Skill` 会先判断你的工作属于方法、理论、机制研究、系统、Benchmark/Data，还是 Position Paper；然后校准标题、Abstract、Introduction、Figure 1 / 主定理、实验和结论是否在证明同一件事。

## 传统模仿 vs. Oral 校准

| | 传统模仿 Oral | Oral Paper Skill |
|---|---|---|
| 找 idea | 从论文 A 搬方法，接到论文 B 的场景 | 找到一个重要、可证伪、值得整篇论文押注的主张 |
| 写贡献 | Contributions 1、2、3、4 平均陈列 | 所有贡献共同服务一个中心 claim |
| Figure 1 | 画复杂 pipeline，展示做了多少模块 | 尽早展示主张凭什么成立：结果、定理、反例或 Demo |
| 做实验 | 找容易赢的 baseline，继续堆表 | 正面面对最可能让论文失去必要性的解释 |
| 留下什么 | 一个很快过期的 leaderboard 数字 | 一个机制、原则、权衡、边界或新研究对象 |

## ORAL 四条原则

- **O — One irreducible claim**：整篇论文到底在押哪一个重要、可证伪的主张？
- **R — Reader-visible proof**：读者能否很早看到它凭什么成立？
- **A — Adversarial evidence**：证据是否面对最强的替代解释，而不是最弱的 baseline？
- **L — Lasting lesson**：榜单过期后，还剩下什么值得领域记住？

Skill 默认只给出五样东西：**Story、Proof carrier、Survival test、GO / WAIT / KILL、Next action。**

## 快速开始

### 方式一：复制提示词（任何 AI 都能用）

直接复制 [`prompts/精简版提示词.txt`](prompts/精简版提示词.txt)（[English](prompts/quick-prompt-en.txt)），粘贴到对话开头，然后发送你的 idea、论文或实验计划。复制即用，零依赖。

### 方式二：安装 Skill

```bash
git clone https://github.com/Adkid-Zephyr/oral-paper-skill.git

# Codex
cp -R oral-paper-skill/skills/oral-paper-skill ~/.codex/skills/

# Claude Code / 其他支持 Skills 的工具
cp -R oral-paper-skill/skills/oral-paper-skill ~/.claude/skills/
```

之后直接说：

```text
使用 $oral-paper-skill 检查这个 idea。
先告诉我整篇论文应该押什么、凭什么成立，以及哪个实验会决定它的生死。
不要先润色语言。
```

## 为什么不是拍脑袋总结

初始版本覆盖 2026-09-02 时最新完成的六个会议周期：

- ICLR 2025–2026：436 个官方 Oral events；
- ICML 2025–2026：289 个；
- NeurIPS 2024–2025：159 个。

合计结构化扫描 **884 个官方 Oral 条目、883 份可用摘要**，再分层深读方法、理论、机制、系统、Benchmark/Data 和 Position Paper 中的代表性 Oral / Best / Outstanding papers，以及官方评奖委员会公开写下的选择理由。

这不是“读完 884 篇全文”。它是一次全量摘要层扫描 + 跨类型深读。完整语料边界、会议链接和委员会标准见 [`oral-patterns.md`](skills/oral-paper-skill/references/oral-patterns.md)。

一个重要发现是：强论文不等于统一的“大 benchmark + SOTA 数字”模板。理论论文可以靠紧致结果与概念意义，机制论文靠控制实验，系统论文靠端到端 frontier，Position Paper 靠证据化立场和可行动的方向。

## 它不会做什么

- 不把 ORAL 评分包装成录取概率；
- 不为尚未得到的结果画成功曲线；
- 不用写作技巧救活已被简单 baseline 击败的方向；
- 不把 pilot、synthetic cases 或机械检查写成泛化结论；
- 不强迫所有论文使用同一种模板。

## 适用场景

- 从一个 idea 建立 paper spine；
- 重写标题、Abstract 和 Introduction；
- 设计 Figure 1、主定理或核心 Demo；
- 重构实验，让每个实验承担明确的论证责任；
- 投稿前做 `GO / WAIT / KILL` 审查；
- 判断应该补实验、换故事，还是停止一个方向。

## 仓库结构

```text
oral-paper-skill/
├── skills/oral-paper-skill/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
│       ├── archetypes.md
│       ├── oral-patterns.md
│       └── review-scorecard.md
├── prompts/
│   ├── 精简版提示词.txt
│   └── quick-prompt-en.txt
└── README.md / README_EN.md
```

## 论文 Skill 系列

第一篇：[`Anti-Defensive Writing`](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) —— 防止论文把自己写弱。

第二篇：`Oral Paper Skill` —— 判断论文是否有一个值得押注的中心主张，以及证据是否真的能让它成立。

欢迎 PR，也欢迎转发给你的同门。
