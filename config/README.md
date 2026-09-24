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

Scaffolding only — no research has run yet. Both external data providers
returned account-level errors on first use (see `data/10_Errors.csv`):

- **Semrush**: out of API units (`no_api_units`).
- **Ahrefs**: "Insufficient plan" (even on the free domain-rating and
  usage-limit endpoints).
- **Make MCP**: proxy refused the connection (403) — not required for
  research, only for a future Sheets-sync scenario.
- **Google Sheets**: no cell/tab-write tool connected; `data/*.csv` is the
  real source of truth for now (see `prompts/sheets_sync.md`).

Once Semrush and/or Ahrefs access is restored, re-run `RUN COMPETITORS` and
`RUN PROSPECTS` per site to populate real data — this system will not
fabricate keyword volumes, competitor lists, or contact details in the
meantime.
