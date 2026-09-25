# BRT-06 — HTML / script injection in title and Petikan

- **Module:** Berita (Admin)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/news` · public `/resources/news`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Edit form open.

## Steps
1. Title `… <b>tebal</b>`.
2. Petikan (Kod HTML) with `<script>`, `<img onerror>`, `javascript:` link.
3. Save; open public detail.

## Expected result
Escaped or stripped; nothing executes.

## Actual result
Title shown as literal text. Public page has no `<script>`, `onerror` or `javascript:` link; `window.__x*` undefined; no dialog fired.

## Evidence
![xss](evidence/brt-detail-xss.png)
