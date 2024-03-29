from django.shortcuts import render, redirect 
from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView , PasswordResetCompleteView 
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView , UpdateView
from django.urls import reverse_lazy
from user.models import UserProfile

import os

from .forms import UserLoginForm, UserRegisterForm, CustomPasswordResetForm, CustomPasswordResetConfirmForm , UserProfileForm

class UserLoginView(LoginView):
    template_name = 'user/auth/login.html'
    authentication_form = UserLoginForm

class UserRegisterView(TemplateView):
    template_name = 'user/auth/register.html'
    
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
    subject_template_name='user/auth/email/password_reset_subject.txt'
    email_template_name='user/auth/email/password_reset_email.txt'
    html_email_template_name='user/auth/email/password_reset_email.txt'
    form_class=CustomPasswordResetForm
    success_url = reverse_lazy('user:password_reset_done')
    
    def form_valid(self, form):
        email = self.request.POST['email']
        student_id = self.request.POST['student_id']
        try:
            UserProfile.objects.get(user__email=email, student_id=student_id)
            self.request.session['email'] = email
            return super().form_valid(form)
        except UserProfile.DoesNotExist:
            form.add_error(None, "입력하신 정보를 찾을 수 없습니다. 다시 확인해주세요.")
            return self.form_invalid(form)

class MyPasswordResetChangeView(PasswordResetConfirmView):
    success_url = reverse_lazy('user:password_reset_complete')
    form_class = CustomPasswordResetConfirmForm

class CustomPasswordResetDoneView(PasswordResetDoneView):
    def get(self, request, *args, **kwargs):
        if 'email' not in request.session:
            return redirect(reverse_lazy('index'))
        return super().get(request, *args, **kwargs)
    
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    def get(self, request, *args, **kwargs):
        if 'email' not in request.session:
            return redirect(reverse_lazy('index'))
        del request.session['email']
        return super().get(request, *args, **kwargs)

class MyforgotidView(TemplateView):
    template_name = 'user/auth/option/forgot_id.html'

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
            context['error'] = "입력하신 정보를 찾을 수 없습니다. 다시 확인해주세요."

        return render(request , self.template_name, context)       
    


@method_decorator(login_required, name='dispatch')
class UserProfileUpdateView(UpdateView):
    model = UserProfile
    template_name = 'user/profile.html' 
    success_url = reverse_lazy('about') 
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        return UserProfile.objects.get(user=self.request.user)

    def form_valid(self, form):
        profile = self.get_object()
        new_image = form.cleaned_data.get('profile_img')
        if new_image:
            if profile.profile_img:
                old_image_path = profile.profile_img.path
                if os.path.basename(old_image_path) != 'default-profile.png':
                    if 'profile_img/' + os.path.basename(old_image_path) != new_image:
                        if os.path.isfile(old_image_path):
                            os.remove(old_image_path)
        
        form.save()
        return super(UserProfileUpdateView, self).form_valid(form)