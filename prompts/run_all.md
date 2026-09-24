# RUN ALL

Executes the full four-site workflow (Master Prompt Section 34). Never sends
emails, never publishes, never creates or purchases backlinks.

## Steps

1. Validate configuration — read `config/websites.json`, `config/scoring_rubric.json`, `config/risk_signals.json`.
2. Load all websites (the four sites in `config/websites.json`).
3. Load keywords — `data/02_Keywords.csv`.
4. Load competitors — `data/03_Competitors.csv`.
5. Discover opportunities — see `prompts/run_prospects.md`.
6. Analyze competitor gaps — see `prompts/run_competitors.md`.
7. Deduplicate — `python3 scripts/normalize_domain.py --dedupe-csv data/04_Prospects.csv --column Domain`.
8. Qualify — score every new prospect with `scripts/score_prospect.py` against `config/scoring_rubric.json`; classify per band.
9. Risk-check — screen against `config/risk_signals.json`; use the exact phrase "Risk signal detected" for uncertain evidence, never a definitive accusation.
10. Generate content opportunities — see `prompts/run_content.md`.
11. Generate outreach drafts — see `prompts/run_outreach.md` (drafts only, status `HUMAN_REVIEW`, never sent).
12. Verify backlinks — see `prompts/run_verify.md`.
13. Update Google Sheets — see `prompts/sheets_sync.md` (currently blocked; see that file for the two remediation paths).
14. Generate reports — see `prompts/reports.md`; write to `reports/daily/<date>.md`.
15. Display the human approval queue (below) and STOP before any external communication.

## Human Approval Queue (always shown at the end of a RUN ALL)

1. Prospects requiring approval
2. Outreach drafts requiring approval
3. Content requiring approval
4. Commercial proposals requiring review
5. Suspicious prospects requiring review
6. Backlinks requiring manual verification

## Hard constraints (never automatic)

See `config/risk_signals.json` → `never_automatically`. No exceptions.

## Data sources this run depends on

- **Ahrefs MCP** (`mcp__Ahrefs__*`) — backlink data, domain rating, organic competitors, keyword ideas.
- **Semrush MCP** (`mcp__Semrush__*`) — domain overview, competitor research, keyword research, backlink research.
- **Google Drive MCP** — file-level Google Sheets creation only (no cell/tab writes).
- **Make MCP** (`mcp__Make__*`) — for a scenario-based Sheets sync path; optional.

If any provider returns a quota/plan error, log it verbatim to `data/10_Errors.csv` (Section 32 format) and continue with the remaining independent steps. Never invent data to fill a gap — use `UNKNOWN`.
