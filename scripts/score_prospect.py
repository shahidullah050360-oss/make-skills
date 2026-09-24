#!/usr/bin/env python3
"""Compute the internal prospect workflow score per Master Prompt Section 8.

This is a workflow triage score, not a Google ranking score.

Usage:
    python3 score_prospect.py --relevance 25 --editorial 15 --audience 10 \
        --organic 10 --authority 7 --contactability 5 --content-quality 4
"""
import argparse
import json
from pathlib import Path

RUBRIC_PATH = Path(__file__).resolve().parent.parent / "config" / "scoring_rubric.json"


def classify(total: int, rubric: dict) -> str:
    for band in rubric["bands"]:
        if band["min"] <= total <= band["max"]:
            return band["label"]
    return "UNKNOWN"


def main() -> None:
    rubric = json.loads(RUBRIC_PATH.read_text())
    weights = rubric["weights"]

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--relevance", type=int, required=True, help=f"0-{weights['topical_relevance']}")
    parser.add_argument("--editorial", type=int, required=True, help=f"0-{weights['editorial_quality']}")
    parser.add_argument("--audience", type=int, required=True, help=f"0-{weights['audience_fit']}")
    parser.add_argument("--organic", type=int, required=True, help=f"0-{weights['organic_visibility']}")
    parser.add_argument("--authority", type=int, required=True, help=f"0-{weights['authority']}")
    parser.add_argument("--contactability", type=int, required=True, help=f"0-{weights['contactability']}")
    parser.add_argument("--content-quality", type=int, required=True, help=f"0-{weights['content_quality']}")
    args = parser.parse_args()

    fields = {
        "topical_relevance": args.relevance,
        "editorial_quality": args.editorial,
        "audience_fit": args.audience,
        "organic_visibility": args.organic,
        "authority": args.authority,
        "contactability": args.contactability,
        "content_quality": args.content_quality,
    }

    for name, value in fields.items():
        cap = weights[name]
        if not 0 <= value <= cap:
            raise SystemExit(f"{name} must be between 0 and {cap} (got {value})")

    total = sum(fields.values())
    print(f"Total Score: {total}/{rubric['max_score']}")
    print(f"Classification: {classify(total, rubric)}")


if __name__ == "__main__":
    main()
