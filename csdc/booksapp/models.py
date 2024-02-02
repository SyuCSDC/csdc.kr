from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_mentor = models.BooleanField(default=False)  # 멘토인지 멘티인지 구분
    department = models.CharField(max_length=100)  # 학과
    bio = models.CharField(max_length=255 , blank=True , null=True) 

    def __str__(self):
        return self.user.username


class Book(models.Model):
    title = models.CharField(max_length=255)  # 책 제목
    author = models.CharField(max_length=100)  # 저자

    def __str__(self):
        return self.title

class Mentorship(models.Model):
    mentor = models.ForeignKey(Profile, related_name='mentorship_mentor', on_delete=models.CASCADE)
    mentee = models.ForeignKey(Profile, related_name='mentorship_mentee', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField()  # 시작 날짜
    end_date = models.DateField()  # 종료 날짜
    deposit = models.DecimalField(max_digits=10, decimal_places=2, default=10000)  # 보증금

    def __str__(self):
        return self.book.title

class Report(models.Model):
    mentorship = models.ForeignKey(Mentorship, on_delete=models.CASCADE)
    submission_date = models.DateField()  # 제출 날짜
    content = models.TextField()  # 보고서 내용
    is_approved = models.BooleanField(default=False)  # 승인 여부


