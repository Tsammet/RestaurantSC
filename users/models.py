from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    USER_ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default = 'user')

    def __str__(self):
        return self.user.username