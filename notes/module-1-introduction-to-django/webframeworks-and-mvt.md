# Web Frameworks and MVT

## What Is a Web Framework?

A web framework provides a structure and tools for building web applications.

A web framework can be summarized into several benefits:

- Faster development
- Clear project structure
- Easier to change and modify applications
- Code reusability
- Built-in tools for common web-development tasks

Django is a Python web framework designed to help developers build web applications efficiently.

Django is:

- Fast
- Feature-rich
- Secure
- Scalable

---

## Three-Tier Architecture

A web application can be thought of as having three major tiers.

### Presentation Tier

The presentation tier is where the user interacts with the application.

Examples:

- Laptop
- Smartphone
- Web browser

### Application Tier

The application tier processes requests and contains the application's logic.

Examples:

- Web server
- Application server
- Django application

### Data Tier

The data tier stores and retrieves application data.

Example:

- Database server

Simplified flow:

User / Browser
      ↓
Presentation Tier
      ↓
Application Tier
      ↓
Data Tier

In backend terms:

Client → Request → Server → Application Logic → Database → Response

---

# Django MVT Architecture

Django uses the **Model-View-Template (MVT)** architecture.

The three main components are:

- **Model** — manages application data and database interaction.
- **View** — receives requests, performs application logic, interacts with models when needed, and returns a response.
- **Template** — controls how information is presented to the user.

Django also uses a **URL dispatcher** to determine which view should handle an incoming request.

---

## Basic MVT Request Flow

A simplified Django request can be visualized as:

User
  ↓
URL
  ↓
URL Dispatcher
  ↓
View
 ↙   ↘
Model  Template
  ↓       ↓
Database Response
          ↓
         User

Another way to think about it:

Client Request
      ↓
urls.py
      ↓
View
      ↓
Application Logic
      ↓
Model / ORM
      ↓
Database
      ↓
View
      ↓
Template or Response
      ↓
Client

---

## URL Dispatcher

Django's URL dispatcher helps route an incoming request to the correct view.

The URL patterns are normally defined in:

`urls.py`

Conceptually:

Request URL → URL Dispatcher → Matching View

The URL dispatcher fills a role similar to routing/controller logic because it determines where a request should go.

---

## View

A Django view is a Python function or class that receives a web request and returns a web response.

A view can work with information from the request such as:

- URL path
- Query parameters
- Request body
- Client request data

The view can also:

- Perform application logic
- Interact with a model
- Read or modify database data
- Perform CRUD operations
- Send data to a template
- Return a response

Backend flow:

Request → View → Logic → Model/Database → Response

The view is therefore an important part of Django's **application logic layer**.

---

## Model

A Django model represents the structure of application data.

Models are Python classes that Django can map to database tables through the ORM.

Conceptually:

Python Model
     ↓
Django ORM
     ↓
Database Table

A Django application can contain multiple model classes.

Models allow the application to work with stored data without writing raw SQL for every database operation.

Common database operations include:

- Create
- Read
- Update
- Delete

These are the standard **CRUD operations**.

---

## Template

A template controls the presentation of information returned to the user.

A view can retrieve or process data and pass that data to a template.

Conceptually:

Database → Model → View → Template → Browser

Templates are primarily part of the **presentation/output side** of the Django request cycle.

---

# Key Takeaways

- A web framework provides reusable structure and tools for developing web applications.
- Django is a Python web framework.
- Django follows the Model-View-Template architecture.
- The **URL dispatcher** determines which view handles a request.
- The **View** handles the request and coordinates application logic.
- The **Model** represents and interacts with stored data.
- Django's **ORM** connects Python model objects with database data.
- The **Template** controls how information is presented.
- CRUD means Create, Read, Update, and Delete.
- Django's MVT architecture separates responsibilities instead of putting the entire application into one piece.

## Mental Model

When I see Django MVT, think:

**URL → View → Model → Database → View → Template → Response**

And connect it to the larger backend system:

**Client → Request → Server → Application Logic → Database → Response**