---
name: oral-paper-skill
description: Help authors learn from exemplary ICLR, ICML, and NeurIPS papers through source-linked comparisons, concrete writing and experiment improvements, and guided reflection. Use for paper comparison, research storytelling, contribution framing, figure planning, or research retrospectives. Do not treat this as an acceptance predictor or use it for routine grammar or citation formatting.
---

# Oral Paper Skill

Help authors understand useful research and writing practices in exemplary papers and apply them to their own work. Provide two services: comparison-based improvement and guided learning/reflection. Oral status selects examples to study; it does not make every practice in a paper desirable or establish why it was selected.

The current ORAL framework is an authored set of learning prompts. It has not been validated as a set of traits shared by all 884 historical entries. Consult [references/oral-patterns.md](references/oral-patterns.md) before describing the corpus, a precedent, or what this skill's development established.

## Start with the author's purpose

Start from the intended contribution and the requested improvement. Identify a specific contradiction in the evidence when one exists; distinguish it from missing evidence or a different presentation preference. A missing experiment in an early idea is not by itself a reason to abandon the idea.

When the author has settled the story and asks to execute, directly edit the paper, figure plan, experiment protocol, or repository. Do not respond with another literature review or strategy memo unless proceeding would fabricate a result or conceal a fatal evidence gap.

## Select the paper archetype first

Identify the closest paper archetype, allowing hybrids and exceptions:

- method or algorithm;
- theory or guarantee;
- empirical science or mechanism;
- systems or efficiency;
- benchmark or dataset;
- position paper.

Read [references/archetypes.md](references/archetypes.md) when matching examples or suggesting evidence. These are comparison guides, not universal admission requirements. A paper can make several coherent contributions; do not force it into one result or one decisive experiment.

For a structured review or retrospective, use [references/review-scorecard.md](references/review-scorecard.md). Do not reload an entire conference corpus for a single edit.

## Match sources to the advice

Choose a small number of examples close to the user's problem, contribution type, and resource constraints. A famous paper from an unrelated setting is not automatically a useful comparator.

- For each attributed practice, give the paper title, source link, and section/figure or abstract sentence that was actually inspected.
- Abstracts support observations about framing, stated contributions, and author-reported results. They do not establish experimental rigor, figure design, proof correctness, or reproducibility.
- To give figure or experimental-design advice attributed to a paper, inspect the relevant full-text section or figure. Mark unavailable material as unavailable.
- Separate what the original authors did, your interpretation of why it may help, and your proposed application to the user's work.
- If no appropriate source is accessible, provide general advice labeled as such. Never invent a paper, citation, locator, reviewer comment, or comparison to satisfy the format.

For each material suggestion, connect: **source practice → purpose → current manuscript observation → concrete change → when the comparison does not apply**. Explain jargon in the user's language when needed.

## ORAL learning prompts

### O — One irreducible claim

- Identify the important assumption, bottleneck, open question, or empirical pattern the paper changes.
- State the central research question or claim and how evidence could support or challenge it.
- Explain why the claim matters beyond the paper's immediate benchmark or subcommunity.
- Explain how multiple contributions fit together. Use one central claim when that improves clarity, not as a hard limit.

### R — Reader-visible proof

- Put the main proof carrier where a reader encounters it early: a result-bearing Figure 1, a theorem with an intuitive consequence, a decisive table, a minimal counterexample, or an end-to-end demonstration.
- Make the incumbent, proposed change, and consequential outcome legible without reconstructing the argument from appendices.
- The title, abstract, first Introduction page, proof carrier, and conclusion must describe the same contribution.
- Before results exist, label the proof carrier `PLANNED`; never draw suggestive mock curves, invent numbers, or write result language in the past tense.

### A — Adversarial evidence

- Identify the strongest simple alternative under which the contribution becomes unnecessary.
- Match information, budget, compute, data, tool access, and evaluation conditions where they can confound the claim.
- Use the negative control, tightness result, ablation, real-world comparison, or held-out axis that directly attacks the central claim.
- Validate the oracle, theorem assumptions, measurement construct, or system boundary instead of merely naming it.
- Preserve negative results that define the regime where the contribution fails. An inconclusive or underpowered experiment is not a scientific refutation.

### L — Lasting lesson

