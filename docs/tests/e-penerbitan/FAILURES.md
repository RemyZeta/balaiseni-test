# E-Penerbitan — Failures & Issues

No test failed. Observations and cosmetic issues only.

| # | Severity | Type | Issue | Source |
|---|---|---|---|---|
| E-I1 | Medium | Observation | Deleted (and rejected) PDFs stay downloadable from the CDN cache (`public, max-age=2592000`, 30 days) even though the dialog says the file is removed; a cache-busted request returns 404 | [EPB-10](EPB-10-delete-and-file.md), [EPB-09](EPB-09-reject-reapprove.md) |
| E-I2 | Low | Gap | Rejecting is instant with no reason or confirmation (same as other modules) | [EPB-09](EPB-09-reject-reapprove.md) |
| E-I3 | Low | Cosmetic | English text in server validation ("The Fail PDF field must be a file of type: application/pdf.") and native tooltip | [EPB-04](EPB-04-pdf-fake-content.md), EPB-01 |
| E-I4 | Low | Observation | Pautan luar is hidden on the public page when a PDF is attached | [EPB-06](EPB-06-public-listing-download.md) |
| E-I5 | Low | Observation | Slug does not change after the title is edited | [EPB-07](EPB-07-edit.md) |

## Positive
Server-side content check rejects a text file renamed .pdf (EPB-04); HTML/script input is neutralised (EPB-08).

## Note on E-I1
An admin unpublishing sensitive material may expect it to disappear immediately. If that matters, purge the CDN cache on delete/reject or use short cache times for these files.
