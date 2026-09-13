#!/usr/bin/env python3
"""Summarize review coverage and verify explicit corrections without hiding first-pass errors."""
from collections import Counter
import json
import re

from distill_abstracts import BASE, now, save


def main():
    groups = {"pilot": [], "random_audit": [], "targeted_temporality": [], "synthesis_flagged": []}
    expected_random = set(json.loads((BASE / "audit_ids.json").read_text())["entry_ids"])
    pilot = set(json.loads((BASE / "corpus/pilot_ids.json").read_text())["entry_ids"])
    for file in sorted((BASE / "reviews").glob("*.json")):
        if "provenance" in file.name:
            continue
        key = next((group for prefix, group in [("pilot-", "pilot"), ("audit-", "random_audit"), ("targeted-", "targeted_temporality"), ("flagged-", "synthesis_flagged")] if file.name.startswith(prefix)), None)
        if key:
            groups[key].extend(json.loads(file.read_text())["records"])
    summary = {}
    for name, records in groups.items():
        ids = [r["paper_id"] for r in records]
        summary[name] = {"records": len(records), "unique_papers": len(set(ids)),
                         "first_check_status_counts": dict(Counter(r.get("first_pass_status", "unknown") for r in records))}
    random_ids = [r["paper_id"] for r in groups["random_audit"]]
    random_coverage_ok = set(random_ids) == expected_random and len(random_ids) == 36 and not (set(random_ids) & pilot)
    corrections, errors = [], []
    for file in (BASE / "pilot_corrections.json", BASE / "audit_corrections.json", BASE / "additional_corrections.json"):
        if not file.exists():
            continue
        for correction in json.loads(file.read_text())["corrections"]:
            value = json.loads((BASE / "cards" / (correction["paper_id"] + ".json")).read_text())["extraction"]
            for key in re.findall(r"[^.\[\]]+", correction["field"]):
                value = value[int(key) if key.isdigit() else key]
            if value != correction["value"]:
                errors.append({"paper_id": correction["paper_id"], "field": correction["field"], "error": "Correction not reflected in current card"})
            corrections.append((correction["paper_id"], correction["field"]))
    flags = set()
    correction_keys = set(corrections)
    unhandled = []
    for group, records in groups.items():
        for record in records:
            for finding in record.get("findings", []):
                field = finding.get("field", "")
                if finding.get("severity") in {"minor", "material", "material_error"} and not field.startswith("synthesis:"):
                    if (record["paper_id"], field) not in correction_keys:
                        unhandled.append({"paper_id": record["paper_id"], "field": field, "group": group})
    for file in (BASE / "synthesis").glob("*.json"):
        if "provenance" not in file.name:
            flags.update(f["paper_id"] for f in json.loads(file.read_text()).get("source_checks_needed", []))
    flagged_reviewed = {r["paper_id"] for r in groups["synthesis_flagged"]}
    targeted_expected = set(json.loads((BASE / "targeted_ids.json").read_text())["entry_ids"])
    targeted_reviewed = {r["paper_id"] for r in groups["targeted_temporality"]}
    report = {"updated_at": now(), "groups": summary, "random_coverage_matches_frozen_36": random_coverage_ok,
              "pending_targeted_ids": sorted(targeted_expected - targeted_reviewed),
              "synthesis_flagged_unique": len(flags), "pending_synthesis_flag_ids": sorted(flags - flagged_reviewed),
              "explicit_field_corrections": len(set(corrections)), "corrected_unique_cards": len({x[0] for x in corrections}),
              "correction_application_errors": errors,
              "unhandled_review_findings": unhandled,
              "limitations": "Reviews are AI source checking. Targeted groups overlap other groups and are not random or necessarily full-card audits. First-check counts in targeted temporality include the explicitly inherited Seer finding, not a new independent error. No corpus-wide accuracy, scientific validity or measured user benefit is established."}
    save(BASE / "review_summary.json", report)
    print(json.dumps({"groups": summary, "random_coverage_matches_frozen_36": random_coverage_ok,
                      "pending_targeted": len(report["pending_targeted_ids"]),
                      "synthesis_flagged": len(flags), "pending_synthesis_flags": len(report["pending_synthesis_flag_ids"]),
                      "explicit_corrections": len(set(corrections)), "corrected_cards": report["corrected_unique_cards"],
                      "application_errors": errors, "unhandled_findings": unhandled}))
    return 1 if errors else 0


if __name__ == "__main__":
    main()
