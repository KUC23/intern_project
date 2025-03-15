from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# AbstractUser는 Django의 인증 시스템에 필요한 기본 필드들을 이미 가지고 있다.
# 즉 nickname 필드만 추가 필요
class User(AbstractUser):
    nickname = models.CharField(max_length=100)

    def __str__(self):
        return self.username
