# BRT-07 — Pautan laporan asal validation

- **Module:** Berita (Admin)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/news` · public `/resources/news`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P1
- **Status:** **PASS (observation: message says https only)**

## Preconditions
Edit form open.

## Steps
1. Enter `javascript:window.__x4=1`; save.
2. Enter `http://example.com/tanpa-https`; save.

## Expected result
Only safe URLs accepted.

## Actual result
`javascript:` rejected with 'Medan Pautan laporan asal mesti URL yang sah, bermula dengan https://' (in Malay). `http://` (no TLS) was **accepted** and saved, although the message says the URL must start with https://. Message and rule disagree (minor; confirm whether http:// is intended).

## Evidence
-
