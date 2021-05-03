from django.urls import path, include
from . import views

urlpatterns = [
    path('userinfo/', views.userinfo),
    #path('users/', include('users.urls')),
    path('mypage/', views.mypage),
]