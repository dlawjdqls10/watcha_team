from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('check/<pk>/', views.check, name='check'),
]

# r'^post/(?P<pk>\d+)/$

# url(r'^$', views.main, name='main'),