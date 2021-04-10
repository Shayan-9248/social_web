# Generated by Django 3.1.7 on 2021-04-08 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210408_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='relation',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'accept'), ('p', 'pending'), ('r', 'reject')], max_length=30),
        ),
    ]