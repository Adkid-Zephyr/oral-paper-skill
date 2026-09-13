# Abstract-level distillation: run results

Run date: 2026-09-13 (Europe/London).

Completed: per-abstract extraction, 21 batch syntheses, source-check corrections,
Astra xhigh final synthesis, seven-practice Skill integration, and two
fresh-context usage checks. Fourteen selected publication examples were checked
directly against original abstracts; one model-class qualifier was restored.

[Seven practices and examples](../../skills/oral-paper-skill/references/abstract-derived-practices.md)
· [Final synthesis](final_synthesis.json) · [Example check](final_examples_review.json)
· [Usage-check outputs and limits](behavior/README.md)

## What was actually processed

| Conference cycle | Official indexed entries | Eligible abstracts |
|---|---:|---:|
| ICLR 2025 | 213 | 213 |
| ICLR 2026 | 223 | 223 |
| ICML 2025 | 120 | 120 |
| ICML 2026 | 169 | 168 |
| NeurIPS 2024 | 72 | 72 |
| NeurIPS 2025 | 87 | 87 |
| Total | 884 | 883 |

The extra ICML 2026 entry, `icml-2026-oral-83917`, points to
[a workshop/session event](https://icml.cc/virtual/2026/workshop/54094), not a
paper. It remains in the index with an exclusion status. No duplicates were
found by entry ID, event URL, or normalized title; this is not an external
bibliographic-ID deduplication study.

All 883 eligible abstracts have a structured card with problem/gap,
contribution, author-reported evidence, narrative sequence, candidate lessons,
unknowns, source locators/hashes and execution provenance. The collector
retrieved the six official index pages, rather than issuing 884 page requests.

## Model division and actual execution

- **GPT-5.6 Luna, low:** 883 one-paper-per-context extraction calls, using the
  existing local Codex ChatGPT login and CLI 0.147.0.
- **GPT-6 Astra, medium:** source checking and 21 non-overlapping batch
  syntheses, each covering at most 48 cards. CLI calls used the application's
  existing CLI 0.153.4; other source checks used explicitly configured agents.
- **GPT-6 Astra, xhigh:** final cross-batch selection and editorial synthesis.
  The completed call reported 197,002 input and 8,959 output tokens, with 4,645
  reasoning-output tokens separately reported. See its [provenance](final_synthesis.json.provenance.json).

No new separately billed API backend or usage-reset credit was used. Raw
input/output/log files remain local; no credentials were copied into the repo.

## Checks and corrections

- All 24 purposively selected pilot cards received original-abstract checking.
  Initial results: 1 material-error card, 7 minor, 16 pass. Eleven field changes
  across eight cards were subsequently checked against their sources.
- A separately frozen, stratified random sample of 36 cards excluded the pilot.
  Initial results: 2 material-error cards, 14 minor, 20 pass. These are sample
  extraction-review outcomes, not a corpus-wide accuracy estimate.
- Eighteen source records with future-release wording received targeted
  temporal checks after one drift was found. This set overlaps other checks.
- The synthesizer flagged 184 distinct papers for source checks. All flags
  were resolved against original abstracts. Targeted outcomes: 20 material,
  21 minor, 143 pass. A flag is not itself an error, and this is not a random
  or necessarily full-card audit.
- Across these reviews, 86 explicitly reviewed fields in 65 distinct cards
  were corrected. Initial reviews and before/after editorial trails remain
  available. These counts do not mean 65 original papers were wrong.

One Luna output serialized optional JSON `null` as the string `"null"`. It was
initially quarantined, then normalized without another model call. Thus the
original extraction ledger retains **882 completed + 1 failed validation**,
while the canonical card verification passes for **883/883**. This is an
intentional retained failure trail, not a missing card or a hidden retry.

## Usage and reproducibility

The 883 extraction calls reported 11,303,299 input tokens, including 9,917,952
cached input tokens, and 693,614 output tokens. Reasoning output was reported
separately as 76,198 tokens; these fields should not be blindly added together.
Per-call usage and outcomes are in [the ledger](call_ledger.jsonl).

Astra CLI analyses have adjacent `.provenance.json` records. Agent-orchestration
usage and transport probes are not included in the extraction totals, so these
numbers are not a complete project bill or a subscription-percentage estimate.

Batch synthesis inputs are retained as local snapshots. Later source-review
corrections can supersede their wording; final curation must use the correction
records and current cards rather than silently treating an old batch as current.

[Collection](corpus/collection_summary.json) · [Public index](corpus/index.jsonl)
· [Card verification](verification.json) · [Review summary](review_summary.json)
· [Pilot gate](pilot_review.json) · [Extraction prompt](extraction_prompt.txt)

## Scope

This is AI-assisted, abstract-level knowledge extraction and synthesis. It does
not verify full papers, figures, experiments, proofs, true novelty, reviewers'
opinions, or why a paper was selected for Oral presentation. Source checking is
AI checking, not independent human scientific review. No manuscript-quality
gain, time saving, acceptance probability, or Skill effectiveness has been
measured. The final selected examples were checked against original abstracts
before being promoted to the Skill; fresh-context checks assessed two bounded
outputs, not comparative or general effectiveness.
