import os
from django.core.mail import send_mail, EmailMultiAlternatives
from dotenv import load_dotenv
from functools import wraps
from accounts.models import User
from chat.models import ChatMessage, ChatRoom
from typing import List, Dict, Optional

load_dotenv()


def send_email(receiver_email: str, message_body: str) -> bool:
    """
    메일 전송 함수
    params:
    - receiver_email: str
    - message_body: str
    return:
    - 메일 전송 성공 시 True, 실패 시 False
    """
    sender_email = os.getenv("EMAIL_HOST_USER")

    msg = EmailMultiAlternatives(
        subject="메시지가 도착했습니다.",
        body=f"{message_body}",
        from_email=sender_email,
        to=[receiver_email],
    )
    try:
        msg.send()
        return True
    except Exception as e:
        print(e)
        return False


def exception_handler(view: bool = False):
    """
    예외처리 데코레이터
    params:
    - view: bool
    return:
    - 예외 발생 시, 에러 메시지 출력
    """

    def exception_handler_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except User.DoesNotExist as e:
                print(f"exception_handler: An error occurred in {func.__name__}: {e}")
                return "An error occurred"
            except ChatRoom.DoesNotExist as e:
                print(f"exception_handler: An error occurred in {func.__name__}: {e}")
                return "An error occurred"
            except ChatMessage.DoesNotExist as e:
                print(f"exception_handler: An error occurred in {func.__name__}: {e}")
                return "An error occurred"
            except Exception as e:
                print(f"exception_handler: An error occurred in {func.__name__}: {e}")
                return "An error occurred"

        return wrapper

    return exception_handler_decorator
