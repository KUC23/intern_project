# users/views.py
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# jwt토큰 인증
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



User = get_user_model()

class SignupView(APIView):
    # Swagger 문서화
    @swagger_auto_schema(
        operation_description="사용자 회원가입 API",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username', 'password', 'nickname'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='사용자 아이디'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='비밀번호'),
                'nickname': openapi.Schema(type=openapi.TYPE_STRING, description='닉네임'),
            }
        ),
        responses={
            201: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'username': openapi.Schema(type=openapi.TYPE_STRING),
                    'nickname': openapi.Schema(type=openapi.TYPE_STRING),
                }
            ),
            400: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'code': openapi.Schema(type=openapi.TYPE_STRING),
                            'message': openapi.Schema(type=openapi.TYPE_STRING),
                        }
                    )
                }
            )
        }
    )

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        # 이미 존재하는 사용자인지 확인
        if User.objects.filter(username=request.data.get('username')).exists():
            return Response({
                "error": {
                    "code": "USER_ALREADY_EXISTS",
                    "message": "이미 가입된 사용자입니다."
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # 유효성 검사 및 저장
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "username": user.username,
                "nickname": user.nickname
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    @swagger_auto_schema(
        operation_description="사용자 로그인 API",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username', 'password'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='사용자 아이디'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='비밀번호'),
            }
        ),)



    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # JWT 토큰 생성
            refresh = RefreshToken.for_user(user)
            
            return Response({
                "token": str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        
        return Response({
            "error": {
                "code": "INVALID_CREDENTIALS",
                "message": "아이디 또는 비밀번호가 올바르지 않습니다."
            }
        }, status=status.HTTP_401_UNAUTHORIZED)
    



class ProtectedView(APIView):
    authentication_classes = [JWTAuthentication]  # JWT 인증 적용
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능

    def get(self, request):
        return Response({
            "message": f"Hello, {request.user.username}!"
        })
