from django.urls import path
from .views import *  
       
urlpatterns = [
   path('first/', first),
   path('home/', home)
]