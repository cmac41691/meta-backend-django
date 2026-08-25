# Requests and URLs

**Date:** 2026-08-25  
**Course:** Meta Back-End Developer Professional Certificate  
**Course Section:** Django Web Framework — Requests and URLs

---

## HTTP Requests

HTTP is used to transfer resources between a client and a server, such as:

- Web pages
- Images
- Files
- Data

The basic request/response flow is:

Client → HTTP Request → Server → HTTP Response → Client

In a Django application, I can think about this as:

Client → URL → Django URL Dispatcher → View → Application Logic → HTTP Response

---

## HTTP Methods

HTTP methods describe what the client wants to do with a resource.

- `GET` → Retrieve data
- `POST` → Send/create data
- `PUT` → Update data
- `DELETE` → Remove data

Example request:

GET / HTTP/1.1

The request contains information such as:

- HTTP method
- Path
- HTTP version
- Host
- Headers
- Accepted language/content

---

## HTTP Status Codes

The server sends a status code back with the HTTP response.

### Status Code Groups

- `100–199` → Informational
- `200–299` → Successful
- `300–399` → Redirection
- `400–499` → Client error
- `500–599` → Server error

A `200` response means the request was successfully processed.

During my Django URL parameter testing, successful requests returned HTTP `200`.

---

# Request and Response Objects

Django represents incoming HTTP requests with an `HttpRequest` object.

The request object gives the view access to information sent by the client.

Useful request attributes include:

```python
request.method
request.GET
request.POST
request.COOKIES
request.FILES
request.user
request.headers
request.path
# Requests and URLs

**Date:** 2026-08-25  
**Course:** Meta Back-End Developer Professional Certificate  
**Course Section:** Django Web Framework — Requests and URLs

---

## HTTP Requests

HTTP is used to transfer resources between a client and a server, such as:

- Web pages
- Images
- Files
- Data

The basic request/response flow is:

```text
Client → HTTP Request → Server → HTTP Response → Client
```

In a Django application:

```text
Client → URL → Django URL Dispatcher → View → Application Logic → HTTP Response
```

---

## HTTP Methods

HTTP methods describe what the client wants to do with a resource.

- `GET` → Retrieve data
- `POST` → Send/create data
- `PUT` → Update data
- `DELETE` → Remove data

Example request:

```text
GET / HTTP/1.1
```

An HTTP request can contain information such as:

- HTTP method
- Path
- HTTP version
- Host
- Headers
- Accepted language/content

---

## HTTP Status Codes

The server sends a status code with the HTTP response.

- `100–199` → Informational
- `200–299` → Successful
- `300–399` → Redirection
- `400–499` → Client error
- `500–599` → Server error

A `200` response means that the request was successfully processed.

During my Django URL parameter testing, successful requests returned HTTP `200`.

---

# Request and Response Objects

Django represents incoming HTTP requests with an `HttpRequest` object.

The request object gives the view access to information sent by the client.

Useful request attributes include:

```python
request.method
request.GET
request.POST
request.COOKIES
request.FILES
request.user
request.headers
request.path
```

Example:

```python
def home(request):
    path = request.path
```

The `request` object is passed into the Django view when a matching URL is found.

---

## HttpResponse

A Django view returns an HTTP response to the client.

Example:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello")
```

Useful response information can include:

- Status code
- Content
- Headers

Backend flow:

```text
Request → Django View → Processing → HttpResponse → Client
```

---

# Understanding URLs

Example URL:

```text
https://www.littlelemon.com/menu/2026
```

A URL can contain several components:

```text
https://www.littlelemon.com/menu/2026
  │        │              │
scheme   domain          path
```

### Scheme

The scheme identifies the protocol being used.

```text
https://
```

### Subdomain

A subdomain can identify a particular section or service.

```text
www
```

### Domain

The domain identifies the website or application.

```text
littlelemon.com
```

### Path

The path identifies a particular resource or endpoint.

```text
/menu/2026
```

---

# Creating Requests and Responses in Django

A request enters Django through the URL configuration and is routed to a view.

```text
Client
  ↓
URL
  ↓
urls.py
  ↓
View
  ↓
views.py
  ↓
HttpResponse
  ↓
Client
```

Example view:

```python
from django.http import HttpResponse

def home(request):
    path = request.path
    return HttpResponse(path)
```

