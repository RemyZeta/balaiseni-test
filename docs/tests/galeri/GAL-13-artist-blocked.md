# GAL-13 — Artist cannot access the Galeri module

- **Module:** Galeri (Galeri user, Admin)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/galleries` · public `/resources/galleries`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Artist QA logged in.

## Steps
1. Check the sidebar.
2. Open `/dashboard/galleries` and `/dashboard/galleries/11/edit` directly.

## Expected result
Access denied.

## Actual result
Sidebar has no Galeri entry (Tutorial, Perkongsian, Koleksi, Art For Sale, Profil Saya, Inbox only); both URLs return 403.

## Evidence
![403](evidence/gal-403.png)
