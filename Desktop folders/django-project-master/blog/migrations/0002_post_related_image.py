# Generated by Django 3.0.3 on 2020-05-07 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='related_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]