# Perkhidmatan — Failures & Issues

No test failed. One test blocked; observations only.

| # | Severity | Type | Issue | Source test |
|---|---|---|---|---|
| V-B1 | — | BLOCKED | Contact form needs a human to tick reCAPTCHA; sending and the provider Inbox are unverified | [SVC-05](SVC-05-contact-provider.md) |
| V-I1 | Low | Gap | Rejecting is instant with no reason or confirmation (same as other modules) | [SVC-07](SVC-07-reject-reapprove.md) |
| V-I2 | Low | Cosmetic | English native tooltips on required fields | [SVC-01](SVC-01-required-fields.md) |
| V-I3 | Low | Observation | The listing has no category or type field, so the public directory cannot be filtered by kind of service (framing, insurance, …), although the page lists these kinds | [SVC-04](SVC-04-public-listing-detail.md) |

## Positive
Non-admins get 403 (SVC-09); HTML/script in the name, description and offerings is escaped (SVC-06); uploads are validated (SVC-02); deleted items return 404 (SVC-08).
