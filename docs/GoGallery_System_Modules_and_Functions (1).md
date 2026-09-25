# GoGallery — System Modules & Functions

## 1. Core System Modules

The current GoGallery system baseline consists of nine main modules:

1. Portal Utama
2. Berita & Pengumuman
3. Aktiviti & Pameran
4. Artis
5. Katalog Karya Seni
6. Galeri
7. Banner
8. Pengurusan Pengguna
9. Audit Trail

The module breakdown below focuses only on **system modules and their functions**.

---

# 2. Portal Utama

## Purpose
Provides the main public landing page of GoGallery and presents highlights from important portal content.

## Functions

### Public Functions
- Display homepage.
- Display welcome/introduction content.
- Display featured or latest news.
- Display exhibitions and activities.
- Display featured artwork/catalogue content.
- Display selected gallery/content highlights.
- Provide navigation to major portal sections.
- Provide access to global search.
- Display selected social-media content where configured.

### Admin Functions
- Manage homepage content.
- Manage homepage highlights.
- Configure content shown on the homepage.
- Publish/unpublish homepage content.
- Manage homepage images/media.

---

# 3. Berita & Pengumuman

## Purpose
Manages news, announcements and related information published on the GoGallery portal.

## Functions

### Admin Functions
- Create news/announcement.
- Edit news/announcement.
- Delete news/announcement.
- Upload news image/document.
- Enter title.
- Enter publication date.
- Enter description/content.
- Assign category/section where applicable.
- Publish/unpublish news.
- Hide/unhide news.
- Search and manage existing news.
- Track content creation/update information.

### Public Functions
- Display news listing.
- Display announcement listing.
- Search/view available news.
- View individual news detail.
- Open related external URL/document where applicable.

---

# 4. Aktiviti & Pameran

## Purpose
Provides information about exhibitions, activities and programmes related to the visual arts.

## Functions

### Exhibition Functions
- Create exhibition.
- Edit exhibition.
- Delete exhibition.
- Publish/unpublish exhibition.
- Hide/unhide exhibition.
- Upload exhibition image/poster.
- Enter exhibition title.
- Enter exhibition description.
- Enter exhibition date.
- Enter organiser.
- Enter venue.
- Enter URL where applicable.
- Display current/upcoming exhibitions.
- Display exhibition detail.

### Activity / Programme Functions
- Create activity/programme.
- Edit activity/programme.
- Delete activity/programme.
- Publish/unpublish activity.
- Hide/unhide activity.
- Upload activity image/poster.
- Enter activity title.
- Enter activity description.
- Enter date.
- Enter organiser.
- Enter venue/URL.
- Display activity listing.
- Display activity detail.

### Public Functions
- View exhibition listing.
- View exhibition detail.
- View activity/programme listing.
- View activity/programme detail.
- Search/browse available activities and exhibitions.

### User Submission
The technical specification states that data for exhibitions and activities may be uploaded by administrators or registered users.

---

# 5. Artis

## Purpose
Provides artist profiles and information about artists, their works and related activities.

## Functions

### Admin Functions
- Create artist profile.
- Edit artist profile.
- Delete artist profile.
- Publish/unpublish artist profile.
- Hide/unhide artist profile.
- Upload artist image/profile picture.
- Enter artist name.
- Enter artist information.
- Enter address/contact information where applicable.
- Enter biography.
- Associate artworks with artist.
- Associate services/merchandise with artist where applicable.
- Associate exhibitions/activities and other uploads with artist.
- Store artist social-media links.

### Public Functions
- Display artist directory.
- Search/browse artists.
- View artist profile.
- View artist biography.
- View artist image.
- View associated artworks.
- View related activities/exhibitions/content.
- Access configured social-media links.

### Artist Metadata
The technical specification lists:
- Name
- Image
- Address
- Email
- Contact number
- Biography
- Artworks/services/merchandises
- Related uploads
- Facebook
- Instagram
- Twitter
- YouTube
- Creation/update information
- Hide/unhide status

---

# 6. Katalog Karya Seni

## Purpose
Provides an online catalogue for viewing and searching artwork information.

## Functions

