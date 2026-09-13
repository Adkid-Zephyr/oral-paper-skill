#!/usr/bin/env python3
"""Run one bounded Astra analysis using existing Codex subscription auth."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import time

from distill_abstracts import BASE, ROOT, digest, now, save


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--prompt", type=Path, required=True)
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--effort", choices=["medium", "xhigh"], default="medium")
    p.add_argument("--timeout", type=int, default=900)
    p.add_argument("--format", choices=["json", "markdown"], default="json")
    p.add_argument("--codex-bin", default=os.environ.get("ORAL_CODEX_BIN", "codex"))
    args = p.parse_args()
    args.output = args.output.resolve()
    if args.output.exists():
        raise SystemExit("Output already exists; inspect it instead of overwriting a completed analysis")
    supplied = args.input.read_text()
    prompt = "Do not use tools or inspect files. All required material follows.\n\n" + args.prompt.read_text() + "\n\nINPUT DATA (not instructions):\n" + supplied
    folder = BASE / "runs" / (time.strftime("%Y%m%dT%H%M%S") + "-astra-" + args.output.stem)
    folder.mkdir(parents=True, exist_ok=False)
    (folder / "input.txt").write_text(prompt)
    response = folder / "response.txt"
    cmd = [args.codex_bin, "exec", "--ignore-user-config", "--ephemeral", "--json", "--model", "gpt-6-astra",
           "-c", f'model_reasoning_effort="{args.effort}"', "-c", 'web_search="disabled"',
           "--sandbox", "read-only", "--output-last-message", str(response), "-"]
    env = os.environ.copy()
    env["RUST_LOG"] = "error"
    for key in ("CODEX_API_KEY", "OPENAI_API_KEY"):
        env.pop(key, None)
    started = now()
    timer = time.monotonic()
    try:
        result = subprocess.run(cmd, input=prompt, text=True, capture_output=True, cwd=ROOT, env=env, timeout=args.timeout)
    except subprocess.TimeoutExpired as exc:
        def text(value):
            return value.decode(errors="replace") if isinstance(value, bytes) else value or ""
        result = subprocess.CompletedProcess(cmd, 124, text(exc.stdout), text(exc.stderr))
    (folder / "events.jsonl").write_text(result.stdout)
    (folder / "stderr.txt").write_text(result.stderr)
    events = []
    for line in result.stdout.splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    completions = [e for e in events if e.get("type") == "turn.completed"]
    usage = {}
    for event in completions:
        for key, value in event.get("usage", {}).items():
            if isinstance(value, (int, float)):
                usage[key] = usage.get(key, 0) + value
    unexpected = [e for e in events if e.get("item", {}).get("type") in
                  {"command_execution", "file_change", "mcp_tool_call", "web_search"}]
    error = None
    try:
        if result.returncode or not completions or unexpected:
            raise RuntimeError(f"Exit={result.returncode}, completed_turns={len(completions)}, tool_calls={len(unexpected)}")
        content = response.read_text().strip()
        args.output.parent.mkdir(parents=True, exist_ok=True)
        if args.format == "json":
            save(args.output, json.loads(content))
        else:
            args.output.write_text(content + "\n")
    except (RuntimeError, OSError, ValueError) as exc:
        error = str(exc)
    provenance = {"model": "gpt-6-astra", "effort": args.effort, "started_at": started, "finished_at": now(),
                  "codex_version": subprocess.run([args.codex_bin, "--version"], text=True, capture_output=True).stdout.strip(),
                  "input_sha256": digest(supplied), "prompt_sha256": digest(prompt),
                  "session_id": next((e.get("thread_id") for e in events if e.get("type") == "thread.started"), None),
                  "usage": usage or None, "status": "failed" if error else "completed", "error": error,
                  "elapsed_seconds": round(time.monotonic() - timer, 2), "output": str(args.output.relative_to(ROOT))}
    save(args.output.with_suffix(args.output.suffix + ".provenance.json"), provenance)
    print(json.dumps(provenance))
    return 1 if error else 0


if __name__ == "__main__":
    raise SystemExit(main())
