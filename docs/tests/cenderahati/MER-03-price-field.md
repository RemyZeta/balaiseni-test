# MER-03 — Harga (RM) rules

- **Module:** Cenderahati (Merchandises) (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/merchandises` · public `/shop/merchandises`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P1
- **Status:** **PASS (observation: whole numbers only)**

## Preconditions
Create form open.

## Steps
1. Enter -5.
2. Enter 45.5.
3. Enter 45.

## Expected result
Sensible price validation.

## Actual result
-5 refused ('Value must be greater than or equal to 0.'). 45.5 refused ('The two nearest valid values are 45 and 46.') — whole ringgit only, so sen cannot be entered (same as Art For Sale). 45 accepted.

## Evidence
-
