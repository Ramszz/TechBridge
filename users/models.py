from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model for TechBridge backend.
    Distinguishes students and alumni with a 'role' field and basic profile fields.
    """
    ROLE_CHOICES = (
        ("student", "Student"),
        ("alumni", "Alumni"),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")
    branch = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=200, blank=True)
    headline = models.CharField(max_length=250, blank=True)
    skills = models.TextField(blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
