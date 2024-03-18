from django.shortcuts import render

from user.models import User, UserProfile

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html', {
        'admins': User.objects.filter(is_superuser=True),
        'mentors': UserProfile.objects.filter(role='Mentor'),
        'mentees': UserProfile.objects.filter(role='Mentee'),
    })

def privacypolicy(request):
    return render(request, 'privacypolicy.txt')

def tos(request):
    return render(request, 'ToS.txt' )