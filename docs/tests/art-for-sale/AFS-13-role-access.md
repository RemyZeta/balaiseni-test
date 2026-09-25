# AFS-13 — Role access

- **Module:** Art For Sale (Admin, Artist)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/art-for-sale` · public `/shop/art-for-sale`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Galeri QA and Artist QA accounts.

## Steps
1. Galeri: check the sidebar; open `/dashboard/art-for-sale`.
2. Artist: use the module (AFS-01 to AFS-11).

## Expected result
Artist and Admin allowed; Galeri denied.

## Actual result
Galeri has no Art For Sale entry and gets 403. Artist and Admin have full access. Anonymous access to the dashboard was not re-tested (covered in other modules).

## Evidence
![403](evidence/afs-403.png)
