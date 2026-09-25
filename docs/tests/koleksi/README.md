# Koleksi — Test Documentation

Feature folder: **koleksi**. Module `/dashboard/collection` is used by three roles. Admin sees all works (about 2,566) and creates items that are approved directly; Artist and Galeri see only their own works and their new works wait for admin approval. Two types: **Karya artis** (public `/resources/artists-art`) and **Koleksi Tetap Balai Seni Negara** (public `/resources/nag-collection`; admin only). Both appear on `/collection`. Accounts: Artist QA, Galeri QA, Admin via login-page quick-login. Real items (for example another user's pending 'Karya Baru') were not touched.

| ID | Test | Status |
|---|---|---|
| [KOL-01](KOL-01-required-title.md) | Create — required title (Artist) | PASS (cosmetic) |
| [KOL-02](KOL-02-image-validation.md) | Image — wrong type and over 4 MB | PASS |
| [KOL-03](KOL-03-artist-create-pending.md) | Artist creates a karya → pending | PASS |
| [KOL-04](KOL-04-galeri-create-pending.md) | Galeri creates a karya → pending, own items only | PASS |
| [KOL-05](KOL-05-pending-hidden.md) | Pending karya hidden from public | PASS |
| [KOL-06](KOL-06-admin-approve.md) | Admin reviews and approves → public | PASS |
| [KOL-07](KOL-07-admin-reject-reapprove.md) | Admin rejects Galeri item, then re-approves | PASS (observation: no reason) |
| [KOL-08](KOL-08-admin-create.md) | Admin creates works directly (auto-approved, Koleksi Tetap) | PASS |
| [KOL-09](KOL-09-edit-koleksi-type.md) | Admin changes an item's Koleksi type on edit | FAIL |
| [KOL-10](KOL-10-edit-approved-bypass.md) | Artist/Galeri edits an approved karya | FAIL (if re-review required) — needs product decision |
| [KOL-11](KOL-11-html-sanitisation.md) | HTML / script injection | PASS |
| [KOL-12](KOL-12-delete.md) | Delete with confirmation (Artist, Galeri, Admin) | PASS |

Two tests failed (KOL-09, KOL-10). See [FAILURES.md](FAILURES.md).

## Not tested
Rejected item edited and resubmitted by its owner, another user opening or editing someone else's item by direct URL, Art For Sale sharing (Kategori seni is shared with that module), replacing or removing an image, PNG/WebP upload, more than one art category, the dashboard collection/status/category filters and search results, very long descriptions (limit 5,000), pagination of 2,500+ items, the 'Tempah lawatan kajian' and share buttons.

## Cleanup
All four QA works were deleted. Admin totals are back to 2,566 / 99 Koleksi Tetap / 2,467 Karya artis.
