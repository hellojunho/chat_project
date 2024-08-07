from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from config.utils import exception_handler

@exception_handler(view=True)
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat:search_user')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


@exception_handler(view=True)
def login_view(request):
    """
    로그인 view
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('chat:search_user')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})



@login_required
@exception_handler(view=True)
def logout_view(request):
    """
    로그아웃 view
    """
    logout(request)
    return redirect('chat:get_chat_list') 