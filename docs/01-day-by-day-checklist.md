# Day-by-Day Implementation Checklist (Two-Developer, No-Collision)
## Samar Construction Visibility Website (Django)
**Scope:** Dynamic Blog + Services/Products + Portfolio + Leads + Static Pages  
**Goal:** Low-maintenance website where the company updates content via Django Admin.

This plan **explicitly includes** all items from the “Django Website Development Guide” you listed:
- Virtualenv, dependencies, apps, settings, media/static/templates
- Models (Blog/Catalog/Portfolio/Leads) with required fields
- Admin configuration (filters/search/inlines/slug prepopulate)
- URLs + views for core/blog/catalog/portfolio
- Templates structure + design guidance (WhatsApp, cards, hero)
- Lead capture (save to DB; optional email later)
- Migrations, superuser, content population, QA checks
- Useful additions: **Search**, **SEO basics (meta + sitemap)**, **Analytics later**
- Deployment stack: Render/Railway + PostgreSQL + Cloudinary

---

## Team Roles and Anti-Collision Rules
**Developer A (Backend / Models / Admin / Views / URLs / Deployment)**  
**Developer B (Frontend / Templates / UX / Static styling / Content formatting)**

### Branching (recommended)
- `main` (stable)
- `dev-backend` (Developer A)
- `dev-frontend` (Developer B)

### Daily merge rule (prevents clashes)
1. Morning: `git pull` from `main`
2. Work on your branch only
3. End of day: open PR to `main` OR merge to `main` after a quick review
4. Do not edit the same file on the same day unless the checklist says “Shared”

---

# DAY 1 — Environment + Project Skeleton (PHASE 1)
### Developer A
- [ ] Create/activate venv  
  ```bash
  python -m venv venv
  # Windows: venv\Scripts\activate
  # Mac/Linux: source venv/bin/activate
  ```
- [ ] Upgrade pip  
  ```bash
  python -m pip install --upgrade pip
  ```
- [ ] Install dependencies  
  ```bash
  pip install django pillow
  ```
- [ ] Freeze requirements  
  ```bash
  pip freeze > requirements.txt
  ```
- [ ] Ensure Django project exists (skip if already created)  
  ```bash
  django-admin startproject config .
  ```

### Developer B
- [ ] Create folders in project root (same level as manage.py):
  - `templates/`
  - `static/`
  - `media/`
- [ ] Create `static/` structure:
  - `static/css/`
  - `static/js/`
  - `static/images/`
- [ ] Create `templates/partials/` folder

**Deliverable**
- [ ] `python manage.py runserver` works without errors

---

# DAY 2 — Apps + settings.py + media/static/templates wiring (PHASE 1 & 2)
### Developer A
- [ ] Create apps (if not already)  
  ```bash
  python manage.py startapp core
  python manage.py startapp blog
  python manage.py startapp catalog
  python manage.py startapp portfolio
  python manage.py startapp leads
  ```
- [ ] Register apps in `settings.py` (`INSTALLED_APPS`): core, blog, catalog, portfolio, leads
- [ ] Add templates DIRS in `settings.py`  
  ```python
  TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates']
  ```
- [ ] Add static/media configuration in `settings.py`  
  ```python
  STATIC_URL = '/static/'
  STATICFILES_DIRS = [BASE_DIR / 'static']

  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media'
  ```
- [ ] Configure development media serving in project `urls.py`  
  ```python
  from django.conf import settings
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```
- [ ] Run migrations + create superuser  
  ```bash
  python manage.py migrate
  python manage.py createsuperuser
  ```

### Developer B
- [ ] Create base template files (skeleton only):
  - `templates/base.html`
  - `templates/partials/navbar.html`
  - `templates/partials/footer.html`
- [ ] Add placeholders for:
  - WhatsApp button in navbar/footer (dummy number for now)
  - Footer contact placeholders

**Deliverable**
- [ ] Admin panel accessible at `/admin/`
- [ ] Base template renders (even with placeholder content)

---

# DAY 3 — Core URLs + Core Views + Layout integration (PHASE 4 & 6)
### Developer A
- [ ] Create core views: Home, About, Contact (page only today; form comes later)
- [ ] Add core urls and include them in project urls:
  - `/` → home
  - `/about/` → about
  - `/contact/` → contact

### Developer B
- [ ] Implement base layout usage:
  - base.html includes navbar/footer partials
  - block structure: `{% block title %}`, `{% block content %}`
