# Oral Paper Skill · Top-Paper Calibration

**Stop copying A+B from Oral papers. Distill the research standards behind 884 official ICLR, ICML, and NeurIPS Oral entries into an AI skill for calibrating ideas, claims, Figure 1, and experiments.**

[中文 README](README.md) · [Full Skill](skills/oral-paper-skill/SKILL.md) · [Quick Prompt](prompts/quick-prompt-en.txt)

[![Corpus: 884 Orals](https://img.shields.io/badge/corpus-884%20official%20Orals-blue)](skills/oral-paper-skill/references/oral-patterns.md)
[![Dependencies: Zero](https://img.shields.io/badge/dependencies-zero-brightgreen)](skills/oral-paper-skill/SKILL.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/Adkid-Zephyr/oral-paper-skill/pulls)

---

## What is this?

A traditional first step in research training is to read exemplary papers. If you want to publish at ICLR, you study past ICLR Orals; for ICML or NeurIPS, you do the same. You learn the topics, methods, experiments, and presentation, then look for an A+B combination or a local improvement.

This can produce papers. It can also teach only the surface: **swap a module, add a setting, run more benchmarks—yet never explain why the paper deserves to exist.**

This is **surface imitation**.

The alternative is not to ask AI for another A+B. It is to learn the research judgment behind strong papers:

> **Do not copy what an Oral paper did.**
> **Learn why its central wager matters and how the paper makes that wager believable.**

`Oral Paper Skill` first identifies the paper's center of gravity—method, theory, empirical mechanism, systems, benchmark/data, or position paper—then aligns the title, abstract, Introduction, Figure 1 or main theorem, experiments, and conclusion around one claim.

## Surface imitation vs. Oral calibration

| | Surface imitation | Oral Paper Skill |
|---|---|---|
| Finding an idea | Move method A into setting B | Find an important, falsifiable claim worth betting the paper on |
| Contributions | List Contributions 1, 2, 3, and 4 evenly | Make every contribution support one central claim |
| Figure 1 | Display a complicated pipeline | Show early why the claim should be believed: result, theorem, counterexample, or demo |
| Experiments | Choose a baseline that is easy to beat | Confront the strongest explanation that would make the paper unnecessary |
| What remains | A leaderboard number that soon expires | A mechanism, principle, trade-off, bound, or new scientific object |

## ORAL

- **O — One irreducible claim:** What important, falsifiable claim does the whole paper bet on?
- **R — Reader-visible proof:** Can readers see early why they should believe it?
- **A — Adversarial evidence:** Does the evidence confront the strongest alternative rather than the weakest baseline?
- **L — Lasting lesson:** What remains worth remembering after leaderboards change?

By default, the skill returns only five things: **Story, Proof carrier, Survival test, GO / WAIT / KILL, and Next action.**

## Quick start

### Option 1: Copy the prompt (works with any AI)

Copy [`prompts/quick-prompt-en.txt`](prompts/quick-prompt-en.txt) ([中文](prompts/精简版提示词.txt)), paste it at the start of a conversation, then provide your idea, paper, or experiment plan. Zero dependencies.

### Option 2: Install the Skill

```bash
git clone https://github.com/Adkid-Zephyr/oral-paper-skill.git

# Codex
cp -R oral-paper-skill/skills/oral-paper-skill ~/.codex/skills/

# Claude Code / other tools with Skills support
cp -R oral-paper-skill/skills/oral-paper-skill ~/.claude/skills/
```

Then ask:

```text
Use $oral-paper-skill to inspect this idea.
Tell me what the whole paper should bet on, why the claim should be believed,
and which experiment decides whether it survives. Do not begin with copyediting.
```

## Evidence base

The initial version covers the latest completed cycles available on 2026-09-02:

- ICLR 2025–2026: 436 official Oral events;
- ICML 2025–2026: 289;
- NeurIPS 2024–2025: 159.

It structurally analyzed **884 official Oral entries and 883 available abstracts**, then deep-read a stratified set of representative Oral, Best, and Outstanding papers across methods, theory, empirical mechanisms, systems, benchmark/data, and position work, together with official award-committee explanations.

This is not a claim of reading all 884 full papers. It is a full abstract-level scan plus cross-archetype deep reading. See [`oral-patterns.md`](skills/oral-paper-skill/references/oral-patterns.md) for the corpus boundary and primary sources.

One result matters for how the skill is designed: strong papers do not share a universal “large benchmark + SOTA number” template. Theory can win through a tight result and conceptual consequence; mechanism papers through controlled interventions; systems through end-to-end frontiers; position papers through an evidence-backed thesis and actionable direction.

## What it will not do

- convert an ORAL assessment into an acceptance probability;
- invent successful-looking curves before results exist;
- use rhetoric to revive a direction defeated by a simple baseline;
- inflate pilots, synthetic cases, or mechanical checks into generalization;
- force every paper archetype into the same template.

## Use cases

- build a paper spine from an idea;
- rewrite a title, abstract, or Introduction;
- design Figure 1, a main theorem presentation, or a core demo;
- restructure experiments around clear argumentative duties;
- run a pre-submission `GO / WAIT / KILL` audit;
- decide whether to add evidence, change the story, or stop a direction.

## Repository structure

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

## Paper Skill series

Part 1: [`Anti-Defensive Writing`](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) prevents a paper from rhetorically weakening itself.

Part 2: `Oral Paper Skill` checks whether the paper has a central claim worth betting on and evidence capable of supporting it.

PRs and labmate sharing are welcome.
