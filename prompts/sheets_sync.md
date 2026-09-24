# SYNC SHEETS

Master Prompt Section 20 calls for one spreadsheet, "CLARITY SEO COMMAND
CENTER", with 10 tabs (`config/sheet_schema.json`). As of 2026-09-24, this
session's Google Drive connector (`mcp__Google_Drive__*`) can only
create/read/rename whole files — it has no API for adding sheet tabs or
writing cell ranges inside an existing spreadsheet. So `data/*.csv` in this
repo is the real source of truth today, not a live Sheet.

An empty shell spreadsheet named "CLARITY SEO COMMAND CENTER" was created
in the connected Google Drive account (owner: shahidullah050360@gmail.com)
as a placeholder — it has no tabs yet:
https://docs.google.com/spreadsheets/d/1EuuO0zribOUcMBWaIYf6IzRi-0N3g-NfdYyq6j6PAdY/edit

## Two real paths to a fully live sync (neither is done yet)

1. **Make.com scenario (fits this repo's actual purpose).** Once the
   `make` MCP connector reconnects (currently `ERR_PROXY_TUNNEL: 403`, see
   `data/10_Errors.csv`), build a scenario per
   `skills/make-scenario-building` + `skills/make-module-configuring` that
   watches `data/*.csv` (or a webhook/API) and upserts rows into each tab
   via Make's Google Sheets modules (`Add a Row`, `Update a Row`,
   `Search Rows`) with a unique-ID watermark for dedupe.
2. **Manual import (works right now).** Open the shell spreadsheet, create
   the 10 tabs named exactly as in `config/sheet_schema.json`, paste in the
   header row for each from that file, then import each
   `data/0N_*.csv` into its matching tab.

## What NOT to do

Do not fabricate a "sync complete" status. Until one of the two paths above
is actually executed, `09_Reports` / any status report should say the
Sheet has zero populated tabs.
