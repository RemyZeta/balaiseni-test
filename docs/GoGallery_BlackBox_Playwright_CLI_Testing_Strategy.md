# GoGallery Black-Box Testing Strategy — Playwright CLI

## 1. Purpose

This document defines the black-box functional testing strategy for the GoGallery portal using Playwright CLI.

### Important project condition

The tester **does not have the GoGallery source code**.

Testing must therefore be performed from the outside through:

- Website URL
- Browser UI
- Visible page content
- Forms and controls
- Navigation
- Search/filter behaviour
- Login/logout behaviour
- File upload controls, where accessible
- Public website behaviour
- Admin/CMS behaviour, only when valid test credentials are available
- Browser console/network information when useful for diagnosing an observable failure

This is **black-box testing**.

The AI must not assume knowledge of:

- Laravel controllers
- Database tables
- API implementation
- Internal classes
- Source-code routes
- Database records
- Backend architecture
- Internal business logic that cannot be observed through the website

---

# 2. Testing Objective

The main objective is to determine whether the existing GoGallery website behaves correctly from a user's perspective and whether its observable functions satisfy the agreed system requirements.

The test should answer:

> "Can a real user successfully perform the required task through the website, and does the website produce the expected observable result?"

Testing is not merely checking whether pages load.

For example:

### Weak test

```text
Open /artis
Check HTTP 200
PASS
```

### Proper black-box test

```text
Open Artist page
Search for an artist
Open the artist profile
Verify artist information is displayed
Verify associated artworks are displayed when expected
Verify navigation works
Verify no visible error occurs
PASS
```

---

# 3. Scope

The current GoGallery project baseline contains these core modules:

1. Portal Utama
2. Berita & Pengumuman
3. Aktiviti & Pameran
4. Artis
5. Katalog Karya Seni
6. Galeri
7. Banner
8. Pengurusan Pengguna
9. Audit Trail

Because this is black-box testing, only functionality that can actually be reached and observed through the supplied website URL should be tested.

If a function exists in the requirements but cannot be accessed from the current website, mark it:

```text
NOT OBSERVABLE
```

Do not automatically mark it as PASS.

---

# 4. Black-Box Testing Principles

The AI tester must follow these principles.

## 4.1 Test behaviour, not implementation

Do not attempt to infer whether the application is implemented using:

- Laravel
- Joomla
- PHP
- JavaScript framework
- REST API
- MySQL
- MariaDB
- specific database schema

unless this information is explicitly observable and relevant.

The test result must be based on user-visible behaviour.

---

## 4.2 Test from the user's perspective

Think like:

- public visitor
- content administrator
- system administrator
- authorised staff user

depending on the available account.

---

## 4.3 Do not assume a function exists

If the requirements mention a function but the website does not expose it:

```text
Status: NOT OBSERVABLE
```

If the function is visible but broken:

```text
Status: FAIL
```

If the function is visible and works as expected:

```text
Status: PASS
```

If the test cannot be executed because of environment/account/network problems:

```text
Status: BLOCKED
```

---

# 5. Required Inputs

Before testing, the AI should identify:

```text
TARGET_URL
ADMIN_URL          (if known)
PUBLIC_TEST_ACCOUNT (if required)
ADMIN_TEST_ACCOUNT  (if available)
```

Example:

```text
TARGET_URL=https://example.com
ADMIN_URL=https://example.com/admin
```

Do not invent URLs.

If only the public URL is supplied, begin with public black-box testing.

If login credentials are supplied, test authenticated functionality only within the permissions of that account.

Never attempt to bypass authentication.

---

# 6. Playwright CLI Testing Workflow

The recommended workflow is:

```text
1. Open website
2. Observe initial state
3. Take snapshot
4. Map navigation
5. Identify visible functions
6. Run smoke tests
7. Build functional test cases
8. Execute module tests
9. Test positive cases
10. Test negative/validation cases
11. Test important cross-page workflows
12. Capture evidence
13. Investigate failures
14. Re-test failed scenarios
15. Produce black-box test report
```

