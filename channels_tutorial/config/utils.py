import os
from django.core.mail import send_mail, EmailMultiAlternatives
from dotenv import load_dotenv
load_dotenv()

def send_email(receiver_email, message_body):
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
