# PTU-04 — Sembunyi / Papar a section

- **Module:** Portal Utama (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/homepage` (tabs Bahagian, Banner) · public homepage `/`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Karya seni pilihan visible on the homepage.

## Steps
1. Sembunyi; check homepage.
2. Papar; check homepage.

## Expected result
Hidden from the homepage while off; back when on.

## Actual result
Toast 'Bahagian Karya seni pilihan disembunyikan.' — the section disappears from the homepage; Papar restores it ('… dipaparkan.'). No confirmation for either action.

## Evidence
![hidden](evidence/ptu-hidden.png)
