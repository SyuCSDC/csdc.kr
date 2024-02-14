from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserLoginForm, UserRegisterForm

from django.contrib.auth.views import LoginView

class UserLoginView(LoginView):
    template_name = 'user/login.html'
    authentication_form = UserLoginForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/reports/book_list/')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


