# SVC-03 — Create a service (auto-approved)

- **Module:** Perkhidmatan (Services) (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/services` · public `/shop/services`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Admin logged in. Image `7-_One_step_at_a_time…jpg`.

## Steps
1. Fill Nama `QA Perkhidmatan Framing 01`, Penyedia `QA Penyedia`, Huraian, Khidmat ditawarkan `Framing, Packing`, Beroperasi di `Kuala Lumpur`.
2. Simpan perkhidmatan.

## Expected result
Saved and approved directly (the form says so).

## Actual result
Toast '… telah ditambah.'; counters 0→1, DILULUSKAN 1; card 'QA PENYEDIA · Diluluskan' with offerings and location.

## Evidence
![filled](evidence/svc-filled.png) ![created](evidence/svc-created.png)
