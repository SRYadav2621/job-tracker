# JobTrack — Job Application Tracker

A beginner-friendly Django project for tracking job applications. It includes login, a personal dashboard, CRUD operations, search, status filtering, summary counts, and a responsive interface.

## Features
- Login/logout using Django authentication
- Each user can only see and manage their own applications
- Create, view, edit, and delete job applications
- Search by company, role, or notes
- Filter by status: Applied, Assessment, Interview, Offer, Rejected
- Dashboard summary cards
- Optional MySQL configuration; SQLite works out of the box
- Django admin for reviewing records

## 1. Setup (Windows)
Open a terminal in this folder and run:

```bash
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations applications
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` and log in using the superuser you created. For local development, that account can manage applications. Add normal-user registration as a future enhancement.

If `mysqlclient` fails to install on your machine, install Django first with `pip install Django python-dotenv`, and use SQLite while practising. `mysqlclient` is only required for MySQL mode.

## 2. Optional MySQL setup
Create a database in MySQL:

```sql
CREATE DATABASE job_tracker CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

In Windows PowerShell, set these environment variables before running Django:

```powershell
$env:DB_ENGINE="mysql"
$env:DB_NAME="job_tracker"
$env:DB_USER="root"
$env:DB_PASSWORD="your_mysql_password"
$env:DB_HOST="127.0.0.1"
$env:DB_PORT="3306"
python manage.py migrate
python manage.py runserver
```

Do not commit real passwords or production secret keys to GitHub.

## Main files
- `applications/models.py` — database model
- `applications/forms.py` — form validation and fields
- `applications/views.py` — dashboard, search, CRUD logic
- `applications/urls.py` — app routes
- `applications/templates/` — HTML templates
- `applications/static/applications/styles.css` — responsive UI
- `jobtracker/settings.py` — project configuration and database settings

## Resume description (use after you have run and understood the project)
**JobTrack — Job Application Tracker | Python, Django, SQLite/MySQL, HTML, CSS**
- Built a Django web application to manage job applications with secure login and user-specific records.
- Implemented CRUD operations, search, status filters, and dashboard metrics for application progress.
- Designed a responsive interface and configured database support for SQLite and MySQL.

## Good next improvements
1. Add user registration and password reset.
2. Add pagination to the dashboard.
3. Add CSV export.
4. Add a REST API using Django REST Framework.
5. Add automated tests for model, views, permissions, and search.
6. Push the finished project to GitHub with screenshots and setup instructions.
