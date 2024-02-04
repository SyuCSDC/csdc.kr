from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/reports/report_list/')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


