"""
URL configuration for intern_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin       # Django 관리자 인터페이스를 위한 모듈
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view  # Swagger 문서의 스키마 뷰를 생성하는 함수
from drf_yasg import openapi                # OpenAPI 스펙에 따른 문서 정보를 정의하는 모듈


# swagger 문서화 설정
schema_view = get_schema_view(
    openapi.Info(
        title = 'Project_API', # 프로젝트 이름
        default_version = 'v1', # 프로젝트 버전
        description = 'intern_project API 문서', # 해당 문서 설명
        terms_of_service = "https://www.google.com/policies/terms/", # 서비스 이용약관 링크
        # contact = openai.Contact(email = ''),  # 연락처 정보
        # license=openapi.License(name=""), # 라이센스 정보
    ),
    public = True, # 문서가 공개적으로 접근 가능
    permission_classes = (permissions.AllowAny,),


)
urlpatterns = [
    # 프로젝트 url
    path('admin/', admin.site.urls),
    path('', include('users.urls')),

    # Swagger UI
    # URL에 Swagger UI를 연결
    path('swagger/', schema_view.with_ui('swagger', cache_timeout = 0), name = 'schema_view_swagger_ui'),
    # ReDoc 스타일의 API 문서를 제공하는 URL을 설정
    path('redoc/', schema_view.with_ui('redoc', cache_timeout = 0), name = 'schema_view_redoc'),
]



