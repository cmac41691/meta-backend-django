from django.urls import path
from . import views
# drinks
urlpatterns = [
        #path('admin/', admin.site.urls), 
        path('drinks/<str:drink_name>', views.drinks, name="drink_name"),  
        #path('urlparamsproject/', include('urlparamsproject.urls'))
    ]
