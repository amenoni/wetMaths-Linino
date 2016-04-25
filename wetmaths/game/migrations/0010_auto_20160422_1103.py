# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-22 11:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_auto_20160331_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='player1_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='game',
            name='player2_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='game',
            name='player3_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='move',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 4, 22, 11, 3, 20, 254724, tzinfo=utc)),
        ),
    ]