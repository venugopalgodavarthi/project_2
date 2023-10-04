from django.urls import path
from calls.views import hello, index, home

urlpatterns = [
    path(route='hello/', view=hello, name="hello"),
    path(route='index/', view=index, name="index"),
    path(route='home/', view=home, name="home"),
]
