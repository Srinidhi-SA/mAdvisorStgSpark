# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20170829_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='robo',
            name='dataset_analysis_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='robo',
            name='robo_analysis_done',
            field=models.BooleanField(default=True),
        ),
    ]