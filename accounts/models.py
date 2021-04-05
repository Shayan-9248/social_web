from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.user.username


def user_profile_save(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile(user=kwargs['instance'])
        user_profile.save()

post_save.connect(user_profile_save, sender=User)
