# Oral Paper Skill · Learn from Exemplary Papers

**Starting from 884 top-conference Oral entries, develop reusable research and writing lessons for comparing, improving, and reflecting on your own paper.**

[中文 README](README.md) · [Full Skill](skills/oral-paper-skill/SKILL.md) · [Quick prompt](prompts/quick-prompt-en.txt) · [Research progress](docs/ABSTRACT_DISTILLATION.md)

[![Starting index: 884 entries](https://img.shields.io/badge/starting%20index-884%20entries-blue)](skills/oral-paper-skill/references/oral-patterns.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Adkid-Zephyr/oral-paper-skill/pulls)

This is a learning-tool prototype informed by a historical abstract scan, selected full-text passages and figures, and official award commentary. Per-abstract semantic extraction is not complete; 884 describes the historical index size.

## Why I am building this

I believe that papers selected for Oral presentation contain research decisions worth studying. Exemplary papers are a practical starting point for learning how to do and communicate good research.

Research training often begins with classic papers. If you want to submit to ICLR, ICML, or NeurIPS, a traditional approach is to study past papers from that venue, find inspiration, combine method A with setting B, or improve one part of an existing approach.

That path has produced publications. But if all we learn is how to combine components, what have we understood about why the problem matters, what makes the contribution useful, or how the evidence supports it? Combinations and incremental advances can be valuable; understanding that value is the point.

AI can help us organize and compare these examples more systematically, extract useful patterns, and apply them to our own ideas and writing.

After my anti-defensive-writing video brought in a few hundred followers, I kept thinking about what to share next. I have accumulated useful personal Skills; Oral Paper Skill is the second public project in this series.

**The goal is to study Oral entries and other exemplary papers from the latest two completed cycles of ICLR, ICML, and NeurIPS, then turn their useful practices into reusable learning guidance.**

Here, “distillation” means extracting and synthesizing knowledge into instructions and examples. We start at the abstract level and supplement it with passages and figures actually inspected.

## Two uses

### 1. Compare and improve

Choose examples relevant to your problem and contribution type. Explain what they do, why the comparison fits, and which changes could improve your manuscript.

A substantial suggestion should connect: **source practice and locator → relevance → observation about your draft → concrete change.**

For example, a draft claiming lower compute cost may need a comparison of end-to-end cost at matched quality. This illustrates the form of advice; attributing it to a particular paper requires reading that source.

### 2. Learn and reflect

Explain how exemplary papers develop their introduction, distinguish their contribution, present the central figure, and use experiments to address alternative explanations. Include applicability and exceptions, then help authors reflect on their own work.

## ORAL: four reflection questions

- **O — One irreducible claim:** What is the central research question, and how do the contributions connect?
- **R — Reader-visible proof:** Where does the reader encounter the main evidence?
- **A — Adversarial evidence:** Which alternative explanation deserves testing, and are comparisons fair?
- **L — Lasting lesson:** What finding, method, or resource value does the work offer?

These are editorial learning prompts, not empirically established requirements for all Oral papers. The default output is a few supported improvements or a reflection exercise, not an Oral score or an automatic decision to abandon research.

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

The extraction log from September 2, 2026 reported:

| Conference cycles | Oral entries |
|---|---:|
| ICLR 2025–2026 | 436 |
| ICML 2025–2026 | 289 |
| NeurIPS 2024–2025 | 159 |
| Total | 884 |

It reported 883 available abstracts. The original index was not archived in this repository; rebuilding and validating the entry-to-paper mapping remains necessary.

Completed work consists of lexical abstract scans, selected full-text passages and figure inspection, and award-commentary notes. A semantic record for every abstract and full-paper distillation of all 884 entries have not been completed.

[Sources and reading levels](skills/oral-paper-skill/references/oral-patterns.md) · [Abstract-distillation plan](docs/ABSTRACT_DISTILLATION.md)

## Interpreting the advice

Oral status identifies examples to learn from; this tool does not represent conference criteria or guarantee acceptance. Abstracts support analysis of framing and author-reported contributions; figure design, experiment details, and proofs require the relevant full text.

User benefit has not been established by an independent comparison. Source-linked examples, corrections, and actual manuscript feedback are welcome.

## Paper Skill series

[Anti-Defensive Writing](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill): improve academic expression.

Oral Paper Skill: learn from exemplary papers through comparison and reflection.
