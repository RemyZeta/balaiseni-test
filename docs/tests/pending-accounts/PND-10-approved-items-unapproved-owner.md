# PND-10 — Approved items from an unapproved account

- **Module:** Unapproved Artist and Galeri accounts (cross-module)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/review-queue` · roles Artist and Galeri
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P1
- **Status:** **PASS (observation)**

## Preconditions
Earlier modules: admin approved items created by the unapproved QA accounts.

## Steps
1. Approve an item from an unapproved account.
2. Check the public page.

## Expected result
Either allowed, or blocked until the account is approved.

## Actual result
Admin's approval of the item was enough: approved Perkongsian, Koleksi, Art For Sale and galeri items appeared publicly under the unapproved account's name (see those test docs). Item approval is independent of membership approval.

## Evidence
-
