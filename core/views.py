from django.shortcuts import render
from django.http import HttpResponse

# html page create - httprepone
# view build - 
# url link create - 

# html - templates 

# def index(request):
#     return HttpResponse("Hello this is My Django Firdt View")

def home(request):
    return render(request,"index.html")

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')