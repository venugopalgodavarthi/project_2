from django.urls import path
from calls.views import hello, index, home,  update, register, list_details, delete

app_name = 'calls'

urlpatterns = [
    path(route='hello/', view=hello, name="hello"),
    path(route='index/', view=index, name="index"),
    path(route='home/', view=home, name="home"),
    path(route='register/', view=register, name="register"),
    path(route='list/', view=list_details, name="list"),
    path(route='update/<int:pk>/', view=update, name="update"),
    path(route='delete/<int:pk>/', view=delete, name="delete"),
]
