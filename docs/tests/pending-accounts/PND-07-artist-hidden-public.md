# PND-07 — Unapproved Artist in the public directory

- **Module:** Unapproved Artist and Galeri accounts (cross-module)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/review-queue` · roles Artist and Galeri
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **PASS**

## Preconditions
QA Artist unapproved, profile now has a photo.

## Steps
1. Anonymous searches `/resources/artists?search=QA Test Artis`.
2. Try a guessed profile slug.

## Expected result
Not listed until approved.

## Actual result
0 artis found; guessed slug returns 404. The directory lists 687 artists without the QA account.

## Evidence
-
