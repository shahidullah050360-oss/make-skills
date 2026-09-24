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

## Status as of 2026-09-24 (final for this pass)

**Scaffolding is complete for all four sites.** Config, data tables, RUN-command
runbooks, helper scripts, and the Drive spreadsheet shell all exist and have
been re-validated: every `data/*.csv` header matches `config/sheet_schema.json`
exactly, every row has the correct field count (a real column-misalignment bug
found during closeout review was fixed and re-verified), `scripts/normalize_domain.py`
reports 0 duplicate domains across the 9 prospect leads, and `scripts/score_prospect.py`
runs correctly. `data/*.csv` is the system's real source of truth — there is
no live Google Sheets sync yet.

Five open blockers remain in `data/10_Errors.csv`, none fixed automatically
by design (this system never invents API access or credentials):

- **Semrush**: out of API units (`no_api_units`) — re-checked twice, still open. Fix: add units at https://www.semrush.com/mcp-access.
- **Ahrefs**: "Insufficient plan" on every endpoint, including free ones — re-checked twice, still open. Fix: upgrade/verify the connected Ahrefs plan.
- **Make MCP**: proxy refused the connection (403) — not required for
  research, only for a future Sheets-sync scenario. Fix: reconnect/re-authenticate the Make connector.
- **Google Sheets**: no cell/tab-write tool connected; `data/*.csv` is the
  real source of truth for now (see `prompts/sheets_sync.md`). Fix: manually
  import the CSVs into the shell spreadsheet, or wire up a Make scenario once
  the Make MCP connector reconnects.
- **Network egress**: this environment's network policy blocks `WebFetch`
  to most third-party domains, so the 9 leads found via `WebSearch` on
  2026-09-24 could not be independently verified and sit at
  `NEEDS_EVIDENCE`/`REJECTED` in `data/04_Prospects.csv`. Fix: broaden
  Network access from the cloud environment menu (session title bar → Edit
  → Network access) — e.g. to "Allow all" — or allowlist the specific domains.

`data/04_Prospects.csv` has 9 unscored leads and `data/07_Content.csv` has
8 keyword-unvalidated topic ideas from a WebSearch-only pass. `data/03_Competitors.csv`
has 4 user-identified competitors (one per site: nerdwallet.com, nytimes.com/wirecutter,
education.com, howtogeek.com) — real, topically legitimate picks, but their
traffic/CPC/RPM figures are user-supplied and explicitly flagged as
unverified in each row's `Notes`, since Semrush/Ahrefs remain blocked.
`data/05_Competitor_Gaps.csv`, `data/06_Outreach.csv`, `data/08_Backlinks.csv`,
and `data/02_Keywords.csv` are still header-only pending Semrush/Ahrefs access. No
outreach has been sent, no content published, and no backlinks created.
Once Semrush/Ahrefs access is restored and/or network access is broadened,
re-run `RUN COMPETITORS` and `RUN PROSPECTS` per site to verify and score
real data — this system will not fabricate keyword volumes, competitor
lists, authority/organic scores, or contact details in the meantime.
