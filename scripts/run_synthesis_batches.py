#!/usr/bin/env python3
"""Run bounded Astra-medium synthesis jobs and verify identity/locator coverage."""
import argparse
import fcntl
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import subprocess
import sys
import threading

from distill_abstracts import BASE, ROOT, digest, now, save


def check(result, packet):
    ids = {x["identity"]["paper_id"] for x in packet["cards"]}
    covered = result.get("covered_ids", [])
    if result.get("batch_id") != packet["batch_id"] or set(covered) != ids or len(covered) != len(ids):
        raise ValueError("Synthesis did not preserve exact batch identity/coverage")
    card_units = {pid: {u["id"] for u in json.loads((BASE / "cards" / f"{pid}.json").read_text())["source_units"]} for pid in ids}

    def walk(value):
        if isinstance(value, dict):
            if "paper_id" in value:
                pid = value["paper_id"]
                if pid not in ids:
                    raise ValueError(f"Invented or out-of-batch paper: {pid}")
                if "source_ids" in value and (not value["source_ids"] or not set(value["source_ids"]) <= card_units[pid]):
                    raise ValueError(f"Invalid synthesis locator: {pid}")
            if "paper_ids" in value and not set(value["paper_ids"]) <= ids:
                raise ValueError("Out-of-batch paper IDs")
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)
    walk(result)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--codex-bin", default="codex")
    p.add_argument("--workers", type=int, default=2)
    p.add_argument("--cycles", nargs="+", help="Disjoint conference strata for an overlapping synthesis driver")
    args = p.parse_args()
    batches = json.loads((BASE / "synthesis_batches.json").read_text())["batches"]
    if args.cycles:
        batches = [b for b in batches if any(b["batch_id"].startswith(cycle + "-") for cycle in args.cycles)]
    progress_file = BASE / ("synthesis_progress-" + "_".join(args.cycles) + ".json" if args.cycles else "synthesis_progress.json")
    prompt = BASE / "synthesis_prompt.txt"
    lock = threading.Lock()
    state = {"stage": "batch_synthesis", "total_batches": len(batches), "completed": 0,
             "cached": 0, "failed": 0, "started_at": now(), "status": "running"}

    def run_unlocked(batch):
        input_file = BASE / batch["input_file"]
        packet = json.loads(input_file.read_text())
        output = BASE / "synthesis" / (batch["batch_id"] + ".json")
        cached = output.exists()
        if not cached:
            cmd = [sys.executable, str(ROOT / "scripts/run_astra_analysis.py"), "--prompt", str(prompt),
                   "--input", str(input_file), "--output", str(output), "--effort", "medium", "--codex-bin", args.codex_bin]
            result = subprocess.run(cmd, text=True, capture_output=True, cwd=ROOT)
            if result.returncode:
                raise RuntimeError(f"Batch {batch['batch_id']} failed: {result.stdout[-1500:]}")
        provenance = json.loads(output.with_suffix(output.suffix + ".provenance.json").read_text())
        if provenance["status"] != "completed" or provenance["input_sha256"] != digest(input_file.read_text()):
            raise RuntimeError(f"Stale or failed batch provenance: {batch['batch_id']}")
        check(json.loads(output.read_text()), packet)
        with lock:
            state["cached" if cached else "completed"] += 1
            save(progress_file, state)
            print(json.dumps(state), flush=True)

    def run(batch):
        locks = BASE / "runs/synthesis-locks"
        locks.mkdir(parents=True, exist_ok=True)
        with (locks / (batch["batch_id"] + ".lock")).open("w") as handle:
            try:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise RuntimeError(f"Another driver owns synthesis batch {batch['batch_id']}")
            run_unlocked(batch)

    save(progress_file, state)
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for future in as_completed([pool.submit(run, batch) for batch in batches]):
            try:
                future.result()
            except Exception as exc:
                with lock:
                    state["failed"] += 1
                    state.setdefault("errors", []).append(str(exc))
                    save(progress_file, state)
                    print(str(exc), flush=True)
    state["status"] = "failed" if state["failed"] else "completed"
    state["finished_at"] = now()
    save(progress_file, state)
    return 1 if state["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
