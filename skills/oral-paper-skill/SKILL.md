---
name: oral-paper-skill
description: Calibrate and improve ML/AI papers using cross-venue patterns from recent ICLR, ICML, and NeurIPS Oral and award papers. Use when shaping a research story, title, abstract, Introduction, Figure 1, theorem presentation, experiment architecture, or submission-level audit. Do not use for routine grammar edits, citation formatting, or literature summaries with no paper to improve.
---

# Oral Paper Skill

Adjust a paper toward the standards repeatedly visible in strong ICLR, ICML, and NeurIPS papers: one irreducible contribution, reader-visible proof, adversarial evidence, and a lasting lesson. Do not imitate fashionable wording, topic choice, or figure styling. Oral and award papers are precedents for research compression and evidence quality, not an acceptance recipe.

## Preserve the author's research decision

Start from the author's intended contribution. Strengthen or challenge it using the actual evidence, but do not silently replace the direction. If evidence defeats the intended centerpiece, say so and propose the smallest meaningful choice.

When the author has settled the story and asks to execute, directly edit the paper, figure plan, experiment protocol, or repository. Do not respond with another literature review or strategy memo unless proceeding would fabricate a result or conceal a fatal evidence gap.

## Select the paper archetype first

Classify the intended centerpiece as one primary archetype:

- method or algorithm;
- theory or guarantee;
- empirical science or mechanism;
- systems or efficiency;
- benchmark or dataset;
- position paper.

Read [references/archetypes.md](references/archetypes.md) when selecting the proof carrier, decisive experiment, or paper structure. A paper may contain several contribution types, but its main story needs one center of gravity.

Read [references/oral-patterns.md](references/oral-patterns.md) only when explaining the evidence base, choosing precedents, or rebuilding a story. Do not reload the conference corpus for ordinary application work.

## ORAL calibration

### O — One irreducible claim

- Identify the important assumption, bottleneck, open question, or empirical pattern the paper changes.
- State one central claim that can be false.
- Explain why the claim matters beyond the paper's immediate benchmark or subcommunity.
- Let secondary contributions support the claim instead of competing with it.

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
- Preserve negative results that define the regime where the contribution fails.

### L — Lasting lesson

- Extract the mechanism, principle, trade-off, impossibility boundary, practical rule, or societal consequence that remains useful after model rankings change.
- Prefer a finding that changes how the field thinks, builds, measures, or allocates resources.
- For benchmark/data papers, the lasting lesson must exceed “we release a large dataset.”
- For method papers, a small metric gain can still matter when the principle is broad, simple, or durable; do not require SOTA theater.

## Evidence integrity

Keep `OBSERVED`, `SUPPORTED`, `INFERRED`, `PLANNED`, and `INVALIDATED` distinct while working, even if the final prose does not expose those labels.

- Do not upgrade pilots, seeded examples, mechanical checks, synthetic mechanisms, or AI judgments into prevalence, transfer, novelty, or paper-readiness claims.
- Do not use prose to rescue a centerpiece already dominated by a simple baseline or contradicted by the results.
- Check the closest primary work before claiming novelty. A new name for an occupied formulation is not a contribution.
- Treat `ABSTAIN`, `UNKNOWN`, unsupported, and out-of-scope as valid outcomes.
- Separate reproducibility of the computation from scientific correctness, external replication, and future impact.

## Working modes

- **Calibrate:** Give a fast `GO`, `WAIT`, or `KILL` verdict on a proposed story.
- **Build:** Turn an evidence package into a title, claim, narrative spine, proof carrier, and survival test.
- **Experiment adjust:** Redesign experiments around the strongest alternative explanation and the paper's actual estimand.
- **Apply:** Edit the supplied paper or repository and align all main sections with the chosen claim.
- **Audit:** Use [references/review-scorecard.md](references/review-scorecard.md) for a submission-level review.

## Workflow

### 1. Establish the decision-relevant evidence

Inspect the current draft, repository, results, failed paths, and experiment status. Keep only the facts that change the paper decision:

- strongest supported result or theorem;
- most important invalidated route;
- closest-work collision;
- strongest simple baseline or alternative explanation;
- whether the evidence is retrospective, synthetic, prospective, held out, or independently replicated.

Do not make the author review the full inventory unless requested.

### 2. Write the spine before polishing prose

Produce:

1. a working title containing the research wager;
2. one sentence for the field's current belief or bottleneck;
3. one sentence for the paper's central claim;
4. a three-beat story: accepted view → decisive tension → new result/principle;
5. the appropriate reader-visible proof carrier;
6. the one test, theorem condition, or comparison that can kill the paper.

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
- primary estimand and kill condition.

Put implementation codes and exhaustive baseline catalogs in the experiment protocol, not the interactive decision brief.

### 4. Apply and align

When authorized to edit:

1. make the changes directly;
2. align title, abstract, Introduction, proof carrier, primary result, and conclusion;
3. cut material that creates a second competing paper or an unsupported obligation;
4. preserve necessary limitations without turning the paper into an attack on itself;
5. report the material changes and next scientific gate.

## Silent three-pass loop

For substantial work, run up to three internal passes and stop early when no material decision changes:

1. **Compression:** Remove details that do not change O, R, A, L, the verdict, or the next action.
2. **Falsification:** Replace weak comparisons with the strongest simple alternative; check confounders, assumptions, oracle validity, and closest work.
3. **Alignment:** Verify that every main section and figure makes the same claim at the same evidence level.

Do not expose intermediate drafts or narrate the loop unless the user asks.

## Default output contract

Lead with the adjusted story or verdict. Default to one screen:

1. **Story** — at most three short paragraphs;
2. **Proof carrier** — Figure 1, theorem, table, counterexample, or demo;
3. **Survival test** — the single experiment or condition that decides the claim;
4. **Verdict** — `GO`, `WAIT`, or `KILL` with one sentence of evidence;
5. **Next action** — what to edit or build now.

Mention at most three blocking gaps. Do not output a paper-by-paper survey, long rubric, or baseline taxonomy unless explicitly requested. The edited artifact may be long; the handoff stays concise.

## Verdicts

- **GO:** The claim is important and falsifiable, the proof carrier is legible, and no observed simple alternative already defeats it.
- **WAIT:** The story is coherent, but one named evidence, assumption, baseline, validity, or transfer gate is missing.
- **KILL:** The centerpiece is unfalsifiable, occupied, contradicted, or dominated. Preserve useful negative evidence; do not rescue it with rhetoric.

Never convert an ORAL assessment into an acceptance probability. Venue decisions are heterogeneous and partly subjective.