- [ ] Create core templates:
  - `templates/core/home.html`
  - `templates/core/about.html`
  - `templates/core/contact.html`
- [ ] Apply design guidance:
  - hero section placeholder on home
  - card grid placeholders for services/projects/blog
  - WhatsApp button visible

**Deliverable**
- [ ] Home/About/Contact pages render with consistent layout

---

# DAY 4 — Blog Models + Admin (PHASE 3 & 4)
### Developer A (Backend)
- [ ] Create `blog/models.py`:
  - Post fields: title, slug(unique), excerpt, content, featured_image, status(DRAFT/PUBLISHED), published_at, created_at, updated_at
  - Optional Category model (only if you want categories on blog)
- [ ] Run migrations  
  ```bash
  python manage.py makemigrations blog
  python manage.py migrate
  ```
- [ ] Configure `blog/admin.py`:
  - list_display: title, status, published_at
  - list_filter: status
  - search_fields: title, excerpt
  - prepopulate slug from title

### Developer B (Frontend)
- [ ] Create blog template structure (UI skeleton + placeholders):
  - `templates/blog/post_list.html`
  - `templates/blog/post_detail.html`

**Deliverable**
- [ ] Posts can be created/edited in admin with Draft/Published control

---

# DAY 5 — Blog Views + URLs + Templates (PHASE 4 & 6)
### Developer A
- [ ] Blog list view: shows **published posts only**
- [ ] Blog detail view: by slug
- [ ] Blog URLs:
  - `/blog/` list
  - `/blog/<slug>/` detail
- [ ] Optional: blog search query param `?q=` (basic contains search)

### Developer B
- [ ] Implement blog list UI:
  - cards with featured image, title, excerpt, date
- [ ] Implement blog detail UI:
  - title, date, featured image, content
- [ ] Add “Latest 3 blog posts” section on Home (template ready; context later)

**Deliverable**
- [ ] Blog list + detail fully functional

---

# DAY 6 — Catalog Models + Admin (Services/Products) (PHASE 3 & 4)
### Developer A
- [ ] Create `catalog/models.py`:
  - Category: name, slug
  - Product/Service: name, slug, short_description, description, category, is_active, price_note(optional), created_at
  - ProductImage: product(FK), image
- [ ] Run migrations  
  ```bash
  python manage.py makemigrations catalog
  python manage.py migrate
  ```
- [ ] Admin setup:
  - Category slug prepopulate
  - Product list_display: name, category, is_active
  - filters: category, is_active
  - inline ProductImage (multiple images)

### Developer B
- [ ] Create catalog templates (UI skeleton):
  - `templates/catalog/product_list.html`
  - `templates/catalog/product_detail.html`

**Deliverable**
- [ ] Services/products manageable in admin (with multiple images)

---

# DAY 7 — Catalog Views + URLs + Templates (PHASE 4 & 6)
### Developer A
- [ ] Catalog URLs:
  - `/services/` (or `/products/`) list
  - `/services/<slug>/` detail
- [ ] Views:
  - list shows active products only
  - detail includes image gallery
- [ ] Optional: category filter (via slug) and search `?q=`

### Developer B
- [ ] Build listing UI:
  - category label, short description, CTA button
- [ ] Build detail UI:
  - gallery layout, price_note, WhatsApp “Request Quote” CTA
- [ ] Ensure card-based design and mobile responsiveness

**Deliverable**
- [ ] Services/products list + detail working with images

---

# DAY 8 — Portfolio Models + Admin (PHASE 3 & 4)
### Developer A
- [ ] Create `portfolio/models.py`:
  - Project fields: title, slug, summary, description, location(optional), completed_date(optional), is_active, created_at
  - ProjectImage: project(FK), image
- [ ] Run migrations  
  ```bash
  python manage.py makemigrations portfolio
  python manage.py migrate
  ```
- [ ] Admin setup:
  - list_display: title, is_active
  - inline ProjectImage
  - search_fields: title, location (if present)

### Developer B
- [ ] Create portfolio templates (UI skeleton):
  - `templates/portfolio/project_list.html`
  - `templates/portfolio/project_detail.html`

**Deliverable**
- [ ] Projects manageable in admin (multiple images)

---

# DAY 9 — Portfolio Views + URLs + Templates (PHASE 4 & 6)
### Developer A
- [ ] URLs:
  - `/projects/` list
  - `/projects/<slug>/` detail
- [ ] Views:
  - list shows active projects only
  - detail includes image gallery

