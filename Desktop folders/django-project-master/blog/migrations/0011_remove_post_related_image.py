# Generated by Django 3.0.3 on 2021-02-27 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200512_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='related_image',
        ),
    ]
