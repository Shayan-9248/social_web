# Standard library import
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address


class Post(TimeStamp):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(default='1.jpg')
    like = models.ManyToManyField(User, blank=True, related_name='like')
    dislike = models.ManyToManyField(User, blank=True, related_name='dislike')
    visit_count = models.ManyToManyField(IPAddress, blank=True)
    favourite = models.ManyToManyField(User, blank=True, related_name='favourites')

    class Meta(TimeStamp.Meta):
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user.username} - {self.title[:20]}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('post:detail', args=[self.slug, self.id])

    def like_count(self):
        return self.like.count()
    
    def dislike_count(self):
        return self.dislike.count()
    
    def sum_visit_count(self):
        return self.visit_count.count()


class Comment(TimeStamp):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='user_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
     related_name='post_comment')
    comment = models.TextField()
    reply = models.ForeignKey('self', on_delete=models.CASCADE,
     related_name='reply_comment')
    is_reply = models.BooleanField(default=False)
    show = models.BooleanField(default=False)

    class Meta(TimeStamp.Meta):
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user.username} - {self.post.title}'