# Generated by Django 3.2.5 on 2021-11-23 16:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_auto_20211123_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='date_updated',
        ),
        migrations.AlterField(
            model_name='note',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]