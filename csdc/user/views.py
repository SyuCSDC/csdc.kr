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


class MyPasswordResetView(PasswordResetView):
    subject_template_name='user/password_reset_subject.txt',  # 수정: 파일 이름을 제목용으로 변경
    email_template_name='user/password_reset_email.html',
    html_email_template_name='user/password_reset_email.html',
    success_url = reverse_lazy('user:password_reset_done') 

class MyPasswordResetChangeView(PasswordResetConfirmView):
    success_url = reverse_lazy('user:password_reset_complete')


class MyforgotidView(TemplateView):
    template_name = 'user/forgot_id.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        context = {}
        email = request.POST.get('email')
        student_id = request.POST.get('student_id')

        try:
            user_profile = UserProfile.objects.get(user__email=email, student_id=student_id)
            print(user_profile)
            user_id = user_profile.user.username # 또는 필요한 다른 식별자
            context['user_id'] = user_id  
        except UserProfile.DoesNotExist:
            context['error'] = "No user found with the provided information."

        return render(request , self.template_name, context)       