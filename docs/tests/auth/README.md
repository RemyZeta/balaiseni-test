# Test Documentation Index

Feature folder: **auth** (authentication, registration and role access). One file per test: `<ID>-<slug>.md`; screenshots in `evidence/`.

| ID | Test | Status |
|---|---|---|
| [AUTH-01](AUTH-01-register-artis.md) | Register as Artis | PASS |
| [AUTH-02](AUTH-02-password-too-short.md) | Password too short | PASS |
| [AUTH-03](AUTH-03-password-mismatch.md) | Password mismatch | PASS |
| [AUTH-04](AUTH-04-password-valid.md) | Password valid | PASS (observation) |
| [AUTH-05](AUTH-05-logout.md) | Logout | PASS |
| [AUTH-06](AUTH-06-protected-route-logged-out.md) | Protected route logged out | PASS |
| [AUTH-07](AUTH-07-login-invalid.md) | Login invalid | PASS |
| [AUTH-08](AUTH-08-login-artis.md) | Login Artis | PASS |
| [AUTH-09](AUTH-09-register-login-galeri.md) | Register/login Galeri | PASS |
| [AUTH-10](AUTH-10-role-access-galeri.md) | Role access Galeri→Art For Sale | PASS |
| [AUTH-11](AUTH-11-register-duplicate-email.md) | Duplicate email | PASS (cosmetic) |
| [AUTH-12](AUTH-12-register-required-fields.md) | Required fields | PASS (cosmetic) |

## Test data left on the live site
- `qa.artis.test01@mailinator.com` / `qa.galeri.test01@mailinator.com`, password `Test@12345`; profiles pending admin review. Needs admin cleanup.

## Not yet tested
Forgot password, Remember me, empty login submit, admin approval of profiles.
