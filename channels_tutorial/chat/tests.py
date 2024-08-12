import os
import smtplib
from django.test import TestCase

class TestSmtp(TestCase):
    def test_smtp(self) -> bool:
        """
        SMTP 서버 연결 테스트
        param:
        -
        return:
        - SMTP 서버 연결 성공 시 True, 실패 시 False
        """
        try:
            server = smtplib.SMTP("smtp.naver.com", 587)
            server.starttls()
            server.login(os.getenv("EMAIL_HOST_USER"), os.getenv("EMAIL_HOST_PASSWORD"))
            server.quit()
            return True
        except Exception as e:
            return False
