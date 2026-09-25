# BRT-02 — Image — wrong type and over 4 MB

- **Module:** Berita (Admin)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/news` · public `/resources/news`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P1
- **Status:** **PASS**

## Preconditions
Create form open. `fake.txt`; `still_life_itik.jpg` (4.7 MB from `images/`).

## Steps
1. Choose `fake.txt` in Gambar.
2. Choose the 4.7 MB JPG.

## Expected result
Both rejected.

## Actual result
'Hanya fail JPG, PNG atau WebP diterima.' and 'Gambar melebihi 4 MB.' shown inline (client-side).

## Evidence
![oversize](evidence/brt-oversize.png)
