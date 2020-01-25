from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def Sports(request):
    return HttpResponse("<h1>This is the latest Sports Info</h1>")
