from django.shortcuts import render

from user.models import UserProfile

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html', { 'users': UserProfile.objects.filter(role='Mentor') })