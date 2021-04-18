from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def kristen(request):
    return HttpResponse("Hello, Kristen!")

def ching(request):
    return HttpResponse("Hello, Ching")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })