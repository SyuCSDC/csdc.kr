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
    

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
    type = models.IntegerField(default=1)
    commenter = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content