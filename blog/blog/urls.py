"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from blog.views import HomeView

from django.conf.urls.static import static
from django.conf import settings

from blog.views import UserCreateView, UserCreateDoneTV

urlpatterns = [
    path('admin/', admin.site.urls),

    # 아래 인증 URL 3개 추가

    # 장고 Auth앱의 URLCONF에는 /login/, /logout/처럼 저장되어 있으므로
    # 그 앞에 URL 추가를 원한다면 아래와 같이 이를 표시해야 함. -> /accounts/login/ 등이 됨.
    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),


    path('', HomeView.as_view(), name='home'),

    path('blog/', include('blogapp.urls')),
    path('bookmark/', include('bookmarkapp.urls')),
    path('photo/', include('photo.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# static 함수의 형식은 다음과 같습니다.
# static(prefix(접두사), view=django.views.static.serve, **kwargs)
