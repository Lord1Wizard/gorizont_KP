from django.urls import path, re_path
from . import views
# from django.conf.urls import url

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^authors/$', views.AuthorsView.as_view(), name='authors'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorsDetailView.as_view(), name='author-detail'),
]