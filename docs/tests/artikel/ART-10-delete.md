# ART-10 — Delete with confirmation and Batal

- **Module:** Artikel (Admin)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/articles` · public `/resources/articles`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Approved article.

## Steps
1. Padam → Batal.
2. Padam → Padam.
3. Check dashboard and detail URL.

## Expected result
Batal keeps it; confirm removes it and detail returns 404.

## Actual result
Dialog: 'Padam "…"? Artikel ini akan dibuang terus… tidak boleh dibatalkan.' Batal keeps the item. After confirming, count returns to 11 and the detail URL returns 404.

## Evidence
![delete](evidence/art-delete-confirm.png)
