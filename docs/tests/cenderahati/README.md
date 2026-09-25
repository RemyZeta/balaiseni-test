# Cenderahati (Merchandises) — Test Documentation

Feature folder: **cenderahati**. Admin-only module `/dashboard/merchandises` (sidebar name Cenderahati; page title "Merchandises"). Fields: image (4 MB), Nama barangan and Nama penjual (required), Huraian, Harga (RM, whole numbers), Harga boleh dirunding, Jenis produk. Admin listings are approved directly; public shop `/shop/merchandises` has search and a reCAPTCHA-protected contact form. The module had 0 listings before testing. Test images came from the project `images/` folder.

| ID | Test | Status |
|---|---|---|
| [MER-01](MER-01-required-fields.md) | Create — required name and seller | PASS (cosmetic) |
| [MER-02](MER-02-image-validation.md) | Image — wrong type and over 4 MB | PASS |
| [MER-03](MER-03-price-field.md) | Harga (RM) rules | PASS (observation: whole numbers only) |
| [MER-04](MER-04-create.md) | Create merchandise with negotiable price (auto-approved) | PASS |
| [MER-05](MER-05-public-listing-detail.md) | Public listing and detail | PASS (observation: negotiable not shown) |
| [MER-06](MER-06-contact-seller.md) | Hubungi Penjual contact form | BLOCKED (reCAPTCHA) |
| [MER-07](MER-07-edit-and-injection.md) | Edit (including price) and HTML / script injection | PASS |
| [MER-08](MER-08-reject-reapprove.md) | Reject and re-approve | PASS (observation: no reason) |
| [MER-09](MER-09-delete.md) | Delete with confirmation | PASS |
| [MER-10](MER-10-role-access.md) | Non-admin and anonymous access | PASS (observation: mixed naming) |

No functional test failed; the contact form could not be completed (reCAPTCHA). See [FAILURES.md](FAILURES.md).

## Not tested
Contact form submission and the seller's Inbox (reCAPTCHA), replacing or removing the image, PNG/WebP, price 0 or empty price display, artist- or gallery-created merchandise (they cannot access this module), English pages, dashboard filters and search, pagination.

## Cleanup
The QA listing was deleted; the module is back to 0 listings.
