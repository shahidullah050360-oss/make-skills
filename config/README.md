# Clarity SEO Automation System

Discover → Analyze → Qualify → Verify → Draft → **Human Approval** → Real
editorial action → Verify → Report. Never: AI → mass links → spam → search
manipulation.

This directory tree implements the four-site SEO opportunity and backlink
research system for Coverage Clarity, BuyClarity, Ilm Clarity, and Stack
Clarity. It never sends outreach, publishes content, or creates/purchases
backlinks automatically — every external action requires explicit human
approval (see `config/risk_signals.json` → `never_automatically`).

## Layout

- `config/` — site registry, scoring rubric, risk-signal list, sheet schema (this file's directory)
- `data/` — the live tables (one CSV per planned Sheet tab); source of truth until Sheets sync is wired up
- `prompts/` — one runbook per RUN command, followed by this agent when invoked
- `reports/{daily,weekly,monthly}/` — dated, never-overwritten report files
- `scripts/` — deterministic helpers (domain normalization/dedupe, prospect scoring) with no external dependencies
- `logs/` — per-run execution logs

## Commands

See `prompts/run_all.md` for the master command and the full command table
(RUN SITE 1-4, RUN PROSPECTS, RUN COMPETITORS, RUN CONTENT, RUN OUTREACH,
RUN VERIFY, RUN DAILY/WEEKLY/MONTHLY REPORT, SYNC SHEETS).

## Status as of 2026-09-24

Five open blockers in `data/10_Errors.csv`:

- **Semrush**: out of API units (`no_api_units`) — re-checked, still open.
- **Ahrefs**: "Insufficient plan" on every endpoint, including free ones — re-checked, still open.
- **Make MCP**: proxy refused the connection (403) — not required for
  research, only for a future Sheets-sync scenario.
- **Google Sheets**: no cell/tab-write tool connected; `data/*.csv` is the
  real source of truth for now (see `prompts/sheets_sync.md`).
- **Network egress**: this environment's network policy blocks `WebFetch`
  to most third-party domains, so the 9 leads found via `WebSearch` on
  2026-09-24 could not be independently verified and sit at
  `NEEDS_EVIDENCE`/`REJECTED` in `data/04_Prospects.csv`. Fix from the
  cloud environment menu (session title bar → Edit → Network access).

`data/04_Prospects.csv` has 9 unscored leads and `data/07_Content.csv` has
8 keyword-unvalidated topic ideas from a WebSearch-only pass. Once
Semrush/Ahrefs access is restored and/or network access is broadened,
re-run `RUN COMPETITORS` and `RUN PROSPECTS` per site to verify and score
real data — this system will not fabricate keyword volumes, competitor
lists, authority/organic scores, or contact details in the meantime.
