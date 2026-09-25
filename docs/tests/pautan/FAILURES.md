# Pautan — Failures & Issues

## Summary
| # | Severity | Type | Issue | Source test |
|---|---|---|---|---|
| P-F1 | Medium | FAIL | The URL field has no validation: `javascript:alert(1)` and text with spaces are saved and published as broken links | [PTN-05](PTN-05-url-validation.md) |
| P-I1 | Low | Observation | Kedudukan is only a number (no drag-and-drop); items with equal numbers have no defined order | [PTN-03](PTN-03-public-page.md) |
| P-I2 | Low | Observation | Negative Kedudukan is refused without a visible message | [PTN-06](PTN-06-negative-position.md) |
| P-I3 | Low | Cosmetic | English native tooltip on required fields | [PTN-01](PTN-01-required-fields.md) |
| P-I4 | Low | Observation | Sembunyikan and Paparkan act at once with no confirmation | [PTN-09](PTN-09-hide-show.md) |

## P-F1 — URL not validated
- **Steps:** Tambah pautan → Nama `QA Pautan Invalid`, URL `javascript:alert(1)` → Simpan. Repeat with `not a url with spaces`.
- **Expected:** A validation error such as the one on the Berita link field ("mesti URL yang sah").
- **Actual:** Both saved and are listed on `/links` as `https://javascript:alert(1)` and `https://not a url with spaces`.
- **Impact:** A typo produces a public broken link. The `javascript:` case is not executable because the page prepends `https://`, but the input should still be rejected. Only admins can reach this form, which limits the exposure.

## Positive
Non-admin access returns 403 (PTN-11); names and descriptions are escaped (PTN-08); a typed `https://` prefix is normalised (PTN-04); BM/EN descriptions follow the site language (PTN-03).
