import typing as t
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm
from config.utils import exception_handler


# 응답이 다음 유형 중 하나인 경우의 alias -> views에서 사용
RedirectOrResponse = t.Union[HttpResponseRedirect, HttpResponse]


@exception_handler(view=True)
def signup(request: HttpRequest) -> RedirectOrResponse:
    """
    회원가입 view
    params:
    - request: HttpRequest
    return:
    - POST 요청 시, 회원가입 후 로그인 후 채팅방 검색 페이지로 redirect
    - GET 요청 시, 회원가입 페이지 render
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("chat:search_user")
    else: 
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})


@exception_handler(view=True)
def login(request: HttpRequest) -> RedirectOrResponse:
    """
    로그인 view
    params:
    - request: HttpRequest
    return:
    - POST 요청 시, 로그인 후 채팅방 검색 페이지로 redirect
    - GET 요청 시, 로그인 페이지 render
    """
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("chat:search_user")
    else:
        form = AuthenticationForm()

        return render(request, "accounts/login.html", {"form": form})


@login_required
@exception_handler(view=True)
def logout(request: HttpRequest) -> RedirectOrResponse:
    """
    로그아웃 view
    params:
    - request: HttpRequest
    return:
    - 로그아웃 후 채팅방 목록 페이지로 redirect
    """
    logout(request)

    return redirect("chat:get_chat_list")
