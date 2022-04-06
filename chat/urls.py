from django.urls import path
from .views import (
    lobby,
    room,
)

urlpatterns = [
    path('',  lobby, name='chat_home'),
    path('<str:room_name>/',  room, name='chat_room'),
    
    
]
