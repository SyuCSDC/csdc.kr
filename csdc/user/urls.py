from django.urls import path
from . import views 
from .views import MyPasswordResetView , MyPasswordResetChangeView
from django.contrib.auth import views as auth_views 
from config import settings
from django.urls import reverse_lazy

app_name = "user"

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/' , MyPasswordResetView.as_view(template_name='user/password_reset.html',), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', MyPasswordResetChangeView.as_view(template_name='user/password_reset_confirm.html' ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html' ), name='password_reset_complete'),
    ]
