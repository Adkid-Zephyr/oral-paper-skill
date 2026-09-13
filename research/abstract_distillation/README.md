# Abstract-level knowledge distillation

Run completed on 2026-09-13 (Europe/London). This directory records the actual
abstract-level extraction, synthesis and checks. Start with [the results](RESULTS.md)
or [the seven practices](../../skills/oral-paper-skill/references/abstract-derived-practices.md).

## Execution

- Collection: six official conference Oral lists, with local source snapshots.
- Extraction: one abstract per independent `gpt-5.6-luna` call, low reasoning.
- Source checking and selection: `gpt-6-astra`, medium reasoning.
- Final synthesis and Skill integration: `gpt-6-astra`, xhigh reasoning.
- Authentication: the existing local Codex ChatGPT login. No new API billing,
  credential copying, or automatic redemption of usage-reset credits.

The model identifiers and efforts above are requested execution configuration,
not by themselves evidence of a completed call. Per-card provenance, analysis
provenance and actual call logs document the completed executions.

## Files

- `corpus/index.jsonl`: public record identities, URLs, reading levels and hashes.
- `corpus/collection_summary.json`: collection counts and source provenance.
- `corpus/pilot_ids.json`: the 24 purposively selected calibration records.
- `extraction.schema.json` and `extraction_prompt.txt`: reproducible extraction.
- `cards/`: paraphrased per-paper outputs with source-unit hashes and provenance.
- `call_ledger.jsonl`: actual extraction call outcomes and available usage.
- `progress.json`: current/last driver stage, counts, status and local run path.
- `pilot_gate.md`: semantic review criteria, not a declaration of passing.
- `review_summary.json`: random/targeted coverage, first-pass errors and corrections.
- `final_synthesis.json`: seven selected practices and 14 source-checked examples.
- `behavior/`: two actual fresh-context usage demonstrations, not efficacy tests.

Full source abstracts and raw model logs stay local under ignored paths
`corpus/manifest.jsonl`, `corpus/raw/`, and `runs/`. Public cards use paraphrases,
source URLs and locators, not redistributed full abstracts. Raw execution logs
remain available locally for audit; public counts do not imply full-paper reading.

## Reproduce or resume

```bash
python3 scripts/collect_corpus.py
uv run --with jsonschema python scripts/distill_abstracts.py --stage pilot --workers 3
```

After an actual source-checked `pilot_review.json` PASS bound to the reviewed
configuration and IDs:

```bash
uv run --with jsonschema python scripts/distill_abstracts.py --stage full --workers 6
```

The completed run used eight extraction workers. The original full-run status
retains one format-validation failure, subsequently recovered without another
call; `verification.json` records the 883 valid canonical cards. Do not rerun
the model merely to erase that retained failure status.

Synthesis used `prepare_synthesis.py` and `run_synthesis_batches.py`, with
disjoint conference-cycle jobs. Inputs are frozen snapshots; later source
corrections can supersede their wording. The final synthesis includes those
resolutions and current cards. Reusing a changed input requires an explicit
new analysis version rather than overwriting prior evidence.

Completed cards are reused only when input, schema, prompt, model and effort
match. Three failed records stop dispatching new work; existing evidence is
retained. A single file lock prevents simultaneous extraction drivers.

These are source extraction and AI review records, not scientific validation,
a causal explanation for Oral selection, or a measured effectiveness study.
