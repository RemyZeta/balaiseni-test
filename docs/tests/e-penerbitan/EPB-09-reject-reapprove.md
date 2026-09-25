# EPB-09 — Reject and re-approve

- **Module:** E-Penerbitan (Admin)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/epublications` · public `/resources/e-publications`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS (observation)**

## Preconditions
Approved item.

## Steps
1. Tolak; search public page; open detail URL.
2. Luluskan; open detail URL.

## Expected result
Hidden and 404 when rejected; visible again when approved.

## Actual result
Rejected: toast 'kini Ditolak.' (no reason/confirmation), public search 0 results, detail 404. Approved: detail 200 again. Observation: the PDF file URL still returned 200 while rejected (may be a CDN cache hit, see EPB-10).

## Evidence
-