This connects Django views to the larger backend flow:

```text
Client → Request → URL Routing → View → Application Logic → Response
```

---

# Parameters

Parameters allow information from a URL to be passed into the application.

Two important forms are:

- Path parameters
- Query parameters

---

## Path Parameters

Path parameters are part of the URL path itself.

Example:

```text
/drinks/mocha
```

Here, `mocha` can be captured by Django and passed into a view.

### urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path("drinks/<str:drink_name>/", views.drinks, name="drink_name"),
]
```

The important part is:

```text
<str:drink_name>
```

This tells Django to:

1. Capture part of the URL.
2. Treat it as a string.
3. Store it as `drink_name`.
4. Pass `drink_name` into the matching view.

---

## Path Converters

Django path converters control what kind of URL value can be captured.

Common converters include:

- `str` → Matches a non-empty string excluding `/`
- `int` → Matches zero or positive integers and returns an integer
- `slug` → Matches letters, numbers, hyphens, and underscores
- `uuid` → Matches a formatted UUID
- `path` → Matches a non-empty string and can include `/`

Example:

```python
path("drinks/<str:drink_name>/", views.drinks)
```

The angle brackets `< >` identify the dynamic part of the URL.

---

# Query Parameters

Query parameters appear after `?` in a URL.

Example:

```text
/getuser/?name=Coady&id=1
```

They can be accessed through:

```python
request.GET
```

Example:

```python
def getview(request):
    name = request.GET["name"]
    user_id = request.GET["id"]

    return HttpResponse(
        f"Name: {name} User ID: {user_id}"
    )
```

This differs from a path parameter because the information is supplied through the query string rather than being part of the URL path pattern.

---

# Mapping URLs with Parameters

For the exercise, I created a dynamic URL that sends the requested drink name into the view.

### urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path("drinks/<str:drink_name>/", views.drinks, name="drink_name"),
]
```

The view receives `drink_name` from the URL.

Conceptually:

```text
/drinks/mocha
      ↓
<str:drink_name>
      ↓
drink_name = "mocha"
      ↓
drinks(request, drink_name)
      ↓
dictionary lookup
      ↓
HttpResponse
```

The URL parameter can therefore become input for Python application logic.

---

# Testing URL Parameters

I tested several URLs through the browser while the Django development server was running.

Valid parameters included:

```text
/drinks/mocha
/drinks/tea
/drinks/lemonade
```

The request flow can be represented as:

```text
GET /drinks/tea
        ↓
Django URL Dispatcher
        ↓
drink_name = "tea"
        ↓
drinks() view
        ↓
Dictionary lookup
        ↓
HttpResponse
        ↓
Client
```

Successful requests returned HTTP `200`.

---

## Testing an Invalid Parameter

I also deliberately tested:

```text
/drinks/water
```

Django successfully matched the URL and captured:

```python
drink_name = "water"
```

However, `water` was not a key in the dictionary.

A dictionary lookup such as:

```python
drink[drink_name]
```

therefore attempts:

```python
drink["water"]
```

which can raise:

```text
KeyError: 'water'
```

This showed that the URL routing itself was working.

The error occurred later during the application's Python logic:

```text
Client Request
    ↓
URL matched
    ↓
Parameter captured
    ↓
View called
    ↓
Dictionary lookup
    ↓
Key does not exist
    ↓
KeyError
```

---

# Key Takeaway

This section connected HTTP requests, URLs, Django routing, views, parameters, and responses into one backend process.

```text
Client
  ↓
HTTP Request
  ↓
Project URL Configuration
  ↓
App URL Configuration
  ↓
Path Matching
  ↓
URL Parameter Extraction
  ↓
View
  ↓
Application Logic
  ↓
HttpResponse
  ↓
Client
```

The URL configuration determines **where the request goes**.

The request object provides information about **what the client sent**.

URL parameters provide **dynamic input** to the application.

The view determines **what the application does with that input**.

The response determines **what gets sent back to the client**.

The Mapping URLs with Parameters exercise made this flow clearer because I could change a value in the browser URL and see that value travel through:

```text
Browser URL
    ↓
urls.py
    ↓
URL parameter
    ↓
views.py
    ↓
Python application logic
    ↓
HttpResponse
```