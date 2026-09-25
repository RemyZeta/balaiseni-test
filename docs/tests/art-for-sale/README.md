# Art For Sale — Test Documentation

Feature folder: **art-for-sale**. Module `/dashboard/art-for-sale` for Artist and Admin (Galeri is blocked). Artist listings wait for admin approval; admin listings are approved directly. Public catalogue `/shop/art-for-sale` (filters: category and price range) with a 'Hubungi Penjual' contact form protected by reCAPTCHA. Accounts: Artist QA, Galeri QA (403 test), Admin via login-page quick-login. The 73 real listings were not touched; only QA items were approved, rejected, edited or deleted.

| ID | Test | Status |
|---|---|---|
| [AFS-01](AFS-01-required-fields.md) | Create — required title and artist name | PASS (cosmetic) |
| [AFS-02](AFS-02-image-validation.md) | Image — wrong type and over 4 MB | PASS |
| [AFS-03](AFS-03-price-field.md) | Harga (RM) rules and negotiable checkbox | PASS (observation: whole numbers only) |
| [AFS-04](AFS-04-artist-create-pending.md) | Artist creates listings → pending, hidden | PASS |
| [AFS-05](AFS-05-admin-approve-reject.md) | Admin approves one listing and rejects the other | PASS (observation: no reason) |
| [AFS-06](AFS-06-public-listing-detail.md) | Public listing, filters and detail page | PASS |
| [AFS-07](AFS-07-negotiable-flag.md) | Negotiable flag visibility | PASS (observation: not shown publicly) |
| [AFS-08](AFS-08-contact-seller.md) | Hubungi Penjual form | BLOCKED (reCAPTCHA) |
| [AFS-09](AFS-09-admin-edit-sanitisation.md) | Edit listing; HTML / script injection | PASS |
| [AFS-10](AFS-10-edit-approved-bypass.md) | Artist edits an approved listing (title and price) | FAIL (needs product decision) |
| [AFS-11](AFS-11-delete.md) | Delete listings (Artist) with Batal | PASS |
| [AFS-12](AFS-12-admin-create.md) | Admin creates a listing directly | PASS |
| [AFS-13](AFS-13-role-access.md) | Role access | PASS |

One test failed (AFS-10) and one was blocked (AFS-08). See [FAILURES.md](FAILURES.md).

## Not tested
The contact-seller send and seller Inbox (blocked by reCAPTCHA — a human can tick the box and I can continue), replacing or removing an image, PNG/WebP, editing a rejected listing, one artist seeing another's listing by direct URL, price-range and category filter results with real data, English pages (`/en/shop/…`), very long titles or descriptions, pagination of 73 listings, dashboard filters and search.

## Cleanup
All three QA listings were deleted. Admin counters are back to 73 total / 73 approved / 0 pending.
