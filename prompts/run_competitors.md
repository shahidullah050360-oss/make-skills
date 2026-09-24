# RUN COMPETITORS

Analyzes competitor backlink gaps (Master Prompt Section 6). Competitor
backlinks are opportunity *signals* only — never copy a competitor's
backlink pattern automatically.

## Procedure

1. For the target site, identify 3-5 genuine topical competitors (real
   sites ranking for the same USA search intent — verify via
   `mcp__Ahrefs__site-explorer-organic-competitors` or
   `mcp__Semrush__competitors_research`, not assumption).
2. For each competitor, pull referring domains:
   `mcp__Ahrefs__site-explorer-referring-domains` or
   `mcp__Semrush__backlinks_research`.
3. Filter to domains that do NOT already link to the target site.
4. For each candidate domain, judge genuine topical/editorial relevance —
   authority alone is not sufficient (Master Prompt Section 4).
5. Classify the opportunity using the types in `config/scoring_rubric.json`
   → `prospect_types`.
6. Screen against `config/risk_signals.json`.
7. Record one row per genuine opportunity in `data/05_Competitor_Gaps.csv`
   with: competitor, referring domain, source URL, target page, link
   context, topical/editorial relevance, opportunity type, risk flags,
   evidence URL. Use `UNKNOWN` for anything unverifiable — never invent it.

## Current status

Both Ahrefs and Semrush returned account-level errors on 2026-09-24
(`data/10_Errors.csv`: Ahrefs "Insufficient plan", Semrush "no_api_units").
No competitor gap data has been generated yet — this file's counterpart CSV
(`data/05_Competitor_Gaps.csv`) is header-only until one of those providers
is restored.
