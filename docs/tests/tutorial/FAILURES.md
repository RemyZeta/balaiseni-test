# Tutorial — Failures & Issues

Environment: https://martp.nizamjensani.digital/ · tested 2026-09-25 · headed playwright-cli

## Summary
| # | Severity | Type | Issue | Source test |
|---|---|---|---|---|
| T-F1 | High | FAIL (needs product decision) | Editing an approved tutorial bypasses admin approval | [TUT-08](TUT-08-edit-approved-bypass.md) |
| T-I1 | Medium | Gap | Rejected tutorial cannot be resubmitted by the artist | [TUT-06](TUT-06-artist-edit-rejected.md) |
| T-I2 | Low | Gap | Rejection has no reason and no confirmation | [TUT-05](TUT-05-admin-reject.md) |
| T-I3 | Low | Cosmetic | Native validation tooltip is English on Malay UI | [TUT-01](TUT-01-create-validation.md) |

## T-F1 — Edit after approval publishes without re-review
- **Steps:** Artist creates a tutorial → admin approves → artist clicks Sunting, changes the title, saves.
- **Expected:** Item returns to "Menunggu semakan" (or the change waits for approval), because the form says videos are reviewed before appearing publicly.
- **Actual:** Status stays "Diluluskan" and the new title appears on `/resources/tutorials` immediately.
- **Impact:** An artist can change approved public content (title, description, URL) with no admin check.
- **Evidence:** `evidence/tut-public-after-approve.png`; results in TUT-08.

## T-I1 — No resubmit after rejection
Artist can edit a rejected tutorial, but the status stays "Ditolak". Only an admin can approve it again, and the artist has no signal that this is needed.

## T-I2 — Rejection without reason
Admin's Tolak takes effect instantly (toast only). No reason field, no confirm. The artist sees "Ditolak" with no explanation.

## T-I3 — Cosmetic
"Please fill in this field." shown in English on the Malay page.
