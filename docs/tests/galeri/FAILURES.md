# Galeri — Failures & Issues

## Summary
| # | Severity | Type | Issue | Source test |
|---|---|---|---|---|
| G-F1 | High | FAIL (needs product decision) | Editing an approved galeri publishes changes without admin re-approval | [GAL-09](GAL-09-edit-approved-bypass.md) |
| G-I1 | Medium | Gap | The rejection reason typed by admin is not shown to the owner (list, Lihat, edit page, notifications), although the dialog says it lets them know what to fix | [GAL-11](GAL-11-admin-reject-reason.md) |
| G-I2 | Low | Observation | The rejection reason is optional (empty reason accepted) | [GAL-11](GAL-11-admin-reject-reason.md) |
| G-I3 | Medium | Observation | Deleted images stay downloadable from the CDN cache for up to 30 days (cache-busted URL returns 404) | [GAL-12](GAL-12-delete.md) |
| G-I4 | Low | Observation | Slug does not change when the title is edited | [GAL-09](GAL-09-edit-approved-bypass.md) |
| G-I5 | Low | Cosmetic | English native tooltip on required fields | [GAL-01](GAL-01-required-title.md), [GAL-03](GAL-03-slideshow-create.md) |

## Positive
Galeri is the only module tested so far whose Tolak dialog asks for a reason. Artist access is blocked (403). Injected HTML is escaped (GAL-10). Invalid uploads are skipped with clear messages (GAL-04).

## G-F1 — Edit after approval skips review
Same behaviour as Tutorial (T-F1), Perkongsian (S-F1) and Koleksi (K-F2): the owner renamed an approved galeri and the new title was public at once.

## G-I1 — Rejection reason not visible
Admin entered 'Gambar kurang jelas — sila muat naik semula (ujian QA).' The owner saw the badge 'Ditolak' only. Consider showing the reason on the card or edit page and sending a notification.

## G-I3 — Deleted images cached
The image URL returned 200 after the galeri was deleted (`cache-control: public, max-age=2592000`); a cache-busted request returned 404. Same as E-Penerbitan (E-I1).
