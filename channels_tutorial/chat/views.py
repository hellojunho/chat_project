import typing
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, ChatMessage
from accounts.models import User


RedirectOrResponse = typing.Union[HttpResponseRedirect, HttpResponse]


@login_required
def chat_list(request: HttpRequest) -> HttpResponse:
    """
    채팅방 목록 페이지 view
    params:
    - request: HttpRequest
    return:
    - 채팅방 목록 페이지 render
    """
    try:
        chat_rooms = ChatRoom.objects.filter(sender=request.user.id) | ChatRoom.objects.filter(receiver=request.user.id)
        recent_chats = chat_rooms.distinct().order_by("-id")
        return render(request, "chat/chat_list.html", {"recent_chats": recent_chats})
    except Exception as e:
        print(f"An error occurred in chat_list: {e}")
        return f"An error occurred in chat_list: {e}"


@login_required
def chat_search_user(request: HttpRequest) -> RedirectOrResponse:
    """
    유저 검색 페이지 view
    params:
    - request: HttpRequest
    return:
    - GET 요청 시, 유저 검색 페이지 render
    - POST 요청 시, 검색한 유저의 채팅방으로 redirect
    """
    if request.method == "POST":
        username = request.POST.get("username")
        try:
            user = User.objects.get(username=username)
            return redirect("chat:chat_room", user_id=user.id)
        except Exception as e:
            print(f"An error occurred in search_user: {e}")
            return f"An error occurred in search_user: {e}"
    return render(request, "chat/search_user.html")


@login_required
def chat_room(request: HttpRequest, user_id: int) -> HttpResponse:
    """
    채팅방 페이지 view
    params:
    - request: HttpRequest
    - user_id: int
    return:
    - 채팅방 페이지 render
    """
    try:
        searched_user = User.objects.get(id=user_id)
        chat_room = ChatRoom.objects.filter(Q(sender=request.user, receiver=searched_user) | Q(sender=searched_user, receiver=request.user)).first()
        if not chat_room:
            chat_room = ChatRoom.objects.create(sender=request.user, receiver=searched_user)
        messages = ChatMessage.objects.filter(chat_room=chat_room)

        return render(
            request,
            "chat/chat_room.html",
            {
                "chat_room": chat_room,
                "messages": messages,
                "searched_user": searched_user
            },
        )
    except Exception as e:
        print(f"An error occurred in chat_room: {e}")
        return f"An error occurred in chat_room: {e}"