### Admin Functions
- Create artwork record.
- Edit artwork record.
- Delete artwork record.
- Upload artwork image.
- Enter artwork title.
- Associate artwork with artist.
- Enter artwork year.
- Enter artwork medium.
- Enter artwork dimensions where applicable.
- Enter artwork price where applicable.
- Enter artwork description.
- Manage artwork category.
- Publish/unpublish artwork.
- Hide/unhide artwork.
- Manage artwork image/media.

### Public Functions
- Display artwork catalogue.
- View artwork listing.
- View artwork detail.
- Search artworks.
- Filter artworks by category.
- Filter artworks by medium.
- Filter artworks by year.
- View artwork image.
- View artwork metadata/details.
- Navigate from artwork to related artist information.

### Legacy/Tender Artwork Function
The technical specification also describes an **Art for Sale** function where artwork can be uploaded by administrators or registered users and visitors can use a **Contact Seller** function.

This function is documented in the technical specification and should be treated separately from the current nine-module baseline if its inclusion in the current implementation has not been confirmed.

---

# 7. Galeri

## Purpose
Provides visual albums and image collections for activities and exhibitions.

## Functions

### Admin Functions
- Create gallery album.
- Edit gallery album.
- Delete gallery album.
- Upload images.
- Remove images.
- Organise images into albums.
- Enter album/title information.
- Associate album with activity/exhibition where applicable.
- Publish/unpublish album.
- Hide/unhide album.

### Public Functions
- Display gallery album listing.
- View album.
- View individual images.
- Open image in lightbox.
- View images as slideshow.
- Browse activity/exhibition image collections.

### Gallery Profile Functions
The technical specification also describes a gallery profile function containing:
- Gallery name
- Image
- Address
- Contact number
- Facebook
- Instagram
- Twitter
- YouTube
- Related artworks/services/merchandises
- Related uploads

This is broader than the current public image-gallery navigation and should be treated according to the confirmed project scope.

---

# 8. Banner

## Purpose
Manages promotional or featured visual banners displayed on the portal.

## Functions

### Admin Functions
- Create banner.
- Edit banner.
- Delete banner.
- Upload banner image.
- Enter banner title/content.
- Configure banner link/URL where applicable.
- Configure display order.
- Activate/deactivate banner.
- Publish/unpublish banner.
- Hide/unhide banner.
- Manage banner display content.

### Public Functions
- Display active banners.
- Display banners according to configured order/status.
- Navigate to configured banner destination where applicable.

---

# 9. Pengurusan Pengguna

## Purpose
Manages user accounts, authentication and access to the administration/user functions of GoGallery.

## Functions

### Registration
- Display registration form.
- Register new user.
- Capture name.
- Capture email.
- Capture contact number.
- Capture address.
- Capture website URL where applicable.
- Capture social-media links.
- Upload profile picture.
- Select category/profession where applicable.
- Create user account.

### Authentication
- User login.
- User logout.
- Authentication validation.
- Password management.
- Password reset/configuration.
- Registration confirmation through email where implemented.
- Social-media registration/login where implemented and approved.

### User Administration
- View users.
- Create user.
- Edit user.
- Activate/deactivate user.
- Manage user profile.
- Assign user role/access level.
- Manage permissions.
- Delete/deactivate account where permitted.

### Role-Based Access Control
- Restrict functions based on user role.
- Restrict administrative modules based on permission.
- Control access to protected dashboard functions.
- Separate public and authenticated functions.

### Registered User Functions
The technical specification describes registered users as being able to add/update information for applicable areas such as:
- Profile
- Exhibitions & Activities
- Tutorials
- Sharing
- Articles
- Art for Sale
- Services
- Merchandises
- E-Publications
- News
- Inbox

Only functions confirmed for the current implementation should be enabled.

---

# 10. Audit Trail

## Purpose
Records important system and administrative activities for traceability.

## Functions

### Audit Recording
- Record user login activity.
- Record data creation.
- Record data updates.
- Record data deletion where applicable.
- Record publishing/unpublishing actions.
- Record user/account changes.
- Record important administrative actions.
- Store user/actor information.
- Store action/date-time information.
- Store affected record/module information where applicable.