---

# 7. Initial Website Discovery

Start by opening the supplied website.

Example:

```bash
playwright-cli open https://TARGET_URL
```

Then:

```bash
playwright-cli snapshot
```

Inspect the page for:

- Header
- Logo
- Main navigation
- Search
- Language selector
- Login
- Main content
- Footer
- Links
- Buttons
- Forms
- Cards
- Filters
- Pagination
- Banners
- Error messages

The AI should build a simple map of the observable website.

Example:

```text
PUBLIC WEBSITE
├── Home
├── News
├── Exhibitions
├── Activities
├── Artists
├── Artwork Catalogue
├── Gallery
├── Search
└── Other visible pages
```

Do not assume hidden routes.

---

# 8. Smoke Testing

Smoke testing must happen before deep functional testing.

The objective is to determine whether the website is sufficiently available for further testing.

## Smoke Test

Check:

- Homepage loads
- Main navigation works
- Important public pages load
- Search opens
- Images load
- Main links are clickable
- No obvious fatal error is displayed
- Important forms render correctly

Example:

```text
TC-SMOKE-001
Open homepage
Expected:
Homepage renders successfully
PASS/FAIL
```

---

# 9. Module-Based Black-Box Testing

## 9.1 Portal Utama

Test:

- Homepage loading
- Header
- Navigation
- Hero/banner
- Featured content
- News links
- Exhibition/activity links
- Artist links
- Artwork links
- Gallery links
- Footer
- External/internal links

### Example

```text
Open homepage
Click a featured artwork
Expected:
Artwork detail page opens and displays the selected artwork
```

---

# 9.2 Berita & Pengumuman

Test:

- News listing
- News detail
- Search/filter if available
- Pagination if available
- Date display
- Images
- Back/navigation
- Broken links
- Empty search results

### Example

```text
Open /berita
Select a news item
Verify detail page
Verify title matches selected item
Verify content is visible
```

---

# 9.3 Aktiviti & Pameran

Test separately where the UI separates them.

Test:

- Listing
- Detail
- Date
- Venue
- Description
- Images
- Search/filter
- Pagination
- Navigation
- Public visibility

### Example

```text
Open exhibition listing
Open one exhibition
Verify title
Verify date
Verify venue when present
Verify description
Verify images
```

---

# 9.4 Artis

Test:

- Artist listing
- Artist search
- Artist profile
- Artist biography/details
- Artwork relationship
- Gallery relationship when applicable
- Pagination

### Cross-module test

```text
Artist
  ↓
Artist Profile
  ↓
Associated Artwork
  ↓
Artwork Detail
```

Verify that navigation between these objects works correctly.

---

# 9.5 Katalog Karya Seni

Test:

- Artwork listing
- Artwork detail
- Search
- Filter
- Pagination
- Images
- Metadata
- Artist information
- Category information when visible
- Empty results
- Invalid search terms

### Search test

```text
Enter valid keyword
Submit search
Expected:
Relevant result(s) are displayed
```

### Negative search test

```text
Enter random nonexistent keyword
Submit
Expected:
Clear empty-result state
No unrelated result presented
```

---

# 9.6 Galeri

Test:

- Gallery listing
- Album opening
- Image loading
- Image navigation
- Lightbox if available
- Slideshow if available
- Next/previous controls
- Close controls
- Broken image handling

### Example

```text
Open gallery
Open album
Open image
Click next
Expected:
Next image is displayed
```

---

# 9.7 Banner

From a public black-box perspective, test observable behaviour:

- Banner displayed
- Image loads
- Banner link works
- Carousel works if present
- Previous/next controls
- Automatic rotation if applicable
- Mobile display

If banner management is only available in an admin/CMS area, test management functions only when valid credentials are supplied.

---

# 9.8 Pengurusan Pengguna

This module is normally authenticated.

If an authorised test account exists, test:

