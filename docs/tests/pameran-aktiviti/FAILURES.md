# Pameran & Aktiviti — Failures & Issues

No test failed. Observations and cosmetic issues only.

| # | Severity | Type | Issue | Source |
|---|---|---|---|---|
| P-I1 | Medium | Inconsistency | Registration page says new users get a "Pameran & Aktiviti" dashboard module, but Artist users get 403 on it and have no sidebar entry | [PAM-11](PAM-11-role-access.md) |
| P-I2 | Low | Gap | Rejecting is instant with no reason or confirmation (same as Tutorial/Perkongsian) | [PAM-07](PAM-07-reject-hides.md) |
| P-I3 | Low | Cosmetic | Date validation message is in English | [PAM-05](PAM-05-date-validation.md) |
| P-I4 | Low | Cosmetic | English native tooltip on required title; English "403 This action is unauthorized." | PAM-01, PAM-11 |
| P-I5 | Low | Cosmetic | Modal title stays "Tambah pameran" when Jenis acara is Aktiviti | [PAM-04](PAM-04-create-aktiviti.md) |

## Notes
- The technical spec says exhibition/activity data may be uploaded by registered users too. That could not be observed: the artist and gallery accounts have no access (P-I1). Treat user submission as NOT OBSERVABLE / possible gap until confirmed.
