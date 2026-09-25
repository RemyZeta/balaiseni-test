# TUT-05 — Admin rejects tutorial

- **Module:** Tutorial (Artist dashboard + Admin review)
- **Target:** https://martp.nizamjensani.digital/
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS (observation)**

## Preconditions
Pending item from TUT-02; admin logged in.

## Steps
1. Click Tolak on the item.
2. Log in as the artist and open the Tutorial list.
3. Check the public page.

## Expected result
Status becomes Ditolak; not public; artist sees the status.

## Actual result
Toast '"…" kini Ditolak.' Rejection is immediate with **no reason field or confirmation**. Artist list shows 'Ditolak'. Public search: no result. Observation: artist gets no reason for rejection.

## Evidence
TUT-050
