# Django Views

## What Is a View?

A view contains the application logic that handles a request and returns a response.

Basic flow:

Client → HTTP Request → URL → View → HTTP Response

A view can:

- Process data
- Retrieve data
- Transform data
- Work with models
- Render templates
- Return a response

## Basic View Example

```python
from django.http import HttpResponse

def home(request):
    content = "<html><body><h1>Welcome</h1></body></html>"
    return HttpResponse(content)

The request comes into the view.

The view processes the request and returns an HttpResponse.

Views in MVT

Django uses the MVT architecture:

Model → works with data and the database
View → handles application and request logic
Template → handles presentation

Basic flow:

Client → URL Dispatcher → View → Model
↓
Template

The URL dispatcher finds the correct view for the incoming request.

The view can work with the model to retrieve or change data and can use a template to build the response.

Backend Flow

Client → Request → URL Dispatcher → View → Model → Database → Response    