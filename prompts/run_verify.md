# RUN VERIFY

Verifies known backlinks in `data/08_Backlinks.csv` (Master Prompt Section
19). Never claim a backlink is `ACTIVE` without actually checking it.

## Checks per row

1. Published page exists and is accessible (fetch it).
2. Target URL exists.
3. The link on the published page actually points to the intended target URL.
4. Anchor text matches what was recorded.
5. `rel` attribute (e.g. `nofollow`, `sponsored`, `ugc`).
6. Surrounding context still looks editorial (not later swapped for spam).
7. Redirect status if the source or target has moved.
8. Update `Last Checked` to today's date regardless of outcome.

## Status mapping

- Link found, correct target, live page → `ACTIVE`
- Page loads but link is gone → `LOST`
- Page returns 404/5xx → `PAGE_ERROR`
- Source or target now redirects → `REDIRECTED`
- Anchor/context changed materially → `CHANGED`
- Ambiguous evidence → `REVIEW_REQUIRED`
- Not yet checked → `PENDING`

There are no backlinks recorded yet (`data/08_Backlinks.csv` is
header-only) — this command has nothing to verify until outreach produces
a published, approved link.
