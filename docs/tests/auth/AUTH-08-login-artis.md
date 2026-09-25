# AUTH-08 — Login — Artis valid credentials

- **Module:** Pengurusan Pengguna (Authentication / Registration)
- **Target:** https://martp.nizamjensani.digital/
- **Date:** 2026-09-25
- **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Artis account with password set.

## Steps
1. Open `/login`.
2. Enter `qa.artis.test01@mailinator.com` / `Test@12345`.
3. Submit.

## Expected result
Lands on dashboard with Artis modules.

## Actual result
Redirected to `/dashboard`. Sidebar: Tutorial, Perkongsian, Koleksi, Art For Sale, Profil Saya, Inbox. Profile page loads.

## Evidence
No screenshot captured for this test; result observed via page text.
