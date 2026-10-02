# Update Profile — Failures & Issues

## Summary
| # | Severity | Type | Issue | Source test |
|---|---|---|---|---|
| P-F1 | Low | FAIL | Telefon and Poskod accept letters (`abcdefg`, `ABCDE`); only length is checked | [PRF-04](PRF-04-phone-postcode-format.md) |
| P-I1 | Low | Observation | `http://` links are accepted although the message and hint say links must start with `https://` | [PRF-03](PRF-03-url-validation.md) |
| P-I2 | Low | Observation | Galeri/Artist profile fields (Tentang, address, social) are not shown on the public Galeri owner page, while the form says they are shown in the public directory; could not be checked for an approved account | [PRF-12](PRF-12-public-profile-fields.md) |
| P-I3 | Low | Observation | Audit filter lists each past display name as a separate user; one session logged under three different IPs (possible proxy IP) | [PRF-17](PRF-17-audit-trail.md) |
| P-I4 | Cosmetic | Observation | Account settings toast is English ("Profile updated.") on the Malay site | [PRF-10](PRF-10-artist-name-change.md), [PRF-16](PRF-16-admin-account-name.md) |
| P-I5 | Cosmetic | Observation | "Buang gambar" removes the photo straight away, with no confirmation | [PRF-08](PRF-08-photo-upload-remove.md) |

## P-F1 — Phone and postcode accept letters
- **Steps:** Profil Saya → Telefon `abcdefg` (or Poskod `ABCDE`) → Simpan profil → reload.
- **Expected:** A format error; only digits, `+`, `-` and spaces for phone, digits for postcode.
- **Actual:** Saved with the success toast and kept after reload. Only the 40-character limit is checked.
- **Impact:** Bad contact data. The profile page says this information is shown in the public directory, and the phone is shown to admins in the review queue.

## P-I1 — `http://` accepted
The message "mesti URL yang sah, bermula dengan https://" is shown for invalid links, but `http://example.com` saves. Either allow http and change the text, or enforce https.

## P-I2 — Profile fields not visible publicly for Galeri
The QA Galeri page and approved gallery-owner pages show only name, photo and galleries. Approved artist pages do show social links. Decide whether Galeri owners' Tentang/contact should be public. The related existing failure (pending Galeri already public, [PND-08](../pending-accounts/PND-08-galeri-public-before-approval.md)) is not counted again here.

## P-I3 — Audit trail details
Past names appear as separate entries in the user filter, which makes filtering by person harder. IPs differ between requests from the same browser within minutes, so the logged IP may be the proxy's. The team should check this; it is not verified from the outside.

## P-I4, P-I5 — Cosmetic
English toast on `/settings/profile`; no confirmation before removing a profile photo.

Security checks passed: script/HTML in Tentang and Nama is shown as text on the public page, review queue and audit trail (PRF-14); SVG and fake images are rejected (PRF-06); old photo files are deleted (PRF-08); profile URLs need login (PRF-18).
