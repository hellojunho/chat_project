from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('search/', views.chat_search_user, name='search_user'),
    path('room/<int:user_id>/', views.chat_room, name='chat_room'),
]
