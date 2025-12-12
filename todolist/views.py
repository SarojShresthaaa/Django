from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
   return HttpResponse("<h1>Welcome</h1>")
def home(request):
   return HttpResponse("<h1>This is the Home Page</h1>")