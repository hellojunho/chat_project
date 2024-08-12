from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.accounts_signup, name="signup"),
    path("login/", views.accounts_login, name="login"),
    path("logout/", views.accounts_logout, name="logout"),
]
