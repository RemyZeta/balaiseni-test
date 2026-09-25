# Tutorial Module — Test Documentation

Feature folder: **tutorial** (Artist creates → Admin approves/rejects → Public page). One file per test; screenshots in `evidence/`.

Accounts: artist `qa.artis.test01@mailinator.com` (own QA account); admin via the login page's development quick-login panel (ADMIN "Ahmad Safwan"). No real artist account was used.

| ID | Test | Status |
|---|---|---|
| [TUT-01](TUT-01-create-validation.md) | Create — required title | PASS (cosmetic) |
| [TUT-02](TUT-02-create-pending.md) | Artist creates → pending | PASS |
| [TUT-03](TUT-03-pending-not-public.md) | Pending hidden from public | PASS |
| [TUT-04](TUT-04-admin-sees-pending.md) | Admin sees pending | PASS |
| [TUT-05](TUT-05-admin-reject.md) | Admin rejects | PASS (observation) |
| [TUT-06](TUT-06-artist-edit-rejected.md) | Artist edits rejected | PASS (observation) |
| [TUT-07](TUT-07-admin-approve.md) | Admin approves → public | PASS |
| [TUT-08](TUT-08-edit-approved-bypass.md) | Artist edits approved item | FAIL / needs decision |
| [TUT-09](TUT-09-artist-delete.md) | Artist deletes | PASS |

## Findings
1. **TUT-08:** editing an approved tutorial publishes changes immediately, bypassing admin review.
2. **TUT-05/06:** rejection has no reason, and the artist cannot resubmit a rejected tutorial.
3. **Login page:** shows a "Log masuk pantas" development panel listing real-looking admin/artist/gallery accounts and logging in without a password; its label says it does not exist in production. Confirm it is disabled on the live environment.
4. Cosmetic: English browser validation text on Malay UI.

## Not tested
Cover-image upload, Jenis video options, non-YouTube URLs, HTML editor mode, admin-created tutorials, edit/delete by another artist (ownership), Batal on delete, large-title limits.

## Cleanup
The test tutorial was deleted. QA artist account remains (see auth docs).
