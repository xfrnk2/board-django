from django.views.generic import ListView, DetailView
from bookmarkapp.models import Bookmark

from django.shortcuts import render


class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark
