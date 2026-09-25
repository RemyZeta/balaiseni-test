# BRT-08 — Reject and re-approve

- **Module:** Berita (Admin)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/news` · public `/resources/news`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS (observation: no reason)**

## Preconditions
Approved item.

## Steps
1. Tolak; search public page; open detail URL.
2. Luluskan; open detail URL.

## Expected result
Hidden and 404 when rejected; visible again when approved.

## Actual result
Rejected: toast 'kini Ditolak.' (no reason or confirmation), public search 0 berita, detail 404. Approved: detail 200.

## Evidence
-