- Login
- Logout
- Invalid login
- Password validation
- User listing
- User creation
- User editing
- User deletion/deactivation where permitted
- Role/permission behaviour

Do not attempt privilege escalation.

### Example

```text
Login as normal authorised user
Open restricted admin function
Expected:
Access matches assigned permission
```

---

# 9.9 Audit Trail

Audit trail is tested only if it is exposed to the test account.

A black-box test cannot directly inspect database audit records.

Instead:

```text
Perform observable action
↓
Open Audit Trail
↓
Search/view the resulting record
↓
Verify the action is represented correctly
```

If audit records are not accessible:

```text
Status: NOT OBSERVABLE
```

Do not claim that the database contains an audit record merely because the action succeeded.

---

# 10. CRUD Testing

For authenticated administrative functions, use the following black-box pattern.

## Create

```text
Open management page
Click Add
Enter valid data
Submit
Expected:
Success indication
New record appears
```

## Read

```text
Open listing
Find created record
Open detail/view
Expected:
Correct data is displayed
```

## Update

```text
Open record
Edit a field
Save
Reload/view record
Expected:
Changed value remains visible
```

## Delete

```text
Delete test record
Confirm deletion
Refresh/search
Expected:
Record no longer appears
```

Use only safe synthetic test data.

---

# 11. Test Data Strategy

Use clearly identifiable test data.

Recommended prefix:

```text
PWTEST_
```

Examples:

```text
PWTEST_Artist_001
PWTEST_News_001
PWTEST_Exhibition_001
PWTEST_Artwork_001
PWTEST_Gallery_001
```

This makes test-created content easier to identify and clean up.

Do not use real confidential information.

---

# 12. Positive Testing

Positive testing verifies valid user behaviour.

Examples:

```text
Valid search
Valid login
Valid form submission
Valid image upload
Valid navigation
Valid filter
Valid pagination
Valid CRUD operation
```

Expected behaviour must be defined before marking PASS.

---

# 13. Negative Testing

Negative testing checks how the website handles invalid input.

Examples:

### Login

```text
Wrong username
Wrong password
Empty username
Empty password
```

### Search

```text
Unknown keyword
Very long keyword
Special characters
Empty search
```

### Forms

```text
Required field empty
Invalid email
Invalid date
Oversized upload
Unsupported file type
```

The test should verify that the application:

- rejects invalid data when appropriate
- displays understandable validation
- does not crash
- does not expose sensitive information

---

# 14. Search and Filter Testing

For every visible search/filter feature:

Test:

1. Valid keyword
2. Partial keyword
3. No result
4. Empty keyword
5. Multiple filters
6. Reset filter
7. Pagination after filtering
8. Open result
9. Back to result list

Example:

```text
Search "PWTEST"
→ Results appear
→ Open result
→ Return
→ Search state behaves consistently
```

---

# 15. Navigation Testing

The AI should verify important navigation paths.

Examples:

```text
Home
→ News
→ News Detail
→ Back

Home
→ Artist
→ Artist Profile
→ Artwork
→ Artwork Detail

Home
→ Gallery
→ Album
→ Image
→ Next Image

Home
→ Search
→ Result
→ Detail
```

Check for:

- dead links
- incorrect destination
- unexpected redirects
- 404 pages
- broken navigation
- incorrect breadcrumbs
- browser back/forward problems

---

# 16. Responsive Black-Box Testing

The website should be tested at multiple viewport sizes.

At minimum:

```text
Desktop
Tablet
Mobile
```

Example:

```bash
playwright-cli open https://TARGET_URL
```

Then use supported browser/device configuration as appropriate.

Check:

- navigation
- hamburger menu
- cards
- forms
- images
- tables
- search
- buttons
- text overflow
- horizontal scrolling
- modal/lightbox
- footer

A page passing on desktop does not automatically mean it passes on mobile.

---

# 17. Browser Testing

If the environment allows it, test important workflows across:

```text
Chromium
Firefox
WebKit
```

Prioritise critical workflows first.

