# Generated by Django 5.0.6 on 2024-06-30 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_profile_delete_userbookpreferences"),
    ]

    operations = [
        migrations.CreateModel(
            name="LibraryBook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("published_date", models.DateField()),
                ("description", models.TextField()),
                ("cover_image", models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name="profile",
            name="favorite_books",
            field=models.ManyToManyField(
                blank=True, related_name="favorited_by", to="books.librarybook"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="read_later_books",
            field=models.ManyToManyField(
                blank=True, related_name="read_later_by", to="books.librarybook"
            ),
        ),
    ]
