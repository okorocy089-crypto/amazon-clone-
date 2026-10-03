Amazon Clone

A full-stack e-commerce site inspired by Amazon, built from scratch with Django and vanilla HTML/CSS/JS. Designed from hand-drawn wireframes and a written spec, covering the full shopping flow from browsing to checkout.
![Status](https://img.shields.io/badge/status-in%20progress-yellow)

Features:

Authentication — registration, login, logout, and a security-question-based password reset flow (no email verification service required)

Product catalog — categories, product listings, and a detail page, with stock (`quantity`) that auto-removes a product when it hits zero

Cart — supports both guest sessions and logged-in users, with cart merging on login/registration; add, increase, decrease, and remove items via AJAX with no page reloads

Checkout — an atomic, branching flow: prompts registration if you're not logged in, prompts for a payment card if none is on file, then generates a receipt and decrements stock

Payment cards — add/update a card on file (mocked — no real payment processor)

Order history — past orders grouped by date, with a one-time post-checkout receipt view

Search — live autocomplete suggestions plus a full results page

Homepage — a rotating hero slider, curated category rails, and a "Checkout our other stuff" tile grid

Account management — account deletion with a confirmation step

Responsive UI touches — a slide-in sidebar menu, password visibility toggle, live cart-count badge, and an Amazon-styled header/footer


Tech stack:

Backend: Django (Python), SQLite

Frontend: HTML, CSS, and vanilla JavaScript (AJAX for cart interactions, no frontend framework)

Image handling: Pillow

Project structure


The project is split into four Django apps, each with its own models and templates:

App	Responsibility:

`accounts`	Custom user model, registration/login, security Q&A, payment cards

`catalog`	Categories and products

`cart`	Cart and cart items (guest + authenticated)

`orders`	Orders and order line items (with price/name snapshotting)

All models use UUID primary keys. Templates follow Django's namespaced convention, e.g. `catalog/templates/catalog/`.

GETTING STARTED

Clone the repo
```bash
   git clone https://github.com/okorocy089-crypto/amazon-clone-
   cd amazon
   ```
Create and activate a virtual environment
```bash
   python -m venv .env
   source .env/bin/activate      # macOS/Linux
   .env/Scripts/activate         # Windows
   ```
Install dependencies
```bash
   pip install -r requirements.txt
   ```
Apply migrations
```bash
   python manage.py migrate
   ```
(Optional) Seed sample products
```bash
   python manage.py makemigrations catalog
   python seed_products.py
   ```
Run the dev server
```bash
   python manage.py runserver
   ```
Visit `http://127.0.0.1:8000/`.
> *Note:* keep `DEBUG = True` in `settings.py` for local development — Django only auto-serves static files (CSS/JS/images) via the dev server when `DEBUG` is on. Deployment settings (`DEBUG = False`, `STATIC_ROOT`, `ALLOWED_HOSTS`) are for production only and will break local static file loading if left on.
Known limitations / roadmap

> Payment card numbers and CVVs are currently stored unencrypted (Fernet encryption planned)

> Security question answers are stored in plain text

> No real payment processor — checkout is fully mocked

> Styling polish pass still in progress
