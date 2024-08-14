from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
