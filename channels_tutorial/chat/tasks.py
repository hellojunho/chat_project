import json
from pathlib import Path
import uuid
from celery import shared_task
from django.utils import timezone

from config.utils import send_email

NOW = timezone.now()

@shared_task(bind=True)
def send_email_contain_message(receiver_email, message_body):
    send_email(
        receiver_email,
        message_body
    )
    
