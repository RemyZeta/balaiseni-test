# SHR-06 — Admin rejects Galeri item → stays hidden

- **Module:** Perkongsian (Galeri, Artis and Admin)
- **Target:** https://martp.nizamjensani.digital/ · public page `/resources/sharings`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS (observation: no rejection reason)**

## Preconditions
SHR-02 done.

## Steps
1. Click Tolak on the Galeri item.
2. Search public page.

## Expected result
Status Ditolak; hidden.

## Actual result
Toast '… kini Ditolak.' immediately — no reason and no confirmation. Public search shows only the approved Artis item, not the Galeri one.

## Evidence
See SHR-05 screenshot.
