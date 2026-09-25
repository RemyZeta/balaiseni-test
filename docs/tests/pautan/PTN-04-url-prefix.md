# PTN-04 — URL typed with https:// prefix

- **Module:** Pautan (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/links` · public `/links`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P2
- **Status:** **PASS**

## Preconditions
Create form open.

## Steps
1. Nama `QA Pautan Prefiks`, URL `https://qa-prefiks.example.com`.
2. Save; check the stored link.

## Expected result
Accepted and normalised.

## Actual result
Saved; the link is `https://qa-prefiks.example.com` (no doubled scheme).

## Evidence
-
