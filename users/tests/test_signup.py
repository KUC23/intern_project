# users/tests/test_signup.py
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
class TestSignup:
    def test_signup_success(self, api_client):
        url = reverse('signup')
        data = {
            "username": "testuser",
            "password": "testpassword",
            "nickname": "testnick"
        }
        
        response = api_client.post(url, data, format='json')
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['username'] == data['username']
        assert response.data['nickname'] == data['nickname']
        assert 'password' not in response.data
    
    def test_signup_user_already_exists(self, api_client):
        url = reverse('signup')
        data = {
            "username": "testuser",
            "password": "testpassword",
            "nickname": "testnick"
        }
        
        # 첫 번째 사용자 등록
        api_client.post(url, data, format='json')
        
        # 동일한 사용자명으로 다시 등록 시도
        response = api_client.post(url, data, format='json')
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['error']['code'] == 'USER_ALREADY_EXISTS'