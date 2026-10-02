# PND-03 — What an unapproved Galeri can open

- **Module:** Unapproved Artist and Galeri accounts (cross-module)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/review-queue` · roles Artist and Galeri
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS (observation: no restriction)**

## Preconditions
QA Galeri logged in (profile pending).

## Steps
1. Read the dashboard and sidebar.
2. Open each module URL and note the status.

## Expected result
Same access as an approved galeri, or a restricted view.

## Actual result
Sidebar: Tutorial, Perkongsian, Koleksi, Galeri, Profil Saya, Inbox. Status 200: tutorials, sharings, collection, galleries, profile, inbox. 403: art-for-sale and all admin-only modules. Nothing is restricted because the account is unapproved.

## Evidence
![dash](evidence/dash-galeri.png)
