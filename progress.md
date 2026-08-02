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