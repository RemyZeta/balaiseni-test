# Galeri — Test Documentation

Feature folder: **galeri**. Module `/dashboard/galleries` for the Galeri role (and admin); Artists are blocked. Structure: **galeri** (event album with details) → **slideshows** → **images** (up to 8 MB each, multi-upload, cover, order, caption). New galeri from a Galeri user wait for admin approval. Public: owner directory `/resources/galleries` → owner profile → galeri → slideshow with lightbox. Accounts: Galeri QA, Artist QA (403 test), Admin via login-page quick-login. Only the QA galeri was approved, rejected or deleted; the five real galeri were not touched.

| ID | Test | Status |
|---|---|---|
| [GAL-01](GAL-01-required-title.md) | Create galeri — required title | PASS (cosmetic) |
| [GAL-02](GAL-02-create-pending.md) | Galeri creates a galeri → pending | PASS |
| [GAL-03](GAL-03-slideshow-create.md) | Add a slideshow (with required title) | PASS |
| [GAL-04](GAL-04-image-upload-invalid.md) | Image upload — wrong type and over 8 MB | PASS |
| [GAL-05](GAL-05-image-upload-multi.md) | Upload several images at once | PASS |
| [GAL-06](GAL-06-image-manage.md) | Set cover, reorder, caption, remove image | PASS |
| [GAL-07](GAL-07-pending-hidden.md) | Pending galeri hidden from public | PASS |
| [GAL-08](GAL-08-admin-approve-public.md) | Admin approves → public directory, detail, slideshow, lightbox | PASS |
| [GAL-09](GAL-09-edit-approved-bypass.md) | Owner edits an approved galeri | FAIL (if re-review required) — needs product decision |
| [GAL-10](GAL-10-html-injection.md) | HTML / script injection in title and description | PASS |
| [GAL-11](GAL-11-admin-reject-reason.md) | Admin rejects with a reason dialog, then re-approves | PASS (observation: reason not shown to owner) |
| [GAL-12](GAL-12-delete.md) | Delete slideshow and galeri (with Batal) | PASS (observation: CDN keeps deleted image) |
| [GAL-13](GAL-13-artist-blocked.md) | Artist cannot access the Galeri module | PASS |

One test failed (GAL-09). See [FAILURES.md](FAILURES.md).

## Not tested
Admin creating a galeri directly, reordering slideshows (↑ ↓ with 2+ slideshows), Sunting of a slideshow, editing a rejected galeri, an owner opening another owner's edit URL, PNG/WebP uploads, more than 3 images at once, very large albums, the Buka/Lihat buttons on real galeri, English description shown on the English site, dashboard status filter and search, Galeri 'Slideshow' autoplay ('Main slideshow' opened only via the lightbox).

## Cleanup
The QA galeri (with its slideshow and images) was deleted; the owner's count is 0. Admin totals returned to 5 galeri after deletion (6 during the test).
