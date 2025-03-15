import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model

User = get_user_model()

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return None  # 인증이 필요 없는 요청은 None 반환

        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload["user_id"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed({"code": "TOKEN_EXPIRED", "message": "토큰이 만료되었습니다."})
        except jwt.InvalidTokenError:
            raise AuthenticationFailed({"code": "INVALID_TOKEN", "message": "토큰이 유효하지 않습니다."})
        except User.DoesNotExist:
            raise AuthenticationFailed({"code": "USER_NOT_FOUND", "message": "사용자를 찾을 수 없습니다."})

        return (user, token)  # request.user에 사용자 설정됨
