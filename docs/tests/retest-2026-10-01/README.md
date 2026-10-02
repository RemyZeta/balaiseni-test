# Retest of earlier failed/blocked tests — 2026-10-01

Every earlier test with status FAIL or BLOCKED was run again in a headed browser.

| Original | Test | Before | Retest |
|---|---|---|---|
| [TUT-08](RT-TUT-08.md) | Tutorial: edit after approval | FAIL | **PASS (fixed)** |
| [SHR-09](RT-SHR-09.md) | Perkongsian: edit after approval | FAIL | **PASS (fixed)** |
| [KOL-10](RT-KOL-10.md) | Koleksi: edit after approval (Artist and Galeri) | FAIL | **PASS (fixed)** |
| [GAL-09](RT-GAL-09.md) | Galeri: edit after approval | FAIL | **PASS (fixed)** |
| [AFS-10](RT-AFS-10.md) | Art For Sale: edit after approval (title and price) | FAIL | **PASS (fixed)** |
| [KOL-09](RT-KOL-09.md) | Koleksi: change type on edit | FAIL | **PASS (fixed)** |
| [PTN-05](RT-PTN-05.md) | Pautan: URL validation | FAIL | **PASS (fixed)** |
| [PTU-08](RT-PTU-08.md) | Banner: button link validation | FAIL | **PASS (fixed)** |
| [PTU-11](RT-PTU-11.md) | Banner: delete confirmation | FAIL | **PASS (fixed)** |
| [PND-08](RT-PND-08.md) | Unapproved Galeri in the public directory | FAIL | **FAIL (still open)** |
| [PRF-04](RT-PRF-04.md) | Profile: phone and postcode format | FAIL | **FAIL (still open, all 3 roles)** |
| [AFS-08](RT-AFS-08.md) | Art For Sale: contact seller | BLOCKED | **BLOCKED (reCAPTCHA)** |
| [SVC-05](RT-SVC-05.md) | Perkhidmatan: contact provider | BLOCKED | **BLOCKED (reCAPTCHA)** |
| [MER-06](RT-MER-06.md) | Cenderahati: contact seller | BLOCKED | **BLOCKED (reCAPTCHA)** |

**Result:** 9 fixed (now PASS), 2 still FAIL (PND-08, PRF-04), 3 still BLOCKED by reCAPTCHA (AFS-08, SVC-05, MER-06).

## Main finding
The **edit-after-approval bypass is fixed** in all five modules (Tutorial, Perkongsian, Koleksi, Galeri, Art For Sale). An owner's edit to an approved item is now saved as a pending revision ("Suntingan menunggu"), the approved version stays public, and admin gets "Luluskan suntingan" / "Tolak suntingan". Both admin actions were checked: approving published the new title and price, rejecting kept the old version live.

## New observations
- Rejecting a pending edit shows "\"… (Edit selepas lulus)\" kini Ditolak.", which reads as if the whole item was rejected; no reason is asked (RT-TUT-08).
- Perkhidmatan and Cenderahati have **0 public listings**, so their contact forms can only be reached after adding a listing.

## Accounts used
Artist `qa.artis.test01@mailinator.com`, Galeri `qa.galeri.test01@mailinator.com`, Admin quick-login "Ahmad Safwan".

## Not tested
Sending a contact message (reCAPTCHA, not bypassed), Galeri slideshow/image edits after approval, an owner editing an item that already has a pending edit, and editing a rejected-edit item again.

## Cleanup
All test data was deleted (9 QA RT items, 1 QA link, 1 QA banner, 1 Koleksi item, 1 service, 1 merchandise). Review queue back to 0 apart from the 3 earlier membership requests. Pautan total 8, Koleksi counters 2,565 / 99 / 2,466, one live banner. Profile phone/postcode values restored for all three roles.
