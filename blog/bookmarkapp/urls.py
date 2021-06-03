from django.contrib import admin
from django.urls import path

from bookmarkapp.views import BookmarkLV, BookmarkDV

urlpatterns = [
#
#     # class-based views
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
]