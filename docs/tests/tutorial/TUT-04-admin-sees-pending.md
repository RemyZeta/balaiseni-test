# TUT-04 — Admin sees pending item in review list

- **Module:** Tutorial (Artist dashboard + Admin review)
- **Target:** https://martp.nizamjensani.digital/
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Admin logged in (login page → quick-login panel, ADMIN 'Ahmad Safwan').

## Steps
1. Open `/dashboard/tutorials` and Barisan Semakan.

## Expected result
Pending tutorial visible with Luluskan / Tolak / Padam actions.

## Actual result
Item appears at top with 'Menunggu semakan' and buttons Lihat, Sunting, Luluskan, Tolak, Padam. Counters: 367 total, 365 approved, 1 pending. Sidebar Barisan Semakan badge is shown.

## Evidence
TUT-040
