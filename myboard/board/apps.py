from django.apps import AppConfig


class BoardConfig(AppConfig): # 앱의 메타 데이터를 설정하는 클래스
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'
