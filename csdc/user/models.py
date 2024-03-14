# Create your models here.

from django.db import models
from django.contrib.auth.models import User

GRADE_CHOICES = (
    ('', '학년을 선택해주세요'),
    ('1', '1학년'),
    ('2', '2학년'),
    ('3', '3학년'),
    ('4', '4학년'),
)

DEPARTMENT_CHOICES=(('', '과를 선택해주세요'),
                     ('빅데이터 클라우드공학과',
                       '빅데이터 클라우드공학과'),
                         ('컴퓨터공학부', '컴퓨터공학부'))

ROLE_CHOICES=(('', '역할을 선택해주세요.'), ('Mentor', 'Mentor'), ('Mentee', 'Mentee'))

# 사용자 프로필 모델
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10, choices=GRADE_CHOICES)
    student_id = models.CharField(max_length=20)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES , default='컴퓨터공학부')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    bio = models.TextField('한 줄 소개',blank=True)
    profile_img = models.ImageField(upload_to='profile_img/', default='profile_img/default-profile.png')
    
    def __str__(self):
        # User 모델의 first_name과 last_name을 사용하여 전체 이름 반환
        full_name = f"{self.user.last_name}{self.user.first_name} ".strip()
        return f"{full_name} ({self.student_id})" if full_name else f"{self.user.username}({self.student_id})"