# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-11 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_auto_20180208_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='aircraft_model',
            field=models.CharField(max_length=5, null=True, verbose_name='飞机型号'),
        ),
        migrations.AddField(
            model_name='parameter',
            name='aircraft_number',
            field=models.CharField(max_length=3, null=True, verbose_name='架机号'),
        ),
    ]
