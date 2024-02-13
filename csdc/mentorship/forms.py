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
        empty_label="멘티 선택",
        widget=forms.Select(attrs={'name': 'mentee'})
    )

    
    class Meta:
        model = Mentorship
        fields = ['mentee', 'book', 'start_date', 'end_date', 'status']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(attrs={'placeholder': 'Add notes to question here'}),
        }

    def __init__(self, *args, **kwargs):
        super(MentorshipForm, self).__init__(*args, **kwargs)
        self.fields['book'].empty_label = "책을 선택해주세요."
        self.fields['status'].empty_label = None