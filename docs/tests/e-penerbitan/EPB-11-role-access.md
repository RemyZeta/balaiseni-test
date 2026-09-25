# EPB-11 — Non-admin access

- **Module:** E-Penerbitan (Admin)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/epublications` · public `/resources/e-publications`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Galeri and Artist QA accounts.

## Steps
1. Log in as each; check sidebar.
2. Open `/dashboard/epublications` directly.

## Expected result
Access denied.

## Actual result
No E-Penerbitan sidebar entry for either role; direct URL returns 403 for both.

## Evidence
![403](evidence/epb-403.png)
