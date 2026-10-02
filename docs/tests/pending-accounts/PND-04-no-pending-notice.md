# PND-04 — Is the user told that the account awaits approval?

- **Module:** Unapproved Artist and Galeri accounts (cross-module)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/review-queue` · roles Artist and Galeri
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P1
- **Status:** **PASS (observation: no notice, misleading message)**

## Preconditions
Both accounts logged in.

## Steps
1. Read the dashboard home for a notice.
2. Open notifications.

## Expected result
A visible 'awaiting approval' message.

## Actual result
No such message. The dashboard greets 'Selamat kembali' and shows **site-wide** statistics (73 published works; accounts by role) and, to a pending user, 'Tiada apa-apa dalam barisan. Semua profil telah disemak.' — which is untrue for their own profile. Notifications: none. The registration page said the profile would be reviewed by admin, but the user is not reminded afterwards.

## Evidence
![dash](evidence/dash-artis.png)
