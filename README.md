# Amir Karimov — Developer Portfolio

A professional, modern portfolio website built with **Django** (backend) and **Bootstrap 5** (frontend).

---

## ✨ Features

- **Full single-page portfolio** with Hero, About, Projects, Experience, and Contact sections
- **Dark / Light mode** toggle with localStorage persistence
- **Typing animation** in the hero section cycling through role titles
- **Scroll-triggered animations** via AOS (Animate On Scroll)
- **Project filtering** by technology stack (client-side, no page reload)
- **Skill progress bars** that animate on scroll into view
- **AJAX contact form** with Django backend persistence (no page reload)
- **Sticky navbar** that applies a blur/glass effect on scroll
- **Django Admin** panel to manage Projects, Experiences, and Contact Messages
- **Seed data command** to pre-populate example content instantly
- Fully **responsive** across mobile, tablet, and desktop

---

## 🗂️ Project Structure

```
portfolio_project/
├── manage.py
├── requirements.txt
├── db.sqlite3                   # Created after migrations
│
├── portfolio_site/              # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── portfolio/                   # Main Django app
    ├── models.py                # Project, Experience, ContactMessage
    ├── views.py                 # index view (GET + POST)
    ├── admin.py                 # Admin panel registrations
    ├── urls.py
    ├── management/
    │   └── commands/
    │       └── seed_data.py     # python manage.py seed_data
    ├── templates/
    │   └── portfolio/
    │       └── index.html       # Full portfolio template
    └── static/
        └── portfolio/
            ├── css/
            │   └── style.css    # Custom styles
            └── js/
                └── main.js      # All JavaScript functionality
```

---

## ⚙️ Setup & Installation

### 1. Clone or unzip the project

```bash
cd portfolio_project
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 6. Populate with sample data

```bash
python manage.py seed_data
```

This creates 6 sample projects and 3 work experiences.

### 7. Run the development server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** to view the portfolio.  
Visit **http://127.0.0.1:8000/admin** to manage content.

---

## 🎨 Customization

### Personal Information

Open `portfolio/templates/portfolio/index.html` and update:

- Your **name** (replace "Amir Karimov")
- Your **title** (the typing animation cycles through titles in `main.js`)
- Your **bio** in the About section
- Your **social media links** (GitHub, LinkedIn, Telegram)
- Your **email** address in the Contact section

### Typing Animation Titles

In `portfolio/static/portfolio/js/main.js`, find the `titles` array and edit:

```javascript
const titles = [
    'Python Backend Developer',
    'Django & FastAPI Expert',
    'Cloud-Native Architect',
    'API Design Specialist',
];
```

### Profile Photo

Replace the avatar placeholder with your actual photo by editing the `hero-avatar` div in `index.html`:

```html
<div class="hero-avatar">
    <img src="{% static 'portfolio/images/profile.jpg' %}" alt="Your Name">
</div>
```

Then place your photo at `portfolio/static/portfolio/images/profile.jpg`.

### Color Palette

All colors are CSS custom properties in `style.css`. The primary accent color is `--sky` (`#38bdf8`). Change `--sky-dark` and `--sky-deeper` to use a different brand color throughout.

---

## 🗄️ Django Models

### `Project`
| Field | Type | Description |
|-------|------|-------------|
| title | CharField | Project name |
| description | TextField | Full project description |
| tech_stack | JSONField | List of technology strings |
| github_url | URLField | GitHub repository link |
| live_url | URLField | Live demo URL (optional) |
| is_featured | BooleanField | Highlight in the grid |
| order | IntegerField | Display order |

### `Experience`
| Field | Type | Description |
|-------|------|-------------|
| title | CharField | Job title |
| company | CharField | Company name |
| location | CharField | City / country |
| start_date | DateField | Start date |
| end_date | DateField | End date (null if current) |
| is_current | BooleanField | Mark as current role |
| description | TextField | Responsibilities |
| tech_used | JSONField | Technologies used |

### `ContactMessage`
| Field | Type | Description |
|-------|------|-------------|
| name | CharField | Sender's name |
| email | EmailField | Sender's email |
| subject | CharField | Message subject |
| message | TextField | Message body |
| is_read | BooleanField | Read status in admin |

---

## 📦 Production Deployment Notes

For production deployment (e.g., on a VPS with Nginx + Gunicorn):

1. Set `DEBUG = False` in `settings.py`
2. Set `ALLOWED_HOSTS` to your domain
3. Change `SECRET_KEY` to a strong, randomly generated value
4. Run `python manage.py collectstatic`
5. Configure `EMAIL_BACKEND` to use SMTP for real email delivery
6. Use `gunicorn portfolio_site.wsgi` as the application server

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 4.2 |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Frontend | Bootstrap 5, Custom CSS |
| Fonts | DM Serif Display + DM Sans (Google Fonts) |
| Icons | Bootstrap Icons |
| Animations | AOS (Animate On Scroll) |
| JavaScript | Vanilla JS (ES6+) |

---

© 2024 Amir Karimov. All rights reserved.
