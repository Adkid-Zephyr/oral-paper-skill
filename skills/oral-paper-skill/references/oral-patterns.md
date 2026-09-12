# Sources, reading levels, and current evidence

Updated 2026-09-12. This file distinguishes the project's learning materials from completed corpus analysis. A paper appearing here is not evidence that every page was deeply read.

## Historical index

The September 2 extraction log reported these official Oral entries:

| Cycle | Entries |
|---|---:|
| ICLR 2025 | 213 |
| ICLR 2026 | 223 |
| ICML 2025 | 120 |
| ICML 2026 | 169 |
| NeurIPS 2024 | 72 |
| NeurIPS 2025 | 87 |
| Total | 884 |

The same run reported 883 available abstracts. The raw index and collection scripts were not included in the initial release. These are historical extraction counts, not a newly verified count of 884 unique full papers. Rebuild the manifest, resolve event-to-paper IDs, check duplicates and exclusions, and report any changed denominator.

Official starting points:

- [ICLR 2025](https://iclr.cc/virtual/2025/events/oral)
- [ICLR 2026](https://iclr.cc/virtual/2026/events/oral)
- [ICML 2025](https://icml.cc/virtual/2025/events/oral)
- [ICML 2026](https://icml.cc/virtual/2026/events/oral)
- [NeurIPS 2024](https://neurips.cc/virtual/2024/events/oral)
- [NeurIPS 2025](https://neurips.cc/virtual/2025/events/oral)

## Completed and pending work

- **Completed historically:** index/abstract extraction; keyword-based scans and rough classifications; selected text passages and rendered figure pages from eight ICLR papers; official award-commentary reading.
- **Not established:** structured semantic extraction for every abstract; a full-text deep-reading sample spanning all six archetypes and all three venues; full-paper distillation of 884 papers.
- **Unavailable in the original reading run:** OpenReview reviews and author responses, because access was blocked. No actual reviewer objections were verified.
- **Not measured:** improvement over ordinary prompting, time savings, acceptance probability, or durable impact of the Skill.
- The early keyword counts cannot establish argument quality. Detecting “however,” “we propose,” or digits is not semantic evidence for the ORAL framework.
- The original dry runs were author-generated examples and self-reviews. File validation checks packaging, not user benefit.

The work needed to complete abstract-level extraction is specified in [the repository research plan](https://github.com/Adkid-Zephyr/oral-paper-skill/blob/main/docs/ABSTRACT_DISTILLATION.md). Applying the installed Skill does not require that plan.

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

ORAL is currently an editorial framework inspired by these materials and general research practice. It is useful as a set of questions to consider, not a measured law shared by all papers.

Future rules should connect an inspected source practice to a purpose, an application, and an exception. Record whether evidence comes from an abstract, a full-text passage, a figure, or committee commentary. General guidance without an exemplar remains valid if labeled as general guidance.

Abstract-level extraction may describe framing, stated novelty, and author-reported evidence. Experimental adequacy, causal identification, plot design, and proof correctness require their own relevant sources. Do not infer them from an abstract or from a paper's selection status.
