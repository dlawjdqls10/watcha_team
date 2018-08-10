from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.comment_new),
    path('', views.main, name='main'),
    path('check/<int:pk>/', views.check, name='check'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile),
    path('main/', views.main),
    path('flavor/', views.flavor)
]

# r'^post/(?P<pk>\d+)/$

# url(r'^$', views.main, name='main'),
