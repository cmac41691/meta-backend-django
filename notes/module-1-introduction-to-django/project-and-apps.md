# Projects and Apps

**Date:** 2026-08-03

---

# Project Structure

Create a new Django project.

```bash
django-admin startproject <project_name>
```

Creates:

- manage.py
- settings.py
- urls.py
- asgi.py
- wsgi.py
- __init__.py

---

# Create an App

```bash
python manage.py startapp <app_name>
```

---

# Run the Development Server

```bash
python manage.py runserver
```

Default local address:

```
http://127.0.0.1:8000/
```

Flow:

```
Browser
    ↓
runserver
    ↓
Django Project
```

---

# Create Migration Files

```bash
python manage.py makemigrations
```

Flow:

```
Model Changes
      ↓
Migration Files
```

---

# Apply Migrations

```bash
python manage.py migrate
```

Flow:

```
Migration Files
      ↓
SQLite Database Updated
```

---

# Open Django Shell

```bash
python manage.py shell
```

Interactive Python shell inside the project.

---

# Request Flow

```
User
  ↓
Django
  ↓
URL
  ↓
View
  ↓
Model
  ↓
Database
```

---

# Core Project Files

| File | Purpose |
|------|---------|
| manage.py | Command-line utility for the project |
| settings.py | Project configuration |
| urls.py | Routes requests to views |
| __init__.py | Marks the directory as a Python package |
| asgi.py | ASGI server entry point |
| wsgi.py | WSGI server entry point |

---

# Key Takeaways

- A **project** contains the overall configuration.
- An **app** contains a specific feature or functionality.
- `manage.py` is used for most development commands.
- Django generates much of the project structure automatically.
- Migrations synchronize Python models with the database.