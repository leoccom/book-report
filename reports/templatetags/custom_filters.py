import time
from django import template
from django.utils import timezone
import math

register = template.Library()

@register.filter(name="time_ago")
def time_ago(value):
    now = timezone.now()
    delta = now - value

    years = math.floor(delta.days / 365)
    months = math.floor(delta.days / 30)
    weeks = math.floor(delta.days / 7)
    days = delta.days

    if years > 0:
        return f"{years} year{'s' if years > 1 else ''} ago"
    elif months > 0:
        return f"{months} month{'s' if months > 1 else ''} ago"
    elif weeks > 0:
        return f"{weeks} week{'s' if weeks > 1 else ''} ago"
    elif days > 0:
        return f"{days} day{'s' if days > 1 else ''} ago"
    else:
        return "Today"