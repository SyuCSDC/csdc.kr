from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 사용자 프로필에 역할 저장
            UserProfile.objects.create(user=user, role=form.cleaned_data['role'])
            login(request, user)
            return redirect('/report/reports/')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


