# TUT-02 — Artist creates tutorial — goes to pending

- **Module:** Tutorial (Artist dashboard + Admin review)
- **Target:** https://martp.nizamjensani.digital/
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
Artist QA account `qa.artis.test01@mailinator.com` logged in.

## Steps
1. Tambah tutorial.
2. Fill Tajuk `QA Tutorial Melukis Potret 01`, Tarikh siar 2026-09-25, Huraian, Pembentang `QA Test Artis`, URL video luar (YouTube).
3. Simpan video.

## Expected result
Video saved with status 'Menunggu semakan'. Modal says video will be reviewed by admin before appearing publicly.

## Actual result
Saved. List counters: JUMLAH 1, DILULUSKAN 0, MENUNGGU SEMAKAN 1; card shows 'Menunggu semakan'.

## Evidence
TUT-020
