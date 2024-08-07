from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import ChatRoom, ChatMessage

User = get_user_model()

@login_required
def index(request):
    # 최근 대화 목록 가져오기
    chat_rooms = ChatRoom.objects.filter(sender=request.user) | ChatRoom.objects.filter(receiver=request.user)
    recent_chats = chat_rooms.distinct().order_by('-id')  # 가장 최근에 생성된 채팅방 순으로 정렬

    return render(request, 'chat/index.html', {'recent_chats': recent_chats})


@login_required
def search_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = get_object_or_404(User, username=username)
        return redirect('chat:chat_room', user_id=user.id)
    return render(request, 'chat/search_user.html')


@login_required
def chat_room(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    chat_room, created = ChatRoom.objects.get_or_create(
        sender=request.user if request.user.id < other_user.id else other_user,
        receiver=other_user if request.user.id < other_user.id else request.user
    )
    
    messages = ChatMessage.objects.filter(room=chat_room)
    return render(request, 'chat/chat_room.html', {'chat_room': chat_room, 'messages': messages, 'other_user': other_user})
