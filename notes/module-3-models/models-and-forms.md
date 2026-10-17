# Django Web Framework — Models and Forms

**Course:** Meta Back-End Developer Professional Certificate  
**Module:** 3 — Models  
**Topic:** Models and Forms  
**Completed:** 2026-10-17  
**Status:** Completed

---

## 1. Introduction to Django Forms

Django forms are used to collect, validate, and process information submitted by users.

Common applications include:
- Login and authentication
- User registration
- Contact forms
- Reservations and bookings
- E-commerce transactions

### Backend Workflow

```text
User
  ↓
HTML Form
  ↓
HTTP Request
  ↓
Django View
  ↓
Form Validation
  ↓
Application Logic
  ↓
Model / Database
  ↓
HTTP Response
```

**Key Concept:**
- Form = Input and validation
- View = Processing and application logic
- Model = Data structure and database interaction
- Template = Presentation
- URL = Routing

Not every Django form needs to interact with a database.

---

## 2. GET and POST Requests

### GET Request

GET retrieves information from the server.

Example:

```python
if request.method == "GET":
    form = BookingForm()
```

The server returns an empty form for the user.

### POST Request

POST submits information to the server.

Example:

```python
if request.method == "POST":
    form = BookingForm(request.POST)
```

The submitted information is passed into the form for validation.

### Request Lifecycle

```text
GET Request
    ↓
Django View
    ↓
Create Empty Form
    ↓
Render HTML Template
    ↓
User Enters Information
    ↓
POST Request
    ↓
Django Validates Form
    ↓
Process Valid Data
    ↓
Return Response
```

**Important:** HTTP 200 means the server successfully returned a response. It does not necessarily mean the form was valid or saved.

---

## 3. Creating a Django Form

Import Django's forms module:

```python
from django import forms
```

Create a form using `forms.Form`.

### Example

```python
from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField()
```

Each field defines the expected type of user input.

### Common Form Fields

| Field | Purpose |
|---|---|
| CharField | Text input |
| EmailField | Email address |
| IntegerField | Whole numbers |
| MultipleChoiceField | Multiple selections |
| FileField | File uploads |
| BooleanField | True/false values |
| DateField | Date input |

### Form Field Arguments

```python
name = forms.CharField(
    max_length=100,
    required=True,
    label="Your Name",
    help_text="Enter your full name"
)
```

Common arguments:

- `required` = Determines whether input is mandatory.
- `label` = Controls the displayed field name.
- `initial` = Provides an initial value.
- `help_text` = Displays additional instructions.

**Backend Connection:**

Form fields define the expected input structure before the application processes the submitted information.

---

## 4. Django Form Validation

Validation checks whether submitted information meets the form's requirements.

### Example

```python
form = UserForm(request.POST)

if form.is_valid():
    data = form.cleaned_data
```

### Validation Workflow

```text
User Submits Data
       ↓
Form Receives Data
       ↓
is_valid()
       ↓
   Validation
    /      \
 Valid    Invalid
   ↓         ↓
cleaned_data  form.errors
   ↓         ↓
Continue    Show Errors
```

### is_valid()

```python
form.is_valid()
```

Checks whether submitted information satisfies the validation rules.

Returns:
- `True` = Valid input
- `False` = Invalid input

### cleaned_data

```python
form.cleaned_data
```

Contains validated and converted Python values.

For example, a valid integer submitted through an HTML form becomes a Python integer.

### form.errors

```python
form.errors
```

Contains validation errors that can be displayed to the user.

### Airport Security Analogy

```text
Passenger Arrives
       ↓
Presents Passport
       ↓
Security Checks Information
       ↓
Is Everything Valid?
       ↓
YES → Continue
NO  → Additional Checks / Rejection
```

Django equivalent:

```text
Passenger = Submitted Data
Passport = Form Fields
Security Check = is_valid()
Approved Information = cleaned_data
Problems = form.errors
```

**Key Concept:**

Validation checks incoming information before the application trusts and processes it.

---

## 5. Django Models and Database Fields

A Django model defines the structure of application data.

Models inherit from `models.Model`.

### Example

```python
from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
```

### Database Relationship

```text
Django Model Class
       ↓
Database Table

Model Field
       ↓
Database Column

Model Instance
       ↓
Database Row
```

