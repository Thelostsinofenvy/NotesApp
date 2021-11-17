from django.db import models

# Create your models here.


class Notes(models.Model):
    name = models.CharField(max_length=60)
    text = models.TextField(max_length=300)
