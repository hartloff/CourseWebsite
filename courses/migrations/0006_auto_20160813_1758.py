# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-13 21:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20160813_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_answered',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 13, 21, 58, 52, 5790, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_submitted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
