# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-15 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0048_merge_20180215_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='audioset',
            name='live_status',
            field=models.CharField(choices=[('0', 'Not Started Yet'), ('1', 'Signal Creation Started.'), ('2', 'Trend Created'), ('3', 'ChiSquare Created'), ('4', 'Decision Tree Created'), ('5', 'Density Histogram Created'), ('6', 'Regression Created'), ('7', 'Signal Creation Done')], default='0', max_length=300),
        ),
        migrations.AddField(
            model_name='audioset',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customapps',
            name='live_status',
            field=models.CharField(choices=[('0', 'Not Started Yet'), ('1', 'Signal Creation Started.'), ('2', 'Trend Created'), ('3', 'ChiSquare Created'), ('4', 'Decision Tree Created'), ('5', 'Density Histogram Created'), ('6', 'Regression Created'), ('7', 'Signal Creation Done')], default='0', max_length=300),
        ),
        migrations.AddField(
            model_name='customapps',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='robo',
            name='live_status',
            field=models.CharField(choices=[('0', 'Not Started Yet'), ('1', 'Signal Creation Started.'), ('2', 'Trend Created'), ('3', 'ChiSquare Created'), ('4', 'Decision Tree Created'), ('5', 'Density Histogram Created'), ('6', 'Regression Created'), ('7', 'Signal Creation Done')], default='0', max_length=300),
        ),
        migrations.AddField(
            model_name='robo',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stockdataset',
            name='live_status',
            field=models.CharField(choices=[('0', 'Not Started Yet'), ('1', 'Signal Creation Started.'), ('2', 'Trend Created'), ('3', 'ChiSquare Created'), ('4', 'Decision Tree Created'), ('5', 'Density Histogram Created'), ('6', 'Regression Created'), ('7', 'Signal Creation Done')], default='0', max_length=300),
        ),
        migrations.AddField(
            model_name='stockdataset',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
    ]
