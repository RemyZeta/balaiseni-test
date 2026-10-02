# PRF-03 — Website and social link validation

- **Module:** Profil Pengguna (update profile)
- **Target:** https://martp.nizamjensani.digital/ · `/dashboard/profile` (Profil Saya) · `/settings/profile` (tetapan akaun)
- **Date:** 2026-10-01 · **Tool:** playwright-cli (headed) · **Role:** Artist (QA), Admin
- **Priority:** P1
- **Status:** **PASS (observation: `http://` accepted)**

## Preconditions
Logged in.

## Steps
1. Set Laman web to `example.com`, save.
2. Set Laman web to `javascript:alert(1)`, save.
3. Set Facebook to `bukan url`, save.
4. Set Laman web to `http://example.com`, save.
5. As Admin, set Laman web to `bukan-url`, save.
6. Reload after each case.

## Expected result
Invalid URLs rejected with a message and not saved; `javascript:` never accepted.

## Actual result
`example.com`, `javascript:alert(1)` and Admin `bukan-url`: "Medan laman web mesti URL yang sah, bermula dengan https://" (shown as a toast and under the field), not saved. `bukan url` in Facebook: "Medan Facebook mesti URL yang sah, bermula dengan https://", not saved.

**Observation:** `http://example.com` was **accepted** ("Profil anda telah dikemas kini.") although the message and hint say links must start with `https://`. Low impact. Either the message or the rule should change.

## Evidence
Toast and field text recorded during the run (no screenshot).
