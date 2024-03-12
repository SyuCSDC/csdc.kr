from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView ,PasswordResetView , PasswordResetConfirmView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from user.models import UserProfile

from .forms import UserLoginForm, UserRegisterForm 

class UserLoginView(LoginView):
    template_name = 'user/login.html'
    authentication_form = UserLoginForm

class UserRegisterView(TemplateView):
    template_name = 'user/register.html'
    
    def get(self, request):
        form = UserRegisterForm()
        
        return render(request, self.template_name, { 'form': form })
    
    def post(self, request):
        form = UserRegisterForm(request.POST)
        
        if not form.is_valid():
            return render(request, self.template_name, { 'form': form })
        
        user = form.save()
        login(request, user)
        
        return redirect('/')
