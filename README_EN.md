# Oral Paper Skill

**Turn recurring research standards from recent ICLR, ICML, and NeurIPS Oral and award papers into an actionable paper-calibration skill.**

[中文 README](README.md) · [Skill](skills/oral-paper-skill/SKILL.md) · [Quick Prompt](prompts/quick-prompt-en.txt)

---

## What it does

Reading exemplary papers is a traditional first step in research training. But copying their topics, surface structure, or A+B combinations is not the same as learning why the work matters.

`Oral Paper Skill` calibrates a paper around four questions:

- **O — One irreducible claim:** What important, falsifiable claim does the whole paper bet on?
- **R — Reader-visible proof:** Can readers see early why the claim should be believed?
- **A — Adversarial evidence:** Does the evidence confront the strongest explanation that would make the contribution unnecessary?
- **L — Lasting lesson:** What mechanism, principle, trade-off, or boundary remains after leaderboards change?

The skill first identifies the paper's center of gravity—method, theory, empirical mechanism, systems, benchmark/data, or position paper—then aligns the title, claim, abstract, Introduction, Figure 1 or main theorem, experiments, and conclusion.

## Evidence base

The initial version used the latest completed cycles available on 2026-09-02: ICLR 2025–2026, ICML 2025–2026, and NeurIPS 2024–2025. It structurally analyzed 884 official Oral entries and 883 available abstracts, then deep-read a stratified set of Oral, Best, and Outstanding papers together with official award-committee explanations.

This is not a claim of reading all 884 full papers. See [`oral-patterns.md`](skills/oral-paper-skill/references/oral-patterns.md) for the corpus boundary and primary sources.

## Install

### Codex

```bash
git clone https://github.com/Adkid-Zephyr/oral-paper-skill.git
cp -R oral-paper-skill/skills/oral-paper-skill ~/.codex/skills/
```

Invoke it with:

```text
Use $oral-paper-skill to calibrate this paper's central claim,
proof carrier, evidence, and lasting lesson.
```

### Claude Code

```bash
cp -R oral-paper-skill/skills/oral-paper-skill ~/.claude/skills/
```

### Any AI assistant

Copy [`prompts/quick-prompt-en.txt`](prompts/quick-prompt-en.txt) before providing the paper, research idea, or experiment plan.

## Outputs

By default, the skill returns a concise decision interface:

1. adjusted story;
2. Figure 1, theorem, table, counterexample, or demo that should carry the proof;
3. the single survival test;
4. `GO`, `WAIT`, or `KILL`;
5. the next action.

It does not claim to predict acceptance, invent missing results, revive a direction already defeated by evidence, or force every paper archetype into a benchmark/SOTA template.

## Companion skill

[`Anti-Defensive Writing`](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) prevents a paper from rhetorically weakening itself. `Oral Paper Skill` works upstream: it checks whether the paper has a worthwhile central claim and evidence capable of supporting it.
