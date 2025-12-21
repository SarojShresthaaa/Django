from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here.

def first(request):
   return HttpResponse("<h1>Welcome</h1>")
def about_us(request):
    return HttpResponse("<h1>This is the About Us Page</h1>")

def home(request):
   user = [
      {"name": "Aarav", "age": 15, "address": "Kathmandu"},
      {"name": "Sita", "age": 23, "address": "Bhaktapur"},
      {"name": "Ramesh", "age": 30, "address": "Lalitpur"},
      {"name": "Aarav", "age": 25, "address": "Kathmandu"}, 
      {"name": "Mina", "age": 28, "address": "Pokhara"},
      {"name": "Sita", "age": 23, "address": "Bhaktapur"},
      {"name": "Kiran", "age": 50, "address": "Butwal"},
      {"name": "Kiran", "age": 35, "address": "Butwal"},
      {"name": "Kiran", "age": 35, "address": "Butwal"},
      {"name": "Kiran", "age": 65, "address": "Butwal"},
      {"name": "Nisha", "age": 12, "address": "Dharan"},
      {"name": "Ramesh", "age": 30, "address": "Lalitpur"},
      {"name": "Anil", "age": 57, "address": "Biratnagar"},
   ]

   a = "Welcome to the page"
   context = {
      "title":"Homepage",
      "first_line": a,
      "second_line": "This is a home page. rendering from home function",
      "people" : user
   }
   return render(request, "home.html", context)

def contact(request):
   context = {
      "title" : "Contact",
      "first_line": "Contact Page",
      "second_line":"This is a contact page rendering from contact function"
   }
   return render(request,'contact.html',context)

def task(request):
    tasks = Todo.objects.all()
    total = tasks.count()
    complete = Todo.objects.filter(status = True).count()
    incomplete = Todo.objects.filter(status = False).count()
    context = {
       "tasks": tasks,
       "total_task": total,
       "complete_task": complete,
       "incomplete_task": incomplete
    }
    return render(request, "tasks.html", context)

def task_create(request):
    title = request.POST.get('title')
    description = request.POST.get('Description')
    print(title)
    print(description)
    return render(request,'create.html')






