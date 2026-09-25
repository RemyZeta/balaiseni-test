# ART-08 — Reject → hidden from public

- **Module:** Artikel (Admin)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/articles` · public `/resources/articles`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS (observation: no reason)**

## Preconditions
Approved article.

## Steps
1. Tolak.
2. Search public page; open detail URL.

## Expected result
Hidden; direct URL 404.

## Actual result
Toast 'kini Ditolak.' (no reason / confirmation). Public search 0 results; detail URL returns 404.

## Evidence
-
