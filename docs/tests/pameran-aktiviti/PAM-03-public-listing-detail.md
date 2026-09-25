# PAM-03 — Public listing, search and detail page

- **Module:** Pameran & Aktiviti (Admin)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/exhibitions` · public `/resources/exhibitions`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
PAM-02 done.

## Steps
1. Open `/resources/exhibitions`, search the title.
2. Open the item.

## Expected result
Item listed with correct data; detail page works.

## Actual result
Listed under the Pameran tab (count 1) with organiser, location and 'Dicipta oleh Ahmad Safwan'. Detail page `/resources/exhibitions/qa-pameran-ujian-01` shows title, organiser, dates, location, description and external link.

## Evidence
![public](evidence/pam-public.png) ![detail](evidence/pam-detail.png)
