# Django PJT4
> pair programming

## Project Structure
```
django_pjt4
├── accounts
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── community
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── django_pjt4
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── templates
    └── base.html
```
---

## 가상환경
```bash
$ python -m venv venv
$ source venv/bin/activate
# pip 설치 목록 파일생성
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
```

## Model
```python
class Review(models.Model):
    ...
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
```
* `on_delete=models.CASCADE` : models 자주 실수함. 주의 !!!

### Custom User Model
* django User Model을 변경하여 사용할 경우 `settings.py`에서 `AUTH_USER_MODEL = 'accounts.User'` 추가해줘야 함(앱이름.User)
* `forms.py` 생성 후 `CustomUserCreationForm`, `CustomUserChangeForm` form 커스텀 필요


## 오늘 만난 오류들
### No Reverse Match ~~.
> [Django docs](https://docs.djangoproject.com/en/3.0/ref/exceptions/#django.urls.NoReverseMatch)
* 제일 많이 발생한 오류
    * 발생 원인 : **오타**로 인한 url 오류
        * 급하게 작성하다보니 발생
        * 기존 코딩시 자동완성 기능 자주 사용했기 때문에 자동완성 없이 코딩하는 경우 오타 많이 발생함

### NOT NULL constraint failed ~~.
* `form` 입력 후 DB 저장 시 Null 발생.
    * 외래키 참조하는 필드의 값을 `views.py`에서 추가 입력 안해줘서 발생했음(form에서 데이터 입력받지 않고 자동 입력되도록 처리하려 했음)

### 추가 오류들
* 필드값 & `related_name` 반대로 입력해서 오류 발생
    * 외래키 참조하는 테이블에서는 `related_name`로 접근
    * 외래키 참조하는 필드를 **가진 테이블**에서는 해당 필드값으로 접근

## 오늘의 프로젝트
* `views.py` 작성 시 생각보다 많이 잊혀져 있어서 많이 당황스러웠음
* 오타가 너무 많아서 오타로 인해 발생한 오류 잡느라 최소 1시간 이상 소요
    * 자동완성 너무 의존했었다.

* url 설정 시 `주소/커뮤니티/영화/리뷰` 구조로 만들었는데 리뷰 관련 로직에서 영화 id 값이 사용되지 않은 경우도 있었는데 이 값을 계속 보내주는게 맞는지 의문..

* 팀원과 함께 오늘도 나의 실수를 많이 발견하고 고칠 수 있었다. 오타 제발 조심

* [지난 프로젝트](https://lab.ssafy.com/yueuni123/django_pjt3) 많이 참고했습니다..