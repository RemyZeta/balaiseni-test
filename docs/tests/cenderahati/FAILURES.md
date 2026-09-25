# Cenderahati — Failures & Issues

No test failed. One test blocked; observations only.

| # | Severity | Type | Issue | Source test |
|---|---|---|---|---|
| M-B1 | — | BLOCKED | Contact form needs a human to tick reCAPTCHA; sending and the seller Inbox are unverified | [MER-06](MER-06-contact-seller.md) |
| M-I1 | Medium | Observation | 'Harga boleh dirunding' is saved and shown in the dashboard ('RM 45 boleh runding') but not on the public listing or detail | [MER-05](MER-05-public-listing-detail.md) |
| M-I2 | Low | Observation | Price accepts whole ringgit only | [MER-03](MER-03-price-field.md) |
| M-I3 | Low | Gap | Rejecting is instant with no reason or confirmation (same as other modules) | [MER-08](MER-08-reject-reapprove.md) |
| M-I4 | Low | Cosmetic | English native tooltips; module named 'Cenderahati' in the sidebar but 'Merchandises' on the page | [MER-01](MER-01-required-fields.md), [MER-10](MER-10-role-access.md) |

## Positive
Non-admins get 403 (MER-10); HTML/script in the name, product type and description is escaped (MER-07); uploads are validated (MER-02); deleted items return 404 (MER-09).
