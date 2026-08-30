from django.urls import  path 
from . import views

# Project urls.py uses include() to connect to this app's URLs.
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("menu/",views.menu, name="menu"),
    path("booking/", views.booking, name="booking"),
    
]