### Common Model Fields

| Model Field | Purpose |
|---|---|
| CharField | Text |
| IntegerField | Whole numbers |
| DecimalField | Decimal numbers |
| BooleanField | True/false values |
| DateTimeField | Date and time |
| DateField | Date |
| ForeignKey | Many-to-one relationship |
| OneToOneField | One-to-one relationship |
| ManyToManyField | Many-to-many relationship |

### Database Relationships

```text
One-to-One
    ↓
OneToOneField

One-to-Many
    ↓
ForeignKey

Many-to-Many
    ↓
ManyToManyField
```

### Field Arguments

```python
name = models.CharField(
    max_length=100,
    blank=False,
    null=False
)
```

Important distinction:

- `blank` = Controls whether a field can be empty during validation.
- `null` = Controls whether the database can store NULL.

For text fields, Django generally recommends using an empty string rather than NULL to represent missing text.

---

## 6. Django Models and Migrations

Changes to Django models must be reflected in the database schema.

### Workflow

```text
Modify models.py
       ↓
python manage.py makemigrations
       ↓
Migration File Generated
       ↓
python manage.py migrate
       ↓
Database Schema Updated
```

### Commands

Generate migration files:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Check the Django project:

```bash
python manage.py check
```

### Backend Connection

```text
Model
  ↓
Migration
  ↓
Database Schema
  ↓
Django ORM
  ↓
Database Operations
```

The Django ORM allows Python code to interact with database records without manually writing SQL for every operation.

---

## 7. Understanding ModelForm

Django provides `ModelForm` to create forms based on existing Django models.

### Regular Form

```python
class UserForm(forms.Form):
    name = forms.CharField()
```

A regular form defines its fields explicitly.

It does not automatically save information to a database.

### ModelForm

```python
from django import forms
from .models import Drink

class DrinkForm(forms.ModelForm):

    class Meta:
        model = Drink
        fields = ["name", "price"]
```

A ModelForm generates form fields using the selected model.

### Key Components

**forms.ModelForm**
- Connects a Django form to a model.

**class Meta**
- Defines configuration for the form.

**model**
- Specifies which Django model the form uses.

**fields**
- Specifies which model fields are included.

### ModelForm Workflow

```text
Django Model
     ↓
ModelForm
     ↓
Form Fields Generated
     ↓
User Submits Data
     ↓
Validation
     ↓
form.save()
     ↓
Database Record
```

**Important:**

ModelForm can save validated data to the database, but saving does not happen automatically merely because the form is valid.

---

## 8. Using ModelForm in a Django View

The view coordinates the request, form validation, and database operations.

### Example

```python
from django.shortcuts import render
from .forms import DrinkForm

def create_drink(request):

    if request.method == "POST":
        form = DrinkForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = DrinkForm()

    return render(
        request,
        "drink_form.html",
        {"form": form}
    )
```

### Responsibilities

```text
forms.py
    ↓
Defines Input and Validation

views.py
    ↓
Handles Requests and Application Logic

models.py
    ↓
Defines Database Structure

templates/
    ↓
Displays HTML and Form Fields

urls.py
    ↓
Routes Requests to Views
```

### Backend Thinking

```text
Client
   ↓
URL Routing
   ↓
Django View
   ↓
ModelForm
   ↓
Validation
   ↓
Django ORM
   ↓
SQLite Database
   ↓
HTTP Response
```

---

## 9. Practical Exercise — Booking Form

**Exercise:** Working with Forms  
**Completed:** 2026-10-12

Created a booking application using Django.

### Project Structure

```text
myapp/
│
├── models.py
├── forms.py
├── views.py
├── urls.py
│
├── migrations/
│   └── 0003_booking.py
│
└── templates/
    └── booking.html
```

### Booking Model

```python
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)
```

### Booking ModelForm

```python
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = "__all__"
```

### Booking View

```python
from django.shortcuts import render
from .forms import BookingForm

def form_view(request):

    form = BookingForm()

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()

    context = {"form": form}

    return render(request, "booking.html", context)
```

### Testing Observations

