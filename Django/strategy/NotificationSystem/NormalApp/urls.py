from django.urls import path
from NormalApp.views import home

app_name = "NormalApp"
urlpatterns = [
    path("", home, name="Home"),
]
