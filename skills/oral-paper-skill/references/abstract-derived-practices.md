# Seven abstract-derived practices

Derived from the 2026-09-13 synthesis of 883 eligible abstracts. These are selectable editorial practices, not universal Oral traits or measured causes of acceptance. The 14 examples below were directly checked against original abstracts; one model-class qualifier was restored after that check.

Use one to three relevant practices for comparison, or one example for a learning exercise. Source-unit labels such as S3 belong to the stored abstract snapshot and splitter; they are not official paper section numbers. Reported results remain the original authors' claims.

[Full process and evidence](https://github.com/Adkid-Zephyr/oral-paper-skill/blob/main/research/abstract_distillation/RESULTS.md) · [Reading levels](oral-patterns.md)

## Specify the Research Tension · 写清研究张力

**Observed pattern:** The analyzed abstracts make research questions concrete through unmet operational requirements or discrepancies between theoretical expectations and reported observations.

**Why it may help:** Editorial inference: a specific tension may help readers understand why the study matters and what answering its question would change.

**Try this:** Replace a broad importance or weakness statement with the condition, the unresolved requirement or observation, and its consequence for the research objective. Follow with the question investigated. Label a suspected explanation as a hypothesis.

**Use when:** The draft describes a broad problem but leaves the reason for this particular investigation unclear.

**Exception:** An exploratory question, resource introduction, or focused characterization can lead directly. Do not invent a prior-method failure or theoretical contradiction.

**Examples:**

- [Probabilistic Learning to Defer: Handling Missing Expert Annotations and Controlling Workload Distribution](https://iclr.cc/virtual/2025/oral/31728) (ICLR 2025, abstract S3, S4, S5, S6): Full expert annotation requirements and missing workload control motivate EM for incomplete annotations and a workload constraint solved during the E-step.
- [An analytic theory of creativity in convolutional diffusion models](https://icml.cc/virtual/2025/oral/47202) (ICML 2025, abstract S2, S3, S4): Contrasts memorization suggested by optimal score matching with reported original outputs, then introduces locality and equivariance as an explanatory account with calibrated predictions for convolution-only models.

**Reflect:** Which specific observation or unmet requirement makes my research question worth answering?

## State the Contribution Delta · 明确贡献增量

**Observed pattern:** Abstracts identify contributions through changed outputs, representations, assumptions, or operations, making the claimed difference more specific than a novelty label.

**Why it may help:** Editorial inference: naming the change may let readers assess its relevance without first accepting a priority claim.

**Try this:** Replace 'a novel framework' with the previous object or requirement, the precise change, and the remaining dependencies. Locate the change in the computation or analysis. For several contributions, explain their relationship without claiming independently established component effects.

**Use when:** The draft names modules or claims novelty without making the difference from relevant work identifiable.

**Exception:** A discovery or resource need not replace an existing method. Improvements within unchanged assumptions should be described on their actual terms.

**Examples:**

- [On Differential Privacy for Adaptively Solving Search Problems via Sketching](https://icml.cc/virtual/2025/oral/47198) (ICML 2025, abstract S2, S3, S5): Extends the stated adaptive-query setting from returning optimization costs to returning search solutions, while identifying the additional information those outputs may reveal about internal randomness.
- [Return of Unconditional Generation: A Self-supervised Representation Generation Method](https://neurips.cc/virtual/2024/oral/97963) (NeurIPS 2024, abstract S3, S4, S5, S6): Generates semantic representations in a self-supervised encoder's representation space and uses them to condition image generation without labels.

**Reflect:** After removing the method name and the word 'novel,' can I still state exactly what changes?

## Match Evidence to the Claim · 让证据对应主张

**Observed pattern:** Some abstracts distinguish related properties through separate measurements; others define a precise formal object supporting a broader interpretation.

**Why it may help:** Editorial inference: explicit claim–evidence links may reveal when a convenient score, proof, or demonstration answers a narrower question than the headline.

**Try this:** For each central claim, identify the measured or proved property and the reported result. Keep proxies, hypotheses, proposals, and findings distinct. Where support is narrower, revise the claim or suggest one focused check. An announced evaluation supplies no result by itself.

**Use when:** The draft uses broad capability language or presents several evidence types as interchangeable support.

**Exception:** A descriptive finding can stand without an intervention, and a theorem can stand without experiments. Add evidence only for claims the author intends to make.

**Examples:**

- [RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments](https://iclr.cc/virtual/2026/oral/10006549) (ICLR 2026, abstract S6, S7): Reports attack success separately from attempts, including attempts as high as 92.5%; the authors attribute some failures to capability limitations.
- [Learning Linear Attention in Polynomial Time](https://neurips.cc/virtual/2025/oral/118143) (NeurIPS 2025, abstract S5): Describes a polynomial-time check of whether all multi-head linear-attention networks best-fitting a given dataset perform an identical computation. The dataset determines the solution set; identical computation is not restricted to observed inputs.

**Reflect:** What exact property supports each headline claim, and where am I relying on a proxy or an unreported outcome?

## Choose a Meaningful Comparison · 选择有解释力的比较

**Observed pattern:** Comparison-focused abstracts expose task exposure, shared model components, or resource budgets that affect what a reported advantage means.

**Why it may help:** Editorial inference: identifying the comparison's purpose and conditions may make results useful for a research or deployment decision.

**Try this:** State what the comparison should decide, select the relevant comparator, and identify what stays fixed and what changes. For efficiency, pair quality with the actual resource unit and accounting boundary, including tuning when relevant. Distinguish component attribution from comparison of complete systems.

**Use when:** A ranking could reflect different training exposure, inputs, implementations, or budgets rather than the difference under discussion.

**Exception:** Matching can change the research question. Comparing systems as delivered may be appropriate; controlling one factor does not establish that all budgets or conditions match.

**Examples:**

- [Training on the Test Task Confounds Evaluation and Emergence](https://iclr.cc/virtual/2025/oral/31791) (ICLR 2025, abstract S6, S7, S8): Proposes fine-tuning compared models on the same task-relevant data before evaluation and reports that instances of emergent behavior disappear gradually with training on the test task.
- [daVinci-Dev: Agent-native Mid-training for Software Engineering](https://icml.cc/virtual/2026/oral/71032) (ICML 2026, abstract S4): Reports a Kimi-Dev comparison using the same base model and agentic scaffold under two post-training settings, while explicitly reporting a different mid-training budget of 73.1B tokens.

**Reflect:** Which decision does my comparison resolve, and which differing condition could change its interpretation?

## Keep Conditions Beside Conclusions · 结论紧随适用条件

**Observed pattern:** Theory abstracts distinguish removed restrictions, additional recovery conditions, error metrics, and the particular regimes supporting optimality claims.

**Why it may help:** Editorial inference: adjacent conditions may prevent a scoped result from becoming an unrestricted headline during compression.

**Try this:** Rewrite the result as: for this object, under these consequential conditions, this quantity has this guarantee relative to this comparison class. Separate extensions with different conditions. For empirical work, use tested settings and observed outcomes instead of guarantee language.

**Use when:** A theorem, transfer claim, scaling statement, or scope extension changes meaning when its regime or quantifier is omitted.

**Exception:** Do not invent assumptions, a converse, or multiple regimes. Qualitative results need not become numerical rates, and missing abstract details need not imply missing full-paper justification.

**Examples:**

- [Mixtures Closest To A Given Measure: A Semidefinite Programming Approach](https://icml.cc/virtual/2026/oral/71052) (ICML 2026, abstract S3, S4, S5, S6): Allows a compact basic semi-algebraic parameter set without assuming finiteness, then separates asymptotic convergence from finite convergence and optimal mixing-measure recovery under a rank condition.
- [Statistical Efficiency of Distributional Temporal Difference Learning](https://neurips.cc/virtual/2024/oral/97962) (NeurIPS 2024, abstract S1): Reports p-Wasserstein finite-sample bounds for distributional TD in tabular discounted MDPs, while restricting minimax optimality up to logarithmic factors to p=1.

**Reflect:** Which condition or quantifier would make my conclusion materially stronger if a reader missed it?

## Explain What the Resource Enables · 说明资源支持的研究

**Observed pattern:** Resource contributions specify research activities, contents, or interfaces; integrated papers also distinguish infrastructure from an accompanying training method.

**Why it may help:** Editorial inference: connecting resource design to enabled work may make its contribution assessable beyond collection size or an accompanying model's score.

**Try this:** Describe the resource unit, attached information or interface, construction and access conditions, and the research activity it supports. Separate intended uses from demonstrated uses. Identify each artifact's reported release status independently, preserving prospective wording.

**Use when:** A dataset, benchmark, environment, implementation, or documentation resource carries part or all of the contribution.

**Exception:** A narrow or exploratory resource need not include a leaderboard, new model, or demonstrated downstream gain. An ordinary code-release sentence alone need not become an independent resource contribution.

**Examples:**

- [Machine Learning meets Algebraic Combinatorics: A Suite of Datasets Capturing Research-level Conjecturing Ability in Pure Mathematics](https://icml.cc/virtual/2025/oral/47182) (ICML 2025, abstract S3, S4, S5, S6): Organizes nine algebraic-combinatorics datasets around open-ended research questions and example collections for conjecture generation; the abstract supplies no measured model-performance outcome.
- [AgentGym-RL: An Open-Source Framework to Train LLM Agents for Long-Horizon Decision Making via Multi-Turn RL](https://iclr.cc/virtual/2026/oral/10008786) (ICLR 2026, abstract S3, S4, S7, S8): Describes AgentGym-RL's modular training framework across environments and separately introduces ScalingInter-RL's staged expansion from short to longer interaction horizons.

**Reflect:** What can another researcher investigate, construct, or compare with this resource, and which feature makes that possible?

## Extract a Bounded Lesson · 提炼有边界的认识

**Observed pattern:** Explanatory and position abstracts develop lessons through distinctions that matter: an interaction changes with training stage, or a cross-domain recommendation depends on both similarities and differences.

**Why it may help:** Editorial inference: a bounded implication may give readers something to reconsider or investigate beyond remembering a method name or favorable score.

**Try this:** Replace a generic closing with the specific distinction learned and its implication in the studied setting. Separate the observation from its explanation and any proposed action. Identify a condition or domain difference that would change the lesson.

**Use when:** Results or arguments support a useful change in understanding, interpretation, or a proposed choice.

**Exception:** A descriptive finding need not supply a mechanism or prescription. A single interesting case does not establish a universal design rule.

**Examples:**

- [Strategy Coopetition Explains the Emergence and Transience of In-Context Learning](https://icml.cc/virtual/2025/oral/47206) (ICML 2025, abstract S5, S7, S9, S10): Reports that CIWL helps ICL emerge but later competes with and replaces it in the studied setup; a mathematical model reportedly guides identification of a persistent-ICL setup.
- [Position: Generative AI Regulation Can Learn from Social Media Regulation](https://icml.cc/virtual/2025/oral/40120) (ICML 2025, abstract S5, S6): Compares generative-AI and social-media affordances, preserving similarities and differences before offering four regulatory recommendations; these are proposals, not demonstrated regulatory outcomes.

**Reflect:** What should a reader understand or reconsider after this work, and what would make that lesson fail to transfer?
