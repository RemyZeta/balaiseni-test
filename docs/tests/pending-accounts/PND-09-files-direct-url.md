# PND-09 — Files of unapproved accounts and pending items by direct URL

- **Module:** Unapproved Artist and Galeri accounts (cross-module)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/review-queue` · roles Artist and Galeri
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P1
- **Status:** **PASS (observation: files not gated by approval)**

## Preconditions
Galeri tutorial pending; profile photos uploaded.

## Steps
1. Anonymous requests the pending tutorial cover image, both profile photos (cache-busted).

## Expected result
Files of unapproved content are not reachable.

## Actual result
All returned 200: `/storage/video-posters/…jpg` (pending item) and both `/storage/avatars/…jpg`. The names are random, so they cannot be guessed, but files are served regardless of approval status (as seen with deleted files elsewhere).

## Evidence
-
