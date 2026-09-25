# SVC-01 — Create — required name and provider

- **Module:** Perkhidmatan (Services) (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/services` · public `/shop/services`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P1
- **Status:** **PASS (cosmetic)**

## Preconditions
Admin logged in, `/dashboard/services` (0 listings).

## Steps
1. Tambah perkhidmatan.
2. Simpan empty.
3. Fill only the name; save.

## Expected result
Blocked each time.

## Actual result
Modal stays open; native tooltip 'Please fill in this field.' first on Nama perkhidmatan, then on Nama penyedia (English on Malay UI).

## Evidence
![form](evidence/svc-form.png)
