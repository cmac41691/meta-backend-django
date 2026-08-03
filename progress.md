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