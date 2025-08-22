#!/usr/bin/env python3
"""
Convert YAML question banks in ../question-banks/*.yaml to GIFT files
saved alongside each YAML as *.gift for easy TalentLMS import.

Supported types: multiple choice (mc), true/false (tf)
"""
import sys
import os
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]  # courses/ai-foundations
QB_DIR = ROOT / "question-banks"

GIFT_HEADER = """
// Generated from YAML by build_questions.py
""".lstrip()

def to_gift(qset: dict) -> str:
    title = qset.get("title", "Untitled")
    chunks = [f"// Quiz: {title}", ""]
    for i, q in enumerate(qset.get("questions", []), start=1):
        qtype = str(q.get("type", "")).strip().lower()
        stem = str(q.get("stem", "")).strip()
        name = q.get("name") or f"Q{i}"
        if not stem:
            continue
        if qtype == "mc":
            options = q.get("options", [])
            answer = q.get("answer")
            # Build answer block: '=' for correct, '~' for incorrect
            lines = []
            for opt in options:
                marker = '=' if str(opt) == str(answer) else '~'
                lines.append(f" {marker} {opt}")
            block = "{
" + "
".join(lines) + "
}"
            chunks.append(f"::{name}:: {stem} 
{block}
")
        elif qtype == "tf":
            ans = str(q.get("answer", "")).strip().lower()
            if ans in {"true", "t", "1", "yes"}:
                block = "{T}"
            else:
                block = "{F}"
            chunks.append(f"::{name}:: {stem} 
{block}
")
        else:
            # Unknown type: skip gracefully
            continue
    return GIFT_HEADER + "
".join(chunks)


def main(argv=None):
    argv = argv or sys.argv[1:]
    out_dir = QB_DIR
    if not QB_DIR.exists():
        print(f"question-banks directory not found: {QB_DIR}", file=sys.stderr)
        return 1
    yaml_files = sorted(QB_DIR.glob("*.yaml"))
    if not yaml_files:
        print("No YAML files found in question-banks/", file=sys.stderr)
        return 1
    for yf in yaml_files:
        with open(yf, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        gift = to_gift(data)
        out_path = yf.with_suffix(".gift")
        with open(out_path, "w", encoding="utf-8") as out:
            out.write(gift)
        print(f"Wrote {out_path.relative_to(ROOT)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())