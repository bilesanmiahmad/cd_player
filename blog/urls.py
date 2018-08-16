from django.urls import path, include
from blog.views import viewPost, addPost, PostMonthArchiveView, PostWeekArchiveView

urlpatterns = [
    path('post/<str:slug>', viewPost, name='blog_post_detail'),
    path('add/post', addPost, name='blog_add_post'),
    path('archive/<int:year>/month/<int:month>',
         PostMonthArchiveView.as_view(month_format='%m'),
         name='blog_archive_month'),
    path('archive/<int:year>/week/<int:week>',
         PostWeekArchiveView.as_view(), name='blog_archive_week'),
]
