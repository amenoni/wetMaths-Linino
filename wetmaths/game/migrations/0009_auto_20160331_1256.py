# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 12:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_auto_20160331_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 3, 31, 12, 56, 55, 995922, tzinfo=utc)),
        ),
    ]