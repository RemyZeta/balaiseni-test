# Failures Index (all modules)

| Module | File | Failed tests | Issues / observations |
|---|---|---|---|
| Authentication & Registration | [auth/FAILURES.md](auth/FAILURES.md) | 0 | 4 |
| Tutorial | [tutorial/FAILURES.md](tutorial/FAILURES.md) | 1 (TUT-08) | 3 |
| Perkongsian | [perkongsian/FAILURES.md](perkongsian/FAILURES.md) | 1 (SHR-09) | 2 |
| Pameran & Aktiviti | [pameran-aktiviti/FAILURES.md](pameran-aktiviti/FAILURES.md) | 0 | 5 |
| Artikel | [artikel/FAILURES.md](artikel/FAILURES.md) | 0 | 4 |
| E-Penerbitan | [e-penerbitan/FAILURES.md](e-penerbitan/FAILURES.md) | 0 | 5 |
| Berita | [berita/FAILURES.md](berita/FAILURES.md) | 0 | 4 |
| Koleksi | [koleksi/FAILURES.md](koleksi/FAILURES.md) | 2 (KOL-09, KOL-10) | 3 |
| Galeri | [galeri/FAILURES.md](galeri/FAILURES.md) | 1 (GAL-09) | 5 |
| Pautan | [pautan/FAILURES.md](pautan/FAILURES.md) | 1 (PTN-05) | 4 |
| Portal Utama | [portal-utama/FAILURES.md](portal-utama/FAILURES.md) | 2 (PTU-08, PTU-11) | 4 |
| Art For Sale | [art-for-sale/FAILURES.md](art-for-sale/FAILURES.md) | 1 (AFS-10), 1 blocked (AFS-08) | 5 |
| Perkhidmatan | [perkhidmatan/FAILURES.md](perkhidmatan/FAILURES.md) | 0, 1 blocked (SVC-05) | 3 |
| Cenderahati | [cenderahati/FAILURES.md](cenderahati/FAILURES.md) | 0, 1 blocked (MER-06) | 4 |
| Unapproved Artist/Galeri accounts | [pending-accounts/FAILURES.md](pending-accounts/FAILURES.md) | 1 (PND-08) | 4 |
| Update Profile (Admin, Artist, Galeri) | [profil/FAILURES.md](profil/FAILURES.md) | 1 (PRF-04), 1 not observable (PRF-12) | 5 |
| Rejection reason (approval flow) | [rejection-reason/FAILURES.md](rejection-reason/FAILURES.md) | 1 (RJR-01) | 4 |
| **Retest 2026-10-01** (all earlier FAIL/BLOCKED) | [retest-2026-10-01/FAILURES.md](retest-2026-10-01/FAILURES.md) | 2 still open (PND-08, PRF-04), 3 blocked | 9 fixed |

**Retest 2026-10-01:** the edit-after-approval bypass (TUT-08, SHR-09, KOL-10, GAL-09, AFS-10), the Koleksi type on edit (KOL-09), link validation (PTN-05, PTU-08) and banner delete confirmation (PTU-11) are **fixed**. Still open: unapproved Galeri listed publicly (PND-08) and phone/postcode accepting letters (PRF-04). Contact forms are still blocked by reCAPTCHA (AFS-08, SVC-05, MER-06). The dev quick-login panel is still on the login page.
