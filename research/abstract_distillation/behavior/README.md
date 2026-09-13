# Fresh-context usage checks

Two actual Astra medium calls used the updated Skill and source materials in
fresh contexts. The prompts supplied the task and necessary raw materials, not
an intended answer or a score. The maintainer inspected the returned outputs.

## Compare and revise

Input: the real published abstract of
[OLMoE](https://iclr.cc/virtual/2025/oral/31734), with a request for an English
rewrite under 150 words and two Chinese explanations of source-informed edits.

Observed: [the response](compare-response.md) delivered an illustrative rewrite
within the requested 150-word limit (106 whitespace-separated words), preserved parameter/training quantities, distinguished active
parameters from total cost, and cited relevant supplied source examples. It
marked the rewrite as illustrative and not author-approved.

Its self-reported “113 words” label was inaccurate. The original response is
retained; this small reporting issue is not hidden by the successful length check.

## Learn and plan

Input: a synthetic early-stage idea about reusing retrieval passages by query
intent to reduce RAG latency, with no experimental results. The request asked
for one relevant paper example, a first comparison, and an exercise.

Observed: [the response](learn-response.md) distinguished the source's training
comparison from the proposed caching experiment, included a simple similarity
cache baseline, accounted for intent/caching/fallback overhead, and gave a
focused query-pair exercise. It treated effectiveness as an unanswered question.

Both outputs stayed within the requested services rather than issuing an Oral
score, an acceptance prediction, a fabricated result, or an abandonment verdict.
The output/provenance pairs retain actual model, effort, usage and input hashes.

These are two bounded behavior demonstrations, not a blinded A/B comparison,
independent scientific evaluation, human learning study, or measured evidence
that the Skill improves manuscripts. The synthetic idea is not a research
result; the rewrite is not a modification endorsed by the paper's authors.
