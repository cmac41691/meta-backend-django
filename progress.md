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

## 2026-09-08

### Django Web Framework — Module 3: Models and Migrations

- Began working with Django models and migrations locally.
- Created the `Drinks` model with `drink_name` and `price` fields.
- Registered the `Drinks` model with Django Admin.
- Troubleshot why Django was not detecting changes and found that `myapp` needed to be added to `INSTALLED_APPS`.
- Fixed the model inheritance from `models` to `models.Model`.
- Successfully ran `makemigrations` and generated `0001_initial.py`.
- Successfully applied the migration to the SQLite database.
- Compared the local migration workflow with the Coursera browser environment.
- Learned that Django detects model changes by comparing the current model state against existing migration history.

## 2026-09-12

### Django Web Framework — Module 3: Models

- Completed the Models and Migrations self-review: 100%.
- Completed Models using Foreign Keys.
- Practiced identifying one-to-many relationships between Django models.
- Connected Django `ForeignKey()` syntax to primary key / foreign key relationships from SQL.
- Bypassed the duplicate browser-based Models and Migrations lab after completing the same migration workflow locally.
- Reinforced the workflow: Model change → `makemigrations` → migration file → `migrate` → database. 

## 2026-09-13

### Django Web Framework — Module 3: Models using Foreign Keys

- Completed the Models using Foreign Keys exercise locally.
- Created the `DrinksCategory` model and connected it to the `Drinks` model using `ForeignKey`.
- Used `models.PROTECT` and `default=None` with the foreign key.
- Registered both models with Django Admin.
- Ran `makemigrations` and generated the new migration for `DrinksCategory` and the foreign key relationship.
- Successfully applied the migration to SQLite.
- Used the Django shell to import the models, create a `DrinksCategory` object, and save it to the database.
- Debugged an import error caused by a model-name mismatch (`DrinkCategory` vs `DrinksCategory`).
- Completed the Models using Foreign Keys self-review:
  - Attempt 1: 66.66%
  - Attempt 2: 66.66%
  - Attempt 3: 100%
- Reinforced the relationship:

  Model → ForeignKey → Migration → Database → ORM/Django Shell

## 2026-09-17

### Models & Migrations — Knowledge Check

- Completed the Models & Migrations knowledge check.
- Attempt 1: 20%
- Attempt 2: 40%
- Attempt 3: 60%
- Attempt 4: 80% — Passed
- Reinforced understanding of Django models, migrations, ORM, and model relationships.
- Improved through reviewing incorrect answers and retrying until reaching the passing grade.

## 2026-10-12

### Django Web Framework — Module 3: Working with Forms

- Continued the Working with Forms exercise in the Meta Back-End Developer Certificate.
- Created the `Booking` model and corrected errors identified through Django tracebacks.
- Generated and applied migration `0003_booking`.
- Created `BookingForm` using Django's `ModelForm`.
- Connected `views.py`, `urls.py`, and `booking.html`.
- Implemented a booking form using HTML, Django template syntax, and CSRF protection.
- Successfully ran the Django development server and accessed `/booking/`.
- Submitted test reservations using POST and verified the records in SQLite Viewer.
- Tested required fields, single-character names, browser refreshes, and negative guest counts.
- Identified two issues: negative guest counts being accepted and duplicate records from repeated submissions.
- Reinforced understanding of the workflow:

  **Browser → URL → View → Form → Model → SQLite Database**

**Status:** Working Forms exercise implemented and tested locally.

**Next session — 2026-10-13:**
- Compare my implementation with Meta's provided solution.
- Review differences and document corrections.
- Investigate model validation and duplicate-submission prevention.

## 2026-10-14

### Django Web Framework — Module 3: Working with Forms

- Completed the **Self Review: Working with Forms** practice assignment.
- Achieved a final grade of **100%**, after multiple attempts.
- Reviewed incorrect answers and repeated the assessment to reinforce understanding.
- Reinforced knowledge of Django forms, `ModelForm`, model integration, and form handling.
- Connected the assessment concepts to the booking form implemented and tested locally on 2026-10-12.
- 

**Status:** Self-review completed — 100%.

**Next:** Continue with the *Knowledge Check: Model and Forms* and review any remaining Module 3 material.

## 2026-10-15

### Django Web Framework — Module 3: Knowledge Check — Model and Forms

- Completed the **Knowledge Check: Model and Forms**.
- Attempt 1: **40%**
- Attempt 2: **100% — Passed**
- Reviewed incorrect answers and reinforced understanding of Django models and forms.
- Connected the knowledge check to the practical `Booking` model and `BookingForm` exercise completed on 2026-10-12.

**Status:** Knowledge check completed — 100%.

**Next:** Continue with the remaining Django Web Framework course material.

## 2026-10-17

