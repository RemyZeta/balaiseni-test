# Failures — rejection reason

| ID | Severity | Type | Issue | Source test |
|---|---|---|---|---|
| RJ-F1 | Medium | Gap (needs product decision) | Tolak on user-submitted content (Tutorial; same in Perkongsian, Koleksi, Art For Sale per earlier runs) has no reason field, so the artist cannot be told what to fix | [RJR-01](RJR-01-content-reject-no-reason.md) |
| RJ-O1 | Low | Observation | Galeri has a reason box but the owner never sees it (GAL-11, G-I1) | GAL-11 |
| RJ-O2 | Low | Observation | Membership reason is shown only at the bottom of Profil Saya; no notification, login message or email | [RJR-02](RJR-02-membership-reject-reason.md) |
| RJ-O3 | Low | Observation | Reason is optional everywhere it exists | RJR-02, GAL-11 |

## RJ-F1
Admin's Tolak is instant on Tutorial. The artist sees only the badge 'Ditolak', no note, no notification and no email, so they must guess why. Add a (preferably required) reason and show it on the item card and edit dialog.

## RJ-O2
The only place a reason is visible is Profil Saya → 'Status direktori awam'. A rejected applicant is otherwise told nothing at login or on the dashboard ('Semua profil telah disemak').
