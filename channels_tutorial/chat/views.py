import typing as t
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, ChatMessage
from accounts.models import User
from config.utils import exception_handler


# 응답이 다음 유형 중 하나인 경우의 alias -> views에서 사용
RedirectOrResponse = t.Union[HttpResponseRedirect, HttpResponse]


@login_required
@exception_handler(view=True)
def get_chat_list(request: HttpRequest) -> HttpResponse:
    """
    채팅방 목록 페이지 view
    params:
    - request: HttpRequest
    return:
    - 채팅방 목록 페이지 render
    """
    chat_rooms = ChatRoom.objects.filter(
        sender=request.user.id
    ) | ChatRoom.objects.filter(receiver=request.user.id)
    recent_chats = chat_rooms.distinct().order_by("-id")

    return render(request, "chat/get_chat_list.html", {"recent_chats": recent_chats})


@login_required
@exception_handler(view=True)
def search_user(request: HttpRequest) -> RedirectOrResponse:
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
        user = User.objects.get(username=username)

        return redirect("chat:chat_room", user_id=user.id)

    return render(request, "chat/search_user.html")


@login_required
@exception_handler(view=True)
def chat_room(request: HttpRequest, user_id: int) -> HttpResponse:
    """
    채팅방 페이지 view
    params:
    - request: HttpRequest
    - user_id: int
    return:
    - 채팅방 페이지 render
    """
    searched_user = User.objects.get(id=user_id)
    chat_room = ChatRoom.objects.filter(
        Q(sender=request.user, receiver=searched_user)
        | Q(sender=searched_user, receiver=request.user)
    ).first()
    if not chat_room:
        chat_room = ChatRoom.objects.create(sender=request.user, receiver=searched_user)
    messages = ChatMessage.objects.filter(chat_room=chat_room)

    return render(
        request,
        "chat/chat_room.html",
        {"chat_room": chat_room, "messages": messages, "searched_user": searched_user},
    )
