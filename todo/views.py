from django.shortcuts import render
from .models import Todo


# Create your views here.
def todolist(requset):
    todos = Todo.objects.all()
    # get唯一 filter篩選
    # todos = Todo.objects.filter(id=11)

    print(todos)
    result = {"todos": todos}
    return render(requset, "todo/todolist.html", result)


def viewtodo(requset, id):
    todo = None
    try:
        todo = Todo.objects.get(id=id)
    except Exception as e:
        print(e)

    return render(requset, "todo/viewtodo.html", {"todo": todo})
