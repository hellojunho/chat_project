from django.conf import settings
from django.db import models


class ChatRoom(models.Model):
    """
    채팅방 모델
    id: ChatRoom id
    sender: 채팅방 생성 요청자 (검색을 한 유저)
    receiver: 채팅방 생성 요청 수신자 (검색이 된 유저)
    """
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender"
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver"
    )

    class Meta:
        managed = True
        ordering = ["-id"]
        db_table = "chat_room"


class ChatMessage(models.Model):    
    """
    채팅 메시지 모델
    id: ChatMessage id
    chat_room: 채팅방
    message_sender: 메시지 보낸 사람
    message: 메시지 내용
    created_at: 메시지 생성 시간
    """
    id = models.AutoField(primary_key=True)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message_sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        ordering = ["created_at"]
        db_table = "chat_message"
