from django.urls import path
from .views import *  
       
urlpatterns = [
   path('first/', first),
   path('home/', home),
   path('contact/', contact),
   path('task/', task),
   path('task/create/', task_create),
   path('task/<id>/edit/', task_edit),
   path('task/<id>/', task_mark),
   path('task/<id>/delete/', task_delete)
]