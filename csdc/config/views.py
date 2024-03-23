from django.shortcuts import render
from django.http import JsonResponse  
from django.conf import settings
from user.models import User, UserProfile
from .utils import chat_with_gpt

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

def chat_view(request):
    if request.method == 'POST': 
        prompt = request.POST.get('prompt')
        response = chat_with_gpt(str(prompt))
        return JsonResponse({'response': response}) # JSON 응답 반환
    else:
        return render(request, 'chat_temp.html')