# EPB-02 — Cover image — wrong type and over 4 MB

- **Module:** E-Penerbitan (Admin)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/epublications` · public `/resources/e-publications`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** P1
- **Status:** **PASS**

## Preconditions
Create form open. `fake.txt`; `still_life_itik.jpg` (4.7 MB from `images/`).

## Steps
1. Choose `fake.txt` as Gambar kulit.
2. Choose the 4.7 MB JPG.

## Expected result
Both rejected.

## Actual result
'Hanya fail JPG, PNG atau WebP diterima.' and 'Gambar melebihi 4 MB.' shown inline (client-side).

## Evidence
-
