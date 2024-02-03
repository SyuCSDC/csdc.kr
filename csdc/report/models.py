# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# 책 모델
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    needed_copies = models.IntegerField(default=1)

    def __str__(self):
        return self.title
    

# 보고서 모델
class Report(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Report on {self.book.title} by {self.submitter.username}'
    
class ReportFile(models.Model):
    report = models.ForeignKey(Report, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
