# AUTH-09 — Register, set password, login as Galeri

- **Module:** Pengurusan Pengguna (Authentication / Registration)
- **Target:** https://martp.nizamjensani.digital/
- **Date:** 2026-09-25
- **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Email not previously registered.

## Steps
1. Register at `/register` with Kategori = Galeri (name `QA Test Galeri`, email `qa.galeri.test01@mailinator.com`, phone, address, URL).
2. Set password `Test@12345`.
3. Log out, log in again, log out.

## Expected result
Full flow succeeds; Galeri-specific dashboard.

## Actual result
All steps succeeded. Sidebar has Galeri module (`/dashboard/galleries`) instead of Art For Sale. Profile stored the phone, URL and address entered.

## Evidence
No screenshot captured for this test; result observed via page text.
