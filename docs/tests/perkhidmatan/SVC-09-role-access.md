# SVC-09 — Non-admin and anonymous access

- **Module:** Perkhidmatan (Services) (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/services` · public `/shop/services`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Artist QA, Galeri QA, anonymous.

## Steps
1. Check each sidebar; open `/dashboard/services`.
2. Anonymous opens it.

## Expected result
Denied; anonymous sent to login.

## Actual result
No Perkhidmatan entry in either sidebar; both get 403; anonymous redirected to `/login`.

## Evidence
![403](evidence/403.png)
