# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mentorship
from user.models import UserProfile
from .forms import MentorshipForm
from django.contrib.auth.decorators import login_required ,user_passes_test
from django.db.models import Sum

# 사용자 역할이 멘토인지 확인하는 함수
def is_mentor(user):
    return user.userprofile.role == 'Mentor'

# 멘토만 접근 가능한 데코레이터
mentor_required = user_passes_test(is_mentor, login_url='/')

#현재 진행중인 모든 멘토링
@login_required
def list_mentorships(request):
    #  # 현재 로그인한 사용자의 UserProfile 인스턴스를 가져옵니다.
    # # user_profile = UserProfile.objects.get(user=request.user)
    # # mentorships = Mentorship.objects.filter(mentor=user_profile) | Mentorship.objects.filter(mentee=user_profile)
    # mentorships = Mentorship.objects.all()

    mentorships_with_scores = Mentorship.objects.annotate(
        total_score=Sum('weeklyscore__score')
    ).order_by('-total_score')

    mentorships_with_ranks = []
    last_score = None
    last_rank = 0
    for index, mentorship in enumerate(mentorships_with_scores, start=1):
        if mentorship.total_score != last_score:
            last_rank = index
            last_score = mentorship.total_score
        mentorship.rank = last_rank
        mentorships_with_ranks.append(mentorship)

    return render(request, 'mentorships/list_mentorships.html', {'mentorships': mentorships_with_ranks})

# 멘토링 생성
@login_required
@mentor_required
def create_mentorship_request(request):
    if request.method == 'POST':
        form = MentorshipForm(request.POST or None, request=request)
        if form.is_valid():
            # 폼에서 입력받은 데이터로 Mentorship 객체 생성
            mentorship = form.save(commit=False)
            # 현재 로그인한 사용자의 UserProfile 인스턴스를 mentor 필드에 할당
            mentor_user_profile = UserProfile.objects.get(user=request.user)
            mentorship.mentor = mentor_user_profile
            mentorship.save() 

            mentees = form.cleaned_data['mentees']
            mentorship.mentee.set(mentees)

            return redirect('../mentorship_list/')  # 생성 후 멘토십 목록 페이지로 이동
        else:
            #멘토링에 이미 참여하고 있는 멘티의 ID 목록
            engaged_mentee_ids = Mentorship.objects.values_list('mentee__id', flat=True)
            # 멘티 역할을 가진 사용자 중에서, 멘토링에 참여하지 않은 사용자만 필터링
            available_mentees = UserProfile.objects.filter(role='Mentee').exclude(id__in=engaged_mentee_ids)
            form.fields['mentees'].queryset = available_mentees
    else:
        form = MentorshipForm(request=request)
        #멘토링에 이미 참여하고 있는 멘티의 ID 목록
        engaged_mentee_ids = Mentorship.objects.values_list('mentee__id', flat=True)
        # 멘티 역할을 가진 사용자 중에서, 멘토링에 참여하지 않은 사용자만 필터링
        available_mentees = UserProfile.objects.filter(role='Mentee').exclude(id__in=engaged_mentee_ids)
        form.fields['mentees'].queryset = available_mentees

    return render(request, 'mentorships/create_mentorship_request.html', {'form': form})

# 멘토링 수정
@login_required
@mentor_required
def edit_mentorship(request, pk):
    mentorship = get_object_or_404(Mentorship, pk=pk)
    if request.method == "POST":
        form = MentorshipForm(request.POST or None, instance=mentorship , request=request) 
        
        if form.is_valid():
            # 폼에서 입력받은 데이터로 Mentorship 객체를 일단 저장하지만, ManyToMany 관계는 아직 업데이트하지 않음
            mentorship = form.save(commit=False)
            mentorship.save()  # Mentorship 인스턴스를 DB에 저장. 이 때, ManyToMany 필드는 저장되지 않음
            # form.cleaned_data에서 'mentee' 필드 값을 가져와서 set 메서드를 사용해 업데이트
            mentorship.mentee.set(form.cleaned_data['mentees'])
            return redirect('../mentorship_list/')  # 멘토십 목록 페이지로 리다이렉션
    else:
        form = MentorshipForm(instance=mentorship, request=request, initial={'mentees': mentorship.mentee.all()})
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
