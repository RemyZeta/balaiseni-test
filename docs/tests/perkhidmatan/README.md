# Perkhidmatan (Services) — Test Documentation

Feature folder: **perkhidmatan**. Admin-only module `/dashboard/services` (listing of art-industry services: framing, packing, handling, insurance, restoration, curatorship, rentals, commissions). Fields: image (4 MB), Nama perkhidmatan, Nama penyedia (both required), Huraian, Khidmat ditawarkan, Beroperasi di. Admin listings are approved directly; public directory `/shop/services` has search and a contact form protected by reCAPTCHA. The module had 0 listings before testing. Test images came from the project `images/` folder.

| ID | Test | Status |
|---|---|---|
| [SVC-01](SVC-01-required-fields.md) | Create — required name and provider | PASS (cosmetic) |
| [SVC-02](SVC-02-image-validation.md) | Image — wrong type and over 4 MB | PASS |
| [SVC-03](SVC-03-create.md) | Create a service (auto-approved) | PASS |
| [SVC-04](SVC-04-public-listing-detail.md) | Public listing, search and detail | PASS |
| [SVC-05](SVC-05-contact-provider.md) | Hubungi Pembekal contact form | BLOCKED (reCAPTCHA) |
| [SVC-06](SVC-06-edit-and-injection.md) | Edit and HTML / script injection | PASS |
| [SVC-07](SVC-07-reject-reapprove.md) | Reject and re-approve | PASS (observation: no reason) |
| [SVC-08](SVC-08-delete.md) | Delete with confirmation | PASS |
| [SVC-09](SVC-09-role-access.md) | Non-admin and anonymous access | PASS |

No functional test failed; the contact form could not be completed (reCAPTCHA). See [FAILURES.md](FAILURES.md).

## Not tested
Contact form submission and the provider's Inbox (reCAPTCHA), replacing or removing the image, PNG/WebP, very long text, artist- or gallery-created services (artists and galleries cannot access this module), English pages, dashboard filters and search, pagination.

## Cleanup
The QA listing was deleted; the module is back to 0 listings.
