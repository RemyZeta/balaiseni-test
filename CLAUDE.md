# CLAUDE.md
https://martp.nizamjensani.digital/

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not a code repository**. It contains no GoGallery source code, build system, package manifest, linter or test runner config, and it is not a git repo. It is a workspace for **black-box testing of the GoGallery portal** (a visual-arts gallery website) using the `playwright-cli` skill.

- `docs/GoGallery_System_Modules_and_Functions (1).md` — the requirements baseline: nine modules and the public/admin functions of each.
- `docs/GoGallery_BlackBox_Playwright_CLI_Testing_Strategy.md` — the testing strategy to follow (workflow, per-module tests, evidence, status rules, defect classification).
- `.claude/skills/playwright-cli/` — the `playwright-cli` skill (`SKILL.md` plus `references/` for request mocking, tracing, video, storage state, session management, test generation, etc.).
- `.playwright/` — Playwright CLI working directory (currently empty).

## Ground rules from the testing strategy

- **Black-box only.** The source code is unavailable. Do not infer or assume the framework, database, API, routes or internals; judge only user-visible behaviour through the browser. Console/network output may be used to diagnose an observable failure, but the result must describe the user-visible effect.
- **Do not invent URLs or credentials.** The needed inputs are `TARGET_URL`, and where known `ADMIN_URL`, `PUBLIC_TEST_ACCOUNT` and `ADMIN_TEST_ACCOUNT`. If only the public URL is given, test public behaviour only. Never try to bypass authentication; test authenticated features only within the supplied account's permissions.
- **Result statuses** (do not default to PASS):
  - `PASS`: visible and works as expected.
  - `FAIL`: visible but broken.
  - `BLOCKED`: could not run because of environment, account or network problems.
  - `NOT OBSERVABLE`: required by the requirements but not reachable on the site.
- Tests must check real outcomes (search, open the profile, verify the content shown), not just that a page returns HTTP 200.
- Capture evidence for important failures. Prioritise tests using the P0–P3 scheme in the strategy doc, and classify defects per its section 28.

## Modules under test

Portal Utama, Berita & Pengumuman, Aktiviti & Pameran, Artis, Katalog Karya Seni, Galeri, Banner, Pengurusan Pengguna, Audit Trail. The strategy doc has a section for each and for cross-module flows (Artist→Artwork, Exhibition→Gallery, News→Homepage, Banner→Destination, User→Permission→Action). The technical spec's "Art for Sale / Contact Seller" feature is unconfirmed for the current baseline, so treat it separately.

## Workflow and commands

Testing follows the workflow in the strategy doc: open the site, snapshot, map navigation, smoke test, then module, CRUD, negative, search/filter, navigation, responsive, auth and role tests, then evidence and report. Drive the browser with the `playwright-cli` skill:

```bash
playwright-cli open https://martp.nizamjensani.digital/  # start a session
playwright-cli snapshot                  # list element refs (e1, e2, ...)
playwright-cli click e3 / fill e5 "text" --submit / goto <url>
playwright-cli find "text"               # search the snapshot
playwright-cli close
```

Interact using refs from a fresh snapshot. The strategy prefers stable, user-visible locators and avoids random element IDs. Load the `playwright-cli` skill for the full command reference.
