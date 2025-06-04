from django.urls import path
from . import views

app_name="flight"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>/", views.get_flight, name="get_flight"),
    path("airport/<int:airport_id>/", views.get_airport, name="get_airport"),
    path("<int:flight_id>/add/", views.add_passenger, name="add_passenger")
]