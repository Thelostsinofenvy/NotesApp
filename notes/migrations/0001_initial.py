# Generated by Django 3.2.5 on 2021-12-01 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('text', models.TextField(blank=True, max_length=300, null=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2021, 12, 2, 1, 38, 2, 639002), editable=False)),
            ],
        ),
    ]
