# PAM-01 — Create — required title

- **Module:** Pameran & Aktiviti (Admin)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/exhibitions` · public `/resources/exhibitions`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P1
- **Status:** **PASS (cosmetic)**

## Preconditions
Admin logged in.

## Steps
1. Tambah pameran.
2. Simpan pameran with Tajuk pameran empty.

## Expected result
Blocked.

## Actual result
Modal stays open, native tooltip 'Please fill in this field.' (English on Malay UI).

## Evidence
![form](evidence/pam-form.png)
