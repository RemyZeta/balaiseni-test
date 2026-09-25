# MER-04 — Create merchandise with negotiable price (auto-approved)

- **Module:** Cenderahati (Merchandises) (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/merchandises` · public `/shop/merchandises`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Admin logged in. Image `7-_One_step_at_a_time…jpg`.

## Steps
1. Fill Nama `QA Barangan Baju 01`, Penjual `QA Penjual`, Huraian, Harga 45, tick 'Harga boleh dirunding', Jenis produk `Baju-T`.
2. Simpan barangan.

## Expected result
Saved and approved directly.

## Actual result
Toast '… telah ditambah.'; counters 0→1; card 'QA PENJUAL · Diluluskan · RM 45 boleh runding · Baju-T'.

## Evidence
![filled](evidence/mer-filled.png) ![created](evidence/mer-created.png)
