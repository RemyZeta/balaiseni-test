# TUT-01 — Create tutorial — required title

- **Module:** Tutorial (Artist dashboard + Admin review)
- **Target:** https://martp.nizamjensani.digital/
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P1
- **Status:** **PASS (cosmetic issue)**

## Preconditions
Artist QA account `qa.artis.test01@mailinator.com` logged in, on `/dashboard/tutorials`.

## Steps
1. Click Tambah tutorial.
2. Click Simpan video with Tajuk video empty.

## Expected result
Submission blocked.

## Actual result
Modal stays open; native tooltip 'Please fill in this field.' (English text on Malay UI — cosmetic).

## Evidence
TUT-010
