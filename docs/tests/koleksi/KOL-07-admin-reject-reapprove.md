# KOL-07 — Admin rejects Galeri item, then re-approves

- **Module:** Koleksi (Admin, Artist, Galeri)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/collection` · public `/collection`, `/resources/artists-art`, `/resources/nag-collection`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS (observation: no reason)**

## Preconditions
KOL-04 item pending.

## Steps
1. Tolak the Galeri item; check public.
2. Later Luluskan it; check detail URL.

## Expected result
Hidden when rejected; public after approval.

## Actual result
Rejected: toast 'kini Ditolak.' (no reason or confirmation); not listed publicly. Re-approved: detail `/collection/qa-karya-galeri-01` returns 200.

## Evidence
-
