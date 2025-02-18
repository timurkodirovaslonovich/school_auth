from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, default='student')
    name = models.CharField(max_length=120, default='')
    surname = models.CharField(max_length=120, default='')
    username = models.CharField(max_length=120, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    age = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.username} ({self.role})"
