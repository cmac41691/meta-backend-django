# Progress Log

## 2026-07-31

- Created repository
- Installed Django 6.0.7
- Set up repository structure
- Prepared for Module 1 of the Meta Django course
  
 ## 2026-08-01

- Completed Django course introduction.
- Reviewed development environment requirements.
- Configured VS Code for Django development.
- Installed Python, Pylance, Python Debugger, Django, SQLite Viewer, Markdown All in One, and Error Lens extensions.
- Prepared repository structure for notes, exercises, projects, and reflections.
- Ready to begin creating the first Django project.

  ## 2026-08-02

### Django Web Framework

Completed the Django environment setup and introductory course readings.

### Progress

- Completed:
  - Working with virtual environments on your local machine
  - Working with labs in this course
  - Additional resources

### Local Development Environment

- Created my first Django virtual environment (`env`).
- Activated the virtual environment using Git Bash.
- Explored the virtual environment directory structure (`Lib`, `Scripts`, `pyvenv.cfg`).
- Verified the active Python interpreter and `pip` location.
- Installed Django inside the virtual environment.
- Updated `pip` to the latest version.
- Verified the installation using:
  - `django-admin --version`
  - `pip list`
  - `pip show django`

### Commands Practiced

```bash
py -m venv env
source env/Scripts/activate
python --version
pip --version
which pip
which python
pip list
pip show django
django-admin --version
python -m site
python -c "import sys; print(sys.executable)"
```

### Reflection

Today's goal was not to build a Django application but to understand the development environment that Django runs inside.

Rather than simply installing Django, I explored how the virtual environment works, where Python and pip are located, how packages are isolated from the global installation, and how to verify that the correct interpreter is being used.

This gives me a stronger foundation before beginning Django projects and applications in the next section of the course.

## 2026-08-03

### Meta Django Web Framework
Module 1 – Projects and Apps

Completed:
- Projects and Apps Overview
- Project Structure
- Creating Your First Project
- Knowledge Check: Projects and Apps

Notes:
- Learned the difference between a Django project and a Django app.
- Learned the purpose of core project files:
  - manage.py
  - settings.py
  - urls.py
  - __init__.py
  - asgi.py
  - wsgi.py
- Learned common Django management commands:
  - django-admin startproject
  - python manage.py startapp
  - python manage.py runserver
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py shell
- Continued building handwritten architecture diagrams and command references.

Knowledge Check:
- Attempt 1: 20%
- Attempt 2: 80% (Pass)

Reflection:
Today's focus was understanding how Django organizes projects and apps rather than writing application code. I spent time understanding the purpose of the project structure and how the management commands fit into the backend development workflow. My handwritten notes and diagrams continue to help connect the commands to the overall request → application → database flow.

# Progress Log — 2026-08-07

## Meta Back-End Developer Professional Certificate
**Course:** Django Web Framework

### Completed

- Created my first Django project using:
  - `py -m django startproject myproject`
- Explored the generated project structure.
- Identified the purpose of the core project files:
  - `manage.py`
  - `settings.py`
  - `urls.py`
  - `asgi.py`
  - `wsgi.py`
  - `__init__.py`
- Created my first Django application:
  - `py manage.py startapp myapp`
- Examined the automatically generated app files:
  - `admin.py`
  - `apps.py`
  - `models.py`
  - `views.py`
  - `tests.py`
  - `migrations/`
- Verified the project with:
  - `py manage.py check`
- Started the local development server:
  - `py manage.py runserver`
- Successfully opened the Django welcome page at:
  - `http://127.0.0.1:8000/`
- Successfully accessed the Django Admin login page.
- Learned that Django ships with many built-in features ("batteries included"), including the Admin interface, authentication, sessions, and migrations.
- Reviewed the distinction between a **Django project** and a **Django app**.
- Confirmed the generated project files were correctly staged in Git while leaving the SQLite database untracked.

### Assessment

- Completed the "Creating your first project and app" lab locally.
- Passed the Coursera self-review on the **first attempt** with a **100%** score.

### Key Takeaways

- A **project** manages the overall Django configuration.
- An **app** contains a specific feature or piece of functionality.
- Django generates a large amount of project structure automatically.
- `manage.py` is the primary command-line tool used during development.
- The development server makes it easy to test changes locally before deployment.
- The Admin interface is available immediately after project creation, demonstrating Django's "batteries included" philosophy.
  
  ## 2026-08-08 — Django Applications and MVT

- Continued Module 1: Introduction to Django.
- Reviewed Django project and application structure.
- Reinforced the difference between `django-admin` and `manage.py`.
- Reviewed common Django management commands.
- Completed the discussion on challenges encountered while creating a first Django app.
- Completed the **Knowledge Check: Applications**.
  - Attempt 1: 20%
  - Attempt 2: 40%
  - Attempt 3: 60%
  - Attempt 4: 80% — Passed
- Continued into **Web Frameworks and MVT**.
- Reviewed what a web framework provides and how Django organizes backend applications.
- Studied Django's Model-View-Template (MVT) architecture.
- Connected MVT to the backend request/response lifecycle.
- Completed the **Knowledge Check: Web Frameworks and MVT**.
  - Attempt 1: 40%
  - Attempt 2: 40%
  - Attempt 3: 100% — Passed

