# MER-08 — Reject and re-approve

- **Module:** Cenderahati (Merchandises) (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/merchandises` · public `/shop/merchandises`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS (observation: no reason)**

## Preconditions
Approved item.

## Steps
1. Tolak; check the detail URL.
2. Luluskan; check the detail URL.

## Expected result
404 when rejected; visible again when approved.

## Actual result
Toast 'kini Ditolak.' (no reason or confirmation); detail 404. Luluskan → detail 200.

## Evidence
-
