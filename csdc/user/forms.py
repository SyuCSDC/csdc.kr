from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    grade = forms.CharField(max_length=10, required=False, label="학년")
    student_id = forms.CharField(max_length=20, required=False, label="학번")
    bio = forms.CharField(widget=forms.Textarea, required=False, label="한 줄 소개")
    role = forms.ChoiceField(choices=(('Mentor', 'Mentor'), ('Mentee', 'Mentee')), required=True, label="Role")

    class Meta:
        model = User
        fields = ['username','last_name','first_name' ,'email', 'password1', 'password2','grade', 'student_id' ,'role', 'bio']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            # User 모델 저장 후 UserProfile 모델에 데이터 저장
            UserProfile.objects.create(
                user=user,
                grade=self.cleaned_data['grade'],
                student_id=self.cleaned_data['student_id'],
                role=self.cleaned_data['role'],
                bio=self.cleaned_data['bio'],
            )
        return user