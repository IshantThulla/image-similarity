# Generated by Django 3.0.3 on 2020-05-08 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_related_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='related_image',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]
