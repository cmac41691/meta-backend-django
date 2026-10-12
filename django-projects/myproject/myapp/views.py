from django.shortcuts import render
from .forms import BookingForm
# Create your views here.
# DEFINE form_view to handle HTTP requests
def form_view(request):
# CREATE an empty BookingForm
    form = BookingForm()
# IF request method equals POST
    if request.method == 'POST':
# CREATE BookingForm using submitted data
     form = BookingForm(request.POST)     
# IF submitted form is valid
    if form.is_valid():
# SAVE booking to database
        form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)