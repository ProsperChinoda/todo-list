from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TODO(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    color = models.CharField(max_length=6, default='FFFFFF')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title