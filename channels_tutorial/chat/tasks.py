import os
from config.celery import app
from dotenv import load_dotenv
from django.core.mail import EmailMultiAlternatives
load_dotenv()


@app.task(bind=True)
def send_email_contain_message(self, receiver_email: str, message_body: str) -> bool:
    """
    이메일 전송 Celery task
    params:
    - receiver_email: 이메일을 받을 사람의 이메일 주소
    - message_body: 이메일 본문
    return:
    - 이메일 전송 성공 시 True, 실패 시 False
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
