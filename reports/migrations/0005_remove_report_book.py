# Generated by Django 5.0.6 on 2024-06-14 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_report_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='book',
        ),
    ]
