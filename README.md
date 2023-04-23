# linktoon_project

모든 웹툰을 체크하고 보러갈수있는 사이트

- <a>linktoon</a>

### 개발환경

- `python 3.9`
- `django 4.2`
- `gunicorn 20.1.0`
- `Pillow 9.5.0`
- `mysqlclient 2.1.1`

### 배포환경

- `linux`
- `docker`
- `nginx 1.24`
- `python 3.9`
- `mysql 8.0`

## 주요기능

#### 검색

- 일부분 일치 검색
- 검색내역 표시

<!-- #### 회원가입,로그인

- 이메일 중복 체크
- 이메일 찾기
- PW 찾기
- PW 암호화
- DB값 검증

#### 관리자페이지

- 웹툰 CRUD -->

## 시스템 구조 - <a>상세보기</a>

## 테이블 구조 - <a>상세보기</a>

##### 개발서버 테스트 실행 방법

필요사항 : SECRET_KEY

```
set DJANGO_SETTINGS_MODULE=settings.settings.local
manage.py runserver
```
