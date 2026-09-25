---
name: gogallery-module-test
description: Black-box test a GoGallery portal module (Tutorial, Perkongsian, Pameran & Aktiviti, Artikel, Berita, Galeri, Banner, Katalog, etc.) in a headed browser with playwright-cli, then write one doc per test plus a FAILURES.md. Use this whenever the user asks to test, check, verify or QA any GoGallery dashboard module or role (admin, artist, galeri), asks to "document the tests", or asks for a failures list, even if they don't say "playwright".
---

# GoGallery module test

Tests one module of https://martp.nizamjensani.digital/ from the outside (black-box, see `CLAUDE.md`), then documents every test. Follow what was done for Tutorial, Perkongsian, Pameran & Aktiviti and Artikel; the finished docs in `docs/tests/` are the reference for style.

## Accounts and safety
- Artist QA: `qa.artis.test01@mailinator.com` / `Test@12345`. Galeri QA: `qa.galeri.test01@mailinator.com` / `Test@12345`. Use these for role tests; never act as a real user's account.
- Admin: the login page has a "Log masuk pantas" quick-login panel. Click the button for the ADMIN user (e.g. "Ahmad Safwan"). The user allowed this for testing. Read the panel from the page rather than assuming names.
- Only touch data you created (prefix titles with `QA `). Delete it at the end and record what remains (counts before/after). Real content lives on this site, so never edit, reject or delete an item you did not create.

## Running the browser
- `playwright-cli open <url> --headed` (the user wants a visible browser), then drive it with `playwright-cli run-code "async page => {...}"`. Return `JSON.stringify(...)` and read it with `grep -A1 -E 'Result|Error'`. Snapshot refs go stale on this site's custom dropdowns and modals, so use `getByRole` / `getByLabel` locators inside `page.getByRole('dialog')`.
- Rich-text fields: click the `[contenteditable=true]` element, then `page.keyboard.type`. "Kod HTML" toggles a textarea.
- Toasts appear in `[data-sonner-toast]`; read them right after an action for approve/reject/update results.
- Log out through the "Menu akaun" button → "Log keluar", then wait for the home URL before logging in as another role.
- If a `run-code` call times out, check the page state (`playwright-cli snapshot`) before retrying. A locator failing usually means a 403/404 page or an open dropdown, and that is often a finding itself.
- Close the browser at the end with `playwright-cli close`.
- Test images are in the project `images/` folder (copy one under 4 MB, and `still_life_itik.jpg` at 4.7 MB as the oversize case). Make a `fake.txt` for the wrong-type case, and delete temp files afterwards.

## What to test (adapt to the module)
1. Discover: find the dashboard URL from the admin sidebar, the public URL from the site's "Sumber" menu, the form fields and which are required.
2. Required-field validation (empty submit).
3. File upload, if the form has one: wrong type, over size, valid.
4. Create. Note whether the item starts pending (user roles) or approved (admin), and whether the counters change.
5. Public side: not visible while pending, visible once approved (check as the creator and as an anonymous visitor), listing, search, detail page, uploaded image loads.
6. Edit: fields pre-filled, change saved, public page updated. For user roles also edit an approved item and check whether it returns to review.
7. Approve, reject and re-approve: public visibility follows status, and a rejected item's detail URL gives 404.
8. HTML/script injection in title and body: check it is escaped or sanitised on the public page (no script, `onerror`, `javascript:` and no dialog).
9. Delete: read the confirmation, test Batal, confirm, then check the dashboard count, the public search and the old detail URL (404).
10. Role access: each other role opens the module URL directly, expecting 403 "Akses Dilarang" and no sidebar entry.

Skip steps that don't apply, and add module-specific ones (e.g. date range validation for events). Anything you did not test goes in a "Not tested" list. Do not claim more than you observed.

## Statuses
PASS, FAIL (visible but broken or against a stated rule), BLOCKED, NOT OBSERVABLE. Add a short qualifier such as "(cosmetic)" or "(observation)". If a behaviour might be a business-rule gap rather than a bug (e.g. edits skipping re-approval), mark it FAIL "needs product decision" and say so.

## Documentation output
Write under `docs/tests/<feature>/` (folder name in lower-case, e.g. `artikel`):
- One file per test, `<PREFIX>-<NN>-<slug>.md`, with: title, module/target/date/tool/role, priority, status, Preconditions, Steps, Expected result, Actual result, Evidence (screenshot links).
- Screenshots: take them during the run with `page.screenshot({path:'.playwright-cli/<name>.png'})`, then copy to `<feature>/evidence/`.
- `README.md`: index table (linked IDs, test name, status), accounts used, "Not tested", cleanup.
- `FAILURES.md`: table of severity / type / issue / source test, then a short paragraph per item. State clearly when nothing failed, and keep observations separate from failures.
- Add one row for the module to `docs/tests/FAILURES.md` (module, link, failed-test count, issue count).

There is no Python on this machine. Generate many similar files with a small `node` script written via the Write tool (shell heredocs with mixed quotes broke earlier), and delete the script afterwards.

## Final reply to the user
Short: results table, any failures first with the reason it matters, notable observations, what was not tested, and what test data was cleaned up or left.
