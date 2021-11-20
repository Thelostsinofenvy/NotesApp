from django.db import models
from django.utils import timezone

# Create your models here.


class Note(models.Model):
    name = models.CharField(max_length=60, editable=True)
    text = models.TextField(max_length=300, null=True, blank=True)
    date_created = models.DateTimeField(
        default=timezone.datetime.now())

    def __str__(self):
        return self.name
