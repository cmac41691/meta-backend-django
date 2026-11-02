# Database Configuration in Django

## Overview

Django supports several relational database management systems (RDBMS), including:

- SQLite
- MySQL
- PostgreSQL
- MariaDB (through Django's MySQL backend)
- Oracle

Database configuration allows Django to establish a connection between the application and its database.

## SQLite

SQLite is a lightweight relational database that requires minimal configuration.

**Advantages:**
- Easy to set up and use.
- Does not require a separate database server.
- Suitable for small projects, learning, and rapid prototyping.
- Stores data in a local database file.

SQLite is Django's default database when creating a new project.

## MySQL and PostgreSQL

MySQL and PostgreSQL are widely used relational database management systems.

Unlike SQLite, they typically operate through dedicated database servers.

Both support:
- SQL queries.
- Relational tables.
- Primary and foreign keys.
- Data integrity constraints.
- Transactions.
- Concurrent database connections.

These databases are commonly used in production backend applications.

## Configuring MySQL in Django

Django database connections are configured through the `DATABASES` dictionary inside `settings.py`.

Example:

```python
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'feedback',
        'USER': 'django_user',
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Configuration Parameters

| Parameter | Description |
|-----------|-------------|
| ENGINE | Specifies the database backend Django uses. |
| NAME | Name of the database Django connects to. |
| USER | Database account used for authentication. |
| PASSWORD | Password associated with the database user. |
| HOST | Address of the database server. |
| PORT | Port used by the database server. |

**Note:** MySQL commonly uses port `3306`.

The address `127.0.0.1` refers to the local machine.

Django's development server commonly runs on port `8000`, which is separate from the MySQL database port.

## Python Database Drivers

Django requires a compatible database driver to communicate with MySQL.

Example:

```bash
python -m pip install mysqlclient
```

The `mysqlclient` package provides a MySQL database adapter for Python.

### Backend Connection Flow

```text
Django Application
       |
       v
Django ORM
       |
       v
Database Backend
       |
       v
MySQL Driver (mysqlclient)
       |
       v
MySQL Server
       |
       v
Relational Database
```

The Django ORM allows Python code to interact with database tables through model objects.

## Database Migrations

Django uses migrations to manage changes to database schemas.

Apply migrations:

```bash
python manage.py migrate
```

View migration status:

```bash
python manage.py showmigrations
```

A completed migration is marked with `[X]`.

Migrations allow Django to create and update database structures according to its migration files.

## Security Considerations

Database credentials should not be hardcoded into source files committed to GitHub.

Environment variables can be used to supply sensitive configuration values.

Example:

```python
'PASSWORD': os.environ.get('MYSQL_PASSWORD')
```

Using a dedicated database account instead of the MySQL root account also helps separate application access from database administration.

## Practical Exercise — Django and MySQL

**Project:** `mysqlproject`

**Database:** `feedback`

**Database user:** `django_user`

During the exercise, I:

1. Configured a MySQL database connection in Django.
2. Created and configured a dedicated MySQL user.
3. Troubleshot database authentication errors.
4. Used an environment variable for the database password.
5. Successfully connected Django to MySQL.
6. Applied Django migrations.
7. Verified the migration status.

## Key Takeaways

- SQLite is useful for lightweight development and rapid prototyping.
- MySQL and PostgreSQL provide dedicated relational database server capabilities.
- Django database connections are configured in `settings.py`.
- Database drivers allow Python applications to communicate with database systems.
- The Django ORM provides an abstraction for interacting with relational data.
- Migrations manage database schema changes.
- Database credentials should be handled securely.

**Backend Architecture:**

Client → Request → Django Application → ORM → Database → Response