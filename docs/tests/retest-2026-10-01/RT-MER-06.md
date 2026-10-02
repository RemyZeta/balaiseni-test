# RT-MER-06 — Retest: Cenderahati: contact seller

- **Original test:** [MER-06](../cenderahati/MER-06-contact-seller.md) (was **BLOCKED**)
- **Target:** https://martp.nizamjensani.digital/
- **Date:** 2026-10-01 · **Tool:** playwright-cli (headed) · **Role:** Admin, anonymous visitor
- **Status:** **BLOCKED (reCAPTCHA)**

## Steps
1. The public list had 0 listings, so admin created `QA RT Barangan 01` (approved directly).
2. Anonymous: open it, click Hubungi Penjual; do not send.
3. Admin deletes it.

## Expected result
Message can be sent to the seller.

## Actual result
Same form with reCAPTCHA. Not sent. QA listing deleted (count back to 0).

## Evidence
![form](evidence/rt-merchandises-contact.png)
