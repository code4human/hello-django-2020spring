# hello-django-2020spring

https://docs.djangoproject.com/ko/3.0/intro/ Part1에서 Part4까지 따라하기
간단한 설문조사 polls 앱을 만들어보았다.

마주쳤던 문제들
-----------------
### 1. 가상환경 설정 <br>
프로젝트에 대한 가상환경 Location 설정하는 것에 혼란이 있었다. <br>
이전에 Django를 공부하면서 가상환경 디렉토리가 프로젝트의 상위에 있어야 한다고 잘못 이해했다. <br>
가상환경은 프로젝트마다 필요한 pip, python 등의 버전이 다를 수 있으므로 독립적으로 만들어주는데, 원하는 위치에 생성하면 된다. <br>
pycharm IDE는 python 프로젝트를 위한 가상환경 생성을 편리하게 할 수 있게 지원한다. <br>


알게 된 것들
----------------
### 1. settings.py의 타임존 지정 - USE_TZ 항목 <br>
USE_TZ=True라고 설정하면 장고가 알아서 시간대(time zone)을 조정한다. <br>
DB에는 UTC(협정 세계시)시간으로 저장하고, UI에서 입력받는 폼처리 및 UI에 출력하는 템플릿 처리시에는 TIME_ZONE 항목에 설정한 시간대를 반영하여 처리하는 방식이다. <br>
한국은 일광절약시간제(Daylight Saving Time)를 사용하지 않으므로, Asia/Seoul 시간대를 쓴다면 USE_TZ=False라고 하는게 편리하다. <br>
DB에 저장되는 시간도 UTC가 아니라 한국 시간으로 저장된다. <br>

### 2. get()과 filter()
python manage.py shell 명령을 이용해 대화형 프롬프트에서 연습한 결과, get()은 객체 1개만을, filter()는 해당하는 객체를 리스트로 반환한다는 것을 알 수 있었다. <br>
404에러 처리를 할 때 get()은 get_object_or_404() 함수로, filter()는 get_list_or_404() 함수로 Http404를 동작시킬 수 있다. <br>

### 3. 클래스형 제네릭 뷰
Django에서는 웹 프로그램 개발시 공통적으로 사용할 수 있는 로직을 기본 클래스로 제공한다. <br>
이러한 제네릭 뷰(generic view)를 상속받아 사용할 수 있다.  <br>
제네릭 뷰는 Base View, Generic Display View, Generic Edit View, Generic Date View 네 가지로 분류된다. <br> 
사용했던 제네릭 뷰는 ListView와 DetailView인데, 이들은 Generic Display View에 해당하는 뷰들이다. <br>
ListView는 조건에 맞는 여러 개의 객체를 보여준다. <br>
DetailView는 객체 하나에 대한 상세한 정보를 보여준다. <br>


변경 사항
-----------------
### 1. MariaDB 연동 <br>
Django에서 지원하는 sqlite 대신 익숙한 MariaDB(Mysql)을 사용했다. <br>
settings.py의 DATABASES에서 설정을 변경해주고, migrate하기 전에 지정한 데이터베이스 이름(hello_django)에 해당하는 데이터베이스를 만들어주었다. <br>
원래 데이터베이스 이름을 hello-django로 하려고 했으나 SQL syntax 오류가 떴다. -을 _로 바꾸니 잘 되었다.<br>
MySQL Client 프롬프트 창을 켜서 데이터베이스를 만들었다.

	CREATE DATABASE hello_django;

그리고 데이터베이스를 사용했다. 

	USE DATABASE hello_django;

### 2. admin 등록을 데코레이터(@)로 변경 <br>
변경 파일 polls/admin.py <br>
변경 전 admin.site.resigter(Question) <br>
변경 후 @admin.register(Question)