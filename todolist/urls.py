from django.urls import path
from .views import *  
       
urlpatterns = [
   path('first/', first),
   path('home/', home),
   path('contact/', contact),
   path('task/', task),
   path('task/update/', task_update)
]