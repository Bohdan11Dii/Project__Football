from django.urls import path
from . import views
from team.views import RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('basic/', views.basic, name="basic"),
    path('first/', views.first, name="first"),
    path('players', views.players, name='players'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
    path('bloh', views.bloh, name='bloh'),
    path('registerform/', views.registerform, name="registerform"),
    path('loginform/', views.loginform, name="loginform"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='team/index.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name="logout"),

]


