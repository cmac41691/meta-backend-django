from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse(request)

def about(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."}
    return render(request, 'about.html', {'content':about_content})
   # return HttpResponse(request, about_content)
    #about(HttpResponse)    
def menu(request):
    menu_items = {
        'Moussaka':'Greece',
        'Paella':'Spain',
        'Shakshuka':'North Africa / Middle East'
    }
    return render(request, 'menu.html',{'content' :menu_items} )


#return HttpResponse(request, incoming_request)