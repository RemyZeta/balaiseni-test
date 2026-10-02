# SHR-09 — Galeri edits an approved perkongsian

- **Module:** Perkongsian (Galeri, Artis and Admin)
- **Target:** https://martp.nizamjensani.digital/ · public page `/resources/sharings`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **FAIL (if re-review required)**

## Preconditions
Approved item; Galeri logged in.

## Steps
1. Sunting → title '… (Edit selepas lulus)'; save.
2. Check list and public page.

## Expected result
Item returns to review, or change waits for approval.

## Actual result
**Stays Diluluskan and the new title is public immediately** — no re-review. Same defect as Tutorial TUT-08. **Potential defect — confirm intended rule.**

## Evidence
-

## Retest 2026-10-01
**PASS (fixed)**. See [RT-SHR-09](../retest-2026-10-01/RT-SHR-09.md).
