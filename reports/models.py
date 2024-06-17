from django.db import models
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=200, null=True)
    book_author = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"- {self.title}"