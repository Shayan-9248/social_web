# Generated by Django 3.1.7 on 2021-04-08 20:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210408_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relation',
            name='from_user',
        ),
        migrations.AddField(
            model_name='relation',
            name='from_user',
            field=models.ManyToManyField(related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='relation',
            name='to_user',
        ),
        migrations.AddField(
            model_name='relation',
            name='to_user',
            field=models.ManyToManyField(related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
