# Generated by Django 5.0.6 on 2024-06-30 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0004_librarybook_alter_profile_favorite_books_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="favorite_books",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="read_later_books",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name="LibraryBook",
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
