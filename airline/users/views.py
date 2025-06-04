from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, "users/index.html")
    else:
        return HttpResponseRedirect(reverse("users:login"))


def login_flight(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))

        else:
            return render(request, "users/login.html", {
                "error" : "Credentials are invalids"
            })

    return render(request, "users/login.html")


def logout_flight(request):
    logout(request)
    return render(request, "users/login.html", {
        "message" : "Logout succesfully"
    })
