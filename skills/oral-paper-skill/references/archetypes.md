# Paper archetypes and their proof carriers

Choose one primary archetype for the paper's center of gravity. Use secondary contributions only to support it.

## Method or algorithm

**Core claim:** A new method changes a meaningful quality, capability, or resource frontier.

**Reader-visible proof:** a simple method contrast plus the main quality/resource curve or a minimal case that explains the gain.

**Adversarial evidence:** strongest simple baseline; matched data/compute; component necessity; cross-task or cross-model transfer; failure regime.

**Common failure:** a large implementation whose gain disappears against a tuned baseline or equal budget.

## Theory or guarantee

**Core claim:** A long-standing question, qualitative distinction, or quantitative bound is resolved under explicit assumptions.

**Reader-visible proof:** theorem statement with an intuitive consequence, a tight diagram, or a counterexample that makes the result surprising.

**Adversarial evidence:** tightness; necessity of assumptions; comparison with prior bound; non-vacuous regime; empirical illustration only when it adds understanding.

**Common failure:** technical difficulty without a conceptual message or a theorem whose assumptions pre-decide the conclusion.

## Empirical science or mechanism

**Core claim:** A widely assumed explanation is incomplete, and controlled evidence identifies a more accurate mechanism.

**Reader-visible proof:** the anomaly and the intervention that changes it; a phase diagram or paired mechanism plot.

**Adversarial evidence:** interventions rather than correlations; alternative hypotheses; controlled toy setting connected back to realistic models; replication across regimes.

**Common failure:** many correlations described as a mechanism.

## Systems or efficiency

**Core claim:** A real bottleneck can be removed while preserving the property users actually require.

**Reader-visible proof:** end-to-end quality–latency–memory–cost frontier on realistic workloads.

**Adversarial evidence:** same hardware/software stack; quality matched before speed claims; strong optimized baseline; scaling behavior; overhead and failure cases.

**Common failure:** reporting kernel speedup while hiding end-to-end overhead or quality loss.

## Benchmark or dataset

**Core claim:** Existing evaluations miss a consequential construct, and the new resource measures it validly enough to change scientific understanding.

**Reader-visible proof:** task unit → system behavior → truth/annotation mechanism → new scientific finding.

**Adversarial evidence:** construct and oracle validation; contamination/shortcut checks; human or external criterion; broad baseline coverage; subgroup/transfer analysis; sustainable update path.

**Common failure:** scale and leaderboard without validity or a finding beyond ranking.

## Position paper

**Core claim:** The field is optimizing the wrong objective, neglecting an important issue, or adopting a harmful assumption.

**Reader-visible proof:** a crisp mismatch between current practice and consequence, supported by representative evidence.

**Adversarial evidence:** strongest counterpositions considered fairly; scope clear; practical research or policy actions follow from the thesis.

**Common failure:** opinion without evidence, or criticism without an actionable alternative.
