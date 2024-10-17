from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('home/', views.home_page, name='home'),
    path('user/', views.user_page, name='user'),
    path('album/', views.album_page, name='album'),
    path('photo/', views.photo_page, name='photo'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup')
]
