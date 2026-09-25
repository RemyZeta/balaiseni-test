# AUTH-07 — Login — wrong password / unknown email

- **Module:** Pengurusan Pengguna (Authentication / Registration)
- **Target:** https://martp.nizamjensani.digital/
- **Date:** 2026-09-25
- **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Artis account exists.

## Steps
1. Open `/login`.
2. Enter valid email + `WrongPass@1`; submit.
3. Enter unregistered email + `Test@12345`; submit.

## Expected result
Login refused with a non-revealing error.

## Actual result
Both cases show the same message: 'Emel atau kata laluan tidak betul.' (no account enumeration). Empty-submit case not conclusively verified.

## Evidence
No screenshot captured for this test; result observed via page text.
