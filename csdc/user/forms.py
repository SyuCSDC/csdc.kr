from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    # 역할 선택을 위한 필드 추가
    role = forms.ChoiceField(choices=(('Mentor', 'Mentor'), ('Mentee', 'Mentee')), required=True, label="Role")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
