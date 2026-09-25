# PTU-12 — Non-admin and anonymous access

- **Module:** Portal Utama (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/homepage` (tabs Bahagian, Banner) · public homepage `/`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Artist QA, Galeri QA, anonymous.

## Steps
1. Check each sidebar and open `/dashboard/homepage`.
2. Anonymous opens it.

## Expected result
Denied; anonymous sent to login.

## Actual result
No Portal Utama entry in either sidebar; both get 403; anonymous redirected to `/login`.

## Evidence
![403](evidence/ptu-403.png)
