from django.urls import path
from .views import todolist, viewtodo

urlpatterns = [
    path("", todolist, name="todolist"),
    path("view/<int:id>/", viewtodo, name="viewtodo"),
]
