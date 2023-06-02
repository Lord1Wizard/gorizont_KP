from django.urls import path, re_path, include
from . import views
# from django.conf.urls import url

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^authors/$', views.AuthorsView.as_view(), name='authors'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorsDetailView.as_view(), name='author-detail'),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    re_path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
urlpatterns += [
    re_path(r'^allbooks/$', views.LoanedBooksAllUserListView.as_view(), name='all-borrowed'),
]