Do not require every browser for every low-priority visual check unless the project specifically requires it.

---

# 18. Authentication Testing

When credentials are available:

## Valid login

```text
Enter valid credentials
Submit
Expected:
Authenticated area is displayed
```

## Invalid login

```text
Enter invalid credentials
Submit
Expected:
Authentication fails
Clear error/validation is shown
```

## Logout

```text
Login
Logout
Attempt to access authenticated page
Expected:
User is no longer authenticated
```

## Session behaviour

Check:

- refresh after login
- direct navigation to protected page
- logout
- browser back behaviour
- session expiry when testable

Never attempt to bypass authentication or discover other users' credentials.

---

# 19. Role-Based Access Testing

If multiple authorised test accounts are provided:

```text
Admin
Staff
Content Manager
Normal User
```

test the permissions observable for each role.

Example:

```text
Role A
→ Access management page
→ PASS if authorised

Role B
→ Same page
→ PASS if access is correctly restricted
```

Do not guess the intended permission model. Use the documented requirements or provided account permissions.

---

# 20. File Upload Testing

Where the UI provides upload functionality:

Test:

- valid image
- valid document where supported
- unsupported extension
- oversized file
- empty upload
- filename with spaces
- filename with special characters
- duplicate filename if relevant

Example:

```text
Upload PWTEST_image.jpg
Submit
Expected:
Upload succeeds
Image is visible/associated with the correct record
```

Do not upload malware or dangerous files.

---

# 21. Public Visibility Testing

For CMS-managed content, test the observable publishing lifecycle.

Example:

```text
Create test content
↓
Save
↓
Check public website
↓
Publish if required
↓
Check public website again
↓
Unpublish
↓
Check public website again
```

Expected results must follow the project's actual documented publishing behaviour.

Do not assume every saved record should immediately be publicly visible.

---

# 22. Cross-Module Testing

Black-box testing should not only test pages individually.

Important workflows include:

### Artist → Artwork

```text
Open artist
→ Open associated artwork
→ Verify artwork points to correct artist
```

### Exhibition → Gallery

```text
Open exhibition
→ Follow gallery/media link where available
→ Verify related content
```

### News → Homepage

If the homepage displays news:

```text
Open news
→ Verify public content
→ Return homepage
→ Verify expected homepage placement if applicable
```

### Banner → Destination

```text
Click banner
→ Verify destination
```

### User → Permission → Action

```text
Login with authorised account
→ Perform permitted action
→ Verify success
```

---

# 23. Playwright CLI Interaction Strategy

Use the CLI to inspect the live page before interacting.

Recommended pattern:

```bash
playwright-cli open https://TARGET_URL
playwright-cli snapshot
```

Then use semantic targets from the current page.

Prefer:

```text
role
accessible name
label
visible text
stable test id when available
```

Avoid depending on:

```text
generated CSS classes
random element IDs
deep DOM paths
XPath
position-only selectors
```

After important state changes:

```bash
playwright-cli snapshot
```

Re-inspect the page before continuing.

Do not blindly reuse stale element references after navigation or major DOM changes.

---

# 24. Evidence Collection

For every important failure, capture evidence.

Use:

```bash
playwright-cli screenshot
```

Also capture:

- URL
- page title
- visible error
- test steps
- expected result
- actual result
- browser
- viewport
- timestamp
- relevant console output
- relevant network/request information when useful

For complex failures, use Playwright tracing/debugging capabilities when available.

---

# 25. Console and Network Investigation

Console/network inspection is for **diagnosing observable failures**, not for turning the test into white-box testing.

Useful evidence may include:

```text
JavaScript exception
404 resource
500 response
failed API request
blocked resource
timeout
```

A network error can support a defect report, but the final test result should still describe the user-visible effect.

Example:

```text
Expected:
News detail opens

Actual:
Page displays error and content is unavailable

Evidence:
Browser console shows failed request
```

---

# 26. Test Priority

Use:

