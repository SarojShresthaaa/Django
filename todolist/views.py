from django.shortcuts import render, redirect
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
    if request.method == "POST":
        title1 = request.POST.get('title')
        description1 = request.POST.get('Description')
        if title1 == "" or description1 == "":
            context = {
                "error": "Both fields are required"
            }
            return render(request, 'create.html',context)
        Todo.objects.create(title = title1, description = description1)
        return redirect('/task/')
    return render(request,'create.html')

def task_edit(request, id):
    task = Todo.objects.get(id = id)
    context = {
        "task": task
    }
    if request.method == "POST":
        title1 = request.POST.get('title')
        description1 = request.POST.get('Description')
        task.title = title1
        task.description = description1
        task.save()
        return redirect('/task/')
    return render(request, 'edit.html', context)

def task_mark(request,id):
   task = Todo.objects.get(id = id)
   task.status = True
   task.save()
   return redirect('/task/')
    

def task_delete(request, id):
    task = Todo.objects.get(id = id)
    task.delete()
    return redirect('/task/')





