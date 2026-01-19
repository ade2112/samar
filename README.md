# Samar Construction – Django Website Development Guide

## Project Overview
This project is a Django-based corporate website developed for Samar Construction Sdn. Bhd.
The website focuses on online visibility, credibility, and lead generation, in line with the Marketing Services Agreement.

The system allows the company to:
- Publish blog posts dynamically
- Display services/products dynamically
- Showcase completed projects (portfolio)
- Receive and manage customer inquiries via a contact form
- Manage all content through the Django admin panel

This is not a large system. It is a lean, professional visibility website.

---

## Project Goals
- Improve online presence and brand credibility
- Provide dynamic content management via admin
- Capture customer leads
- Keep development, hosting, and maintenance costs low
- Deliver measurable marketing value (traffic, inquiries, engagement)

---

## Technology Stack
- Backend: Django
- Frontend: Django Templates + Bootstrap or Tailwind CSS
- Database: SQLite (development), PostgreSQL (production)
- Media Storage: Local (development), Cloudinary (recommended for production)
- Hosting: Render / Railway / VPS
- Version Control: Git + GitHub

---

## Core Features

### 1. Dynamic Blog
- Create, edit, publish blog posts from admin
- Draft and Published status
- SEO-friendly URLs (slug-based)
- Featured images
- Blog list and blog detail pages

### 2. Dynamic Services / Products
- Create services or products from admin
- Category support
- Multiple images per item
- Active/Inactive visibility control
- Request Quote / WhatsApp CTA

### 3. Portfolio / Projects
- Showcase completed construction projects
- Multiple images per project
- Optional location and completion date
- Used to build trust and credibility

### 4. Lead Capture (Contact Form)
- Website contact form
- Saves inquiries in database
- Admin can track inquiry status (New, Contacted, Closed)
- Optional email notification

### 5. Static Pages
- Home
- About Us
- Contact Us

---

## Recommended Django App Structure

project_root/
│
├── core/        # Home, About, Contact, shared layout
├── blog/        # Blog posts
├── catalog/     # Services / Products
├── portfolio/   # Projects
├── leads/       # Contact inquiries
│
├── templates/
├── static/
├── media/
├── manage.py
└── requirements.txt

---

## Development Phases

### Phase 1 – Setup
- Create and activate virtual environment
- Install dependencies
- Create Django apps
- Configure templates, static files, and media handling

### Phase 2 – Models
- Blog models (Post, Category)
- Catalog models (Product/Service, Category, Images)
- Portfolio models (Project, Images)
- Lead model (Inquiry)

### Phase 3 – Admin Panel
- Register all models
- Enable search, filters, inline images
- Configure slug auto-generation
- Enable easy content management for non-technical users

### Phase 4 – Views & URLs
- Home page (latest blogs, services, projects)
- Blog list and detail pages
- Product/service list and detail pages
- Project list and detail pages
- Contact form handling

### Phase 5 – Templates
- Base layout with navbar and footer
- Reusable components (partials)
- Responsive card-based layouts
- WhatsApp CTA visible on all pages

### Phase 6 – Lead Handling
- Save inquiries to database
- Display inquiries in admin
- Optional email notification setup

### Phase 7 – Testing & Content
- Populate with sample content
- Test admin CRUD operations
- Verify image uploads
- Test contact form and lead storage

### Phase 8 – Deployment
- Configure production settings
- Use PostgreSQL
- Use Cloudinary for media
- Deploy to Render/Railway/VPS

---

## Admin Panel Responsibilities
The admin panel is the core value of this system.

Admins can:
- Publish blog posts
- Add/edit services or products
- Upload project photos
- View and manage inquiries
- Control what appears on the website

No developer intervention should be required for daily updates.

---

## SEO & Marketing Notes
- Use clean URLs with slugs
- Add meta titles and descriptions
- Add Google Maps embed
- Add WhatsApp click-to-chat
- Connect Google Analytics (optional)

---

## Reporting Alignment (Contract-Friendly)
Development progress and usage can be reported as:
- Website deployment link
- Number of blog posts published
- Number of services/projects listed
- Number of inquiries received
- Screenshots and admin activity logs

---

## Scope Control (Important)
This project intentionally excludes:
- E-commerce checkout
- Payment processing
- Client dashboards
- Complex CMS features
- Custom backend workflows

Any expansion beyond this scope should be handled as a separate agreement.

---

## Future Enhancements (Optional)
- Search and filtering
- Testimonials module
- FAQ module
- Multi-language support
- Newsletter signup
- Google Ads landing pages

---

## Maintainer Notes
- Keep the system simple
- Avoid unnecessary plugins
- Focus on visibility and conversion
- Document all changes clearly
- Protect source code ownership unless otherwise agreed

---

## License / Usage
This project is developed as part of a marketing services engagement and is intended for corporate visibility purposes only.
