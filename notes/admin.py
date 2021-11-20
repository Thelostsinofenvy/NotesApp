from django.contrib import admin

from notes.models import Notes
from notes import models

# Register your models here.
admin.site.register(Notes)
