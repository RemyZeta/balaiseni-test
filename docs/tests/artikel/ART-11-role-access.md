# ART-11 — Non-admin access

- **Module:** Artikel (Admin)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/articles` · public `/resources/articles`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Galeri QA account logged in.

## Steps
1. Check the sidebar.
2. Open `/dashboard/articles` directly.

## Expected result
Access denied.

## Actual result
No Artikel entry in sidebar; direct URL returns 403.

## Evidence
-
