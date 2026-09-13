#!/usr/bin/env python3
"""Assemble final synthesis only after complete coverage and source-check resolution."""
import json

from distill_abstracts import BASE, save


def main():
    review = json.loads((BASE / "review_summary.json").read_text())
    if not review["random_coverage_matches_frozen_36"] or review["pending_targeted_ids"] or review["pending_synthesis_flag_ids"] or review["correction_application_errors"] or review.get("unhandled_review_findings"):
        raise RuntimeError("Source-review coverage or explicit corrections remain pending")
    manifest = json.loads((BASE / "synthesis_batches.json").read_text())
    if manifest["prepared_papers"] != manifest["eligible"]:
        raise RuntimeError("Full corpus not represented in synthesis")
    batches, covered = [], []
    for batch in manifest["batches"]:
        path = BASE / "synthesis" / (batch["batch_id"] + ".json")
        result = json.loads(path.read_text())
        if set(result["covered_ids"]) != set(batch["paper_ids"]) or len(result["covered_ids"]) != len(batch["paper_ids"]):
            raise RuntimeError(f"Coverage mismatch in {batch['batch_id']}")
        covered.extend(result["covered_ids"])
        # Coverage is verified mechanically; avoid sending the same roster twice.
        batches.append({k: v for k, v in result.items() if k != "covered_ids"})
    if len(covered) != len(set(covered)) or len(covered) != manifest["eligible"]:
        raise RuntimeError("Duplicate or incomplete cross-batch coverage")
    resolutions, reviewed_ids = [], set()
    for path in sorted((BASE / "reviews").glob("*.json")):
        if "provenance" in path.name:
            continue
        result = json.loads(path.read_text())
        for record in result["records"]:
            reviewed_ids.add(record["paper_id"])
            if record.get("findings") or record.get("resolution"):
                resolutions.append(dict(record, review_file=path.name))
    # Supply current checked cards used as supporting/contrasting examples;
    # irrelevant metadata, raw logs and duplicate source hashes are omitted.
    referenced = set()
    for batch in batches:
        for practice in batch.get("candidate_practices", []):
            referenced.update(r["paper_id"] for r in practice.get("support", []) + practice.get("contrasts", []))
    full_reviewed_ids = set()
    for prefix in ("pilot-", "audit-"):
        for path in (BASE / "reviews").glob(prefix + "*.json"):
            if "provenance" not in path.name:
                full_reviewed_ids.update(r["paper_id"] for r in json.loads(path.read_text())["records"])
    available = reviewed_ids & referenced
    selected = []
    for cycle in ("iclr-2025", "iclr-2026", "icml-2025", "icml-2026", "neurips-2024", "neurips-2025"):
        pool = sorted((pid for pid in available if pid.startswith(cycle + "-")), key=lambda pid: (pid not in full_reviewed_ids, pid))
        selected.extend(pool[:8])
    current_cards = []
    for pid in selected:
        card = json.loads((BASE / "cards" / (pid + ".json")).read_text())
        current_cards.append({"identity": card["identity"], "extraction": card["extraction"]})
    data = {"coverage": {"official_event_records": 884, "eligible_abstracts": len(covered), "batches": len(batches)},
            "review_summary": review, "batch_syntheses": batches, "source_review_resolutions": resolutions,
            "current_reviewed_example_cards": current_cards,
            "example_pool_selection": "Up to eight supported/contrasting example cards per cycle, prioritizing full pilot/random-source reviewed cards; a bounded pool to reduce duplicate context, not a representativeness claim.",
            "note": "Targeted source checks are not full-card reviews. Final selected examples still require direct original-abstract checking. No full-paper or user-benefit inference."}
    output = BASE / "runs/final-synthesis-input.json"
    save(output, data)
    print(json.dumps({"input_file": str(output), "characters": output.stat().st_size,
                      "batches": len(batches), "current_example_cards": len(current_cards)}))


if __name__ == "__main__":
    main()
