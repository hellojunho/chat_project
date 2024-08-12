import json
from channels.generic.websocket import AsyncWebsocketConsumer
from accounts.models import User
from .models import ChatRoom, ChatMessage
from asgiref.sync import sync_to_async
from chat.tasks import send_email_contain_message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self) -> None:
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code: int) -> None:
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data: str) -> None:
        data = json.loads(text_data)
        message = data["message"]

        await self.save_message(self.scope["user"], message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": self.scope["user"].username,
            },
        )

    async def chat_message(self, event: dict) -> None:
        message = event["message"]
        username = event["username"]

        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "username": username,
                }
            )
        )

    @sync_to_async
    def save_message(self, user: User, message: str) -> bool:
        """
        메시지 저장 및 이메일 전송 메서드
        params:
        - user: User
        - message: str
        return:
        - 메시지 저장 및 이메일 전송 성공 시 True, 실패 시 False
        """
        try:
            chat_room = ChatRoom.objects.get(id=self.room_name)
            recipient = (
                chat_room.receiver if chat_room.sender == user else chat_room.sender
            )
            send_email_contain_message.delay(recipient.email, message)
            ChatMessage.objects.create(
                chat_room=chat_room, message_sender=user, message=message
            )
            return True
        except Exception as e:
            print(f"Error in save_message: {e}")
            return False
