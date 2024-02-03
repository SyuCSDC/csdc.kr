from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "user"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    # 추가적인 URL 패턴이 필요할 경우 여기에 정의
]
