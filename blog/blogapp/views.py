from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from blogapp.models import Post


class PostLV(ListView):
    model = Post
    template_name = 'blogapp/post_all.html'
    context_object_name = 'posts'
    paginate_by = 1

class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    data_field = 'modify_dt'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'

# Create your views here.
