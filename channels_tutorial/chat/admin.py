from django.contrib import admin

from chat.models import ChatMessage, ChatRoom

admin.site.register(ChatMessage)
admin.site.register(ChatRoom)
