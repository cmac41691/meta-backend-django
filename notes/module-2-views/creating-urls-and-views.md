# Creating URLs and Views

**Notes completed:** 2026-09-04

## URL Routing

Django uses URL patterns to connect a client request to the correct view.

```text
Client
  ↓
Request
  ↓
Project urls.py
  ↓
App urls.py
  ↓
View
  ↓
Response
```

A basic app-level `urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("menu/", views.menu, name="menu"),
]
```

The URL determines which view handles the request.

---

## Regular Expressions in URLs

Regular expressions (regex) can match and validate patterns in URLs.

Common uses:

- Searching
- Validation
- Group searching
- Find and replace

Useful regex characters:

```text
^    → beginning / anchor
$    → end of string
[]   → character set
{}   → repetitions
()   → grouping
```

Django commonly uses `path()` for normal routing and `re_path()` when a regex pattern is needed.

---

## URL Namespacing

Different Django apps can have URLs with the same name.

Example:

```text
demoapp → index
newapp  → index
```

Namespaces tell Django which app's URL we mean.

```python
app_name = "demoapp"

urlpatterns = [
    path("", views.index, name="index"),
]
```

Django can identify this URL as:

```text
demoapp:index
   │      │
   │      └── URL name
   └───────── App namespace
```

---

## Reverse URL Lookup

Instead of hardcoding:

```text
/demoapp/login/
```

Django can locate the URL by name:

```python
reverse("demoapp:login")
```

In a template:

```django
{% url "demoapp:login" %}
```

This makes URLs easier to change and maintain.

---

## Views

A view receives a request, performs processing, and returns a response.

```text
URL
 ↓
View
 ↓
Application Logic
 ↓
Response
```

Simple function-based view:

```python
from django.http import HttpResponse

def menu(request):
    return HttpResponse("Menu")
```

Views can:

- Process requests
- Work with application logic
- Access models/database data
- Validate data
- Return responses

---

# Error Handling

Errors are part of the request/response flow.

```text
Request
   ↓
URL → View
       ↓
    Processing
    ↙       ↘
 Success    Error
    ↓        ↓
   200    400 / 403 / 404 / 500
    ↓        ↓
 Response to Client
```

Common HTTP responses:

```text
400 → Bad Request
401 → Authentication required
403 → Forbidden
404 → Resource not found
500 → Internal Server Error
```

Example 404:

```python
return HttpResponseNotFound("Page not found")
```

or:

```python
return HttpResponse("Page not found", status=404)
```

---

## Database Error Example

A URL might contain the ID of a database object.

```text
URL contains product ID
        ↓
View searches database
        ↓
Does product exist?
    ↙          ↘
  YES           NO
   ↓             ↓
  200          Http404
```

Python's `try/except` can handle missing data:

```python
try:
    # Find database object
except:
    # Handle missing object
```

Useful Django exceptions:

```text
Http404                 → requested resource wasn't found
ObjectDoesNotExist      → database object doesn't exist
EmptyResultSet          → query returned nothing
FieldDoesNotExist       → requested model field doesn't exist
MultipleObjectsReturned → expected one object, got several
PermissionDenied        → user isn't allowed to perform action
ViewDoesNotExist        → Django can't find requested view
```

---

## Forms and POST

Submitted data should be validated before processing.

```text
POST Request
     ↓
View
     ↓
Form Validation
     ↓
 is_valid()?
   ↙     ↘
 YES     NO
  ↓       ↓
Process  Error Response
```

---

## DEBUG Mode

During development:

```python
DEBUG = True
```

Django provides detailed debugging information.

In production:

```python
DEBUG = False
```

Detailed debugging information should not be exposed to users.

---

# Class-Based Views (CBVs)

Django views can be written as Python functions or Python classes.

## Function-Based View

```python
def menu(request):
    ...
```

Good for simple and explicit behavior.

## Class-Based View

```python
class MenuView(View):

    def get(self, request):
        # Handle GET
        pass

    def post(self, request):
        # Handle POST
        pass
```

A CBV organizes related HTTP methods:

```text
Client Request
      ↓
     URL
      ↓
     CBV
   ↙     ↘
 GET     POST
  ↓       ↓
Read    Submit/Change
   ↘     ↙
   Response
```

Instead of manually checking:

```python
if request.method == "GET":
```

the class can separate behavior into methods:

```text
get()
post()
```

---

## CBVs and Python OOP

Class-based views build on normal Python concepts:

```text
Python
  ↓
Classes
  ↓
Methods
  ↓
Inheritance
  ↓
Django Class-Based Views
```

A Django CBV can inherit reusable behavior from another Django class.

```text
Function-Based View → simple + explicit
Class-Based View    → organized + reusable
```

---

## KISS Approach

Use the simplest structure that solves the problem.

```text
Simple view?
    ↓
Function-Based View

More related/reusable behavior?
    ↓
Consider Class-Based View
```

Do not use a CBV simply because Django provides one. Use it when the extra organization or reuse actually helps.

---

# TL;DR

```text
Client
  ↓
Request
  ↓
URL Routing
  ↓
View (Function or Class)
  ↓
Application Logic
  ↓
Success / Error
  ↓
HTTP Response
  ↓
Client
```

- URLs route requests to views.
- Namespaces prevent URL-name conflicts between apps.
- `reverse()` and named URLs reduce hardcoded paths.
- Views process requests and return responses.
- Errors should return appropriate HTTP status codes.
- `try/except` can handle failures during processing.
- Forms should validate submitted data.
- Function-based views are simple and explicit.
- Class-based views use Python OOP for organization and reuse.
- Keep the architecture as simple as the problem allows.