from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Reviews(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    review = models.TextField()

    def __str__(self):
        return self.title