# Reports (RUN DAILY REPORT / RUN WEEKLY REPORT / RUN MONTHLY REPORT)

## Daily (`reports/daily/<YYYY-MM-DD>.md`)

Date, Site, New prospects, Qualified prospects, High-priority candidates,
New competitor gaps, New content opportunities, Backlink verification
results, Errors, Human actions required.

## Weekly (`reports/weekly/<YYYY-MM-DD>.md`, one per Monday)

New opportunities, Approved opportunities, Outreach activity, Responses,
Published links, Verified links, Lost links, Competitor gaps, Content
opportunities, Risk signals.

## Monthly (`reports/monthly/<YYYY-MM>.md`)

One section per site (Coverage Clarity, BuyClarity, Ilm Clarity, Stack
Clarity): new/qualified/approved prospects, outreach activity, responses,
published/verified/lost links, competitor gaps, content opportunities,
risk flags, unresolved tasks — plus a combined four-site summary section.

## Rules

- Never overwrite a prior dated report.
- Pull every number from the current state of `data/*.csv` — do not
  estimate or carry forward stale numbers.
- Always end with the six-item Human Approval Queue from `run_all.md`.
