# Oral Paper Skill

**把近两年 ICLR、ICML、NeurIPS Oral / Award papers 的共同研究标准，变成一个可以直接应用到自己论文上的 Skill。**

[English README](README_EN.md) · [Skill](skills/oral-paper-skill/SKILL.md) · [精简版提示词](prompts/精简版提示词.txt)

---

## 这是什么

传统科研训练经常从读经典论文开始。想投某个会议，就去看它往届的 Oral paper：学选题、学方法、学实验、学 Figure 1，再寻找 A+B 或局部优化的机会。

这种训练有效，但也容易只模仿优秀论文的表面。

`Oral Paper Skill` 做的是另一件事：让 AI 先吸收强论文反复体现的研究判断，再把这些判断应用到你的 idea、证据和论文结构中。它不是“顶会写作模板”，也不会承诺录取；它会逼论文回答四个问题：

| | 核心问题 |
|---|---|
| **O — One irreducible claim** | 整篇论文到底在押哪一个重要、可证伪的主张？ |
| **R — Reader-visible proof** | 读者能否很早看到它凭什么成立？ |
| **A — Adversarial evidence** | 证据是否正面面对最可能让论文失去必要性的解释？ |
| **L — Lasting lesson** | 榜单过期后，论文还留下什么机制、原则或边界？ |

## 它从哪里来

初始版本基于 2026-09-02 时最新已完成的六个会议周期：

- ICLR 2025–2026：436 个官方 Oral events；
- ICML 2025–2026：289 个；
- NeurIPS 2024–2025：159 个。

合计结构化扫描 **884 个官方 Oral 条目、883 份可用摘要**，并深读跨类型代表性 Oral / Best / Outstanding papers 与官方评奖委员会的选择说明。

这不是“读完 884 篇全文”，而是一次全量摘要层扫描加分层深读。详细语料边界、会议链接和委员会标准见 [`oral-patterns.md`](skills/oral-paper-skill/references/oral-patterns.md)。

## 它会做什么

Skill 会先判断论文的中心类型：

- 方法或算法；
- 理论或保证；
- 经验科学或机制研究；
- 系统或效率；
- Benchmark 或 Dataset；
- Position Paper。

然后校准标题、核心 claim、Abstract、Introduction、Figure 1 / 主定理、实验结构和结论是否在证明同一件事。它默认只给出 `GO / WAIT / KILL`、核心故事、proof carrier、决定生死的检验和下一步行动。

它不会：

- 把 Oral 风格分数包装成录取概率；
- 为不存在的结果画成功曲线；
- 用写作技巧救活已经被简单 baseline 击败的方向；
- 把 pilot、synthetic cases 或机械检查写成泛化结论；
- 强迫理论、系统和 Benchmark 使用同一种论文模板。

## 快速开始

### Codex

```bash
git clone https://github.com/Adkid-Zephyr/oral-paper-skill.git
cp -R oral-paper-skill/skills/oral-paper-skill ~/.codex/skills/
```

然后直接说：

```text
Use $oral-paper-skill to calibrate this paper's central claim,
proof carrier, evidence, and lasting lesson.
```

### Claude Code / 其他支持 Skills 的工具

```bash
cp -R oral-paper-skill/skills/oral-paper-skill ~/.claude/skills/
```

### 任何 AI

复制 [`prompts/精简版提示词.txt`](prompts/精简版提示词.txt)，放在论文、idea 或实验计划之前。

## 推荐用法

### 从 idea 建立 paper spine

```text
使用 $oral-paper-skill 检查这个 idea。先给出一个中心 claim、合适的 proof carrier，
以及唯一决定它能不能成为论文的实验。不要先润色文字。
```

### 直接改论文

```text
使用 $oral-paper-skill 直接修改这篇论文，让标题、Abstract、Introduction、Figure 1、
主实验和结论围绕同一个 claim。保留真实 evidence boundary。
```

### 投稿前审查

```text
使用 $oral-paper-skill 对当前稿件做 ORAL audit，输出 GO / WAIT / KILL、
最危险的三个缺口，以及决定论文生死的一个补充实验。
```

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
├── README.md
└── README_EN.md
```

## 与 Anti-Defensive Writing 的关系

[`anti-defensive-writing-Skill`](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) 防止论文把自己写弱。

`Oral Paper Skill` 处理更上游的问题：论文是否有一个值得押注的中心主张，以及证据是否真的能让它成立。
