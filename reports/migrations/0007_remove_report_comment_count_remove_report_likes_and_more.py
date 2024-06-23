# Generated by Django 5.0.6 on 2024-06-23 10:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_report_comment_count_report_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='comment_count',
        ),
        migrations.RemoveField(
            model_name='report',
            name='likes',
        ),
        migrations.AddField(
            model_name='report',
            name='user_likes',
            field=models.ManyToManyField(blank=True, related_name='liked_reports', to=settings.AUTH_USER_MODEL),
        ),
    ]