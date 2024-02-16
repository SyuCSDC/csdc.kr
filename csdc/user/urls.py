from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from config import settings
from django.urls import reverse_lazy
app_name = "user"

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
