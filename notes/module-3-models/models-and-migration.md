# Django Models, Migrations & ORM — TL;DR

**Review Date:** 2026-09-18

## Core Backend Flow

Application
    ↓
Django Model
    ↓
ORM
    ↓
Migration
    ↓
Database Table

A Django model is a Python class that represents database data.

Think of it as:

Model class → Database table  
Model field → Database column  
Model object → Database row  
Object attribute → Stored value

---

## 1. Django Models

Models are defined in `models.py`.

Example:

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)

Database thinking:

Product → table  
name → text column  
price → decimal column  
stock → integer column  
available → boolean column

Common fields:

CharField() → short text  
TextField() → large text  
IntegerField() → whole number  
DecimalField() → decimal / money  
DateTimeField() → date + time  
BooleanField() → True / False

---

## 2. Model Relationships

Django models can represent relationships between database tables.

### One-to-One

One object ↔ one object

Example:

College ↔ Principal

Django:

models.OneToOneField()

---

### One-to-Many

One object → many related objects.

Example:

Category → many Drinks

The ForeignKey is stored on the "many" side.

Django:

models.ForeignKey()

Example:

class Category(models.Model):
    name = models.CharField(max_length=200)


class Drink(models.Model):
    name = models.CharField(max_length=200)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

Database idea:

Category
    ↓
Drink
Drink
Drink

The foreign key connects the Drink table to the Category table without duplicating the category data.

---

### Many-to-Many

Many objects ↔ many objects

Example:

Teachers ↔ Subjects

Django:

models.ManyToManyField()

Django/database creates an intermediate junction table to connect the records.

---

## 3. Primary Keys & Foreign Keys

Primary Key (PK):

Uniquely identifies a database record.

Example:

id = 1

Foreign Key (FK):

Connects one table/model to another.

Example:

Drink.category → Category.id

Quick memory:

One ↔ One = OneToOneField()

One → Many = ForeignKey()

Many ↔ Many = ManyToManyField()

---

## 4. `on_delete`

A ForeignKey needs instructions for what should happen when the referenced object is deleted.

Example:

category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE
)

`CASCADE` means deleting the parent can also delete its related child records.

Other `on_delete` behaviours can be used depending on the application's requirements.

---

## 5. Migrations

A migration is Django's way of applying model/schema changes to the database.

Workflow:

models.py changed
    ↓
makemigrations
    ↓
migration file created
    ↓
migrate
    ↓
database schema updated

Commands:

py manage.py makemigrations

py manage.py migrate

Useful check:

py manage.py showmigrations

Important distinction:

makemigrations = CREATE the instructions

migrate = APPLY the instructions

Do not normally edit the database schema manually when Django models and migrations should manage it.

---

## 6. Migration History

Migrations create a reproducible history of database schema changes.

Example:

0001 → create Product table

0002 → add price field

0003 → add available field

Each migration builds on previous migrations.

Mental model:

Git history = code/project timeline

Migration history = database schema timeline

This helps with:

- synchronization
- version control
- maintenance
- reproducible database changes

---

## 7. Django ORM

ORM = Object-Relational Mapping.

The ORM is the bridge between Python/Django objects and the relational database.

Python/Django
    ↓
ORM
    ↓
SQL
    ↓
Database

Instead of manually writing SQL for normal operations, Django lets us interact with database records through Python objects.

---

## 8. CRUD with Django ORM

CRUD:

Create  
Read  
Update  
Delete

### CREATE

category = Category(name="coffee")
category.save()

Conceptually:

Python object
    ↓
ORM
    ↓
INSERT
    ↓
Database row

---

### READ ONE

category = Category.objects.get(pk=1)

Conceptually similar to selecting one matching database record.

---

### READ ALL

categories = Category.objects.all()

Conceptually:

SELECT * FROM category;

---

### FILTER

categories = Category.objects.filter(name="coffee")

Returns records matching the condition.

---

### UPDATE

category = Category.objects.get(pk=1)

category.name = "tea"

category.save()

Flow:

Retrieve object
    ↓
change attribute
    ↓
save()
    ↓
database updated

---

### DELETE

category = Category.objects.get(pk=1)

category.delete()

The ORM translates the operation into the required database action.

---

## 9. Creating Related Objects

First retrieve the related object:

category = Category.objects.get(pk=1)

Then create another object that references it:

drink = Drink(
    name="mocha",
    category=category
)

drink.save()

Relationship:

Category object
    ↓
ForeignKey
    ↓
Drink object

Database:

Category table
    ↓
category_id
    ↓
Drink table

---

## 10. Full Mental Model

Django code:

Python Model
    ↓
Django ORM
    ↓
Migration
    ↓
SQL Database Schema

Runtime database operations:

Client Request
    ↓
Django Application Logic
    ↓
Model / ORM
    ↓
Database
    ↓
ORM converts results to Python objects
    ↓
Application Response

---

## TL;DR

MODEL
Python representation of database data.

MODEL CLASS
Usually represents a database table.

MODEL FIELD
Usually represents a database column.

MODEL OBJECT
Usually represents a database row.

FOREIGN KEY
Connects related models/tables.

ORM
Lets Python code interact with relational database data.

MAKEMIGRATIONS
Creates migration instructions from model changes.

MIGRATE
Applies migration instructions to the database.

CRUD
Create → Read → Update → Delete

Core workflow:

Change Model
    ↓
py manage.py makemigrations
    ↓
py manage.py migrate
    ↓
Database Updated

Core idea:

Python/Django
    ↕
Models + ORM
    ↕
Relational Database