```text
P0 – Critical
P1 – High
P2 – Medium
P3 – Low
```

## P0

- Homepage unavailable
- Login completely unavailable
- Major navigation unavailable
- Critical content cannot be accessed

## P1

- Core module function broken
- Search unusable
- Important CRUD workflow broken
- Important public content inaccessible

## P2

- Secondary function broken
- Validation issue
- Non-critical responsive issue

## P3

- Cosmetic issue
- Minor text/layout problem
- Low-impact inconsistency

Priority is for test execution/defect management, not a quality score for the system.

---

# 27. PASS / FAIL / BLOCKED / NOT OBSERVABLE

Use exactly these statuses.

## PASS

The observed result satisfies the expected behaviour.

## FAIL

The function is observable but does not behave as expected.

## BLOCKED

The test could not be completed because of an environment/dependency problem.

Examples:

```text
Website unavailable
Required test account unavailable
Required external service unavailable
```

## NOT OBSERVABLE

The requirement/function cannot be tested from the supplied public website/account.

This is different from FAIL.

---

# 28. Defect Classification

When something fails, classify it.

```text
APPLICATION BUG
TEST/DATA ISSUE
ENVIRONMENT ISSUE
ACCESS/PERMISSION ISSUE
REQUIREMENT AMBIGUITY
```

Do not immediately modify application code.

The AI is acting as a black-box tester, not a developer.

---

# 29. Defect Report Format

Use this format:

```text
DEFECT ID:
TC ID:
MODULE:
TITLE:
PRIORITY:

PRECONDITION:
URL:

STEPS TO REPRODUCE:
1.
2.
3.
4.

EXPECTED RESULT:

ACTUAL RESULT:

STATUS:

ENVIRONMENT:
Browser:
Viewport:

EVIDENCE:
Screenshot:
Console:
Network:
Trace:

NOTES:
```

Example:

```text
DEFECT ID: BUG-001
TC ID: TC-ARTIST-004
MODULE: Artis
TITLE: Artist search returns unrelated results
PRIORITY: P1

STEPS:
1. Open artist page
2. Enter PWTEST_Artist_001
3. Submit search
4. Inspect results

EXPECTED:
Matching artist is displayed

ACTUAL:
Unrelated artists are displayed

STATUS:
FAIL
```

---

# 30. Test Case Format

Every test should have:

```text
Test ID
Module
Feature
Precondition
Steps
Expected Result
Actual Result
Status
Priority
Evidence
```

Example:

```text
TC-NEWS-001

Module:
Berita & Pengumuman

Feature:
Open news detail

Precondition:
Website is accessible

Steps:
1. Open News
2. Select a news item

Expected:
Selected news detail page opens and displays the corresponding content

Actual:
[record result]

Status:
PASS / FAIL / BLOCKED / NOT OBSERVABLE

Priority:
P1
```

---

# 31. Recommended Test Execution Order

Run tests in this order:

```text
PHASE 1
Website discovery

PHASE 2
Smoke testing

PHASE 3
Navigation testing

PHASE 4
Public module functional testing

PHASE 5
Search/filter testing

PHASE 6
Responsive testing

PHASE 7
Authentication testing
(if credentials available)

PHASE 8
Admin/CMS functional testing
(if accessible)

PHASE 9
CRUD testing
(if accessible)

PHASE 10
Cross-module testing

PHASE 11
Regression testing

PHASE 12
Final report
```

---

# 32. AI Autonomous Testing Instructions

The AI must follow this workflow.

### Step 1 — Understand the target

Identify:

```text
Website URL
Available credentials
Accessible modules
Known requirements
```

### Step 2 — Discover the website

Open the URL and inspect the actual UI.

Do not invent routes.

### Step 3 — Build an observable test map

Record:

```text
Page
URL
Feature
Available action
Expected observable behaviour
```

### Step 4 — Run smoke tests

Do not begin deep testing if the website is fundamentally unavailable.

### Step 5 — Generate test cases

