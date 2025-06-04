from django.shortcuts import render
from .models import Flight, Airport, Passenger
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseBadRequest

# Create your views here.


def index(request):
    return render(request, "flight/index.html", {
        "flights" : Flight.objects.all(),
        "airports" : Airport.objects.all()
    })

def get_flight(request, flight_id):
    flight = Flight.objects.get(pk = flight_id)
    return render(request, "flight/flight.html", {
        "flight" : flight,
        "passengers" : flight.passengers.all(),
        "non_passengers" : Passenger.objects.exclude(flights=flight).all()
    })

def get_airport(request, airport_id):
    airport = Airport.objects.get(pk = airport_id)
    return render(request, "flight/airport.html", {
        "airport" : airport,
        "list_departures" : airport.departure.all(),
        "list_arrivals" : airport.arrival.all()
    }) 

def add_passenger(request, flight_id):
    if request.method == "POST":
        try:
            passenger_id = request.POST["passenger"]
            passenger = Passenger.objects.get(pk=passenger_id)
            flight = Flight.objects.get(pk=flight_id)
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no Flight chosen")
        except Flight.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: Flight does not exist")
        except Passenger.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: Passenger does not exist")

        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight:get_flight", args=(flight_id, )))