# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-20 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_insight_viewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='command_array',
            field=models.TextField(default='{}'),
        ),
    ]
