# Create your models here.
from django.db import models
from django.db.models.constraints import UniqueConstraint
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
        mentor_full_name = f"{self.mentor.user.last_name}{self.mentor.user.first_name}".strip()
        mentee_names = [f"{mentee.user.last_name}{mentee.user.first_name}".strip() for mentee in self.mentee.all()]
        mentees_str = ", ".join(mentee_names)
        return f"{mentor_full_name} mentoring {mentees_str} for {self.book.title}"
    

class WeeklyScore(models.Model):
    mentorship = models.ForeignKey(Mentorship, on_delete=models.CASCADE)
    week = models.PositiveIntegerField()
    score = models.PositiveIntegerField() 

    class Meta:
        constraints = [
            UniqueConstraint(fields=['mentorship', 'week'], name='unique_mentorship_week')
        ]

    def __str__(self):
        return f"{self.mentorship.mentor}"