import os
os.chdir(r"docs/tests/pameran-aktiviti")
T = [
("PAM-01","required-title","Create — required title","P1","Admin logged in.",
 "1. Tambah pameran.\n2. Simpan pameran with Tajuk pameran empty.","Blocked.",
 "Modal stays open, native tooltip 'Please fill in this field.' (English on Malay UI).","PASS (cosmetic)","![form](evidence/pam-form.png)"),
("PAM-02","create-pameran","Create Pameran → auto-approved, listed","P0","Admin logged in.",
 "1. Tambah pameran; Jenis acara = Pameran.\n2. Fill Tajuk `QA Pameran Ujian 01`, Penganjur, dates 2026-10-01 to 2026-10-31, Huraian, Lokasi, Pautan luar.\n3. Simpan pameran.",
 "Saved; the form says admin-added items are approved directly.",
 "Saved as **Diluluskan** immediately; card shows 'AKAN DATANG' (upcoming) computed from dates. Counters 173→174.","PASS","![created](evidence/pam-created.png)"),
("PAM-03","public-listing-detail","Public listing, search and detail page","P0","PAM-02 done.",
 "1. Open `/resources/exhibitions`, search the title.\n2. Open the item.","Item listed with correct data; detail page works.",
 "Listed under the Pameran tab (count 1) with organiser, location and 'Dicipta oleh Ahmad Safwan'. Detail page `/resources/exhibitions/qa-pameran-ujian-01` shows title, organiser, dates, location, description and external link.","PASS","![public](evidence/pam-public.png) ![detail](evidence/pam-detail.png)"),
("PAM-04","create-aktiviti","Create Aktiviti","P0","Admin logged in.",
 "1. Tambah pameran; set Jenis acara = Aktiviti (options: Pameran, Aktiviti).\n2. Fill `QA Aktiviti Ujian 01`, Penganjur, 10–12 Nov 2026, Lokasi `Dewan QA`.\n3. Simpan.",
 "Saved as an Aktiviti, approved, listed under the Aktiviti tab.",
 "Card 'AKTIVITI … Diluluskan'. Public `?kind=activity` shows it under the Aktiviti tab (count 1). Minor: the modal title stays 'Tambah pameran' even when Jenis acara is Aktiviti.","PASS (minor wording)","![created](evidence/act-created.png) ![public](evidence/act-public.png)"),
("PAM-05","date-validation","End date before start date","P1","Create form open.",
 "1. Set Tarikh mula 2026-11-10 and Tarikh tamat 2026-11-01.\n2. Save.","Rejected with a clear error.",
 "Not saved; modal stays open with 'The Tarikh tamat field must be a date after or equal to Tarikh mula' — English text mixed with the Malay field name (cosmetic).","PASS (cosmetic)","![baddate](evidence/act-baddate.png)"),
("PAM-06","edit","Edit exhibition","P0","PAM-02 item exists.",
 "1. Sunting.\n2. Check pre-filled values; change title and Lokasi; save.","Form pre-filled; changes saved.",
 "Pre-filled correctly (title, date, location). Saved; toast 'telah dikemas kini'; list and public page show the new values.","PASS","-"),
("PAM-07","reject-hides","Reject → hidden from public","P0","Approved item.",
 "1. Click Tolak.\n2. Search public page.","Status Ditolak; hidden.",
 "Toast '… kini Ditolak.' (no reason or confirmation). Public search: 0 results.","PASS (observation: no reason)","![rejected](evidence/pam-public-rejected.png)"),
("PAM-08","reapprove","Re-approve → visible again","P0","Item rejected in PAM-07.",
 "1. Click Luluskan.\n2. Search public page.","Visible again.",
 "Toast '… kini Diluluskan.' and the item is back on the public page with the edited title.","PASS","-"),
("PAM-09","delete","Delete with confirmation","P0","Two QA items (Pameran, Aktiviti).",
 "1. Padam on each → dialog → Padam.\n2. Check dashboard, public search and the old detail URL.","Removed everywhere; detail URL returns 404.",
 "Dialog: 'Padam \"…\"? Pameran ini akan dibuang terus… Tindakan ini tidak boleh dibatalkan.' After confirming both, the dashboard count returned to 173, public search shows 0 results, and the detail URL returns '404 Tidak Dijumpai'.","PASS","![delete](evidence/pam-delete-confirm.png)"),
("PAM-10","status-filter","Dashboard status filter options","P2","Admin on `/dashboard/exhibitions`.",
 "1. Open the 'Semua status' dropdown.","Filter by status.",
 "Options: Semua status, Menunggu semakan, Diluluskan, Ditolak. Only the option list was checked, not the filtering results.","PASS (partial)","-"),
("PAM-11","role-access","Non-admin access to admin module","P0","Artist QA account logged in.",
 "1. Open `/dashboard/exhibitions` directly.","Access denied.",
 "HTTP 403; page 'Akses Dilarang', body '403 This action is unauthorized.' (English). Artist sidebar has no Pameran & Aktiviti entry. Inconsistency: the registration page lists 'Pameran & Aktiviti' among the modules new users get in their dashboard.","PASS (observation)","-"),
]
for i,s,t,p,pre,steps,exp,act,st,ev in T:
    open(f"{i}-{s}.md","w",encoding="utf-8").write(f"""# {i} — {t}

- **Module:** Pameran & Aktiviti (Admin)
- **Target:** https://martp.nizamjensani.digital/ · admin `/dashboard/exhibitions` · public `/resources/exhibitions`
- **Date:** 2026-09-25 · **Tool:** playwright-cli (headed) · **Role:** Admin (login-page quick-login, "Ahmad Safwan")
- **Priority:** {p}
- **Status:** **{st}**

## Preconditions
{pre}

## Steps
{steps}

## Expected result
{exp}

## Actual result
{act}

## Evidence
{ev}
""")
rows="\n".join(f"| [{i}]({i}-{s}.md) | {t} | {st} |" for i,s,t,p,pre,steps,exp,act,st,ev in T)
open("README.md","w",encoding="utf-8").write(f"""# Pameran & Aktiviti — Test Documentation

Feature folder: **pameran-aktiviti**. Admin-only module (`/dashboard/exhibitions`); exhibitions and activities share one form (Jenis acara). Public pages: `/resources/exhibitions` with Pameran/Aktiviti tabs. Admin via login-page quick-login ("Ahmad Safwan").

| ID | Test | Status |
|---|---|---|
{rows}

No functional test failed. See [FAILURES.md](FAILURES.md).

## Not tested
Poster upload, external-link safety, HTML editor mode, user submission, filtering results, dashboard search, pagination, very long titles, duplicate titles/slugs.

## Cleanup
Both QA items were deleted. Counts returned to 173.
""")
open("FAILURES.md","w",encoding="utf-8").write("""# Pameran & Aktiviti — Failures & Issues

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
""")
