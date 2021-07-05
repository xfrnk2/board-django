from django.contrib import admin
from django.urls import path
from bookmarkapp import views

app_name = 'bookmark'
urlpatterns = [
#
#     # class-based views
    path('', views.BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),
    # 추가
    path('add/', views.BookmarkCreateView.as_view(), name='add',),
    path('change/', views.BookmarkChangeLV.as_view(), name='change',),
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name='update',),
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name='delete',),
]