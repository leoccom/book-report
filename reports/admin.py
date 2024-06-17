from django.contrib import admin
from .models import Report

# Register your models here.
class ReportAdmin(admin.ModelAdmin):
    list_display = ["user", "book_title", "book_author", "created_at"]

admin.site.register(Report, ReportAdmin)