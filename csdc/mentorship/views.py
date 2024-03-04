# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mentorship
from user.models import UserProfile
from .forms import MentorshipForm
from django.contrib.auth.decorators import login_required ,user_passes_test

# 사용자 역할이 멘토인지 확인하는 함수
def is_mentor(user):
    return user.userprofile.role == 'Mentor'

# 멘토만 접근 가능한 데코레이터
mentor_required = user_passes_test(is_mentor, login_url='/users/login/')

#현재 진행중인 모든 멘토링
@login_required
def list_mentorships(request):
     # 현재 로그인한 사용자의 UserProfile 인스턴스를 가져옵니다.
    # user_profile = UserProfile.objects.get(user=request.user)
    # mentorships = Mentorship.objects.filter(mentor=user_profile) | Mentorship.objects.filter(mentee=user_profile)
    mentorships = Mentorship.objects.all()
    return render(request, 'mentorships/list_mentorships.html', {'mentorships': mentorships})

# 멘토링 생성
@login_required
@mentor_required
def create_mentorship_request(request):
    if request.method == 'POST':
        form = MentorshipForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            # 폼에서 입력받은 데이터로 Mentorship 객체 생성
            mentorship = form.save(commit=False)
            # 현재 로그인한 사용자의 UserProfile 인스턴스를 mentor 필드에 할당
            mentor_user_profile = UserProfile.objects.get(user=request.user)
            mentorship.mentor = mentor_user_profile
            mentorship.save() 

            mentees = form.cleaned_data['mentees']
            print(mentees)
            mentorship.mentee.set(mentees)
            return redirect('../mentorship_list/')  # 생성 후 멘토십 목록 페이지로 이동
    else:
        form = MentorshipForm()
    
    return render(request, 'mentorships/create_mentorship_request.html', {'form': form})

# 멘토링 수정
@login_required
@mentor_required
def edit_mentorship(request, pk):
    mentorship = get_object_or_404(Mentorship, pk=pk)
    if request.method == "POST":
        form = MentorshipForm(request.POST, instance=mentorship)
        if form.is_valid():
            # 폼에서 입력받은 데이터로 Mentorship 객체를 일단 저장하지만, ManyToMany 관계는 아직 업데이트하지 않음
            mentorship = form.save(commit=False)
            mentorship.save()  # Mentorship 인스턴스를 DB에 저장. 이 때, ManyToMany 필드는 저장되지 않음
            # form.cleaned_data에서 'mentee' 필드 값을 가져와서 set 메서드를 사용해 업데이트
            mentorship.mentee.set(form.cleaned_data['mentees'])
            return redirect('../mentorship_list/')  # 멘토십 목록 페이지로 리다이렉션
    else:
        form = MentorshipForm(instance=mentorship, initial={'mentees': mentorship.mentee.all()})
    return render(request, 'mentorships/edit_mentorship.html', {'form': form})


#멘토링 삭제
@login_required
@mentor_required
def delete_mentorship(request, pk):
    mentorship = get_object_or_404(Mentorship, pk=pk)
    
    # 멘토십 삭제 처리
    if request.method == "POST":
        mentorship.delete()
        return redirect('mentorship:list_mentorships')  # 멘토십 목록 페이지로 리다이렉션
    
    return render(request, 'mentorships/delete_mentorship.html', {'mentorship': mentorship})


# @login_required
# def mentorship_detail(request, id):
#     mentorship = get_object_or_404(Mentorship, id=id)
#     return render(request, 'mentorships/mentorship_detail.html', {'mentorship': mentorship})
