# AFS-02 — Image — wrong type and over 4 MB

- **Module:** Art For Sale (Admin, Artist)
- **Target:** https://martp.nizamjensani.digital/ · dashboard `/dashboard/art-for-sale` · public `/shop/art-for-sale`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P1
- **Status:** **PASS**

## Preconditions
Create form open. `fake.txt`; `still_life_itik.jpg` (4.7 MB from `images/`).

## Steps
1. Choose `fake.txt`.
2. Choose the 4.7 MB JPG.

## Expected result
Both rejected.

## Actual result
'Hanya fail JPG, PNG atau WebP diterima.' and 'Gambar melebihi 4 MB.' shown inline (client-side).

## Evidence
![oversize](evidence/afs-oversize.png)
