from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    Permission,
    _user_get_permissions
)
from django.contrib.auth.models import PermissionsMixin
from django.db.models.signals import post_save


class UserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email,
            username,
            password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    permission = models.ManyToManyField(Permission, related_name='users')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def get_user_permissions(self, obj=None):
        return _user_get_permissions(self, obj, 'user')
    
    def get_all_permissions(self, obj=None):
        return _user_get_permissions(self, obj, 'all')


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


class Relation(models.Model):
    STATUS = (
        ('a', 'accept'),
        ('r', 'reject'),
    )
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower', null=True, blank=True)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.from_user.username} following {self.to_user.username}'