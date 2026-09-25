# MER-01 — Create — required name and seller

- **Module:** Cenderahati (Merchandises) (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/merchandises` · public `/shop/merchandises`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P1
- **Status:** **PASS (cosmetic)**

## Preconditions
Admin logged in, `/dashboard/merchandises` (0 listings).

## Steps
1. Tambah barangan.
2. Simpan empty.
3. Fill only the name; save.

## Expected result
Blocked each time.

## Actual result
Modal stays open; native tooltip 'Please fill in this field.' first on Nama barangan, then on Nama penjual (English on Malay UI).

## Evidence
![form](evidence/mer-form.png)
