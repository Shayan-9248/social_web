# Generated by Django 3.1.7 on 2021-07-18 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20210413_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='1.jpg', upload_to=''),
        ),
    ]