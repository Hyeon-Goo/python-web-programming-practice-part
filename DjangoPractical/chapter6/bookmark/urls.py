from django.urls import path
from bookmark.views import BookmarkDV, BookMarkLV

app_name = 'bookmark'
urlpatterns = [
    path('', BookMarkLV.as_view(), name='index'),
    path('<int:pk>', BookmarkDV.as_view(), name='detail')
]