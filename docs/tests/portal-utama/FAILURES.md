# Portal Utama — Failures & Issues

## Summary
| # | Severity | Type | Issue | Source test |
|---|---|---|---|---|
| U-F1 | Medium | FAIL | Banner delete has no confirmation dialog (unlike every other module); the click deletes at once | [PTU-11](PTU-11-banner-delete.md) |
| U-F2 | Medium | FAIL | Banner button link is not validated: `javascript:alert(1)` is saved and published as the broken link `/lert(1)` | [PTU-08](PTU-08-banner-link-validation.md) |
| U-I1 | Low | Observation | No warning for a banner image far below the recommended 1920 × 820 px | [PTU-07](PTU-07-banner-create-validation.md) |
| U-I2 | Low | Observation | Drag reorder has no keyboard alternative; one drag direction did not work in automation (not confirmed) | [PTU-06](PTU-06-drag-reorder.md) |
| U-I3 | Low | Cosmetic | English native validation text on a Malay UI | [PTU-03](PTU-03-edit-auto-section.md) |
| U-I4 | Low | Observation | Sembunyi/Papar act at once with no confirmation, so the homepage can change with one click | [PTU-04](PTU-04-hide-show-section.md) |

## U-F1 — Banner delete without confirmation
- **Steps:** Portal Utama → Banner tab → Padam on a banner.
- **Expected:** A dialog such as 'Padam "…"? … tidak boleh dibatalkan.' with Batal, as in every other module.
- **Actual:** The banner is removed on the first click.
- **Impact:** The hero banner on the live homepage can be deleted by an accidental click, and the deletion cannot be undone.

## U-F2 — Banner link not validated
- **Steps:** Banner baharu → Pautan butang `javascript:alert(1)` → Simpan; open the homepage and click the button.
- **Expected:** A validation error (compare the Berita link field, which rejects it).
- **Actual:** Saved. The value is sanitised when displayed and the button links to `/lert(1)` (404). Not executable, but the same missing-validation pattern as Pautan (P-F1).

## Positive
Text and HTML input is escaped everywhere tested (PTU-02, PTU-09); item limits are validated (PTU-03); all changes are visible on the homepage immediately; non-admins get 403 (PTU-12); the empty section Berita terkini is not shown publicly.
