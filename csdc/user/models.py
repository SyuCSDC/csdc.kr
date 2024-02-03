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
        return self.user.username
