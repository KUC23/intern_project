import sys
import os
import django

# 현재 파일의 디렉토리 (프로젝트 루트)를 Python 경로에 추가
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'intern_project.settings'
django.setup()