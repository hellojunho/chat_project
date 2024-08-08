import os
import smtplib
from django.test import TestCase
from config.utils import send_email


class TestSendEmail(TestCase):
    def test_send_email(self) -> bool:
        """
        이메일 전송 테스트
        param:
        -
        return:
        - 이메일 전송 성공 시 True, 실패 시 False
        """
        try:
            result_to_send_email = send_email("junho991026@naver.com", "test message")
            self.assertTrue(result_to_send_email)
            return True
        except Exception as e:
            return False


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
