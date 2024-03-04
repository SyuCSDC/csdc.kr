from django.db import models
from django.utils import timezone
from user.models import UserProfile

class Board(models.Model):
    type = models.IntegerField(default=1) # 0: notice / 1: free
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='board')

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title