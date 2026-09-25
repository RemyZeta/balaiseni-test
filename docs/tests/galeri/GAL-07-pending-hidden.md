# GAL-07 — Pending galeri hidden from public

- **Module:** Galeri (Galeri user, Admin)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/galleries` · public `/resources/galleries`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Galeri pending; owner and anonymous visitor.

## Steps
1. Search `QA Galeri` on `/resources/galleries` as owner and as anonymous.
2. Check the owner's dashboard list.

## Expected result
Not public; owner sees own item only.

## Actual result
0 results for both. The owner's list shows only their own galeri (1), with 'Menunggu semakan'.

## Evidence
![list](evidence/gal-list-after.png)
