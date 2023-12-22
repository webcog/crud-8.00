from django.shortcuts import render
from django.http import HttpResponse

# html page create - httprepone
# view build - 
# url link create - 

def index(request):
    return HttpResponse("Hello this is My Django Firdt View")

def about(request):
    return HttpResponse("This is Our About Page")