# PTN-11 — Non-admin and anonymous access

- **Module:** Pautan (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/links` · public `/links`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Artist QA, Galeri QA, anonymous.

## Steps
1. Check each user's sidebar and open `/dashboard/links`.
2. Anonymous opens `/dashboard/links`.

## Expected result
Denied for non-admins; anonymous sent to login.

## Actual result
No Pautan entry in either sidebar; both get 403. Anonymous is redirected to `/login`. The page itself says 'Hanya Admin boleh menyuntingnya.'

## Evidence
![403](evidence/ptn-403.png)
