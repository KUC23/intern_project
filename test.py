import sys
print(sys.path)
try:
    import intern_project
    print("성공!")
except ImportError:
    print("실패: intern_project 모듈을 찾을 수 없습니다.")