- Tested required field validation.
- Tested single-character names.
- Tested valid booking submissions.
- Tested negative guest counts.
- Tested repeated form submissions.
- Verified SQLite database persistence.

### Issue 1 — Negative Guest Counts

The database accepted `-5` as a guest count.

This demonstrated that `IntegerField` accepts negative values unless additional validation is configured.

Possible improvement:

```python
guest_count = models.PositiveIntegerField()
```

A stricter rule could require at least one guest.

### Issue 2 — Duplicate Bookings

Repeated POST submissions created duplicate database records.

This demonstrated the importance of preventing unintended duplicate submissions.

A common improvement is the Post/Redirect/Get pattern.

```text
POST
 ↓
Validate and Save
 ↓
Redirect
 ↓
GET
```

This helps prevent duplicate submissions caused by refreshing the page after a successful POST.

### Important Observation

The reservation field uses:

```python
reservation_time = models.DateField(auto_now=True)
```

This automatically sets the date when the model instance is saved.

It does not allow users to select a future reservation date.

A real booking application would typically use a separate field for the requested reservation date.

---

## 10. Lessons Learned

### Forms Handle Input

Forms define what information the application expects from users.

### Validation Protects Application Logic

Django checks submitted information before it is processed.

### Models Define Persistent Data

Models describe how information is represented in the database.

### ModelForm Connects Forms and Models

ModelForm simplifies validation and database operations.

### Views Coordinate the Workflow

Views handle HTTP requests, validate information, and return responses.

### Testing Reveals Missing Business Rules

A technically valid submission is not necessarily a logically valid one.

Example:

```text
-5 = Valid Integer

-5 Guests = Invalid Business Logic
```

This demonstrates why backend developers must consider application requirements beyond basic data types.

---

## 11. Final Backend Mental Model

```text
USER
  ↓
HTML FORM
  ↓
HTTP REQUEST (GET / POST)
  ↓
URL ROUTING
  ↓
DJANGO VIEW
  ↓
MODELFORM
  ↓
VALIDATION
  ↓
APPLICATION LOGIC
  ↓
DJANGO MODEL / ORM
  ↓
SQLITE DATABASE
  ↓
HTTP RESPONSE
  ↓
USER
```

### Summary

**Form = Input and Validation**

**View = Request Handling and Application Logic**

**Model = Data Structure and Database Interaction**

**Template = Presentation**

**URL = Routing**

Together, these components create a functional Django backend application.

---

## 12. Course Progress

### 2026-10-12

**Working with Forms Exercise**

- Created the Booking model.
- Created BookingForm using ModelForm.
- Connected forms.py, views.py, urls.py, and booking.html.
- Generated and applied database migrations.
- Tested form submissions.
- Verified SQLite database records.
- Committed and pushed the implementation to GitHub.

### 2026-10-14

**Self Review — Working with Forms**

- Completed the self-review.
- Required multiple attempts.
- Final result: 100%.

### 2026-10-15

**Knowledge Check — Model and Forms**

- Attempt 1: 40%.
- Attempt 2: 100%.
- Reviewed incorrect answers.
- Reinforced understanding of Django models and forms.
- Updated progress.md.
- Committed and pushed progress to GitHub.

### 2026-10-17

**Models and Forms Subsection Completed**

- Consolidated handwritten notes.
- Reviewed Django forms and field types.
- Reviewed validation and cleaned_data.
- Reviewed models and database relationships.
- Reviewed migrations and ORM concepts.
- Reviewed ModelForm architecture.
- Connected concepts to the completed Booking exercise.
- Created a permanent Markdown reference.

**Status:** Models and Forms subsection completed.

**Next:** Continue with the remaining Django Web Framework course material.

---

## Final Reflection

The Models and Forms subsection helped connect individual Django components into a complete backend workflow.

Earlier concepts focused on defining forms, fields, and models.

Later concepts demonstrated how forms receive user input, validate information, interact with models, and store records in SQLite.

The Booking exercise provided practical experience connecting:

Input → Processing → Validation → Storage → Output

This reinforced the importance of understanding backend architecture rather than simply memorizing Django syntax.

The most important lesson was that Django provides tools for handling data, but the developer must still define appropriate application rules.

These concepts will be useful when developing larger backend projects, including the Meta capstone and future portfolio applications.