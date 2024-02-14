from django.urls import path
from . import views
from .views import UserLoginView
from django.contrib.auth import views as auth_views
from config import settings
from django.urls import reverse_lazy
app_name = "user"

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
