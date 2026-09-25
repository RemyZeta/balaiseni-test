# SVC-07 — Reject and re-approve

- **Module:** Perkhidmatan (Services) (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/services` · public `/shop/services`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS (observation: no reason)**

## Preconditions
Approved item.

## Steps
1. Tolak; check detail URL and public search.
2. Luluskan; check detail URL.

## Expected result
Hidden and 404 when rejected; visible again when approved.

## Actual result
Toast 'kini Ditolak.' (no reason or confirmation); detail 404; public search '0 penyenaraian aktif'. Luluskan → detail 200.

## Evidence
-
