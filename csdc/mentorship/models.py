# Create your models here.
from django.db import models
from user.models import UserProfile
from report.models import Book 

class Mentorship(models.Model):
    mentor = models.ForeignKey(UserProfile, related_name='mentorships_as_mentor', on_delete=models.CASCADE)
    mentee = models.ManyToManyField(UserProfile, related_name='mentorships_as_mentee')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Book 모델과의 연결
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=(('', '상태를 선택하세요'),('Active', '활동'), ('Completed', '완료'), ('Pending', '보류')))

    def get_mentees_display(self):
        return ", ".join([mentee.user.get_full_name() for mentee in self.mentee.all()])

    def __str__(self):
        mentees_str = ", ".join([mentee.user.username for mentee in self.mentee.all()])
        return f"{self.mentor.user.username} mentoring {mentees_str} for {self.book.title}"
