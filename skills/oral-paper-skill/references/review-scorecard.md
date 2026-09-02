# ORAL reviewer scorecard

Use for a substantial draft, paper spine, or experiment plan. This diagnoses argument quality; it does not estimate acceptance probability.

Rate each dimension `PASS`, `WEAK`, or `MISSING` and cite the exact section, theorem, figure, table, result, or evidence artifact.

## O — One irreducible claim

`PASS` when a reader can state the important problem and one falsifiable contribution after the title, abstract, and first Introduction page.

Ask:

- Is this a consequential problem, open question, bottleneck, or assumption—not just an unused feature?
- Is there one center of gravity?
- Does the claim matter beyond a single benchmark or niche configuration?
- Does it survive the closest primary work?

## R — Reader-visible proof

`PASS` when the appropriate proof carrier makes the central claim legible early.

Ask:

- Does Figure 1, theorem, table, counterexample, or demo show the actual wager?
- Can the reader see the incumbent, change, and consequence?
- Is the main result hidden in an appendix or diluted across many figures?
- For pre-result work, is the outcome marked `PLANNED` without mock numbers or success-shaped curves?

## A — Adversarial evidence

`PASS` when the strongest simple alternative is tested under fair conditions and the evidence can genuinely kill the claim.

Ask:

- Could more compute, data, calls, context, tools, tuning, or a stronger model explain the result?
- Is the baseline optimized and matched on the relevant resource?
- Is there a negative control, tightness argument, intervention, or held-out axis aimed at the central claim?
- Are the oracle, assumptions, construct, and system boundary validated?
- Are repeated runs being mistaken for independent tasks?

## L — Lasting lesson

`PASS` when the paper leaves a mechanism, principle, bound, trade-off, practical rule, new scientific object, or societal consequence that remains useful after rankings change.

Ask:

- What sentence from this paper should still matter in three years?
- Does the work change how the field thinks, builds, measures, or allocates resources?
- Are negative and heterogeneous results used to define the regime rather than hidden?

## Alignment and integrity

`PASS` when title, abstract, Introduction, proof carrier, primary result, and conclusion state the same claim at the same evidence level.

Ask:

- Are pilots, synthetic cases, or mechanical checks being inflated into prevalence or transfer?
- Has a killed direction returned through rhetoric?
- Are retrospective, prospective, held-out, and independently replicated evidence separated?
- Can ambiguity produce `ABSTAIN`, `UNKNOWN`, or out-of-scope?
- Are limitations necessary and scoped, or is the paper arguing against itself?

## Verdict

- `GO`: O, R, A, L and integrity pass; remaining work does not change the centerpiece.
- `WAIT`: the centerpiece is coherent, but one named evidence, assumption, baseline, validity, or transfer gate is missing.
- `KILL`: the centerpiece is occupied, unfalsifiable, contradicted, or dominated by a simple alternative.

## Concise audit output

```markdown
Verdict: GO | WAIT | KILL

Story: <one-sentence problem and central claim>

ORAL:
- O: PASS | WEAK | MISSING — <evidence>
- R: PASS | WEAK | MISSING — <evidence>
- A: PASS | WEAK | MISSING — <evidence>
- L: PASS | WEAK | MISSING — <evidence>
- Alignment/integrity: PASS | WEAK | MISSING — <evidence>

Proof carrier:
<Figure 1, theorem, table, counterexample, or demo>

The survival test:
<single comparison or theorem condition + kill criterion>

Next action:
<what to edit or build now>
```

Do not append a broad literature survey or implementation catalog unless requested.
