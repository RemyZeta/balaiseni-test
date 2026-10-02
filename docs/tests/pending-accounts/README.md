# Unapproved (new) Artist and Galeri accounts — Test Documentation

Feature folder: **pending-accounts**. Question tested: can a new Artist or Galeri upload or do anything before admin approves the account? The registration flow says new profiles are reviewed by admin before they appear in the public directories. The two QA accounts registered in the first tests were never approved (confirmed in the review queue, PND-01), so they were reused instead of registering more accounts.

**Short answer:** yes — an unapproved account can log in, use every module that its role has, upload images and files, submit content (which waits for item approval), and edit its profile with a photo. Only the Artist directory hides the account until approval; the Galeri directory does not (PND-08, failed).

| ID | Test | Status |
|---|---|---|
| [PND-01](PND-01-verify-unapproved.md) | Confirm the QA accounts are still unapproved | PASS (precondition) |
| [PND-02](PND-02-access-unapproved-artist.md) | What an unapproved Artist can open | PASS (observation: no restriction) |
| [PND-03](PND-03-access-unapproved-galeri.md) | What an unapproved Galeri can open | PASS (observation: no restriction) |
| [PND-04](PND-04-no-pending-notice.md) | Is the user told that the account awaits approval? | PASS (observation: no notice, misleading message) |
| [PND-05](PND-05-content-uploads.md) | Submit content while unapproved | PASS (observation: uploads allowed before approval) |
| [PND-06](PND-06-profile-edit-photo.md) | Edit profile and upload a photo while unapproved | PASS (observation: allowed before approval) |
| [PND-07](PND-07-artist-hidden-public.md) | Unapproved Artist in the public directory | PASS |
| [PND-08](PND-08-galeri-public-before-approval.md) | Unapproved Galeri in the public directory | FAIL |
| [PND-09](PND-09-files-direct-url.md) | Files of unapproved accounts and pending items by direct URL | PASS (observation: files not gated by approval) |
| [PND-10](PND-10-approved-items-unapproved-owner.md) | Approved items from an unapproved account | PASS (observation) |

One test failed (PND-08). See [FAILURES.md](FAILURES.md).

## Not tested
A brand-new registration (the QA accounts already exist), what happens after admin *rejects* a membership, blocked users ('Disekat'), rate limits on submissions, whether admin approval of the account changes anything visible, the English site, the Perkhidmatan, Cenderahati, Artikel and other admin-only modules (403 for these roles).

## Cleanup
The QA Galeri tutorial was deleted and both profiles' Tentang and Bandar fields were cleared. The two profile photos remain uploaded (the profile page has a remove-photo button that I did not use). Both accounts are still pending in the review queue.
