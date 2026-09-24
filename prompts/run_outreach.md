# RUN OUTREACH

Generates personalized outreach drafts for qualified prospects only
(`Total Score` ≥ 70, or a documented exception). **Never sends anything.**

## Rules (Master Prompt Sections 3, 14, 17)

- Never fabricate relationships, prior conversations, article reads,
  statistics, names, companies, or credentials.
- Never promise guaranteed rankings, traffic, backlinks, or SEO results.
- Never force exact-match keyword anchors — suggest brand name, site name,
  or a natural descriptive phrase; the publisher keeps editorial control.
- Ask whether the proposed topic fits the publisher's editorial guidelines.
- Keep it concise and professional.

## Procedure

1. Pull the prospect row from `data/04_Prospects.csv`.
2. Draft using only verified fields from that row (contact name/email may
   be `UNKNOWN` — if so, the draft is not sendable and stays `NEW`/`DRAFTED`
   until a real contact is found).
3. Append a new row to `data/06_Outreach.csv` with `Status = HUMAN_REVIEW`
   and `Approval = PENDING`.
4. Surface it in the human approval queue. A human must move `Approval` to
   `APPROVED` and set `Date Sent` manually (or via an explicit, separate
   send action a human triggers) before anything leaves the system.
