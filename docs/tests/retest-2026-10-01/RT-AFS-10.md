# RT-AFS-10 — Retest: Art For Sale: edit after approval (title and price)

- **Original test:** [AFS-10](../art-for-sale/AFS-10-edit-approved-bypass.md) (was **FAIL**)
- **Target:** https://martp.nizamjensani.digital/
- **Date:** 2026-10-01 · **Tool:** playwright-cli (headed) · **Role:** Artist (QA), Admin
- **Status:** **PASS (fixed)**

## Steps
1. Owner creates a new QA item (titles `QA RT …`); admin approves it with Luluskan.
2. Anonymous visitor checks the public page: item visible.
3. Owner opens Sunting, changes the title to `… (Edit selepas lulus)` (Art For Sale also price 1500 → 9999), saves.
4. Check the owner dashboard card and counters, then the public page as an anonymous visitor.
5. Admin checks the card actions and Barisan Semakan; deletes the QA items at the end.

## Expected result
The new title and price wait for admin review; the approved price stays public.

## Actual result
The edit form now says **"Perubahan anda akan disemak oleh pentadbir. Versi semasa kekal dipaparkan kepada umum sehingga diluluskan."** Saving gives the toast **"Suntingan "…" dihantar untuk semakan. Versi semasa kekal dipaparkan sehingga diluluskan."** The card changes from "Diluluskan" to **"Suntingan menunggu"**, still shows the old title, and the counters show DILULUSKAN 1 and MENUNGGU SEMAKAN 1. The anonymous public page still shows the **old** title. Admin sees "Luluskan suntingan" / "Tolak suntingan" on the card, and Barisan Semakan counts the edit under Karya.

While pending, the card and the public listing kept **RM 1,500** ("…kekal dipaparkan kepada pembeli sehingga diluluskan"). Admin then clicked **"Luluskan suntingan"**: toast "…kini Diluluskan.", and the public listing switched to "QA RT Jual 01 (Edit selepas lulus)" **RM 9,999**. The full review cycle works.

## Evidence
![owner card (RM 1,500, Suntingan menunggu)](evidence/rt-bypass-art-for-sale-artis.png) ![public after admin approved edit](evidence/rt-afs10-approved-edit-public.png) ![review queue](evidence/rt-bypass-review-queue.png)
