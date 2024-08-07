import os
from django.core.mail import send_mail, EmailMultiAlternatives
from dotenv import load_dotenv
from functools import wraps
from accounts.models import CustomUser
from chat.models import ChatMessage, ChatRoom
load_dotenv()

def send_email(receiver_email, message_body):
        """
        메일 전송 함수
        """
        msg = EmailMultiAlternatives(
            "메시지가 도착했습니다.",
            f"{message_body}",
            os.getenv("EMAIL_HOST_ID"),
            [receiver_email] 
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
    """
    def exception_handler_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except CustomUser.DoesNotExist as e:
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