from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import (
    ArchiveIndexView,
    YearArchiveView,
    MonthArchiveView,
    DayArchiveView,
    TodayArchiveView
)
from blog.models import Post


# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2


class PostDV(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modified_dt'
    template_name = 'blog/post_archive.html'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modified_dt'
    template_name = 'blog/post_archive_year.html'


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modified_dt'
    template_name = 'blog/post_archive_month.html'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modified_dt'
    template_name = 'blog/post_archive_day.html'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modified_dt'
    template_name = 'blog/post_archive_day.html'
