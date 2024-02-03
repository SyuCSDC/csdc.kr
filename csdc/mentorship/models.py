# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from report.models import Book 

class Mentorship(models.Model):
    mentor = models.ForeignKey(User, related_name='mentorships_as_mentor', on_delete=models.CASCADE)
    mentee = models.ForeignKey(User, related_name='mentorships_as_mentee', on_delete=models.CASCADE)
    start_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=(('Active', 'Active'), ('Completed', 'Completed'), ('Pending', 'Pending')))

    def __str__(self):
        return f"{self.mentor.username} mentoring {self.mentee.username}"
