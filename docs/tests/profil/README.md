# Update Profile (Admin, Artist, Galeri) — Test Documentation

Feature folder: **profil**. Black-box test of updating a user's own profile for the three roles, in a headed browser on 2026-10-01. Two pages make up the feature:

- **Profil Saya** `/dashboard/profile`: photo, Tentang, contact, address, social links (Admin has a smaller form).
- **Tetapan akaun** `/settings/profile`: display name and email.

| ID | Test | Role | Status |
|---|---|---|---|
| [PRF-01](PRF-01-profile-page-fields.md) | Profile page opens with role-specific fields | Artist, Galeri, Admin | PASS |
| [PRF-02](PRF-02-artist-update-fields.md) | Artist updates profile fields and they persist | Artist | PASS |
| [PRF-03](PRF-03-url-validation.md) | Website and social link validation | Artist, Admin | PASS (observation: `http://` accepted) |
| [PRF-04](PRF-04-phone-postcode-format.md) | Phone and postcode format validation | Artist | FAIL (Low, input validation) |
| [PRF-05](PRF-05-about-max-length.md) | Tentang 2000-character limit | Artist | PASS |
| [PRF-06](PRF-06-photo-invalid-type.md) | Profile photo: wrong file types | Artist | PASS |
| [PRF-07](PRF-07-photo-oversize.md) | Profile photo: file over 5 MB | Artist | PASS |
| [PRF-08](PRF-08-photo-upload-remove.md) | Profile photo: valid upload and remove | Artist | PASS (observation: no confirmation before removing) |
| [PRF-09](PRF-09-account-validation.md) | Account settings: name and email validation | Artist | PASS |
| [PRF-10](PRF-10-artist-name-change.md) | Artist changes display name | Artist | PASS (cosmetic: English toast) |
| [PRF-11](PRF-11-galeri-update-fields.md) | Galeri updates profile fields and they persist | Galeri | PASS |
| [PRF-12](PRF-12-public-profile-fields.md) | Updated profile fields on the public directory | Artist, Galeri, anonymous visitor | NOT OBSERVABLE |
| [PRF-13](PRF-13-galeri-photo-name-public.md) | Galeri photo and name changes on the public page | Galeri, anonymous visitor | PASS |
| [PRF-14](PRF-14-html-injection.md) | HTML/script injection in Tentang and Nama | Galeri, Admin | PASS |
| [PRF-15](PRF-15-admin-update-profile.md) | Admin updates profile fields and photo | Admin | PASS |
| [PRF-16](PRF-16-admin-account-name.md) | Admin changes display name; invalid email | Admin | PASS (cosmetic: English toast) |
| [PRF-17](PRF-17-audit-trail.md) | Profile updates recorded in the audit trail | Admin | PASS (observations) |
| [PRF-18](PRF-18-anonymous-access.md) | Profile pages need login | Anonymous visitor | PASS |

**Result:** 16 PASS, 1 FAIL (PRF-04, Low), 1 NOT OBSERVABLE (PRF-12). See [FAILURES.md](FAILURES.md).

## Accounts used
- Artist: `qa.artis.test01@mailinator.com` (QA account, membership still pending)
- Galeri: `qa.galeri.test01@mailinator.com` (QA account, membership still pending)
- Admin: login-page quick-login "Ahmad Safwan" (a real admin account; every change was reverted right away)

## Change since earlier runs
The Artist/Galeri profile page now shows a "Status direktori awam: Menunggu semakan pentadbir" notice. Observation PND-04 (no pending notice) looks fixed on this page.

## Not tested
- Changing an email to a new address (could need re-verification or lock the account). Only invalid and duplicate emails were tried.
- Password change ("Keselamatan"), "Penampilan" and "Padam akaun".
- Admin editing *another* user's profile through Pengguna, and approving/rejecting memberships (no approve/reject was done).
- Public display of profile fields for an **approved** Artist/Galeri (PRF-12); no approved QA account exists.
- Phone/postcode format on the Galeri and Admin forms (same fields as Artist; checked on Artist only).
- AVIF/WebP/GIF uploads, HEIC message, image cropping or resizing, the English (EN) site, mobile layout.

## Cleanup
- Artist: all fields restored to the starting values. The photo was **removed** (it had one from an earlier run), so the account now has no photo. Name restored.
- Galeri: all fields and the name restored. The photo was **replaced** with a new one (BENGAL_CAT_II.jpg); the old file is deleted.
- Admin "Ahmad Safwan": fields restored to empty, no photo (as before), name restored.
- Audit trail rows from these changes remain (read-only by design).
- Temporary upload files were deleted.
