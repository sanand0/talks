#!/usr/bin/env python3
"""Deterministic part of CATALOG.md: paths, sizes, counts, date ranges.

Usage: python make_catalog.py <corpus_dir>
Writes CATALOG.draft.md in <corpus_dir>. Add one-line descriptions by hand.
"""
import csv, io, json, re, sys
from pathlib import Path

DATE = re.compile(r"\b(19|20)\d{2}-\d{2}-\d{2}\b")

def describe(p: Path):
    size = p.stat().st_size
    tokens = size // 4
    rows, dates = "", ""
    try:
        text = p.read_text(errors="ignore")
        if p.suffix.lower() in (".csv", ".tsv"):
            rows = f"{max(0, text.count(chr(10)) - 1)} rows"
        elif p.suffix.lower() in (".json", ".jsonl"):
            if p.suffix.lower() == ".jsonl":
                rows = f"{text.count(chr(10))} records"
            else:
                data = json.loads(text)
                rows = f"{len(data)} records" if isinstance(data, list) else "1 object"
        all_dates = sorted(set(m.group(0) for m in DATE.finditer(text)))
        if all_dates:
            dates = f"{all_dates[0]} to {all_dates[-1]}"
    except Exception:
        pass
    parts = [f"~{tokens:,} tok"]
    if rows: parts.append(rows)
    if dates: parts.append(dates)
    return ", ".join(parts)

def main():
    root = Path(sys.argv[1])
    lines = ["# Catalog", "", "<!-- Add a one-line description after each entry. -->", ""]
    total = 0
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.name != "CATALOG.draft.md" and not p.name.startswith("."):
            total += p.stat().st_size
            lines.append(f"- `{p.relative_to(root)}` ({describe(p)}): DESCRIBE_ME")
    lines.insert(1, f"\nCorpus total: ~{total // 4:,} tokens across the files below.")
    (root / "CATALOG.draft.md").write_text("\n".join(lines) + "\n")
    print(f"Wrote {root / 'CATALOG.draft.md'} (~{total // 4:,} tokens total). "
          f"Now replace every DESCRIBE_ME.")

if __name__ == "__main__":
    main()
