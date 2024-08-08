from functools import wraps
from accounts.models import User
from chat.models import ChatMessage, ChatRoom


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
