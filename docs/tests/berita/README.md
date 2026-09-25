# Berita — Test Documentation

Feature folder: **berita**. Admin-only module (`/dashboard/news`), public `/resources/news` (with Kategori, year and Media filters). Admin-created items are approved directly. The module had 0 items before testing. Test images came from the project `images/` folder (24 KB valid; 4.7 MB oversize).

| ID | Test | Status |
|---|---|---|
| [BRT-01](BRT-01-required-title.md) | Create — required title | PASS (cosmetic) |
| [BRT-02](BRT-02-image-validation.md) | Image — wrong type and over 4 MB | PASS |
| [BRT-03](BRT-03-create-approved.md) | Create berita → auto-approved | PASS |
| [BRT-04](BRT-04-public-listing-detail.md) | Public listing, facets and detail | PASS |
| [BRT-05](BRT-05-edit.md) | Edit berita | PASS |
| [BRT-06](BRT-06-html-sanitisation.md) | HTML / script injection in title and Petikan | PASS |
| [BRT-07](BRT-07-link-validation.md) | Pautan laporan asal validation | PASS (observation: message says https only) |
| [BRT-08](BRT-08-reject-reapprove.md) | Reject and re-approve | PASS (observation: no reason) |
| [BRT-09](BRT-09-delete.md) | Delete with confirmation and Batal | PASS |
| [BRT-10](BRT-10-role-access.md) | Non-admin access | PASS |

No functional test failed. See [FAILURES.md](FAILURES.md).

## Not tested
PNG/WebP upload, replacing or removing the image, Petikan over 2000 characters, category "Tiada kategori", the year and Media filters with real data, future Tarikh siar, a berita without a link, pagination, dashboard search and status filter.

## Cleanup
The QA berita was deleted; count is back to 0.
