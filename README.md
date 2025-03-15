
# 인턴과제 20250316

작성자: 강의찬


### swagger 문서 페이지
http://52.78.161.60:8000/swagger/


<br>

### 기술스택
**Backend**
- Python (3.10.6)
- Django REST framework(3.15.2)

**Deploy**
- AWS EC2

<br>

### 구현기능
 - 로그인 기능
 - 회원가입 기능


<br>

### pytest 결과

##### 로그인 성공
intern_project/users/tests/test_login.
py::TestLogin::test_login_success PASSED [ 25%] <br>

##### 로그인 실패
intern_project/users/tests/test_login.
py::TestLogin::test_login_invalid_credentials PASSED [ 50%]<br>

##### 회원가입 성공
intern_project/users/tests/test_signup.
py::TestSignup::test_signup_success PASSED [ 75%]<br>

##### 회원가입 실패(존재하는 아이디디)
intern_project/users/tests/test_signup.
py::TestSignup::test_signup_user_already_exists PASSED [100%]<br>


### 트러블 슈팅
<details>
<summary> 정적파일을 가져오지 못하는 이슈  </summary>
<div markdown="1">

#### 문제발생
**/swagger/** 에 정상적으로 접속되었지만 
api 문서가 정상적으로 출력되지 않은 이슈가 발생

#### 해결
whitenoise를 가상환경에 설치


```bash
# whitenoise 설치
pip install whitenoise


INSTALLED_APPS = ['whitenoise.runserver_nostatic'] #추가

MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

```

**정상출력 확인**

</div>
</details>
