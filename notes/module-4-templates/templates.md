## TL;DR — Django Template Examples

- Django views handle HTTP requests and return HTTP responses.
- `HttpResponse` can return HTML directly, but embedding HTML inside Python code becomes difficult to maintain.
- Django templates separate HTML presentation from Python application logic.
- Template variables use `{{ variable }}` to display values passed from a view.
- Template filters use `{{ variable|filter }}` to format or transform displayed values.
- The `render()` function combines a request, template, and optional context dictionary into an HTTP response.

**Backend flow:** Client → URL → View → Template + Context → HTML Response → Browser

**Key takeaway:** Views prepare data; templates present it.

## Django view (views.py)

```python
from django.shortcuts import render

def greeting(request):
    context = {"name": "Developer"}
    return render(request, "greeting.html", context)
```

## Django template (greeting.html)

```html
<h1>Hello, {{ name|upper }}!</h1>
```

## Output

```text
Hello, DEVELOPER!
```