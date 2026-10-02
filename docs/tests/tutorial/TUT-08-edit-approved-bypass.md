# TUT-08 — Artist edits an approved tutorial

- **Module:** Tutorial (Artist dashboard + Admin review)
- **Target:** https://martp.nizamjensani.digital/
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed)
- **Priority:** P0
- **Status:** **FAIL (if re-review is required) — needs product decision**

## Preconditions
Approved tutorial live publicly; artist logged in.

## Steps
1. Click Sunting, change title to '… (Edit selepas lulus)'.
2. Simpan video.
3. Check list and public page.

## Expected result
Either the item returns to 'Menunggu semakan' or the change waits for admin re-approval.

## Actual result
**Status stays Diluluskan and the new title is public immediately** — no re-review. This lets an artist change approved content without admin approval. **Potential defect / business-rule gap — confirm intended behaviour.**

## Evidence
TUT-080

## Retest 2026-10-01
**PASS (fixed)**. See [RT-TUT-08](../retest-2026-10-01/RT-TUT-08.md).
