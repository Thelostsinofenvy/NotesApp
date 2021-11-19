from django.db import models

# Create your models here.


class Notes(models.Model):
    name = models.CharField(max_length=60, editable=True)
    text = models.TextField(max_length=300, null=True, blank=True)
