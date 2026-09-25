# Pameran & Aktiviti — Test Documentation

Feature folder: **pameran-aktiviti**. Admin-only module (`/dashboard/exhibitions`); exhibitions and activities share one form (Jenis acara). Public pages: `/resources/exhibitions` with Pameran/Aktiviti tabs. Admin via login-page quick-login ("Ahmad Safwan").

| ID | Test | Status |
|---|---|---|
| [PAM-01](PAM-01-required-title.md) | Create — required title | PASS (cosmetic) |
| [PAM-02](PAM-02-create-pameran.md) | Create Pameran → auto-approved, listed | PASS |
| [PAM-03](PAM-03-public-listing-detail.md) | Public listing, search and detail page | PASS |
| [PAM-04](PAM-04-create-aktiviti.md) | Create Aktiviti | PASS (minor wording) |
| [PAM-05](PAM-05-date-validation.md) | End date before start date | PASS (cosmetic) |
| [PAM-06](PAM-06-edit.md) | Edit exhibition | PASS |
| [PAM-07](PAM-07-reject-hides.md) | Reject → hidden from public | PASS (observation: no reason) |
| [PAM-08](PAM-08-reapprove.md) | Re-approve → visible again | PASS |
| [PAM-09](PAM-09-delete.md) | Delete with confirmation | PASS |
| [PAM-10](PAM-10-status-filter.md) | Dashboard status filter options | PASS (partial) |
| [PAM-11](PAM-11-role-access.md) | Non-admin access to admin module | PASS (observation) |

No functional test failed. See [FAILURES.md](FAILURES.md).

## Not tested
Poster upload, external-link safety, HTML editor mode, user submission, filtering results, dashboard search, pagination, very long titles, duplicate titles/slugs.

## Cleanup
Both QA items were deleted. Counts returned to 173.
