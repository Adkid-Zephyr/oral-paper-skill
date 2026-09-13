# Oral Paper Skill · Learn from Exemplary Papers

**Starting from 884 top-conference Oral entries, extract lessons from 883 abstracts to compare, improve, and reflect on your own paper.**

[中文 README](README.md) · [Full Skill](skills/oral-paper-skill/SKILL.md) · [Quick prompt](prompts/quick-prompt-en.txt) · [Distillation process](research/abstract_distillation/RESULTS.md)

[![Starting index: 884 entries](https://img.shields.io/badge/starting%20index-884%20entries-blue)](skills/oral-paper-skill/references/oral-patterns.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Adkid-Zephyr/oral-paper-skill/pulls)

Abstract-level AI extraction, source checks, and cross-paper synthesis are complete, yielding **seven selectable practices and 14 examples checked against original abstracts**. “Distillation” means knowledge synthesis, not model training or full-text reading of all 883 papers.

## Why I am building this

I believe that papers selected for Oral presentation contain research decisions worth studying. Exemplary papers are a practical starting point for learning how to do and communicate good research.

Research training often begins with classic papers. If you want to submit to ICLR, ICML, or NeurIPS, a traditional approach is to study past papers from that venue, find inspiration, combine method A with setting B, or improve one part of an existing approach.

That path has produced publications. But if all we learn is how to combine components, what have we understood about why the problem matters, what makes the contribution useful, or how the evidence supports it? Combinations and incremental advances can be valuable; understanding that value is the point.

AI can help us organize and compare these examples more systematically, extract useful patterns, and apply them to our own ideas and writing.

After my anti-defensive-writing video brought in a few hundred followers, I kept thinking about what to share next. I have accumulated useful personal Skills; Oral Paper Skill is the second public project in this series.

**The goal is to study Oral entries and other exemplary papers from the latest two completed cycles of ICLR, ICML, and NeurIPS, then turn their useful practices into reusable learning guidance.**

Here, “distillation” means extracting and synthesizing knowledge into instructions and examples. This run extracted abstracts individually, compared their practices, checked sources, and synthesized lessons. Advice depending on full text or figures requires reading that material separately.

## Two uses

### 1. Compare and improve

Choose examples relevant to your problem and contribution type. Explain what they do, why the comparison fits, and which changes could improve your manuscript.

A substantial suggestion should connect: **source practice and locator → relevance → observation about your draft → concrete change.**

For example, a draft claiming lower compute cost may need a comparison of end-to-end cost at matched quality. This illustrates the form of advice; attributing it to a particular paper requires reading that source.

### 2. Learn and reflect

Explain how exemplary papers develop their introduction, distinguish their contribution, present the central figure, and use experiments to address alternative explanations. Include applicability and exceptions, then help authors reflect on their own work.

## What to learn from these papers

- **Specify the research tension:** Which concrete requirement or observation makes the question worth investigating?
- **State the contribution delta:** What changes after removing the method name and “novel”?
- **Match evidence to the claim:** Is the measured property the capability being claimed?
- **Choose a meaningful comparison:** What should it decide, and what stays fixed or changes?
- **Keep conditions beside conclusions:** Which model class, quantifier, or tested regime must remain visible?
- **Explain what the resource enables:** What can researchers do with its data, environment, or interfaces?
- **Extract a bounded lesson:** What can readers take away, and when would it not apply?

Each has source-linked examples, an author action, and an exception in [the practices reference](skills/oral-paper-skill/references/abstract-derived-practices.md). Select what fits; default to at most three improvements or one focused exercise.

The original ORAL questions can remain a mnemonic, not a common law or scorecard. Methods, theory, findings, systems, resources, and position papers do not need the same evidence package.

## Quick start

Copy the [English prompt](prompts/quick-prompt-en.txt) or [中文提示词](prompts/精简版提示词.txt), then provide an idea, draft, or experiment plan. The prompt has no additional dependencies; accessing reference papers depends on your AI tool.

To install the Skill:

```bash
git clone https://github.com/Adkid-Zephyr/oral-paper-skill.git
```

Place `skills/oral-paper-skill` in your tool's skills directory, such as `~/.codex/skills/` or `~/.claude/skills/`. Compare an existing version before replacing local modifications.

```text
Use $oral-paper-skill to compare my manuscript with relevant exemplary papers.
Give three useful improvements with source locations, applicability, and concrete edits.
```

```text
Use $oral-paper-skill to explain what I can learn from these papers'
storytelling and experimental design, then guide a retrospective on my draft.
```

## What 884 means

The six official lists were rebuilt on September 13, 2026:

| Conference cycles | Indexed entries | Eligible abstracts |
|---|---:|---:|
| ICLR 2025–2026 | 436 | 436 |
| ICML 2025–2026 | 289 | 288 |
| NeurIPS 2024–2025 | 159 | 159 |
| Total | 884 | 883 |

One entry points to [a workshop/session event](https://icml.cc/virtual/2026/workshop/54094), not a paper, and was excluded. All 883 eligible abstracts have per-paper semantic records and are covered by 21 batch syntheses, consolidated into seven practices.

Luna performed extraction, Astra medium handled source checking and selection, and Astra xhigh performed final synthesis. Checks include a 24-paper pilot, a separately fixed random sample of 36, and targeted reviews of flagged issues. This is not human full-corpus close reading or verification of every scientific claim.

[Per-paper records](research/abstract_distillation/cards) · [Process, errors, and corrections](research/abstract_distillation/RESULTS.md) · [Sources and reading levels](skills/oral-paper-skill/references/oral-patterns.md)

## Interpreting the advice

Oral status identifies examples to learn from; this tool does not represent conference criteria or guarantee acceptance. Abstracts support analysis of framing and author-reported contributions; figure design, experiment details, and proofs require the relevant full text.

User benefit has not been established by an independent comparison. Source-linked examples, corrections, and actual manuscript feedback are welcome.

## Paper Skill series

[Anti-Defensive Writing](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill): improve academic expression.

Oral Paper Skill: learn from exemplary papers through comparison and reflection.
