# MER-05 — Public listing and detail

- **Module:** Cenderahati (Merchandises) (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/merchandises` · public `/shop/merchandises`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS (observation: negotiable not shown)**

## Preconditions
MER-04 done.

## Steps
1. Open `/shop/merchandises?search=QA`.
2. Open the item.

## Expected result
Listed with image, seller, product type and price.

## Actual result
Listing: image, seller, 'Produk Baju-T', 'RM 45', 'Hubungi Penjual'. Detail `/shop/merchandises/qa-barangan-baju-01` shows the same. There are no category or price filters (only a search box). The 'boleh runding' flag is **not shown publicly** (same observation as Art For Sale).

## Evidence
![public](evidence/mer-public.png) ![detail](evidence/mer-detail.png)
