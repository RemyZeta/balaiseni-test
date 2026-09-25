# AUTH-12 — Register — required fields

- **Module:** Pengurusan Pengguna (Authentication / Registration)
- **Target:** https://martp.nizamjensani.digital/
- **Date:** 2026-09-25
- **Tool:** playwright-cli (headed)
- **Priority:** P1
- **Status:** **PASS (cosmetic issue)**

## Preconditions
Logged out.

## Steps
1. Open `/register`.
2. Leave No. telefon and Alamat empty; submit.

## Expected result
Submission blocked.

## Actual result
Browser-native tooltip 'Please fill in this field.' Cosmetic: English text on a Malay page.

## Evidence
![evidence](evidence/dup.png)
