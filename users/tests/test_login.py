# users/tests/test_login.py
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    def _create_user(username, password, nickname):
        return User.objects.create_user(
            username=username,
            password=password,
            nickname=nickname
        )
    return _create_user

@pytest.mark.django_db
class TestLogin:
    def test_login_success(self, api_client, create_user):
        # 테스트 사용자 생성
        create_user(username="testuser", password="testpassword", nickname="testnick")
        
        url = reverse('login')
        data = {
            "username": "testuser",
            "password": "testpassword"
        }
        
        response = api_client.post(url, data, format='json')
        
        assert response.status_code == status.HTTP_200_OK
        assert 'token' in response.data
    
    def test_login_invalid_credentials(self, api_client):
        url = reverse('login')
        data = {
            "username": "wronguser",
            "password": "wrongpassword"
        }
        
        response = api_client.post(url, data, format='json')
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.data['error']['code'] == 'INVALID_CREDENTIALS'