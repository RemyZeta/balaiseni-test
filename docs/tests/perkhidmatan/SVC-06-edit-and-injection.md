# SVC-06 — Edit and HTML / script injection

- **Module:** Perkhidmatan (Services) (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/services` · public `/shop/services`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Approved item.

## Steps
1. Sunting; read pre-filled values.
2. Change the name to `… <b>tebal</b>`, description (Kod HTML) with `<script>`, `<img onerror>`, `javascript:` link, offerings `<b>Framing</b>, Restorasi`; save.
3. Open the public detail.

## Expected result
Pre-filled; saved; markup escaped.

## Actual result
Pre-filled (name, provider, offerings, location, image). Saved; toast 'telah dikemas kini'. Name and offerings appear as literal text (`<b>Framing</b>`); no `<b>`, `<script>`, `onerror` or `javascript:` link; `window.__x*` undefined.

## Evidence
![edit](evidence/svc-edit.png) ![xss](evidence/svc-detail-xss.png)
