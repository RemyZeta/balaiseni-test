# AUTH-03 — Set password — confirmation mismatch

- **Module:** Pengurusan Pengguna (Authentication / Registration)
- **Target:** https://martp.nizamjensani.digital/
- **Date:** 2026-09-25
- **Tool:** playwright-cli (headed)
- **Priority:** P1
- **Status:** **PASS**

## Preconditions
On `/password/renew`.

## Steps
1. Enter `Test@12345` and confirmation `Different@999`.
2. Click Simpan dan teruskan.

## Expected result
Validation error; stays on page.

## Actual result
Error shown: 'Pengesahan kata laluan tidak sepadan.'

## Evidence
No screenshot captured for this test; result observed via page text.
