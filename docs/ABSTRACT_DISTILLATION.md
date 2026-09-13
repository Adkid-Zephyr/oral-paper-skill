# Abstract-level distillation: implementation plan

Status on 2026-09-13: completed for the eligible abstract corpus. Six official
lists yielded 884 records, including one excluded workshop/session event;
883 abstracts received per-paper extraction and 21-group synthesis. Source
checks, corrections, final Astra xhigh synthesis and Skill integration are
complete. See [the actual results](../research/abstract_distillation/RESULTS.md).
No full-paper coverage or measured Skill effectiveness is implied.

## Purpose

Extract useful practices for comparison-based paper improvement and guided
reflection. “Distillation” means synthesizing knowledge into examples and
instructions, not training model weights or predicting conference decisions.

The first corpus is the historical six-cycle Oral index (reported 884 entries,
883 abstracts). Broader full-paper reading remains a possible later extension.
Reviews, rebuttals, slides, videos, and Poster controls are not part of this phase.

## Work sequence

1. **Recover the index.** Collect the six official lists linked in
   [sources](../skills/oral-paper-skill/references/oral-patterns.md). Save retrieval
   dates, event IDs, title, paper ID/URL and reading level in a durable manifest.
   Reconcile duplicates, missing abstracts, and presentation tracks. Report
   actual counts; do not force a reconstructed corpus to equal 884.
2. **Pilot the extraction.** Read 24 diverse abstracts individually. Record
   problem, stated contribution, author-reported evidence, narrative sequence,
   and candidate learning points, each linked to supporting abstract sentences.
   Missing details must remain unknown. Let categories emerge; do not require
   every entry to fit ORAL. Check source accuracy before freezing the schema.
3. **Process every eligible abstract.** Use independent per-paper contexts,
   bounded outputs, resumable jobs, and explicit failed/missing statuses. A
   lower-cost model may extract; a stronger model checks difficult cases and
   a random sample. Retain actual usage for budget estimates.
4. **Synthesize by paper type.** Read evidence cards in manageable groups.
   Propose rules with source examples, purpose, applicability, and exceptions.
   Return to original sources for disputed or weakly supported points. Separate
   frequently observed practices from rare but potentially useful ideas.
5. **Apply and reflect.** Add only actionable lessons to the Skill, keeping
   examples in references. Test on actual manuscript tasks; distinguish a
   demonstration, self-review, independent assessment, and measured benefit.

## Minimal evidence card

- Identity: event ID, paper ID, title, venue/year, source URL, retrieval date.
- Reading level: abstract only, full-text passage, figure, or other explicit level.
- Problem and significance framing, with sentence locators.
- Stated contribution and author-reported evidence, with sentence locators.
- Narrative sequence: what each part of the abstract does.
- Candidate lesson: source observation, interpretation, application, exception.
- Unknowns and extraction issues.
- Extraction record: model/configuration, source hash, output, validation state.

Full abstracts and long excerpts should not be copied into public examples
without checking source terms. Public learning cards should favor original
paraphrases, short necessary excerpts, and links to the authors' work.

## What completion means

Every eligible entry has a source-linked record or a visible failure status.
Candidate rules can be traced back to inspected material. A source-check sample
is reported, including errors and corrections. No abstract-only card claims to
verify figures, experiments, proof correctness, or actual reproducibility.

Only then describe that coverage as completed abstract-level distillation.
Report the successful, missing, and failed counts separately; unresolved entries
must not be included in a claim of completed extraction coverage.
Do not describe full-paper coverage or measured user benefit unless separately
completed and documented. Comparison with a generic prompt on actual drafts
can assess usefulness; it is not required to publish an honestly labeled prototype.

## Cost gate

Use the pilot's measured input/output usage and extraction error rate to
estimate a full run. Retain partial results and retry only failed records.
The owner authorized Luna for extraction, Astra medium for checking/selection,
and Astra xhigh for final synthesis. Calls use the existing local Codex ChatGPT
login; no separately billed API fallback or usage-reset redemption is enabled.