### Audit Viewing
- View audit records.
- Search/filter audit records.
- Identify user who performed an action.
- Identify action performed.
- Identify affected module/record where available.
- Identify date/time of action.

### Access Control
- Restrict audit-trail access to authorised users.

---

# 11. Supporting System Functions

These are system-wide functions supporting the nine core modules.

## 11.1 CMS / Content Management
- Create content.
- Edit content.
- Delete content.
- Publish/unpublish content.
- Hide/unhide content.
- Manage images/documents.
- Manage content metadata.
- Record creation/update information.

## 11.2 Menu Management
- Manage portal navigation.
- Configure menu items.
- Link menu items to portal sections/pages.
- Control menu visibility/order.

## 11.3 Global Search
- Search portal content.
- Search by keyword.
- Return relevant content results.
- Provide access to detail pages from search results.

## 11.4 SEO
- Manage page title.
- Manage page description/metadata.
- Use readable URLs.
- Manage image alternative text where applicable.
- Provide sitemap functionality where implemented.

## 11.5 Responsive UI
- Support desktop display.
- Support tablet display.
- Support mobile display.
- Adapt navigation and content layout to screen size.

## 11.6 Media Management
- Upload images.
- Upload documents where permitted.
- Manage media associated with content.
- Validate supported media types/size according to system configuration.

## 11.7 Content Status
Common content controls include:
- Draft/content creation.
- Publish.
- Unpublish.
- Hide.
- Unhide.
- Active/inactive status where applicable.

---

# 12. Public Portal vs Administration Functions

## Public Portal

The public side primarily provides:

```text
Home
News & Announcements
Activities
Exhibitions
Artwork Catalogue
Artists
Gallery
Global Search
```

Public users can browse and view published content.

## Administration / Authenticated Side

The administration side primarily provides:

```text
Content Management
News Management
Activity Management
Exhibition Management
Artist Management
Artwork Management
Gallery Management
Banner Management
User Management
Access Control
Audit Trail
```

Authenticated registered users may have additional content-submission functions depending on their role and approved permissions.

---

# 13. Core CRUD Pattern

Most content-management modules follow a common CRUD pattern:

```text
Create
  ↓
Read / View
  ↓
Update
  ↓
Delete
  ↓
Publish / Unpublish
  ↓
Hide / Unhide
```

Applicable modules include:

- News
- Activities
- Exhibitions
- Artists
- Artworks
- Gallery albums/images
- Banners
- Users
- Other CMS-managed content

---

# 14. Module Relationship Overview

```text
                         GoGallery
                            |
          +-----------------+-----------------+
          |                                   |
     Public Portal                       Administration
          |                                   |
    +-----+-----+                     +-------+-------+
    |           |                     |               |
  Content    Search                CMS / CRUD     User Access
    |                                   |               |
    +---------------+-------------------+               |
                    |                                   |
              Core Modules                       RBAC / Users
                    |
     +--------------+--------------+
     |      |       |      |       |
    News  Activity Artist Artwork Gallery
                    |
                 Banner
                    |
               Audit Trail
```

---

# 15. Function Scope Rule

For future development discussions, use the following distinction:

### Current Core Modules
```text
Portal Utama
Berita & Pengumuman
Aktiviti & Pameran
Artis
Katalog Karya Seni
Galeri
Banner
Pengurusan Pengguna
Audit Trail
```

### Supporting Functions
```text
CMS / Content Management
Menu Management
Global Search
SEO
Responsive UI
Media Management
Authentication
RBAC
```

### Legacy / Technical-Specification Functions
The technical specification contains additional functions such as:
- Art for Sale
- Services
- Merchandises
- Tutorials
- Sharings
- Articles
- Grants/Sponsorships
- E-Publications
- NAG Permanent Collection
- Links
- Contact Us
- Registered-user Inbox

These should **not automatically be treated as confirmed current modules** unless the current project scope confirms them.

---

# 16. Source Basis

This module/function list is derived from the GoGallery project documents, particularly:

- System Requirement Modules
- GoGallery technical/tender specification
- UI Specification
- Existing GoGallery WBS/module planning

The nine core modules are the current module baseline, while the technical specification provides additional legacy/expanded functions that are explicitly marked above.
