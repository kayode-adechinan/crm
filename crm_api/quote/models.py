from django.db import models

# Create your models here.
class Quote(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)