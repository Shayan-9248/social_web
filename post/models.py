from django.db import models
from accounts.models import User


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Post(TimeStamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    description = models.TextField()
    image = models.ImageField(default='1.jpg')

    def __str__(self):
        return f'{self.user} - {self.title[:20]}'