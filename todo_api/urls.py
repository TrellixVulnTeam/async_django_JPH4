from django.urls import path 
from .views import (
    getRoutes,
    getToDoList,
    getToDo,
    updateToDo,
    deleteToDo,
    createToDo,
    
)

urlpatterns = [
    path('', getRoutes, name='todo_routes'),
    path('list/', getToDoList, name='todo_list'),
    path('<int:pk>/', getToDo, name='todo'),
    path('create/', createToDo, name='create_todo'),
    path('<int:pk>/update/', updateToDo, name='update_todo'),
    path('<int:pk>/delete/', deleteToDo, name='delete_todo'),
]
