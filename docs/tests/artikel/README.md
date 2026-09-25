# Artikel — Test Documentation

Feature folder: **artikel**. Admin-only module (`/dashboard/articles`), public `/resources/articles`. Admin-created articles are approved directly. Test images came from the project `images/` folder (24 KB valid; 4.7 MB oversize).

| ID | Test | Status |
|---|---|---|
| [ART-01](ART-01-required-title.md) | Create — required title | PASS (cosmetic) |
| [ART-02](ART-02-image-invalid-type.md) | Image upload — wrong file type | PASS |
| [ART-03](ART-03-image-oversize.md) | Image upload — over 4 MB | PASS |
| [ART-04](ART-04-create-with-image.md) | Create article with cover image → auto-approved | PASS |
| [ART-05](ART-05-public-listing-detail.md) | Public listing, search, detail with image | PASS |
| [ART-06](ART-06-edit.md) | Edit article | PASS |
| [ART-07](ART-07-html-sanitisation.md) | HTML / script injection in title and body | PASS |
| [ART-08](ART-08-reject-hides.md) | Reject → hidden from public | PASS (observation: no reason) |
| [ART-09](ART-09-reapprove.md) | Re-approve → visible again | PASS |
| [ART-10](ART-10-delete.md) | Delete with confirmation and Batal | PASS |
| [ART-11](ART-11-role-access.md) | Non-admin access | PASS |

No functional test failed. See [FAILURES.md](FAILURES.md).

## Not tested
PNG/WebP upload, replacing or removing an existing image, Petikan over 500 characters, Badan penuh over 5000, Pautan sumber validation (non-URL), future Tarikh siar visibility, server-side size check, pagination, dashboard search, user (non-admin) submission.

## Cleanup
The QA article was deleted. Count back to 11.