### Developer B
- [ ] Build portfolio listing UI (cards)
- [ ] Build portfolio detail UI (gallery + description)
- [ ] Add “Latest projects” section layout on Home (template ready)

**Deliverable**
- [ ] Projects list + detail functional

---

# DAY 10 — Leads: Contact Form + Inquiry Storage (PHASE 7)
### Developer A
- [ ] Create `leads/models.py` Inquiry:
  - name, phone, email(optional), subject(optional), message, source_page(optional), created_at
  - status choices: New, Contacted, Closed
- [ ] Create `leads/forms.py` (Django Form)
- [ ] Contact view submit logic:
  - validate form
  - save Inquiry
  - show success message
- [ ] Register Inquiry in admin:
  - list_display: name, phone, status, created_at
  - filter: status
  - search: name, phone
- [ ] Run migrations  
  ```bash
  python manage.py makemigrations leads
  python manage.py migrate
  ```
- [ ] Optional email notification: **defer by default** (add later after deployment email config is stable)

### Developer B
- [ ] Finalize contact page UI:
  - clean form styling
  - success and error message display
  - WhatsApp fallback CTA

**Deliverable**
- [ ] Contact form saves inquiries in DB and appears in admin

---

# DAY 11 — Home Page Dynamic Integration (PHASE 5)
### Developer A
- [ ] Home view loads:
  - latest 3 published blog posts
  - featured 3 active services/products
  - latest 4 active projects
- [ ] Ensure queryset ordering is correct (latest first)

### Developer B
- [ ] Build Home sections properly:
  - hero + CTA buttons
  - services preview grid
  - projects preview grid
  - blog preview list/cards
- [ ] Ensure mobile responsiveness

**Deliverable**
- [ ] Home is fully dynamic and looks professional

---

# DAY 12 — Useful Additions + SEO Basics + QA + Content Population (PHASE 9 & 10)
### Developer A
- [ ] Search (blog + catalog):
  - `?q=` on list views (basic search)
- [ ] SEO basics:
  - ensure slugs are used everywhere
  - add page title blocks
  - add meta description blocks (base template)
- [ ] Sitemap (recommended):
  - simple sitemap endpoint OR django sitemap framework (if you want)
- [ ] Analytics placeholder:
  - add section in base.html for future GA/analytics script injection (do not hardcode keys)

### Developer B
- [ ] UI QA:
  - spacing consistency
  - image card sizing
  - typography and readability
- [ ] Mobile UX checks:
  - nav collapse (if used)
  - CTA button visibility
- [ ] Footer correctness:
  - phone/email/address/WhatsApp

### Shared
- [ ] Populate initial content in admin:
  - 5 services/products
  - 6 projects with photos
  - 3 blog posts
  - About text + contact details
- [ ] Functional checklist:
  - blog list shows only published
  - blog detail works
  - product list/detail works
  - project list/detail works
  - images render
  - contact form creates Inquiry
  - admin CRUD works for all modules

**Deliverable**
- [ ] Client-ready demo on local/staging + screenshots for reporting

---

# DAY 13 — Deployment (PHASE 11)
### Developer A (Owner)
- [ ] Add production dependencies:
  - `gunicorn`
  - `psycopg2-binary` (Postgres)
  - Cloudinary packages (if using Cloudinary)
- [ ] Prepare production settings:
  - DEBUG=False
  - ALLOWED_HOSTS
  - SECRET_KEY from env
  - database from env
  - static collection
- [ ] Deploy to Render/Railway:
  - connect GitHub repo
  - set environment variables
  - run migrations on server
- [ ] Configure Cloudinary for media (recommended)

### Developer B
- [ ] Post-deploy UI verification:
  - confirm media loads
  - confirm responsive pages
  - confirm no broken CSS/JS
- [ ] Prepare client handover screenshots:
  - Home, Blog, Services, Projects, Contact success, Admin pages

**Deliverable**
- [ ] Live website link (staging/production)

---

## Daily Git Checklist (Non-Negotiable)
- [ ] Pull latest from `main` before coding
- [ ] Work only on your branch
- [ ] Commit small and clear:
  - `feat(blog): add Post model and admin config`
  - `feat(catalog): implement product list and detail views`
  - `style(core): build responsive home sections`
- [ ] Merge at day end only

---

## Notes on Scope Control
This plan intentionally excludes:
- ecommerce checkout/payment
- user accounts/customer dashboards
- heavy CMS features
Any of those require a separate agreement.

---
