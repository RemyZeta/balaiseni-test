# AFS-09 — Edit listing; HTML / script injection

- **Module:** Art For Sale (Admin, Artist)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/art-for-sale` · public `/shop/art-for-sale`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Approved item `Runding 02`.

## Steps
1. Sunting; read pre-filled values.
2. Set price 800, tick negotiable, title `… <b>tebal</b>`, description `<script>`/`onerror`; save.
3. Open the public page.

## Expected result
Saved; markup escaped.

## Actual result
Pre-filled correctly. Saved (toast 'telah dikemas kini'); title shown literally; no `<b>`, `<script>` or `onerror` elements; `window.__x*` undefined.

## Evidence
-
