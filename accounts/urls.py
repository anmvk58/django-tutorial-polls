from django.urls import path
from django.contrib.auth import views as authentication_views
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', views.register, name='logout')
]