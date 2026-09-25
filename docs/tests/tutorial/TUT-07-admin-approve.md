# TUT-07 — Admin approves tutorial → appears publicly

- **Module:** Tutorial (Artist dashboard + Admin review)
- **Target:** https://martp.nizamjensani.digital/
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Rejected item from TUT-06; admin logged in.

## Steps
1. Click Luluskan (available on rejected items).
2. Open `/resources/tutorials?search=QA%20Tutorial`.

## Expected result
Status Diluluskan and item visible on public page.

## Actual result
Toast '"…" kini Diluluskan.' Public page lists the tutorial with title, date, description, and 'Dicipta/Dikemas kini' by QA Test Artis. Artist list shows 'Diluluskan'.

## Evidence
TUT-070
