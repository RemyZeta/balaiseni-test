# Art For Sale — Failures & Issues

## Summary
| # | Severity | Type | Issue | Source test |
|---|---|---|---|---|
| F-F1 | High | FAIL (needs product decision) | An artist can edit an approved listing — including its price — and the change is public at once, without admin re-approval | [AFS-10](AFS-10-edit-approved-bypass.md) |
| F-B1 | — | BLOCKED | Contact-seller submission needs a human to tick reCAPTCHA; sending and the seller Inbox are unverified | [AFS-08](AFS-08-contact-seller.md) |
| F-I1 | Medium | Observation | The 'Harga boleh dirunding' (negotiable) flag is saved and shown in the dashboard but not on the public listing or detail | [AFS-07](AFS-07-negotiable-flag.md) |
| F-I2 | Low | Observation | Price accepts whole ringgit only (step 1), so prices with sen cannot be entered | [AFS-03](AFS-03-price-field.md) |
| F-I3 | Low | Gap | Rejecting is instant with no reason or confirmation (same as other modules) | [AFS-05](AFS-05-admin-approve-reject.md) |
| F-I4 | Low | Cosmetic | English native tooltips on required fields | [AFS-01](AFS-01-required-fields.md) |
| F-I5 | Low | Observation | Opening an `/en/…` public page while logged in as admin switched the dashboard to English until BM was chosen again | AFS-07 run |

## F-F1 — Edit after approval publishes changes
Same defect as Tutorial, Perkongsian, Koleksi and Galeri. Here the changed field was the **price**: an approved RM 1,500 listing became RM 9,999 publicly with no admin check. For a sales catalogue this affects buyers directly.

## F-I1 — Negotiable not visible publicly
Dashboard cards read 'RM 800 boleh runding', but the public card and detail read 'RM 800'. If buyers are meant to know, the public page should show it.

## Positive
Approval gating works for new listings (AFS-04, AFS-05); HTML/script input is escaped (AFS-09); price negative values and non-images are refused (AFS-02, AFS-03); Galeri gets 403 (AFS-13); the contact form is protected by reCAPTCHA and a honeypot field.
