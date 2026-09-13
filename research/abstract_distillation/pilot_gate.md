# Abstract extraction pilot and source audit

This is an operational quality gate for source-faithful extraction, not a test
of scientific validity, Oral selection factors, or whether the Skill improves
manuscripts. No batch has passed merely because these instructions exist.

## Pilot: 24 source-linked cards

Choose 24 eligible abstracts across all six conference cycles, aiming for four
per cycle. Within that coverage include varied contribution types, lengths,
qualitative and numerical claims, and difficult or ambiguous abstracts. Save
the selected IDs and selection procedure before extraction. Do not silently
replace failures or choose only convenient examples.

Run each abstract in an independent context. Retain original source units,
source hash, raw response, parsed card, model/configuration, prompt/schema
versions, attempt status, and actual usage where available. Missing usage is
unknown, never zero. Do not infer dollar cost without applicable pricing.

For all 24 cards, the runner checks JSON/schema, exact identity, abstract-only
reading level, and every locator against that paper's supplied units. A
non-null sourced claim must have support IDs; null claims must have none.
Check 0–2 lessons and flag prose exceeding the 400-word target for compression;
a small length overrun alone is not a semantic failure.

An Astra reviewer at medium reasoning reads every one of the 24 original
abstracts alongside its card. The review is AI source checking, not independent
scientific validation. For each card record reviewed status, affected field,
source IDs, material errors, proposed correction, and final disposition.
The reviewer checks actual entailment rather than only valid locators:

- Attribution and scope: no invented result, method, novelty, condition, or
  author practice; no claim strengthened beyond the abstract.
- Faithfulness: preserve direction, important qualifiers, units and comparator
  when reporting numbers; no central contribution lost through a misleading
  summary; no proposed activity presented as completed evaluation.
- Learning value: observation is supported; interpretation and proposed
  application are visibly distinct; exceptions are plausible; do not invent
  a lesson to satisfy a quota.
- Narrative and unknowns: actual sequence is represented; material uncertainty
  stays explicit without alleging that unseen full-paper content is absent.

Material errors change a reader's understanding of the paper, its evidence,
or the source basis for a suggested practice. Minor wording or optional detail
is not a material error. Record first-pass errors as well as corrected results;
do not erase them by reporting only the final pass.

Correct affected cards. If a recurring error suggests a prompt/schema or
segmentation defect, fix that cause and re-extract affected pilot cards; review
new outputs and any other pilot cards implicated by the same defect. Keep
revisions traceable. An unresolved ambiguous interpretation can be removed or
marked unknown rather than repeatedly optimized into a positive finding.

Proceed to the full eligible corpus only when all 24 have intact locators and
completed semantic review with no remaining material fabrication or
misattribution (including unsupported strengthening). Other material errors
must likewise be corrected or explicitly resolved by omission/unknown. Freeze
the extraction configuration and report measured pilot usage, first-pass
material error counts, corrections, and estimated remaining input/output usage.
If those conditions fail, retain partial results and repair the extraction
method before expansion. This gate requires no additional owner questionnaire.

## Full run and an additional 36-card audit

After the gate, extract every eligible record with visible failed/missing
statuses and resumable attempts. Apply mechanical checks to every output.
Review all automatically flagged or genuinely difficult cases separately.

Select 36 additional cards, excluding the pilot, by a recorded random seed
within conference-cycle strata (target six per cycle). Spread selection across
available contribution types where practical and document any allocation
shortfall or oversampling. Do not call convenience-selected difficult cases a
random sample. Astra at medium checks these 36 against original abstracts
using the same semantic rubric. Report their first-pass errors separately
from targeted review and pilot errors, with denominators and corrections.

When an audit error reveals a systematic failure pattern, identify affected
records across the corpus and repair/review that subset. Expand review only
where the observed failure justifies it. Preserve the original sample outcome
even after fixes; unresolved errors remain visible in final coverage/status.

Report extraction success, missing abstracts, failures, reviewed records and
unreviewed records separately. The 36-card audit is a limited source-quality
check; it does not establish that all other cards are accurate, validate
scientific claims, or measure lesson effectiveness. Synthesis must retain
source links and tentative applicability, and consult original abstracts
again when a rule depends on a disputed or thinly supported interpretation.
