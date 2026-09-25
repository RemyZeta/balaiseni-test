# Koleksi — Failures & Issues

## Summary
| # | Severity | Type | Issue | Source test |
|---|---|---|---|---|
| K-F1 | High | FAIL | Admin cannot change an item's Koleksi type on edit; the toast says updated but the type stays 'Karya artis' | [KOL-09](KOL-09-edit-koleksi-type.md) |
| K-F2 | High | FAIL (needs product decision) | Editing an approved karya (Artist or Galeri) publishes changes without admin re-approval | [KOL-10](KOL-10-edit-approved-bypass.md) |
| K-I1 | Low | Gap | Rejecting is instant with no reason or confirmation (same as other modules) | [KOL-07](KOL-07-admin-reject-reapprove.md) |
| K-I2 | Low | Observation | Kategori seni offers a single lower-case option 'realisme' | [KOL-02](KOL-02-image-validation.md) |
| K-I3 | Low | Cosmetic | English native tooltip on required title | [KOL-01](KOL-01-required-title.md) |

## K-F1 — Koleksi type not saved on edit
- **Steps:** Create an admin work as 'Karya artis' (default). Sunting → change Koleksi to 'Koleksi Tetap Balai Seni Negara' → Simpan. Reload and reopen.
- **Expected:** Type changes; the KOLEKSI TETAP counter goes 99→100; the work appears on `/resources/nag-collection`.
- **Actual:** Toast says updated, but the type is still 'Karya artis' (counter stays 99, nag-collection shows 0). Reproduced twice. The same choice made at creation is saved correctly.
- **Impact:** A work created in the wrong collection cannot be moved without deleting and re-creating it.

## K-F2 — Edit after approval skips review
Same behaviour as Tutorial (T-F1) and Perkongsian (S-F1). An Artist and a Galeri each renamed an approved work and the new title was public at once. Likely one shared root cause across modules that use the same workflow.
