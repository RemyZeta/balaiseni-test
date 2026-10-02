# RT-AFS-08 — Retest: Art For Sale: contact seller

- **Original test:** [AFS-08](../art-for-sale/AFS-08-contact-seller.md) (was **BLOCKED**)
- **Target:** https://martp.nizamjensani.digital/
- **Date:** 2026-10-01 · **Tool:** playwright-cli (headed) · **Role:** Anonymous visitor
- **Status:** **BLOCKED (reCAPTCHA)**

## Steps
1. Open an approved listing; Hubungi Penjual.
2. Check the form; do not send.

## Expected result
Message can be sent to the seller.

## Actual result
Dialog "Mesej anda akan dihantar kepada … berkenaan …" with Nama, Emel, Mesej and a Google reCAPTCHA (anchor and challenge frames loaded). Still needs a human tick; nothing was sent.

## Evidence
![form](evidence/rt-afs-contact.png)
