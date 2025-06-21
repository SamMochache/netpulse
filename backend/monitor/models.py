from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('analyst', 'Analyst'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='analyst')

    def __str__(self):
        return f"{self.username} ({self.role})"

class ScanResult(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='scan_results'
    )
    subnet = models.CharField(max_length=100)
    results = models.JSONField()  # Stores scanned hosts info (IP, hostname, state, etc.)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.subnet} @ {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"