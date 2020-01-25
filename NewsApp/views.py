from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def News(request):
    return HttpResponse("<h1>This is our latest news</h1>")

def Home(request):
    return HttpResponse("<h1>Welcome to the home page</h1>")

def Contact(request):
    return HttpResponse("<h1>You can contact me on this page</h1>")