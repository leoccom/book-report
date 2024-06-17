from django.db import models
from django.contrib.auth.models import User
from reports.models import Report

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"Comment by {self.user.username} on {self.report.title}"