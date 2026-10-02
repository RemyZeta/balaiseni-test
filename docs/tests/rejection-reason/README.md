# Rejection reason — approval-flow tests

Question: when an admin declines a submission, does the requester see a message or note explaining why?
Date 2026-10-02 · playwright-cli (headed) · accounts: Artist QA, Admin (quick login Ahmad Safwan).

| ID | Test | Status |
|---|---|---|
| [RJR-01](RJR-01-content-reject-no-reason.md) | Content (Tutorial) rejected: reason asked / shown to artist | FAIL (gap, needs product decision) |
| [RJR-02](RJR-02-membership-reject-reason.md) | Membership rejected with reason: shown to applicant | PASS (observation: buried on Profil Saya, no notification) |

## Summary across the site
| Approval type | Reason field for admin | Reason visible to requester |
|---|---|---|
| Membership (Artis/Galeri profile) | Yes, optional | **Yes** — Profil Saya → 'Status direktori awam' (RJR-02) |
| Galeri | Yes, optional (GAL-11, 2026-09-25, not re-run) | No (GAL-11) |
| Tutorial | No — instant (RJR-01) | No |
| Perkongsian, Koleksi, Art For Sale (user-submitted modules) | No — instant (earlier runs, not re-run) | No |
| Artikel, Berita, E-Penerbitan, Pameran, Perkhidmatan, Cenderahati (admin-only) | No — instant | n/a, admin-only |

No notification (bell), inbox message or email was sent in any case checked.

## Not tested
Galeri and the other user modules were not re-run today; the Galeri result comes from GAL-11. Membership rejection of a Galeri account, rejection with an empty reason, re-approval clearing the old reason, edit-and-resubmit of a rejected item, and email delivery to a real mailbox (only the Mailinator public inbox was checked).

## Cleanup
`QA Tolak Sebab Tutorial` deleted by the artist (artist Tutorial count back to 0). **`QA Test Artis` was left rejected** (reason text above); `QA Test Galeri` is still pending. Temp files removed.
