from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from .models import UserProfile , GRADE_CHOICES  , DEPARTMENT_CHOICES , ROLE_CHOICES


class UserLoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": mark_safe("아이디 또는 비밀번호를 잘못 입력했습니다. <br /> 입력하신 내용을 다시 확인해주세요."),
    }
    
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].label = '아이디'
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].label = '비밀번호'
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

class UserRegisterForm(UserCreationForm):
    grade = forms.ChoiceField(choices=(('','학년을 선택해주세요.'), ('1','1'), ('2','2') ,('3','3'), ('4','4')), required=True, label='학년')
    student_id = forms.CharField(max_length=20, required=True, label='학번')
    department = forms.ChoiceField(choices=(('','과를 선택해주세요.'),('빅데이터 클라우드공학과','빅데이터 클라우드공학과'),('컴퓨터공학부','컴퓨터공학부')), required=True, label='Department')
    role = forms.ChoiceField(choices=(('', '역할을 선택해주세요.'), ('Mentor', 'Mentor'), ('Mentee', 'Mentee')), required=True, label='Role')
    bio = forms.CharField(widget=forms.Textarea, required=False, label='한 줄 소개')
    class Meta:
        model = User
        fields = ['username','last_name','first_name' ,'email', 'password1', 'password2','grade', 'student_id', 'department' ,'role', 'bio']
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name:
            raise forms.ValidationError('성을 입력해주세요.')
        return last_name
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name:
            raise forms.ValidationError('이름을 입력해주세요.')
        return first_name
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError('이메일을 입력해주세요.')
        return email
    
    # def clean_grade(self):
    #     grade = self.cleaned_data['grade']
    #     if not grade:
    #         raise forms.ValidationError('학년을 입력해주세요.')
    #     return grade
    
    def clean_student_id(self):
        student_id = self.cleaned_data['student_id']
        if not student_id:
            raise forms.ValidationError('학번을 입력해주세요.')
        return student_id
    
    # def clean_bio(self):
    #     bio = self.cleaned_data['bio']
    #     if not bio:
    #         raise forms.ValidationError('한 줄 소개를 입력해주세요.')
    #     return bio

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        # if commit:
        #     user.save()
        #     UserProfile.objects.create(
        #         user=user,
        #         grade=self.cleaned_data['grade'],
        #         student_id=self.cleaned_data['student_id'],
        #         department=self.cleaned_data['department'],
        #         role=self.cleaned_data['role'],
        #         bio=self.cleaned_data['bio'],
        #     )
        if commit:
            user.save()
            profile = UserProfile.objects.create(
                user=user,
                profile_img='static/default-profile.png',
                grade=self.cleaned_data['grade'],
                student_id=self.cleaned_data['student_id'],
                department=self.cleaned_data['department'],
                role=self.cleaned_data['role'],
                bio=self.cleaned_data['bio'],
            )
            profile.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            
        self.fields['username'].label = '아이디'
        
        self.fields['grade'].widget.attrs.update({'class': 'form-select'})
        self.fields['role'].widget.attrs.update({'class': 'form-select'})
        self.fields['department'].widget.attrs.update({'class': 'form-select'})
        
class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)
    
    student_id = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '학번을 입력하세요.',
    }))
    
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': '이메일을 입력하세요.',
    }))

class CustomPasswordResetConfirmForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetConfirmForm, self).__init__(*args, **kwargs)
    
    new_password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '새 비밀번호를 입력하세요.',
    }))
    
    new_password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '새 비밀번호를 다시 입력하세요.',
    }))

class UserProfileForm(forms.ModelForm):
    profile_img = forms.ImageField(
        required=False,  # 필수가 아닌 경우
        widget=forms.FileInput(
            attrs={
                'class' : 'form-control',
                'onchange': 'previewImage(this);'
                }
            )
        )
    
    grade = forms.ChoiceField(
        required=True,
        choices=GRADE_CHOICES,  
        widget=forms.Select(
            attrs={
                'class': 'form-select form-select'
            }
        ),
   
    )
    
    student_id = forms.CharField(
        required=True,  
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control'
            }
        )
    )

    department = forms.ChoiceField(
        choices=DEPARTMENT_CHOICES,
        required=True,  
        widget=forms.Select(
            attrs={
                'class': 'form-select form-select'
            }
        ),
    )

    role = forms.ChoiceField(
        choices=ROLE_CHOICES, 
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-select form-select'
            }
        ),
    )

    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control'
            }
        )
    )

    class Meta:
        model = UserProfile
        fields = ['profile_img','grade', 'student_id', 'department', 'role', 'bio'] 
        
        def __init__(self, *args, **kwargs):
            super(UserRegisterForm, self).__init__(*args, **kwargs)
            
            