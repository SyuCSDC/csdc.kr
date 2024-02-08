from django import forms
from .models import Mentorship 
from user.models import UserProfile

class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        # obj는 UserProfile 객체입니다. 여기서 원하는 문자열 형태로 반환합니다.
        return f"{obj.student_id} - {obj.user.last_name}{obj.user.first_name}"

class MentorshipForm(forms.ModelForm):
    mentee = CustomModelChoiceField(
        queryset=UserProfile.objects.filter(role='Mentee').order_by('student_id'),
        label="멘티 선택",
        help_text="멘토링을 받을 멘티를 선택해주세요.",
        widget=forms.Select(attrs={'name': 'mentee'})
    )
    
    class Meta:
        model = Mentorship
        fields = ['mentee', 'book', 'start_date', 'end_date', 'status']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(MentorshipForm, self).__init__(*args, **kwargs)
        
    #     # 멘티 선택 필드에 학번과 이름을 함께 표시하기 위해 옵션 리스트를 생성합니다.
    #     mentee_choices = [(profile.student_id, f"{profile.student_id} - {profile.user.last_name}{profile.user.first_name} ") for profile in UserProfile.objects.filter(role='Mentee')]
        
    #     # 선택 필드의 choices 속성을 설정합니다.
    #     self.fields['mentee'].choices = mentee_choices