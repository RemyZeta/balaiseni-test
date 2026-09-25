# Pautan — Test Documentation

Feature folder: **pautan**. Admin-only list of useful links (`/dashboard/links`) shown on the public `/links` page. Fields: Nama, URL (typed without https://), Huraian BM / English, Kedudukan (sort number). There is no approval step: saved links are public at once, and links can be hidden (Sembunyikan) or shown (Paparkan). The module had 8 links before testing; the eight originals were not edited.

| ID | Test | Status |
|---|---|---|
| [PTN-01](PTN-01-required-fields.md) | Create — Nama and URL required | PASS (cosmetic) |
| [PTN-02](PTN-02-create-valid.md) | Create a valid pautan (published immediately) | PASS |
| [PTN-03](PTN-03-public-page.md) | Public /links: order, language, search, link attributes | PASS |
| [PTN-04](PTN-04-url-prefix.md) | URL typed with https:// prefix | PASS |
| [PTN-05](PTN-05-url-validation.md) | Invalid URLs | FAIL |
| [PTN-06](PTN-06-negative-position.md) | Negative Kedudukan | PASS (observation: message not captured) |
| [PTN-07](PTN-07-edit.md) | Edit pautan | PASS |
| [PTN-08](PTN-08-html-escaping.md) | HTML / script in name and description | PASS |
| [PTN-09](PTN-09-hide-show.md) | Sembunyikan / Paparkan | PASS |
| [PTN-10](PTN-10-delete.md) | Delete with confirmation | PASS |
| [PTN-11](PTN-11-role-access.md) | Non-admin and anonymous access | PASS |

One test failed (PTN-05). See [FAILURES.md](FAILURES.md).

## Not tested
Drag/keyboard reordering (position is only a number), duplicate URLs or names, very long names or descriptions, a link with a port or IPv6 address, an English-only or BM-only description on the other language page, unicode names, the Lihat button, pagination beyond 12 links, dashboard search.

## Cleanup
All four QA links were deleted. Counters are back to 8 / 8 / 0.
