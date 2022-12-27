from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Todo, Category

def index(request):
    categories = Category.objects.all()
    todos = Todo.objects.all()
    for category in categories:
        category.todos = todos.filter(category_id = category.id)
    return render(request, "todo.html", {"categories": categories})

@require_http_methods(["GET", "POST"])
def get_todos(request, category_id):
    todos = Todo.objects.get(category_id = category_id)
    return render(request, "todo.html", {"todos": todos})

def add_category(request):
    name = request.POST["category_name"]
    category = Category(name=name)
    category.save()
    return redirect("index")

def add_todo(request, category_id):
    name = request.POST["todo_name"]
    todo = Todo(name=name, category_id = category_id)
    todo.save()
    return redirect("index")

def update_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.complete = not category.complete
    category.save()
    return redirect("index")

def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect("index")

def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect("index")

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")