# SVC-05 — Hubungi Pembekal contact form

- **Module:** Perkhidmatan (Services) (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/services` · public `/shop/services`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **BLOCKED (reCAPTCHA)**

## Preconditions
Detail page; anonymous visitor.

## Steps
1. Click Hubungi Pembekal.
2. Check the fields and protection.

## Expected result
Message can be sent to the provider.

## Actual result
Dialog opens ('Mesej anda akan dihantar kepada QA Penyedia berkenaan “…”') with Nama, Emel, Mesej and a reCAPTCHA. The same form as on Art For Sale, where a human must tick 'I'm not a robot'. I did not submit or bypass it, so sending and the provider's Inbox are unverified.

## Evidence
![contact](evidence/svc-contact.png)
