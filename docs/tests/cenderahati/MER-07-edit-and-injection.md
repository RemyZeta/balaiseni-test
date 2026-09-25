# MER-07 — Edit (including price) and HTML / script injection

- **Module:** Cenderahati (Merchandises) (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/merchandises` · public `/shop/merchandises`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Approved item.

## Steps
1. Sunting; read pre-filled values (price 45, negotiable ticked, product type).
2. Change price to 60, name `… <b>tebal</b>`, product type `<script>…</script>Baju`, description with `<script>`/`onerror`; save.
3. Open the public detail.

## Expected result
Pre-filled; saved; markup escaped.

## Actual result
Pre-filled correctly. Saved; the public page shows RM 60. Name and product type appear as literal text (the product type shows `<script>window.__x=1</script>Baju` as plain text); no elements created; `window.__x*` undefined.

## Evidence
![edit](evidence/mer-edit.png) ![xss](evidence/mer-detail-xss.png)