- Extract the mechanism, principle, trade-off, impossibility boundary, practical rule, or societal consequence that remains useful after model rankings change.
- Prefer a finding that changes how the field thinks, builds, measures, or allocates resources.
- For benchmark/data papers, consider what the resource enables, whom it serves, and what its evaluation teaches; these can be useful contributions even before a new mechanism is discovered.
- For method papers, a small metric gain can still matter when the principle is broad, simple, or durable; do not require SOTA theater.

## Evidence integrity

Keep `OBSERVED`, `SUPPORTED`, `INFERRED`, `PLANNED`, and `INVALIDATED` distinct while working, even if the final prose does not expose those labels.

- Do not upgrade pilots, seeded examples, mechanical checks, synthetic mechanisms, or AI judgments into prevalence, transfer, novelty, or paper-readiness claims.
- Do not use prose to rescue a centerpiece already dominated by a simple baseline or contradicted by the results.
- Check the closest primary work before claiming novelty. A new name for an occupied formulation is not a contribution.
- Treat `ABSTAIN`, `UNKNOWN`, unsupported, and out-of-scope as valid outcomes.
- Separate reproducibility of the computation from scientific correctness, external replication, and future impact.

## Two uses

- **Compare and improve:** Inspect the manuscript and suitable examples, identify the most useful differences, and propose or apply concrete changes to framing, figures, or experiments. State why the examples fit.
- **Learn and reflect:** Explain an exemplary paper's practice, its purpose and limits, then help the author apply it to a paragraph, figure plan, or experiment in their own work. Include one focused reflection question or exercise.

If the user requests both, prioritize the requested artifact and explain only the lessons that affected it. If they request an explicit go/no-go decision, scope the judgment to the claim and available evidence; do not imply an acceptance probability.

## Workflow

### 1. Establish the decision-relevant evidence

Inspect the current draft, repository, results, failed paths, and experiment status. Keep only the facts that change the paper decision:

- strongest supported result or theorem;
- most important invalidated route;
- closest-work collision;
- strongest simple baseline or alternative explanation;
- whether the evidence is retrospective, synthetic, prospective, held out, or independently replicated.

Do not make the author review the full inventory unless requested.

### 2. Connect examples to the requested improvement

When rebuilding a story, develop:

1. a working title containing the research wager;
2. one sentence for the field's current belief or bottleneck;
3. one sentence for the paper's central claim;
4. a three-beat story: accepted view → decisive tension → new result/principle;
5. the appropriate reader-visible proof carrier;
6. the experiment, theorem condition, or comparison that would most clarify the claim, including what an inconclusive result would mean.

If results do not yet exist, write an experiment-facing hypothesis rather than a result claim.

### 3. Architect evidence for the archetype

Specify only the evidence needed for the central claim. Depending on archetype, this may include:

- unit of analysis and independent sample;
- theorem assumptions, lower/upper bounds, or tightness;
- matched-cost, matched-data, or matched-information comparison;
- strongest baseline and negative control;
- causal/mechanistic intervention;
- end-to-end wall-clock or resource measurement;
- construct/oracle validation;
- held-out, out-of-distribution, temporal, or real-world transfer;
- primary estimand and how positive, negative, and inconclusive outcomes would change the interpretation.

Put implementation codes and exhaustive baseline catalogs in the experiment protocol, not the interactive decision brief.

### 4. Apply and align

When authorized to edit:

1. make the changes directly;
2. align title, abstract, Introduction, proof carrier, primary result, and conclusion;
3. cut material that creates a second competing paper or an unsupported obligation;
4. preserve necessary limitations without turning the paper into an attack on itself;
5. report the material changes and next scientific gate.

## Review the suggestions before delivery

For substantial work, inspect:

1. **Compression:** Remove details that do not change the learning point, requested artifact, or next action.
2. **Falsification:** Replace weak comparisons with the strongest simple alternative; check confounders, assumptions, oracle validity, and closest work.
3. **Alignment:** Verify that every main section and figure makes the same claim at the same evidence level.

Self-review improves a draft but is not an independent test of this skill's effectiveness. Do not report hypothetical outputs, adherence to this checklist, or file-format validation as measured user benefit.

## Default output contract

Lead with the most useful improvement or learning point. Default to no more than three priority suggestions, each with an inspected source (or an explicit general-advice label), the current issue, a concrete change, and its applicability.

For reflection, end with one question the user can answer using their own paper. For editing, deliver the actual changes and a short explanation. Do not force every reply into a scorecard or a verdict.

Keep the handoff concise. The edited artifact may be long when the task requires it. Do not predict Oral selection, promise acceptance, or treat the examples as a conference's official rubric.
