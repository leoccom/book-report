# Generated by Django 5.0.6 on 2024-06-30 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0009_alter_report_book_author_alter_report_book_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="book_author",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="report",
            name="book_title",
            field=models.CharField(max_length=200),
        ),
    ]
