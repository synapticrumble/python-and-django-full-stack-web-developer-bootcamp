# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-07 14:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 7, 14, 13, 9, 757705, tzinfo=utc)),
        ),
    ]
