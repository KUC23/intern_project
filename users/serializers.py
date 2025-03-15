# users/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'nickname') # 시리얼라이저에서 사용할 필드들을 지정
        extra_kwargs = {'password': {'write_only': True}} # 추가적인 필드 설정을 지정, 비밀번호가 응답에 포함되지 않도록
    
    def create(self, validated_data):
        user = User.objects.create_user( # Django의 User 모델에서 제공하는 메소드로, 새로운 사용자를 생성
            username=validated_data['username'],
            password=validated_data['password'],
            nickname=validated_data['nickname']
        )
        return user