Generate tests from:

1. Documented GoGallery requirements
2. Observable website functions
3. User workflows

### Step 6 — Execute tests

Use Playwright CLI.

### Step 7 — Verify results

Do not mark PASS simply because:

```text
click succeeded
page loaded
HTTP request returned
toast appeared
```

Verify the resulting observable state.

### Step 8 — Capture failures

Take screenshots and collect useful browser evidence.

### Step 9 — Investigate

Use console/network/tracing information where useful.

### Step 10 — Classify

Choose:

```text
PASS
FAIL
BLOCKED
NOT OBSERVABLE
```

### Step 11 — Regression test

After a failure is fixed externally, rerun:

```text
Original failed test
Related test
Cross-module test
Smoke test
```

### Step 12 — Report

Produce a clear test summary.

---

# 33. What the AI Must NOT Do

The AI must NOT:

- assume source-code implementation
- claim database state that cannot be observed
- invent hidden URLs
- bypass authentication
- attempt credential attacks
- manipulate production data without authorisation
- delete real production records
- upload dangerous files
- mark unavailable functionality as PASS
- treat a successful click as proof of success
- treat HTTP 200 alone as proof of correct functionality
- change application code during testing unless explicitly instructed
- hide failed tests
- silently convert BLOCKED into PASS

---

# 34. Production Safety

If the supplied URL is a live production system:

Default behaviour must be non-destructive.

Prefer:

```text
Read
Search
Open
Filter
Navigate
Login with authorised account
```

Before performing:

```text
Create
Update
Delete
Publish
Unpublish
Upload
```

confirm that the environment and test account are intended for testing.

If no safe test account/data is available, report the relevant test as:

```text
BLOCKED
```

rather than modifying real production data.

---

# 35. Test Report

At the end of the testing run, produce:

## Executive Summary

```text
Target:
Test Date:
Browser:
Environment:

Total Tests:
PASS:
FAIL:
BLOCKED:
NOT OBSERVABLE:
```

## Module Summary

| Module | PASS | FAIL | BLOCKED | NOT OBSERVABLE |
|---|---:|---:|---:|---:|
| Portal Utama | | | | |
| Berita & Pengumuman | | | | |
| Aktiviti & Pameran | | | | |
| Artis | | | | |
| Katalog Karya Seni | | | | |
| Galeri | | | | |
| Banner | | | | |
| Pengurusan Pengguna | | | | |
| Audit Trail | | | | |

## Critical Defects

List:

```text
BUG ID
Module
Problem
Priority
Reproduction status
Evidence
```

## Coverage Gaps

List functions that could not be tested because they were:

```text
Not accessible
Not observable
Missing test credentials
Blocked by environment
Not available in current website
```

---

# 36. Definition of Done

A black-box test cycle is complete when:

- Website discovery is completed
- Smoke tests are completed
- All observable core modules are tested
- Important public workflows are tested
- Search/filter functions are tested where available
- Authentication is tested where authorised credentials exist
- Admin functions are tested where accessible
- CRUD is tested where applicable
- Negative/validation cases are tested
- Responsive behaviour is checked
- Important cross-module workflows are tested
- Failures have evidence
- BLOCKED and NOT OBSERVABLE cases are explicitly recorded
- Regression tests are run for fixed defects
- Final test report is produced

---

# 37. Final Instruction to the AI Tester

You are performing **black-box functional testing of the GoGallery website**.

You do not have source code.

Your source of truth for actual behaviour is the website itself plus the approved GoGallery requirements.

Always:

```text
Observe
→ Interact
→ Verify
→ Record
→ Evidence
→ Classify
```

Do not guess.

If the website behaves correctly, mark PASS.

If an observable function behaves incorrectly, mark FAIL.

If testing cannot proceed because of an external dependency, mark BLOCKED.

If a requirement cannot be observed from the supplied website/account, mark NOT OBSERVABLE.

The goal is to provide an objective functional test report based on what can actually be demonstrated through the website.
