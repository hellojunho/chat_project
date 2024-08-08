# chat_project

## 개요
이 프로젝트는 1:1 실시간 채팅 애플리케이션을 구현하기 위한 웹 애플리케이션입니다.  
Django와 Django-Channels를 사용하여 실시간 통신 환경을 구축하고, Celery를 통해 비동기 처리를 수행하며, Docker와 Docker-Compose를 사용하여 컨테이너화된 환경에서 애플리케이션을 실행합니다.  

<hr>

## 기술 스택

### Backend
- Django
- Django-Channels
- Celery
- Docker
- Docker-Compose

### Frontend
- HTML
- CSS
- JavaScript

### Database
- Redis
- PostgreSQL (Docker 환경)
- SQLite3 (로컬 환경)

<hr>

## 기능 요구 사항

### 최소 요구 사항
✅ 1:1 대화를 주고받는 웹 어플리케이션을 작성합니다.  
✅ 대화 상대별로 대화방이 나뉘며, 각 대화방끼리 이동할 수 있습니다.  
✅ 메시지를 전송하고 서로 확인할 수 있습니다.  
✅ 새 메시지 버튼 클릭 시 새로운 대화방 생성 및 대화 상대 검색이 가능합니다.  
✅ 대화 내용은 서버에 저장되어 언제든지 확인할 수 있습니다.  
✅ Django 또는 Flask로 작성해 주시길 바랍니다.  
✅ Github, Bitbucket 등 접속 가능한 Git Remote Repository로 전달 바랍니다.

### Optional(선택사항)
✅ 로그인 및 로그아웃 기능을 제공합니다.  
✅ 비로그인 사용자는 로그인하도록 유도합니다.  
✅ 새 메시지 버튼 클릭 후 새 대화방 생성 시 대화 상대 검색이 가능합니다.  
✅ 메시지 전송 시 상대방에게 메일로 메시지 내용을 전송합니다.  
✅ Production 환경을 구축하여 동작 가능한 URL로 접속할 수 있도록 합니다.  
⬜️ Responsive를 지원합니다.  
⬜️ 대화에 URL이 있는 경우 클릭 가능한 형태로 출력합니다.  
⬜️ 읽지 않은 메시지가 있는 경우 화면에서 다르게 표기합니다.  
⬜️ 대화를 검색할 수 있는 기능을 추가합니다.  

<hr>

## 설치 및 실행 방법

### 로컬 개발 환경
1. requirements.txt 설치
```
pip install -r requirements.txt
```

2. 데이터베이스 마이그레이션
```
make migrate
```

3. 서버 실행
```
python manage.py runserver
```

### Docker 환경
1. Docker Compose로 실행
```
docker-compose up --build
```

2. 1번 완료 후 docker 컨테이너 진입
```
docker ps
docker exec -it [web_image_name] /bin/bash
```
```
make migrate
```

<hr>

## 사용법
1. 로그인/회원가입
- 어플리케이션을 실행하면, 가장 처음 로그인 화면이 나와 로그인 및 회원가입을 수행할 수 있습니다.  

2. 대화방 생성 및 이동
- `새 메시지` 버튼을 클릭하여 대화하고자 하는 `사용자 이름`을 검색합니다.  
- 검색에 성공한 순간 1:1 대화방이 생성됩니다.
- `채팅방 목록` 화면에는 생성한 대화방의 대상의 이름이 나타나고, 클릭하면 해당 대화방으로 이동합니다.

3. 대화 시작
- 대화방에 입장 후 메시지를 작성하고 전공하면, 상대방에게 실시간으로 전달됩니다.  
- 메시지를 전송하면, 수신자에게는 메시지의 본문이 포함된 이메일이 발송됩니다.  

4. 로그아웃
- 로그인 되어있는 사용자라면 우측 상단 `로그아웃` 버튼을 클릭하여 로그아웃을 진행할 수 있습니다.  
- 만약 로그인 되어있지 않은 사용자라면, `로그인` 버튼과 `회원가입` 버튼이 활성화 됩니다.  

<hr>

## 참고 자료
❗️ [Django Channels 공식 문서](https://channels.readthedocs.io/en/latest/)  
❗️ [Channels 사용하기 - 2](https://oraange.tistory.com/23)  
❗️ [파이썬/장고로 웹채팅 서비스 만들기 (Feat. Channels) - 기본편](https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EC%9B%B9%EC%B1%84%ED%8C%85-%EC%B1%84%EB%84%90%EC%8A%A4-%EA%B8%B0%EB%B3%B8/dashboard)  
<hr>

## 기술 및 고려사항 등을 정리한 문서
🍀 [Notion 페이지](https://rose-catshark-09a.notion.site/7e65435b400d4acc86170a85eb177063)

<hr>

## HTTPS 배포
[https://hellojunho.shop/](https://hellojunho.shop/)
