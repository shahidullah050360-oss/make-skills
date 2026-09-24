#!/usr/bin/env python3
"""Normalize and deduplicate domains per Master Prompt Section 11.

Usage:
    python3 normalize_domain.py "https://www.example.com/path/?utm_source=x"
    python3 normalize_domain.py --dedupe-csv data/04_Prospects.csv --column Domain
"""
import argparse
import csv
import sys
from urllib.parse import urlsplit


def normalize_domain(raw: str) -> str:
    raw = raw.strip()
    if "://" not in raw:
        raw = "http://" + raw
    netloc = urlsplit(raw).netloc or raw
    netloc = netloc.split("@")[-1]  # strip userinfo if present
    netloc = netloc.split(":")[0]  # strip port
    if netloc.lower().startswith("www."):
        netloc = netloc[4:]
    return netloc.lower().rstrip("/")


def dedupe_csv(path: str, column: str) -> None:
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    seen = {}
    duplicates = []
    for row in rows:
        norm = normalize_domain(row.get(column, ""))
        row["_normalized_domain"] = norm
        if norm in seen:
            duplicates.append((row, seen[norm]))
        else:
            seen[norm] = row
    print(f"{len(rows)} rows, {len(seen)} unique normalized domains, {len(duplicates)} duplicate(s).")
    for dup, original in duplicates:
        print(f"  duplicate: {dup.get(column)!r} matches {original.get(column)!r} (normalized: {dup['_normalized_domain']})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("domain", nargs="?", help="A single URL or domain to normalize")
    parser.add_argument("--dedupe-csv", help="Path to a CSV to check for duplicate normalized domains")
    parser.add_argument("--column", default="Domain", help="Column name holding the domain/URL (default: Domain)")
    args = parser.parse_args()

    if args.dedupe_csv:
        dedupe_csv(args.dedupe_csv, args.column)
    elif args.domain:
        print(normalize_domain(args.domain))
    else:
        parser.print_help()
        sys.exit(1)
