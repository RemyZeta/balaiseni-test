# SVC-04 — Public listing, search and detail

- **Module:** Perkhidmatan (Services) (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/services` · public `/shop/services`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
SVC-03 done.

## Steps
1. Open `/shop/services?search=QA`.
2. Open the item.
3. Search a non-matching text.

## Expected result
Listed with image, provider, offerings and location; detail works.

## Actual result
Listing: image, provider, 'Perkhidmatan Framing, Packing', 'Lokasi Kuala Lumpur', 'Hubungi Pembekal', 'Dicipta oleh Ahmad Safwan'. Detail `/shop/services/qa-perkhidmatan-framing-01` shows the same. Non-match: '0 penyenaraian aktif · Tiada hasil sepadan dengan carian ini'.

## Evidence
![public](evidence/svc-public.png) ![detail](evidence/svc-detail.png)
