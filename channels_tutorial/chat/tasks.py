from celery import shared_task
from django.utils import timezone
from config.utils import send_email

NOW = timezone.now()

@shared_task(bind=True)
def send_email_contain_message(receiver_email: str, message_body: str) -> bool:
    """
    이메일 전송 Celery task
    params:
    - receiver_email: 이메일을 받을 사람의 이메일 주소
    - message_body: 이메일 본문
    return:
    - 이메일 전송 성공 시 True, 실패 시 False
    """
    try:
        send_email(
            receiver_email,
            message_body
        )
        return True
    except Exception as e:
        print(e)
        return False    
