from django.urls import path
from . import views

app_name="users"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_flight, name="login"),
    path("logout", views.logout_flight, name="logout"),

]