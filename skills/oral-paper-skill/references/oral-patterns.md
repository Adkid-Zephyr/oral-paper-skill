# Sources, reading levels, and current evidence

Updated 2026-09-13. This file distinguishes abstract-level evidence, earlier reading leads, and what has actually been checked. A paper appearing here is not evidence that every page was deeply read.

## Rebuilt corpus and completed abstract-level work

The six official lists were rebuilt. Entry counts remain:

| Cycle | Entries |
|---|---:|
| ICLR 2025 | 213 |
| ICLR 2026 | 223 |
| ICML 2025 | 120 |
| ICML 2026 | 169 |
| NeurIPS 2024 | 72 |
| NeurIPS 2025 | 87 |
| Total | 884 |

One ICML 2026 entry points to a [workshop/session](https://icml.cc/virtual/2026/workshop/54094), not a paper. It is retained as excluded; 883 abstracts are eligible. No duplicate entry IDs, event URLs, or normalized titles were found. The public index stores identities, source links and hashes; raw source pages and full abstracts are retained locally.

All 883 eligible abstracts received one-paper-per-context Luna extraction. Astra medium performed 21 batch syntheses, the 24-paper pilot review, a separately fixed random 36-paper audit, and targeted source checks. Astra xhigh consolidated the results into seven practices. Fourteen selected examples were directly rechecked against original abstracts; one model-class qualifier was restored before publication.

Use [the seven practices and examples](abstract-derived-practices.md) for application. The [run results](https://github.com/Adkid-Zephyr/oral-paper-skill/blob/main/research/abstract_distillation/RESULTS.md) link the index, cards, checks, corrections and available model-usage records. These are AI source checks, not independent human scientific validation.

Official starting points:

- [ICLR 2025](https://iclr.cc/virtual/2025/events/oral)
- [ICLR 2026](https://iclr.cc/virtual/2026/events/oral)
- [ICML 2025](https://icml.cc/virtual/2025/events/oral)
- [ICML 2026](https://icml.cc/virtual/2026/events/oral)
- [NeurIPS 2024](https://neurips.cc/virtual/2024/events/oral)
- [NeurIPS 2025](https://neurips.cc/virtual/2025/events/oral)

## Scope and historical boundary

- **Before this run:** the initial release used index/abstract extraction, keyword scans, rough classifications, selected passages and figures from eight ICLR papers, and award commentary. That stage did not complete per-abstract semantic distillation.
- **Completed in this run:** semantic records for all 883 eligible abstracts, cross-batch synthesis, source-check correction trails, and seven curated practices with checked examples.
- **Not established:** full-paper distillation, a systematic full-text/figure sample covering every type and venue, or verification of the underlying scientific claims.
- **Unavailable in the original reading run:** OpenReview reviews and author responses, because access was blocked. No actual reviewer objections were verified.
- **Not measured:** improvement over ordinary prompting, time savings, acceptance probability, or durable impact of the Skill.
- The early keyword counts cannot establish argument quality. Detecting “however,” “we propose,” or digits is not semantic evidence for the ORAL framework.
- The original dry runs were author-generated examples and self-reviews. File validation checks packaging, not user benefit.

The [repository workflow](https://github.com/Adkid-Zephyr/oral-paper-skill/blob/main/docs/ABSTRACT_DISTILLATION.md) describes the process. Applying the installed Skill does not require rerunning the corpus.

## Original ICLR case-study leads

The initial work downloaded PDFs and inspected selected sections and figures of these papers. Treat these as retrieval leads; inspect the relevant original material again before making a specific attributed comparison. Do not infer uniform complete reading or current paper versions from this list.

- [SWE-bench](https://arxiv.org/abs/2310.06770), ICLR 2024.
- [Scaling LLM Test-Time Compute Optimally](https://arxiv.org/abs/2408.03314), ICLR 2025.
- [Limits to Scalable Evaluation at the Frontier](https://arxiv.org/abs/2410.13341), ICLR 2025.
- [Trust or Escalate](https://arxiv.org/abs/2407.18370), ICLR 2025.
- [Gaia2](https://arxiv.org/abs/2602.11964), ICLR 2026.
- [AstaBench](https://arxiv.org/abs/2510.21652), ICLR 2026.
- [Reliable Weak-to-Strong Monitoring](https://arxiv.org/abs/2508.19461), ICLR 2026.
- [CyberGym](https://arxiv.org/abs/2506.02548), ICLR 2026.

## Official award commentary

The initial synthesis also consulted these announcements. Committee explanations describe particular award judgments; they do not establish the causes of Oral selection across the corpus.

- [ICLR 2025 awards](https://blog.iclr.cc/2025/04/22/announcing-the-outstanding-paper-awards-at-iclr-2025/)
- [ICLR 2026 awards](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/)
- [ICML 2026 awards](https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/)
- [NeurIPS 2024 awards](https://blog.neurips.cc/2024/12/10/announcing-the-neurips-2024-best-paper-awards/)
- [NeurIPS 2025 awards](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)

## Learning guidance versus empirical findings

The seven practices are editorial guidance distilled from the abstract material, not measured laws shared by every paper. The older ORAL mnemonic remains optional; it was not treated as the answer the corpus had to confirm.

Connect an inspected source practice to a purpose, an application, and an exception. Record whether evidence comes from an abstract, full-text passage, figure, or committee commentary. General guidance without an exemplar remains valid if labeled as such. Source-review corrections override earlier synthesis snapshots when they disagree.

Abstract-level extraction may describe framing, stated novelty, and author-reported evidence. Experimental adequacy, causal identification, plot design, and proof correctness require their own relevant sources. Do not infer them from an abstract or from a paper's selection status.
