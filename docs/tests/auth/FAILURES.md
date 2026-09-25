# Authentication & Registration — Failures & Issues

Environment: https://martp.nizamjensani.digital/ · tested 2026-09-25 · headed playwright-cli

No functional test failed. All 12 tests passed. The items below are observations and cosmetic issues to review.

## Summary
| # | Severity | Type | Issue | Source test |
|---|---|---|---|---|
| A-I1 | High (verify) | Security observation | Login page shows a "Log masuk pantas" dev panel that logs in as real-looking admin/artist/gallery accounts without a password | Seen while starting Tutorial tests (see [tutorial/README.md](../tutorial/README.md)) |
| A-I2 | Medium | Design question | New Artis/Galeri dashboard shows site-wide stats under "Panel Pentadbiran" | [AUTH-04](AUTH-04-password-valid.md) |
| A-I3 | Low | Cosmetic | Native validation tooltip is English on Malay UI | [AUTH-12](AUTH-12-register-required-fields.md) |
| A-I4 | Low | Cosmetic | Duplicate-email error is lowercase and misaligns the phone field | [AUTH-11](AUTH-11-register-duplicate-email.md) |

## A-I1 — Development quick-login panel on the login page
The panel is labelled "PEMBANGUNAN SAHAJA … Panel ini tidak wujud pada produksi" and lists super admins, admins, artists and galleries with real-looking names and emails. Clicking one logs in with no password. If this domain is (or shares data with) production, anyone could get admin access. **Confirm it is disabled outside development.** It was used to log in as an admin for the Tutorial and Perkongsian tests, as instructed.

## A-I2 — Site-wide statistics for non-admin roles
A brand-new Artis or Galeri sees "Panel Pentadbiran" and account counts per role (Artis 724, Galeri 64, Ahli biasa 21, Disekat 74) plus 73 published artworks. Confirm this is intended for non-admin roles.

## A-I3 / A-I4 — Cosmetic
- "Please fill in this field." appears in English on required phone and address fields.
- "alamat emel tersebut telah digunakan." starts lowercase, and the phone field shifts out of line with the email field.

## Not tested
Forgot password, "Ingat saya", empty login submit, admin approval of new profiles.
