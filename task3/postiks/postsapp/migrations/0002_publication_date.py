# Generated by Django 3.2.4 on 2021-06-29 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
