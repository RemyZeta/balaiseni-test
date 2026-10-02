# Unapproved accounts — Failures & Issues

## Summary
| # | Severity | Type | Issue | Source test |
|---|---|---|---|---|
| N-F1 | Medium | FAIL | An unapproved Galeri account is listed in the public gallery directory and its profile page and photo are public; unapproved Artists are correctly hidden | [PND-08](PND-08-galeri-public-before-approval.md) |
| N-I1 | Medium | Observation | Unapproved accounts have full module access and can upload files and submit content; the only gate is item approval | [PND-05](PND-05-content-uploads.md) |
| N-I2 | Low | Observation | No 'awaiting approval' message; the dashboard even says 'Semua profil telah disemak' to a pending user and shows site-wide stats | [PND-04](PND-04-no-pending-notice.md) |
| N-I3 | Low | Observation | Profile photos and pending-item images are served publicly by direct URL regardless of approval status | [PND-09](PND-09-files-direct-url.md) |
| N-I4 | Low | Observation | Admin approval of an item publishes it under the name of an account whose membership is still unapproved | [PND-10](PND-10-approved-items-unapproved-owner.md) |

## N-F1 — Unapproved Galeri visible publicly
- **Steps:** Register as Galeri, set a password; upload a profile photo; open `/resources/galleries?search=<name>` as an anonymous visitor.
- **Expected:** Not listed until admin approves the membership (the registration page says profiles are shown after admin review).
- **Actual:** The account is listed ('Galeri 0') with its photo and its profile page opens. An unapproved Artist with the same steps is not listed.
- **Impact:** Anyone can appear in the public gallery directory, with a photo and name, without admin review.

## Decision needed
Confirm whether unapproved accounts should be allowed to upload files and submit content at all (N-I1). If not, block the modules or show a clear message until the membership is approved.
