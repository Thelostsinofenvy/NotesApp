# Generated by Django 3.2.5 on 2021-11-23 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_auto_20211123_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 22, 31, 18, 409954), editable=False),
        ),
    ]