### Django Web Framework — Module 3: Models and Forms

- Completed the Models and Forms subsection.
- Consolidated six pages of handwritten notes into `notes/module-3-models/models-and-forms.md`.
- Reviewed Django forms, field types, validation, `cleaned_data`, and `ModelForm`.
- Reinforced understanding of models, migrations, ORM, and database relationships.
- Connected the concepts to the completed Booking Form exercise.
- Documented practical lessons involving validation, negative guest counts, and duplicate submissions.
- Created a permanent Markdown reference for future backend projects.

**Status:** Models and Forms subsection completed.

**Next:** Continue with Django Admin.

### 2026-10-24 — Django Admin Lab

**Course:** Django Web Framework  
**Module:** Models and Forms — Django Admin  
**Session:** 7:30 AM – 10:30 AM (3 hours)

**Completed:**
- Completed the Using Django Admin exercise.
- Created the `Employees` model and database migration.
- Registered the model in Django Admin.
- Created the `jason_chef` user and assigned permissions.
- Reviewed and updated `.gitignore` to exclude local database and environment files.
- Committed and pushed changes to GitHub (`f2bba24`).
- Verified a clean Git working tree.

**Reflection:**

Gained a better understanding of how Django Admin manages models, users, and permissions. Practiced protecting local files through `.gitignore` and reviewing changes before committing.

### 2026-10-25 — Django Admin: Self-Review and Knowledge Check

**Course:** Django Web Framework  
**Module:** Models and Forms — Django Admin

**Completed:**
- Completed Self-Review: Using Django Admin.
  - Attempt 1: 33.33%
  - Attempt 2: 66.66%
  - Attempt 3: 100%
- Completed Knowledge Check: Admin.
  - Attempt 1: 80%
- Reviewed the official Django Admin lab solution and compared it against my implementation from October 24.

**Reflection:**

Improved my understanding of Django Admin, model registration, user management, and permissions. The self-review required multiple attempts, but each attempt helped reinforce the concepts. Achieved 80% on the knowledge check on the first attempt.

**Next:** Continue into the next section of the Django Web Framework course.

## 2026-10-27 — Django Database Configuration: MySQL Setup

**Course:** Meta Back-End Developer Professional Certificate  
**Module:** Django Web Framework — Module 3  
**Section:** Database Configuration

### Completed
- Installed and configured MySQL Server 8.0.46.
- Connected successfully to the local MySQL server using MySQL Workbench.
- Verified the server version using `SELECT VERSION();`.
- Created a new database named `mydatabase`.
- Confirmed the database exists using `SHOW DATABASES;`.
- Activated the Django project's Python virtual environment.
- Verified that pip uses the correct virtual environment.
- Successfully installed `mysqlclient` 2.3.0.
- Located the `DATABASES` dictionary in Django's `settings.py`.
- Confirmed that `.gitignore` excludes `.env` files and the virtual environment.
- Reviewed the Meta course reading on configuring a MySQL connection.

### Technical Understanding

MySQL is a separate database server, unlike SQLite, which stores data in a local database file.

Django communicates with MySQL through a database driver:

**Django → mysqlclient → MySQL Server → Database**

The `DATABASES` dictionary in `settings.py` determines which database Django connects to.

### Current Status

MySQL is installed and the database has been created successfully.

Django is still configured to use SQLite. The MySQL connection and migrations have not yet been completed.

### Next Session — 2026-10-28

- Watch *Setting up a MySQL connection*.
- Prepare the MySQL connection configuration in Django.
- Keep database credentials out of GitHub.
- Begin *Exercise: Connecting to a Database*.
- Test the connection before running migrations.

### Reflection

Today I moved beyond working with SQLite and began setting up a separate relational database server for Django.

I successfully configured MySQL, created a database, and installed the Python driver. This helps me understand how backend applications communicate with database servers.

**Progress:** MySQL environment ready; Django connection pending.

### 2026-10-31 — Django Database Configuration

**Status:** Completed

**Accomplishments:**
- Resolved MySQL Error 1045 (authentication failure).
- Successfully authenticated using `django_user`.
- Verified access to the `feedback` database.
- Connected Django to MySQL using environment-based credentials.
- Executed `python manage.py migrate` successfully.
- Verified applied migrations using `python manage.py showmigrations`.

**Key Takeaways:**
- Understood how Django connects to a MySQL database.
- Learned the difference between SQL syntax errors and authentication errors.
- Gained hands-on experience troubleshooting database connections.
- Observed how Django migrations create and manage database structures.

**Reflection:**
Successfully configured Django to communicate with MySQL after troubleshooting authentication issues. This exercise strengthened my understanding of backend architecture, database persistence, and framework configuration.

**Next Step:** Continue to the next Meta Django lesson or exercise.