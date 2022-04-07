from django.shortcuts import render

# Create your views here.
def lobby(request):
    return render(request, 'chat/lobby.html', {'title': 'Lobby'})

def room(request, room_name):
    return render(request, 'chat/chatroom.html', {
        'room_name': room_name,
        'title': 'Chat Room'
    })


