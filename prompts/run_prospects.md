# RUN PROSPECTS

Discovers and qualifies prospects (Master Prompt Sections 7-11).

## Discovery sources

- Editorial/resource-page opportunities surfaced via competitor gap analysis (`run_competitors.md`).
- Original research / statistics citation opportunities relevant to the site's niche.
- Broken-link opportunities — only where evidence exists (a verified 404/dead page with a live, real replacement), never guessed.
- Journalist/source opportunities (e.g. HARO-style requests) — record only real, sourced requests.

## Per-prospect data (all fields in `data/04_Prospects.csv`)

Fill every column. Use `UNKNOWN` for anything that cannot be verified —
never invent a contact name, email, or metric.

## Scoring

Run `python3 scripts/score_prospect.py --relevance N --editorial N --audience N --organic N --authority N --contactability N --content-quality N` for each candidate and record the printed Total Score + classification. Weights and bands live in `config/scoring_rubric.json`.

## Deduplication

Before adding a new row, run
`python3 scripts/normalize_domain.py --dedupe-csv data/04_Prospects.csv --column Domain`
and resolve any reported duplicates. One domain may have more than one row
only when the opportunities are genuinely different and editorially
meaningful.

## Risk screening

Check every candidate against `config/risk_signals.json` → `signals`. Use
the literal phrase "Risk signal detected" in the `Risk Flags` column when
evidence is uncertain; do not make a definitive accusation.

## Below-50 handling

Reject (`Status = REJECTED`) unless there is a documented reason to retain
it in the `Reason` column.
