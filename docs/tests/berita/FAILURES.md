# Berita — Failures & Issues

No test failed. Observations and cosmetic issues only.

| # | Severity | Type | Issue | Source |
|---|---|---|---|---|
| B-I1 | Low | Inconsistency | Validation says the report link must start with https://, but http:// is accepted | [BRT-07](BRT-07-link-validation.md) |
| B-I2 | Low | Gap | Rejecting is instant with no reason or confirmation (same as other modules) | [BRT-08](BRT-08-reject-reapprove.md) |
| B-I3 | Low | Cosmetic | English native tooltip on required title | [BRT-01](BRT-01-required-title.md) |
| B-I4 | Low | Observation | Slug does not change after the title is edited | [BRT-05](BRT-05-edit.md) |

## Positive
`javascript:` links are rejected server-side (BRT-07); HTML/script input is neutralised (BRT-06); public filters work (BRT-04).
