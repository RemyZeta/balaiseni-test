# Perkongsian — Failures & Issues

Environment: https://martp.nizamjensani.digital/ · tested 2026-09-25 · headed playwright-cli

## Summary
| # | Severity | Type | Issue | Source test |
|---|---|---|---|---|
| S-F1 | High | FAIL (needs product decision) | Editing an approved perkongsian bypasses admin approval | [SHR-09](SHR-09-edit-approved-bypass.md) |
| S-I1 | Low | Gap | Rejection has no reason and no confirmation | [SHR-06](SHR-06-admin-reject.md) |
| S-I2 | Low | Cosmetic | Native validation tooltip is English on Malay UI | [SHR-01](SHR-01-create-validation.md) |

## S-F1 — Edit after approval publishes without re-review
- **Steps:** Galeri creates a perkongsian → admin approves → Galeri clicks Sunting, changes the title, saves.
- **Expected:** Item returns to pending, or the change waits for approval.
- **Actual:** Stays "Diluluskan"; the new title `QA Perkongsian Galeri 01 (Edit selepas lulus)` is public immediately at `/resources/sharings`.
- **Impact:** Same as the Tutorial module (T-F1). Approved public content can be changed with no admin check. Likely a shared root cause, since both modules use the same form.
- **Evidence:** results in SHR-09.

## S-I1 — Rejection without reason
Tolak is instant with no reason field or confirmation; the user only sees "Ditolak".

## S-I2 — Cosmetic
English "Please fill in this field." on the Malay page.

## Not tested
Whether a rejected item can be resubmitted by Galeri/Artis. Expect the same gap as Tutorial (T-I1); unverified.
