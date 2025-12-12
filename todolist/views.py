from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
   return HttpResponse("<h1>Welcome</h1>")
def home(request):
   return HttpResponse("<h1>This is the Home Page</h1>")
def contact(request):
    return HttpResponse("<h1>This is the Contact Page</h1>")
def about_us(request):
    return HttpResponse("<h1>This is the About Us Page</h1>")
