# AUTH-02 — Set password — too short

- **Module:** Pengurusan Pengguna (Authentication / Registration)
- **Target:** https://martp.nizamjensani.digital/
- **Date:** 2026-09-25
- **Tool:** playwright-cli (headed)
- **Priority:** P1
- **Status:** **PASS**

## Preconditions
AUTH-01 done; on `/password/renew`.

## Steps
1. Enter `abc` in both password fields.
2. Click Simpan dan teruskan.

## Expected result
Validation error; stays on page.

## Actual result
Error shown: 'Medan kata laluan mesti sekurang-kurangnya 8 aksara.' Stays on `/password/renew`.

## Evidence
No screenshot captured for this test; result observed via page text.
