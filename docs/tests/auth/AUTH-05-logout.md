# AUTH-05 — Logout

- **Module:** Pengurusan Pengguna (Authentication / Registration)
- **Target:** https://martp.nizamjensani.digital/
- **Date:** 2026-09-25
- **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Logged in as Artis.

## Steps
1. Click Menu akaun.
2. Click Log keluar.

## Expected result
Session ends; user returned to public site.

## Actual result
Menu shows Tetapan and Log keluar. After Log keluar, URL is `/`.

## Evidence
No screenshot captured for this test; result observed via page text.
