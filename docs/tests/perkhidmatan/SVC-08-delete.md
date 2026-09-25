# SVC-08 — Delete with confirmation

- **Module:** Perkhidmatan (Services) (Admin only)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/services` · public `/shop/services`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Approved item.

## Steps
1. Padam → Batal.
2. Padam → Padam.
3. Check counter and detail URL.

## Expected result
Batal keeps; confirm removes; detail 404.

## Actual result
Dialog: 'Padam "…"? Penyenaraian ini akan dibuang terus daripada portal. Tindakan ini tidak boleh dibatalkan.' Batal keeps (count 1). After confirming: count 0 and detail URL 404.

## Evidence
![delete](evidence/svc-delete-confirm.png)
