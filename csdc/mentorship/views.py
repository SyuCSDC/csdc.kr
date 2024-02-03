# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mentorship
from django.contrib.auth.decorators import login_required

@login_required
def list_mentorships(request):
    mentorships = Mentorship.objects.filter(mentor=request.user) | Mentorship.objects.filter(mentee=request.user)
    return render(request, 'mentorships/list_mentorships.html', {'mentorships': mentorships})

@login_required
def create_mentorship_request(request):
    # 여기서 멘토십 요청 생성 로직 구현
    # 폼 처리 후 Mentorship 객체 생성
    return render(request, 'mentorships/create_mentorship_request.html')

@login_required
def mentorship_detail(request, id):
    mentorship = get_object_or_404(Mentorship, id=id)
    return render(request, 'mentorships/mentorship_detail.html', {'mentorship': mentorship})
