# TUT-09 — Artist deletes tutorial

- **Module:** Tutorial (Artist dashboard + Admin review)
- **Target:** https://martp.nizamjensani.digital/
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Approved tutorial from TUT-08; artist logged in.

## Steps
1. Click Padam.
2. Confirm dialog text; click Padam.
3. Check list and public page.

## Expected result
Confirmation shown; item removed everywhere.

## Actual result
Dialog: 'Padam "…"? Video ini akan dibuang terus… tidak boleh dibatalkan.' with Batal / Padam. After confirming, artist list is empty (JUMLAH 0) and the public search returns no result.

## Evidence
TUT-090
