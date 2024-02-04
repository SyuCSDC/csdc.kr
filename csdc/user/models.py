# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# 사용자 프로필 모델
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    student_id = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=(('Mentor', 'Mentor'), ('Mentee', 'Mentee')))
    bio = models.TextField('한 줄 소개')

    def __str__(self):
        # User 모델의 first_name과 last_name을 사용하여 전체 이름 반환
        full_name = f"{self.user.first_name} {self.user.last_name}".strip()
        return full_name if full_name else self.user.username