from django.db import models


# Create your models here.

class Poll(models.Model):
    texto = models.CharField(max_length=255)
