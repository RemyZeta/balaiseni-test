# BRT-10 — Non-admin access

- **Module:** Berita (Admin)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/news` · public `/resources/news`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Galeri and Artist QA accounts.

## Steps
1. Log in as each; check sidebar.
2. Open `/dashboard/news` directly.

## Expected result
Access denied.

## Actual result
No Berita sidebar entry for either role; direct URL returns 403 for both.

## Evidence
![403](evidence/brt-403.png)
