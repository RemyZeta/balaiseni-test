# PAM-11 — Non-admin access to admin module

- **Module:** Pameran & Aktiviti (Admin)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/exhibitions` · public `/resources/exhibitions`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS (observation)**

## Preconditions
Artist QA account logged in.

## Steps
1. Open `/dashboard/exhibitions` directly.

## Expected result
Access denied.

## Actual result
HTTP 403; page 'Akses Dilarang', body '403 This action is unauthorized.' (English). Artist sidebar has no Pameran & Aktiviti entry. Inconsistency: the registration page lists 'Pameran & Aktiviti' among the modules new users get in their dashboard.

## Evidence
-
