# PRF-18 — Profile pages need login

- **Module:** Profil Pengguna (update profile)
- **Target:** https://martp.nizamjensani.digital/ · `/dashboard/profile` (Profil Saya) · `/settings/profile` (tetapan akaun)
- **Date:** 2026-10-01 · **Tool:** playwright-cli (headed) · **Role:** Anonymous visitor
- **Priority:** P1
- **Status:** **PASS**

## Preconditions
Logged out.

## Steps
1. Open `/dashboard/profile`.
2. Open `/settings/profile`.

## Expected result
Redirect to login.

## Actual result
Both redirect to `/login`. After logging in, the site returned to the last requested page (`/settings/profile`).

## Evidence
![redirect](evidence/prf-anon-redirect.png)
