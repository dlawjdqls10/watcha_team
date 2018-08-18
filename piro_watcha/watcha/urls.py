from django.urls import path
from . import views

app_name = 'watcha'

urlpatterns = [
    path('comment/', views.comment_new),
    path('', views.main, name='main'),
    path('check/<int:pk>/', views.check, name='check'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('main/', views.main, name='main'),
    path('flavor/', views.flavor, name='flavor'),
    path('loginpage/', views.loginpage, name='login'),
    path('newaccount/', views.UserFormView.as_view(), name='newaccount'),
    path('logout_user/', views.logout_user, name='logout_user'),
]
