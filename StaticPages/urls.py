from django.urls import path
from .views import Home,About

app_name = 'StaticPages'
urlpatterns = [
    path("",Home, name="main"),
    path("about", About, name="About"),
]