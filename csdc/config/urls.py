"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path ,include
from django.conf import settings
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('' , views.index, name='index'),
    path('about/', views.about, name='about'),
    path('privacypolicy/' , views.privacypolicy, name='privacypolicy'),
    path('tos/' , views.tos, name='tos'),
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('reports/' , include('report.urls')),
    path('mentorship/' , include('mentorship.urls')),
    path('boards/', include('board.urls')),
    path('chat/', views.chat_view,name='chat'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # media 경로 추가