### Backend Connection

`Client → Request → URL Routing → View → Model → Database → Template/Response → Client`

### Reflection

Today reinforced how Django organizes a backend application rather than just how to create its files. The Applications knowledge check took four attempts, improving from 20% to 80%. The Web Frameworks and MVT knowledge check took three attempts, going from 40% to 40% and then 100%. Reviewing the mistakes between attempts helped reinforce the distinction between Django's project structure, applications, and MVT architecture.

Next session: continue Module 1 on 2026-08-09.

## 2026-08-09

### Module 1 — Introduction to Django

- Completed Web Frameworks and MVT notes.
- Reviewed Django's Model-View-Template architecture.
- Connected Django's request flow to:
  `Client → Request → URL Dispatcher → View → Model / Database → Template → Response`
- Completed the Module 1 graded quiz.
- Quiz progression:
  - Attempt 1: 60%
  - Attempt 2: 80% — Passed
- Completed Module 1: Introduction to Django.
- Next: Module 2 — Views. 

### Django Views and URL Configuration

- Started Module 2 — Views.
- Created a new Django project for view and URL routing practice.
- Created and configured the `myapp` Django application.
- Created a `home()` view using `HttpResponse`.
- Added HTML output for the Little Lemon test page.
- Created `myapp/urls.py` for application-level URL routing.
- Connected project-level URLs to application URLs using `include()`.
- Registered `myapp` in `INSTALLED_APPS`.
- Troubleshot a `ModuleNotFoundError` caused by the missing `myapp.urls` module.
- Successfully ran the Django development server.
- Verified the root request returned HTTP `200`.
- Successfully rendered `Welcome to Little Lemon!` in the browser.

### Backend Connection

`Client → Request → Project URLs → App URLs → View → HttpResponse → Client`

### Reflection

This exercise helped reinforce that creating a Django view is only one part of the request flow. The project URL configuration must route the request into the application's URL configuration, which then connects the URL to the correct view. Troubleshooting the missing `myapp.urls` file made the relationship between project-level routing, app-level routing, and views much clearer. 

## 2026-08-13

### Django Web Framework — Module 2

- Completed the Views section.
- Completed the Views knowledge check.
- First attempt: 20%
- Second attempt: 80% — Passed
- Reviewed how Django views receive requests and return responses.
- Reviewed how views connect to URL routing.
- Organized my Views notes in the Module 2 notes folder.
- Next: Begin the Requests and URLs section. 
## 2026-08-24

### Django Web Framework — Module 2

- Completed the Mapping URLs with Params exercise.
- Built and tested dynamic URL parameters using `<str:drink_name>`.
- Connected URL parameters to the `drinks` view and dictionary lookup.
- Tested `mocha`, `tea`, and `lemonade` successfully with HTTP 200 responses.
- Tested an invalid `water` parameter and observed the expected `KeyError`.
- Compared my implementation with the Meta solution.
- Completed the Mapping URLs with Params self-review.
- First attempt: 33%
- Second attempt: 66%
- Third attempt: 100% — Passed
- Next: Continue Django Web Framework Module 2 on 2026-08-25.

## 2026-08-26

### Django Web Framework — Module 2

- Completed the Requests and URLs knowledge check.
- First attempt: 0%.
- Second attempt: 80% — Passed.
- Reviewed HTTP requests, responses, URL routing, and parameters.
- Reinforced how Django connects URLs to views through the request/response flow.
- Next: Continue to the next section of Module 2.

## 2026-08-30

### Django Web Framework — Module 2

- Completed the Little Lemon URL mapping project.
- Connected the project-level `urls.py` to the `littlemon` app using `include()`.
- Created separate view functions for home, about, menu, and booking.
- Used `HttpResponse` to verify each view returned the expected response.
- Debugged URL routing, syntax, and view attribute errors.
- Tested `/about/`, `/menu/`, and `/booking/` successfully in the browser.
- Reinforced the Django request flow: URL request → project URLs → app URLs → view → response.
- Project completed and ready to commit.

## 2026-08-30

### Django Web Framework — Module 2

- Completed the Little Lemon URL mapping project.
- Connected project-level URLs to the `littlemon` app and tested the routes in the browser.
- Completed the Creating URLs and Mapping to Views self-review.
- First attempt: 33.33%.
- Second attempt: 66.66%.
- Third attempt: 100% — Passed.
- Completed the Error Handling lesson.
- Reinforced how project URLs, app URLs, views, requests, and responses work together.
- Noticed that debugging this project took days rather than weeks as the relationship between Django's moving parts is becoming easier to trace.
- Next: Continue Django Web Framework — Module 2.  

## 2026-09-04

### Django Web Framework — Module 2: Views

- Completed and organized notes for Creating URLs and Views.
- Completed the Handle Errors in Views knowledge check: 80% on the first attempt.
- Completed the Module 2 Views summary.
- Completed the Module 2 Views quiz.
- First attempt: 50%.
- Second attempt: 90% — Passed.
- Reinforced URL routing, views, error handling, URL namespacing, and class-based views.
- Completed Module 2: Views.
- Next: Begin Module 3.