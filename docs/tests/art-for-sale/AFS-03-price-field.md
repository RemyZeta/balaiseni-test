# AFS-03 — Harga (RM) rules and negotiable checkbox

- **Module:** Art For Sale (Admin, Artist)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/art-for-sale` · public `/shop/art-for-sale`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P1
- **Status:** **PASS (observation: whole numbers only)**

## Preconditions
Create form open.

## Steps
1. Enter -5.
2. Enter 1500.50.
3. Enter 1500.
4. Tick 'Harga boleh dirunding'.

## Expected result
Sensible price validation.

## Actual result
-5 refused ('Value must be greater than or equal to 0.'). 1500.50 refused ('The two nearest valid values are 1500 and 1501.') — the field accepts whole ringgit only (step 1), so prices with sen cannot be entered. 1500 accepted and shown as 'RM 1,500'. The checkbox is unticked by default and does not disable the price field.

## Evidence
-
