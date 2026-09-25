# E-Penerbitan — Test Documentation

Feature folder: **e-penerbitan**. Admin-only module (`/dashboard/epublications`; note the dashboard URL has no hyphen), public `/resources/e-publications`. Admin-created items are approved directly. The module had 0 items before testing. Test files: a 24 KB JPG from `images/`, a 4.7 MB JPG (oversize), and generated PDFs (valid 193 bytes, 41 MB oversize, text renamed .pdf).

| ID | Test | Status |
|---|---|---|
| [EPB-01](EPB-01-required-title.md) | Create — required title | PASS (cosmetic) |
| [EPB-02](EPB-02-cover-image-validation.md) | Cover image — wrong type and over 4 MB | PASS |
| [EPB-03](EPB-03-pdf-validation.md) | PDF — wrong type and over 40 MB | PASS |
| [EPB-04](EPB-04-pdf-fake-content.md) | Text file renamed .pdf | PASS (cosmetic) |
| [EPB-05](EPB-05-create-with-pdf.md) | Create publication with cover and PDF → auto-approved | PASS |
| [EPB-06](EPB-06-public-listing-download.md) | Public listing, detail and PDF download | PASS (observation) |
| [EPB-07](EPB-07-edit.md) | Edit publication | PASS |
| [EPB-08](EPB-08-html-sanitisation.md) | HTML / script injection | PASS |
| [EPB-09](EPB-09-reject-reapprove.md) | Reject and re-approve | PASS (observation) |
| [EPB-10](EPB-10-delete-and-file.md) | Delete removes item and file | PASS (observation: CDN keeps deleted PDF) |
| [EPB-11](EPB-11-role-access.md) | Non-admin access | PASS |

No functional test failed. See [FAILURES.md](FAILURES.md).

## Not tested
Real multi-page PDF, PDF up to 40 MB accepted, replacing or removing an existing PDF/cover, publication with external link only (no PDF), PNG/WebP cover, invalid Pautan luar, future dates, pagination, dashboard search, status filter.

## Cleanup
The QA publication was deleted; count is back to 0.
