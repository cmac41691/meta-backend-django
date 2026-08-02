# Django Environment Setup Reflection

**Date:** 2026-08-02

## Objective

Set up my spare development laptop so it matches my primary backend development environment for the Meta Django course.

---

## What I Completed

- Opened the cloned `meta-backend-django` repository.
- Installed the VS Code extensions I use for backend development:
  - Python
  - Python Debugger
  - Pylance
  - Django
  - Markdown All in One
  - Error Lens
- Verified Python using the Windows Python Launcher (`py`).
- Updated `pip` to the latest version.
- Installed Django 6.0.7.
- Verified the Django installation.
- Pulled the latest repository changes from GitHub.
- Confirmed both laptops are synchronized for future development.

---

## Commands Practiced

```bash
git pull origin main

py --version
py -m pip --version
py -m pip install --upgrade pip
py -m pip install django
py -m django --version
py -m pip list
```

---

## What I Learned

This laptop uses the Windows Python Launcher (`py`), so Python packages are managed with commands such as:

```bash
py -m pip install django
```

instead of:

```bash
pip install django
```

I also reinforced that GitHub acts as the central source for my repositories. After pushing changes from my primary laptop, running:

```bash
git pull origin main
```

downloads only the missing commits and updates the local repository on this machine.

---

## Backend Connection

Development Machine

↓

Python Environment

↓

Django Framework

↓

Application Code

↓

Database

↓

Response

---

## Reflection

Setting up my spare laptop helped reinforce that backend development starts with a reliable development environment.

Both machines now share the same Git repository, Python installation, Django installation, and VS Code extensions, allowing me to switch between computers while keeping my workflow consistent.

This setup also gave me additional Git practice by synchronizing repositories between two development environments.

**Workflow to remember:**

```text
Pull → Work → Test → Commit → Push
```
