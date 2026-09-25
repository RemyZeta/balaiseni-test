# Perkongsian Module — Test Documentation

Feature folder: **perkongsian** (sharing videos by Galeri, Artis and Admin → admin approval → public `/resources/sharings`). Same form as Tutorial. One file per test; screenshots in `evidence/`.

Accounts: QA artist and QA gallery (own accounts) plus admin via login-page quick-login (ADMIN "Ahmad Safwan"). No real artist/gallery account used.

| ID | Test | Status |
|---|---|---|
| [SHR-01](SHR-01-create-validation.md) | Create — required title | PASS (cosmetic) |
| [SHR-02](SHR-02-galeri-create-pending.md) | Galeri create → pending, hidden | PASS |
| [SHR-03](SHR-03-artis-create-pending.md) | Artis create → pending, hidden, own-items-only | PASS |
| [SHR-04](SHR-04-admin-review-list.md) | Admin sees both pending | PASS |
| [SHR-05](SHR-05-admin-approve.md) | Admin approves → public | PASS |
| [SHR-06](SHR-06-admin-reject.md) | Admin rejects → hidden | PASS (observation) |
| [SHR-07](SHR-07-admin-crud.md) | Admin create/edit/delete (auto-published) | PASS |
| [SHR-08](SHR-08-admin-reapprove.md) | Admin re-approves rejected | PASS |
| [SHR-09](SHR-09-edit-approved-bypass.md) | Galeri edits approved item | FAIL / needs decision |
| [SHR-10](SHR-10-owner-delete.md) | Galeri and Artis delete own | PASS |

## Findings
1. **SHR-09:** editing an approved perkongsian publishes changes without re-review (same as Tutorial).
2. Rejection has no reason or confirmation.
3. Admin-created items are auto-approved (reasonable, but note it).
4. Cosmetic: English native validation text on Malay UI.

## Not tested
Rejected-item edit/resubmit for Perkongsian, cover image upload, non-YouTube URLs, one user accessing another's item by direct URL, admin editing another user's item.

## Cleanup
All three test perkongsian were deleted. QA accounts remain.
