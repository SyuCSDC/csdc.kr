# Create your models here.
from django.db import models
from user.models import UserProfile
from report.models import Book 

class Mentorship(models.Model):
    mentor = models.ForeignKey(UserProfile, related_name='mentorships_as_mentor', on_delete=models.CASCADE)
    mentee = models.ForeignKey(UserProfile, related_name='mentorships_as_mentee', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Book 모델과의 연결
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=(('', '상태를 선택하세요'),('Active', '활동'), ('Completed', '완료'), ('Pending', '보류')))

    def __str__(self):
        return f"{self.mentor.user.username} mentoring {self.mentee.user.username} for {self.book.title}"
