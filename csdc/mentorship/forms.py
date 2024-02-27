from django import forms
from .models import Mentorship 
from django.core.exceptions import ValidationError
from user.models import UserProfile

class CustomModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        # obj는 UserProfile 객체입니다. 여기서 원하는 문자열 형태로 반환합니다.
        return f"{obj.student_id} - {obj.user.last_name}{obj.user.first_name}"

class MentorshipForm(forms.ModelForm):
    mentees = CustomModelMultipleChoiceField(
        queryset=UserProfile.objects.filter(role='Mentee').order_by('student_id'),
        widget=forms.SelectMultiple(attrs={'name': 'mentees'})
    )
    
    def __init__(self, *args, **kwargs):
        super(MentorshipForm, self).__init__(*args, **kwargs)
        
        self.fields['mentees'].empty_label = "멘티를 선택해주세요."
        self.fields['mentees'].widget.attrs.update({'class': 'form-select'})
        self.fields['book'].empty_label = '책을 선택해주세요.'
        self.fields['book'].widget.attrs.update({'class': 'form-select'})
        self.fields['start_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-select'})
    
    class Meta:
        model = Mentorship
        fields = ['mentees', 'book', 'start_date', 'end_date', 'status']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        # 시작 날짜와 종료 날짜 비교
        if end_date and start_date and end_date < start_date:
            raise ValidationError("종료 날짜는 시작 날짜보다 뒤에 있어야 합니다.")

        return cleaned_data
