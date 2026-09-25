# SHR-03 — Artist creates perkongsian → pending, hidden

- **Module:** Perkongsian (Galeri, Artis and Admin)
- **Target:** https://martp.nizamjensani.digital/ · public page `/resources/sharings`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Artist QA account logged in.

## Steps
1. Create `QA Perkongsian Artis 01` (no URL).
2. Log out; search public page as anonymous.

## Expected result
Saved as pending; not public; artist sees only own items.

## Actual result
Card 'Menunggu semakan'. Artist list contains only its own item (Galeri's item not visible). Anonymous search: 0 results.

## Evidence
![artis](evidence/shr-artis-created.png)
