from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import ChatRoom, ChatMessage
from accounts.models import CustomUser
from config.utils import exception_handler

@login_required
@exception_handler(view=True)
def get_chat_list(request):
    """
    채팅방 목록을 보여주는 view
    """
    chat_rooms = ChatRoom.objects.filter(sender=request.user)
    recent_chats = chat_rooms.distinct().order_by('-id')

    return render(request, 'chat/get_chat_list.html', {'recent_chats': recent_chats})


@login_required
@exception_handler(view=True)
def search_user(request):
    """
    사용자 검색 view
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        user = CustomUser.objects.get(username=username)
        return redirect('chat:chat_room', user_id=user.id)
    return render(request, 'chat/search_user.html')


@login_required
@exception_handler(view=True)
def chat_room(request, user_id):
    """
    채팅방 view
    """
    searched_user = CustomUser.objects.get(id=user_id)
    chat_room, created = ChatRoom.objects.get_or_create(
        sender=request.user if request.user.id < searched_user.id else searched_user,
        receiver=searched_user if request.user.id < searched_user.id else request.user
    )
    messages = ChatMessage.objects.filter(room=chat_room)
    return render(request, 'chat/chat_room.html', {'chat_room': chat_room, 'messages': messages, 'searched_user': searched_user})
