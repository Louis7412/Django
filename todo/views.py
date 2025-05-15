from django.shortcuts import render
from .models import Todo


# Create your views here.
def todolist(requset):
    todos = Todo.objects.all()
    print(todos)
    result = {"todos": todos}
    return render(requset, "todo/todolist.html", result)
