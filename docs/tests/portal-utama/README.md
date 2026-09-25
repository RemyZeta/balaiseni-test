# Portal Utama — Test Documentation

Feature folder: **portal-utama**. Admin-only page `/dashboard/homepage` that controls the public homepage. **Bahagian** tab: ordered sections (Banner utama, Perutusan, Pameran semasa, Aktiviti & program, Tutorial & perkongsian, Karya seni pilihan, Koleksi Tetap BSN, Berita terkini, Ajakan mendaftar, Carian pantas) — drag to order, Sunting, Sembunyi/Papar. **Banner** tab: hero slides with image, text and two buttons. Automatic sections pull content from other modules. Changes are live at once (no approval).

Because this is the live homepage, every change was reverted immediately and the homepage was compared with the baseline afterwards. The original banner was not touched. The neighbouring admin modules Halaman, Menu, Hero and Footer are separate and were not tested here.

| ID | Test | Status |
|---|---|---|
| [PTU-01](PTU-01-overview.md) | Overview and homepage baseline | PASS |
| [PTU-02](PTU-02-edit-text-section.md) | Edit a text section (Perutusan) | PASS |
| [PTU-03](PTU-03-edit-auto-section.md) | Edit an automatic section (item limit) | PASS (cosmetic) |
| [PTU-04](PTU-04-hide-show-section.md) | Sembunyi / Papar a section | PASS |
| [PTU-05](PTU-05-enable-quick-search.md) | Enable and disable Carian pantas | PASS |
| [PTU-06](PTU-06-drag-reorder.md) | Drag to reorder sections | PASS (observation) |
| [PTU-07](PTU-07-banner-create-validation.md) | Banner — create: required title, image type and size | PASS (observation: no size-dimension warning) |
| [PTU-08](PTU-08-banner-link-validation.md) | Banner button link — invalid value | FAIL |
| [PTU-09](PTU-09-banner-edit.md) | Banner — edit, escaping and link targets | PASS |
| [PTU-10](PTU-10-banner-hide-show.md) | Banner — Sembunyi / Papar | PASS |
| [PTU-11](PTU-11-banner-delete.md) | Banner — delete | FAIL (inconsistent; irreversible without confirmation — needs product decision) |
| [PTU-12](PTU-12-role-access.md) | Non-admin and anonymous access | PASS |

Two tests failed (PTU-08, PTU-11). See [FAILURES.md](FAILURES.md).

## Not tested
Editing the other text section (Ajakan mendaftar) and the remaining automatic sections, the English text of each section on `/en`, the section dark/soft themes visually, banner drag reorder, PNG/WebP/AVIF banner images, banner second-button-only, empty-section behaviour with actual content, replacing the banner image, how the carousel behaves with many slides, mobile layout.

## Cleanup
All changes were reverted: Perutusan heading and theme, the Pameran semasa limit (3), the hidden/shown sections, Carian pantas (off) and the section order. The QA banner was deleted. The public homepage matched the baseline at the end.
